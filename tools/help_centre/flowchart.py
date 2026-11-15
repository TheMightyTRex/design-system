"""Flow charts for the help centre (HELP-WRITING.md, section 11): read a chart written in a ```flow block (or a simple
Mermaid flowchart), draw it as an SVG that follows the theme, and write the same paths out as a nested list.

The flow format, one node a line, answers indented under the node they leave from:

    title: Find your answer                      (optional caption)
    start: A download says Needs attention
    q: What does the message say?
      No files are suitable -> 1
      It asks which episode -> 2
      You do not need it -> 3
    1: Try the import again | Most common
      Still stuck -> 4
    2: Choose the episode by hand
    3: Ignore it | Nothing is deleted
    4: Send it to be looked at #send-it-to-be-looked-at

- start: the problem or the starting point, exactly one, first. A start or step with no answers under it leads to
  the next node.
- q or q<name>: a question (q, q2, qdisk). Each needs at least two answers.
- step<name>: one thing that happens, in order (step, step2, stepbackup); end<name>: a good end; warn<name>: an
  end to avoid or the last thing to try. None of these is numbered.
- <number>: a numbered answer. It matches the article's section whose heading starts with the number ("1. Try
  the import again"), or the heading given with #its-id at the end of the line.
- "| text" after a node adds a short second line.
- An answer line is "<what the reader sees or chooses> -> <target>"; the target is a question, a number, or
  another article (other-article.md, with #heading if wanted).
Nothing here needs a library: the drawing is plain SVG with classes from components.css (.flow-chart).
"""
import html
import re

CHAR_W = 7.0     # average width of a character at 13px, in the chart's own units
LINE_H = 17
PAD = 24         # space between nodes in a row


class FlowError(ValueError):
    pass


def parse_flow(text, where=""):
    """The flow format to {"title", "nodes": {id: node}, "start": id}. Raises FlowError with the line number."""
    nodes, order, title, current = {}, [], "", None
    for n, raw in enumerate(text.splitlines(), 1):
        if not raw.strip() or raw.strip().startswith("%%"):
            continue
        indented = raw[:1] in (" ", "\t")
        line = raw.strip()
        if indented:
            if current is None:
                raise FlowError(f"{where} line {n}: an answer comes before any node")
            m = re.match(r"(.*?)\s*->\s*(\S+)\s*$", line)
            if not m:
                raise FlowError(f"{where} line {n}: an answer needs '<words> -> <target>'")
            nodes[current]["edges"].append((m.group(1).strip(), m.group(2)))
            continue
        m = re.match(r"(title|start|q[\w-]*|step[\w-]*|end[\w-]*|warn[\w-]*|\d+)\s*:\s*(.+)$", line)
        if not m:
            raise FlowError(f"{where} line {n}: start a node with start:, q:, step:, end:, warn: or a number")
        key, rest = m.group(1), m.group(2).strip()
        if key == "title":
            title = rest
            continue
        anchor = ""
        am = re.search(r"\s+#([\w-]+)\s*$", rest)
        if am:
            anchor, rest = am.group(1), rest[:am.start()].rstrip()
        text_, _, sub = rest.partition("|")
        kind = ("start" if key == "start" else "q" if key.startswith("q") else "step" if key.startswith("step")
                else "end" if key.startswith("end") else "warn" if key.startswith("warn") else "answer")
        if key in nodes:
            raise FlowError(f"{where} line {n}: {key} is written twice")
        nodes[key] = {"id": key, "kind": kind, "text": text_.strip(), "sub": sub.strip(), "anchor": anchor,
                      "edges": [], "number": key if kind == "answer" else ""}
        order.append(key)
        current = key
    starts = [k for k in order if nodes[k]["kind"] == "start"]
    if len(starts) != 1 or order[0] != starts[0]:
        raise FlowError(f"{where}: a chart needs exactly one start:, as its first node")
    # A start or a step with no answers under it leads to the next node.
    for i, k in enumerate(order[:-1]):
        if nodes[k]["kind"] in ("start", "step") and not nodes[k]["edges"]:
            nodes[k]["edges"].append(("", order[i + 1]))
    _check(nodes, where, strict=True)
    return {"title": title, "nodes": nodes, "order": order, "start": starts[0]}


def parse_mermaid(text):
    """A simple Mermaid flowchart (flowchart or graph, TD or LR) in the same shape, or None when it is not one this
    reads: nodes A[text], A["text"], A(text), A{text}; links -->, -->|label|, -- label -->."""
    lines = [l.strip() for l in text.strip().splitlines() if l.strip() and not l.strip().startswith("%%")]
    if not lines or not re.match(r"^(flowchart|graph)\b", lines[0]):
        return None
    nodes, order = {}, []
    node_re = r'([A-Za-z_][\w-]*)\s*(?:\[\s*"?(.*?)"?\s*\]|\(\s*"?(.*?)"?\s*\)|\{\s*"?(.*?)"?\s*\})?'

    def node(m):
        nid = m.group(1)
        label = next((g for g in (m.group(2), m.group(3), m.group(4)) if g is not None), None)
        if nid not in nodes:
            nodes[nid] = {"id": nid, "kind": "step", "text": nid, "sub": "", "anchor": "", "edges": [], "number": ""}
            order.append(nid)
        if label is not None:
            nodes[nid]["text"] = html.unescape(label).replace("<br>", " ").replace("<br/>", " ")
            if m.group(4) is not None:
                nodes[nid]["kind"] = "q"
        return nid

    for line in lines[1:]:
        if re.match(r"^(style|classDef|class|linkStyle|click|subgraph|end|direction)\b", line):
            continue
        parts = re.split(r"\s*(--\s*[^->|]+?\s*-->|-->\s*\|[^|]*\|\s*|-->|---|==>|-\.->)\s*", line)
        if len(parts) == 1:
            m = re.fullmatch(node_re, parts[0])
            if not m:
                return None
            node(m)
            continue
        prev = None
        for i in range(0, len(parts), 2):
            m = re.fullmatch(node_re, parts[i].strip().rstrip(";"))
            if not m:
                return None
            cur = node(m)
            if prev is not None:
                arrow = parts[i - 1]
                lab = re.search(r"\|([^|]*)\||--\s*(.+?)\s*-->", arrow)
                label = (lab.group(1) if lab and lab.group(1) is not None else (lab.group(2) if lab else "")) or ""
                nodes[prev]["edges"].append((label.strip().strip('"'), cur))
            prev = cur
    if not order:
        return None
    incoming = {t for n in nodes.values() for _, t in n["edges"]}
    roots = [k for k in order if k not in incoming]
    if len(roots) != 1:
        return None
    nodes[roots[0]]["kind"] = "start"
    try:
        _check(nodes, "")
    except FlowError:
        return None
    return {"title": "", "nodes": nodes, "order": order, "start": roots[0]}


def _check(nodes, where, strict=False):
    for n in nodes.values():
        for _, t in n["edges"]:
            if t not in nodes and not re.match(r"^[\w./-]+\.md(#[\w-]+)?$", t):
                raise FlowError(f"{where}: {n['id']} leads to {t}, which is not in the chart (a question, a number or an .md file)")
        if strict and n["kind"] in ("end", "warn") and n["edges"]:
            raise FlowError(f"{where}: {n['id']} is an end, so nothing can lead on from it")
        if strict and n["kind"] == "q" and len(n["edges"]) < 2:
            raise FlowError(f"{where}: the question {n['id']} needs at least two answers")


def _wrap(text, width):
    chars = max(8, int(width / CHAR_W))
    out, line = [], ""
    for word in text.split():
        if line and len(line) + 1 + len(word) > chars:
            out.append(line)
            line = word
        else:
            line = f"{line} {word}".strip()
    if line:
        out.append(line)
    return out or [""]


def layout(chart, link_title=lambda target: target):
    """Places every node: rows by the longest path from the start, each node under its parents."""
    nodes = chart["nodes"]
    # Articles named as targets become their own end nodes.
    for n in list(nodes.values()):
        for i, (label, t) in enumerate(n["edges"]):
            if t not in nodes:
                nodes[t] = {"id": t, "kind": "link", "text": link_title(t), "sub": "Another article", "anchor": "",
                            "edges": [], "number": "", "href": t}
    level = {chart["start"]: 0}
    changed, guard = True, 0
    while changed:
        changed, guard = False, guard + 1
        if guard > len(nodes) + 2:
            raise FlowError("the chart goes round in a circle; every answer must lead further down")
        for n in nodes.values():
            if n["id"] not in level:
                continue
            for _, t in n["edges"]:
                if level.get(t, -1) < level[n["id"]] + 1:
                    level[t] = level[n["id"]] + 1
                    changed = True
    unreached = [k for k in nodes if k not in level]
    if unreached:
        raise FlowError(f"nothing leads to {', '.join(unreached)}")
    # Answers reached from another answer are the next thing to try: drawn as a warning.
    for n in nodes.values():
        if n["kind"] == "answer":
            for _, t in n["edges"]:
                if nodes[t]["kind"] == "answer":
                    nodes[t]["tone"] = "warn"
    rows = {}
    for k, lv in level.items():
        rows.setdefault(lv, []).append(k)
    depth = max(rows) + 1
    cols = max(len(r) for r in rows.values())
    nw = 200 if cols <= 3 else 170
    width = max(560, cols * (nw + PAD) + PAD)
    parents = {k: [] for k in nodes}
    for n in nodes.values():
        for i, (label, t) in enumerate(n["edges"]):
            parents[t].append((n["id"], i, label))
    pos, y = {}, 14
    for lv in range(depth):
        row = rows[lv]
        for k in row:
            nd = nodes[k]
            inner = nw - (44 if nd["kind"] == "q" else 20)
            nd["lines"] = _wrap(nd["text"], inner)
            nd["sublines"] = _wrap(nd["sub"], inner) if nd["sub"] else []
            nd["w"] = nw
            nd["h"] = len(nd["lines"]) * LINE_H + len(nd["sublines"]) * 15 + (26 if nd["kind"] == "q" else 18)
        # Under its parents, in the order the answers were written.
        def want(k):
            ps = parents[k]
            return sum(pos[p][0] for p, _, _ in ps) / len(ps) if ps else width / 2
        def key(k):
            ps = parents[k]
            return (min((pos[p][0], i) for p, i, _ in ps) if ps else (0, 0))
        row.sort(key=key)
        xs = [want(k) for k in row]
        gap = nw + PAD
        # Spread the row so no two nodes overlap, keeping each group of children centred on what it wants.
        for i in range(1, len(xs)):
            xs[i] = max(xs[i], xs[i - 1] + gap)
        shift = (sum(want(k) for k in row) - sum(xs)) / len(xs)
        xs = [x + shift for x in xs]
        lo, hi = PAD + nw / 2, width - PAD - nw / 2
        if xs[0] < lo:
            xs = [x + lo - xs[0] for x in xs]
        if xs[-1] > hi:
            xs = [x - (xs[-1] - hi) for x in xs]
        rh = max(nodes[k]["h"] for k in row)
        labels_below = 0
        if lv + 1 in rows:
            for k in rows[lv + 1]:
                for p, _, label in parents[k]:
                    if label:
                        labels_below = max(labels_below, len(_wrap(label, nw - 8)))
        for k, x in zip(row, xs):
            pos[k] = (x, y + (rh - nodes[k]["h"]) / 2)
        y += rh + 34 + labels_below * 15
    for k, (x, yy) in pos.items():
        nodes[k]["x"], nodes[k]["y"] = x, yy
    chart["width"], chart["height"] = width, y - 14 - 12
    return chart


def _text(x, y, lines, cls):
    spans = "".join(f'<tspan x="{x:.0f}" dy="{0 if i == 0 else (LINE_H if cls != "flow-chart__sub" else 15)}">{html.escape(t)}</tspan>'
                    for i, t in enumerate(lines))
    return f'<text class="{cls}" x="{x:.0f}" y="{y:.0f}" text-anchor="middle">{spans}</text>'


def svg(chart, uid, label):
    """The chart as an SVG image. Its name says what it is; the words after it are the full text equivalent."""
    nodes, out, labels = chart["nodes"], [], {}
    lines_into = {}
    for n in nodes.values():
        for label_, t in n["edges"]:
            if label_:
                lines_into[t] = max(lines_into.get(t, 0), len(_wrap(label_, n["w"] - 8)))
    # Lines first, so the boxes sit on top.
    for n in nodes.values():
        for label_, t in n["edges"]:
            c = nodes[t]
            x1, y1 = n["x"], n["y"] + n["h"]
            x2, y2 = c["x"], c["y"]
            mid = y1 + 14
            # A line that would cross a node in a row between goes round the side.
            between = [o for o in nodes.values() if o["y"] > y1 and o["y"] + o["h"] < y2 and abs(o["x"] - x2) < o["w"] / 2 + 6]
            if between:
                side = chart["width"] - 8 if x2 > chart["width"] / 2 else 8
                d = f"M{x1:.0f} {y1:.0f} V{mid:.0f} H{side:.0f} V{y2 - 18 - 15 * lines_into.get(t, 0):.0f} H{x2:.0f} V{y2 - 6:.0f}"
            else:
                d = f"M{x1:.0f} {y1:.0f} V{mid:.0f} H{x2:.0f} V{y2 - 6:.0f}"
            out.append(f'<path class="flow-chart__line" d="{d}"/>')
            out.append(f'<path class="flow-chart__head" d="M{x2 - 5:.0f} {y2 - 9:.0f} L{x2 + 5:.0f} {y2 - 9:.0f} L{x2:.0f} {y2 - 1:.0f}z"/>')
            if label_:
                # Each answer's words sit on its line just above the box it leads to; the same words on several lines
                # into one box are written once.
                labels.setdefault((t, label_), (x2, y2, n["w"]))
    for (t, label_), (x2, y2, w) in labels.items():
        lines = _wrap(label_, w - 8)
        top = y2 - 12 - len(lines) * 15
        bw = max(len(l) for l in lines) * 6.4 + 10
        out.append(f'<rect class="flow-chart__label-bg" x="{x2 - bw / 2:.0f}" y="{top:.0f}" width="{bw:.0f}" height="{len(lines) * 15 + 2}"/>')
        out.append(_text(x2, top + 12, lines, "flow-chart__label").replace('dy="17"', 'dy="15"'))
    for n in nodes.values():
        x, y, w, h = n["x"], n["y"], n["w"], n["h"]
        kind = n["kind"]
        cls = {"start": "flow-chart__start", "q": "flow-chart__question", "answer": "flow-chart__answer", "end": "flow-chart__answer",
               "warn": "flow-chart__next", "link": "flow-chart__link", "step": "flow-chart__step"}[kind]
        if n.get("tone") == "warn":
            cls = "flow-chart__next"
        if kind == "q":
            e = 16
            out.append(f'<path class="{cls}" d="M{x - w / 2:.0f} {y + h / 2:.0f} L{x - w / 2 + e:.0f} {y:.0f} H{x + w / 2 - e:.0f} '
                       f'L{x + w / 2:.0f} {y + h / 2:.0f} L{x + w / 2 - e:.0f} {y + h:.0f} H{x - w / 2 + e:.0f}z"/>')
        else:
            out.append(f'<rect class="{cls}" x="{x - w / 2:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}"/>')
        ty = y + 9 + 13
        out.append(_text(x, ty, n["lines"], "flow-chart__text" + (" flow-chart__text--on-accent" if kind == "start" else "")))
        if n["sublines"]:
            out.append(_text(x, ty + len(n["lines"]) * LINE_H - 2, n["sublines"], "flow-chart__sub"))
        if n["number"]:
            out.append(f'<rect class="flow-chart__pill" x="{x - w / 2 - 10:.0f}" y="{y - 10:.0f}" width="22" height="22"/>'
                       f'<text class="flow-chart__n" x="{x - w / 2 + 1:.0f}" y="{y + 6:.0f}" text-anchor="middle">{html.escape(n["number"])}</text>')
    w, h = chart["width"], chart["height"]
    return (f'<svg class="flow-chart__svg" viewBox="0 0 {w:.0f} {h:.0f}" style="--flow-w: {w:.0f}px" role="img" '
            f'aria-labelledby="{uid}-t" focusable="false"><title id="{uid}-t">{html.escape(label)}</title>{"".join(out)}</svg>')


def words(chart, describe):
    """The same chart as a nested list: each answer, then where it leads. describe(node) gives the HTML for a node."""
    nodes, seen = chart["nodes"], set()

    def branch(nid):
        seen.add(nid)
        n = nodes[nid]
        if not n["edges"]:
            return ""
        items = []
        for label, t in n["edges"]:
            lead = f"{html.escape(label)}: " if label else ("Then: " if n["kind"] != "q" else "")
            if t in seen:
                items.append(f"<li>{lead}go to {say(nodes[t])}</li>")
            else:
                items.append(f"<li>{lead}{say(nodes[t])}{branch(t)}</li>")
        return f"<ul>{''.join(items)}</ul>"

    def say(n):
        """The node, with its second line in brackets: the words hold everything the drawing shows."""
        out = describe(n)
        return f"{out} ({html.escape(n['sub'])})" if n.get("sub") else out

    start = nodes[chart["start"]]
    return f"<p>{say(start)}</p>{branch(chart['start'])}"


def render(chart, uid, describe, link_title=lambda t: t, caption=""):
    """The whole chart: the drawing, then the same paths in words, in a figure."""
    layout(chart, link_title)
    start = chart["nodes"][chart["start"]]["text"]
    pic = svg(chart, uid, f"Flow chart: {start}. The same chart is written out in words after it.")
    cap = f'<figcaption class="flow-chart__caption">{html.escape(caption)}</figcaption>' if caption else ""
    return (f'<figure class="flow-chart" id="{uid}">{cap}'
            f'<div class="flow-chart__scroll" role="region" tabindex="0" aria-label="Flow chart, scrolls sideways on a narrow screen">{pic}</div>'
            f'<details class="disclosure flow-chart__words"><summary>The chart in words</summary>'
            f'<div class="disclosure__body">{words(chart, describe)}</div></details></figure>')
