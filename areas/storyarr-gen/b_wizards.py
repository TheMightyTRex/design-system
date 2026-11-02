from shell import *


def steps(items, current):
    out = []
    for k, (name, state) in enumerate(items):
        if k == current:
            out.append(f'<li aria-current="step">{name}<span class="visually-hidden">, current step</span></li>')
        elif state:
            out.append(f'<li data-done>{name}<span class="visually-hidden">, {state}</span></li>')
        else:
            out.append(f"<li>{name}</li>")
    return f'<ol class="steps" aria-label="Steps">{"".join(out)}</ol>'


def onboarding():
    st = steps([("Display", "done"), ("Book details", "done"), ("Library server", None), ("Library folders", None), ("Download sources", None), ("Download client", None), ("Finish", None)], 2)
    body = f"""
{what_changed([
    "<strong>One wizard for setup and upgrades</strong>: the same step list, the same buttons (Continue, Back, Skip this step) and \"Keep the defaults and finish\" at the top. Today the two wizards use different classes, shells and button names.",
    "<strong>One question per step</strong> (\"Connect a library server?\") instead of a whole Settings section with its own Save. Continue saves the answer, so nothing is lost silently.",
    "<strong>No capitals typed in source</strong> (\"STEP 1 OF 9\"), no contractions (\"Let's set up your library\"). Done steps say \"done\" to screen readers, not only with a tick.",
    "<strong>Connecting a server stays a dialog</strong>: it is a short task that must finish before the next step.",
])}
<div class="page-head">
  <div class="page-head__text"><h1>Set up Storyarr</h1><p class="page-head__summary">Step 3 of 7 · about 5 minutes · you can change everything later in Settings</p></div>
  <div class="actions"><button class="btn btn--quiet" type="button">Keep the defaults and finish</button></div>
</div>
{st}
<section class="panel" aria-labelledby="q-h" style="max-width:760px">
  <div style="display:grid;gap:var(--space-1)"><h2 id="q-h">Connect a library server?</h2><p class="muted">Storyarr reads the books you already have from your library server and adds new ones to it.</p></div>
  <fieldset><legend class="visually-hidden">Library server</legend><div class="option-cards">
    <label class="option-card"><input type="radio" name="ob-srv" checked><strong>Audiobookshelf</strong><small>For audiobooks, and ebooks if you keep them there.</small></label>
    <label class="option-card"><input type="radio" name="ob-srv"><strong>Calibre-Web</strong><small>For ebooks.</small></label>
    <label class="option-card"><input type="radio" name="ob-srv"><strong>Not now</strong><small>Storyarr keeps books in its own folders until you connect one.</small></label>
  </div></fieldset>
  <div class="actions"><button class="btn" type="button" data-dialog="dlg-connect">{ic("plug")}Connect Audiobookshelf</button></div>
  <div class="notice" data-tone="success" role="status">{ic("circle-check")}<div class="notice__body"><span class="notice__title">Audiobookshelf connected</span><p>Found 2 libraries: Fiction audiobooks and Children's audiobooks.</p></div></div>
  <div class="actions" style="padding-top:var(--space-4);border-top:1px solid var(--color-divider)"><button class="btn btn--primary" type="button">Continue</button><button class="btn" type="button">Back</button><button class="btn btn--quiet" type="button">Skip this step</button></div>
</section>

{board_divider("Finish step", "The last step sums up the answers, with a link to change each one, and one button.")}
<section class="panel" aria-labelledby="fin-h" style="max-width:760px">
  <h2 id="fin-h">Ready to go</h2>
  <dl class="facts"><dt>Display</dt><dd>Light, text 125% · <a href="#">Change<span class="visually-hidden"> display</span></a></dd><dt>Book details</dt><dd>Hardcover · <a href="#">Change<span class="visually-hidden"> book details</span></a></dd><dt>Library server</dt><dd>Audiobookshelf, 2 libraries</dd><dt>Library folders</dt><dd><code>/data/audiobooks</code>, <code>/data/ebooks</code></dd><dt>Download sources</dt><dd>Skipped · <a href="storyarr-settings-downloads.html">Set up later in Settings</a></dd><dt>Download client</dt><dd>qBittorrent</dd></dl>
  <div class="actions"><a class="btn btn--primary" href="storyarr-discover.html">Start browsing</a><button class="btn" type="button">Back</button></div>
</section>
{phone_section([("phone=1", "On phones the step list wraps above the question. It should collapse to \"Step 3 of 7\" (missing component), so Continue stays close.", 760),
                ("phone=1&dialog=dlg-connect", "The connection dialog nearly fills the width.", 760)], "The wizard on a phone.")}
"""
    dialogs = dialog("dlg-connect", "Connect Audiobookshelf",
                     '<div class="field"><label for="cn-a">Server address</label><span class="hint" id="cn-ah">The address Storyarr uses to reach Audiobookshelf.</span><input class="input" id="cn-a" aria-describedby="cn-ah" value="http://audiobookshelf:13378"></div>'
                     '<div class="field"><label for="cn-k">API key</label><span class="hint" id="cn-kh">In Audiobookshelf: Settings, then API keys.</span><input class="input" id="cn-k" type="password" aria-describedby="cn-kh"></div>',
                     '<button class="btn btn--primary" type="button" data-closes>Test and connect</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>')
    return page("onboarding", "Set up Storyarr", "onboarding", None, body, None, "", dialogs)


def upgrade():
    st = steps([("What is new", None), ("Your backup", None), ("New setting: narrator pages", None), ("Finish", None)], 0)
    body = f"""
{what_changed([
    "<strong>Same wizard as setup</strong>: step list, Continue and Back, \"Keep the defaults and finish\" at the top. \"Remind me later\" is a quiet button beside it, no longer next to the primary button.",
    "<strong>One step per new setting</strong>, skipped when there is none. Today step 3 always shows the whole Display panel.",
    "<strong>Release notes styled once</strong> (Added, Changed, Fixed, Database changes) and shared with the Release notes slide-out from the version in the footer.",
])}
<div class="page-head">
  <div class="page-head__text"><h1>Upgrade to version 1.10.0</h1><p class="page-head__summary">From 1.9.2 · 4 steps · Storyarr backs up your settings first</p></div>
  <div class="actions"><button class="btn btn--quiet" type="button">Remind me later</button><button class="btn btn--quiet" type="button">Keep the defaults and finish</button></div>
</div>
{st}
<section class="panel" aria-labelledby="wn-h" style="max-width:760px">
  <div style="display:grid;gap:var(--space-1)"><h2 id="wn-h">What is new in 1.10.0</h2><p class="muted">Released 28 October 2026.</p></div>
  <section aria-labelledby="wn-a" style="display:grid;gap:var(--space-2)"><h3 id="wn-a">Added</h3><ul style="margin:0;padding-left:var(--space-5);display:grid;gap:var(--space-1)"><li><strong>Narrator pages</strong>: open a narrator from any book to find every book they read in your library, and more by them.</li><li><strong>Slide-outs</strong>: book summaries, requests and connections open beside the list, so you keep your place.</li></ul></section>
  <section aria-labelledby="wn-c" style="display:grid;gap:var(--space-2)"><h3 id="wn-c">Changed</h3><ul style="margin:0;padding-left:var(--space-5);display:grid;gap:var(--space-1)"><li><strong>Settings</strong>: every section saves the same way, with a save bar that stays in view.</li><li><strong>Activity</strong>: one row per request, with details in a slide-out.</li></ul></section>
  <section aria-labelledby="wn-f" style="display:grid;gap:var(--space-2)"><h3 id="wn-f">Fixed</h3><ul style="margin:0;padding-left:var(--space-5);display:grid;gap:var(--space-1)"><li><strong>Notifications</strong>: deleting a channel now asks first.</li></ul></section>
  <details class="disclosure"><summary>Database changes and the way back</summary><div class="disclosure__body"><p>Adds a narrator table. To go back, restore the backup made in the next step from Settings, System, Upgrades and backups.</p></div></details>
  <div class="actions" style="padding-top:var(--space-4);border-top:1px solid var(--color-divider)"><button class="btn btn--primary" type="button">Continue</button></div>
</section>

{board_divider("Your backup and New setting steps", "Each later step asks one thing.")}
<section class="panel" aria-labelledby="bk-h" style="max-width:760px">
  <h2 id="bk-h">Your backup</h2>
  <p>Storyarr saved a backup of version 1.9.2 at 14:02 today. Download a copy if you want one outside the server.</p>
  <dl class="facts"><dt>Backup</dt><dd>storyarr-1.9.2-2026-11-02.zip · 4.2 MB</dd></dl>
  <div class="actions"><button class="btn" type="button">{ic("download")}Download backup</button></div>
  <div class="actions" style="padding-top:var(--space-4);border-top:1px solid var(--color-divider)"><button class="btn btn--primary" type="button">Continue</button><button class="btn" type="button">Back</button></div>
</section>
<section class="panel" aria-labelledby="ns-h" style="max-width:760px">
  <h2 id="ns-h">Show narrator links on books?</h2>
  <div class="option-cards"><label class="option-card"><input type="radio" name="ns" checked><strong>Yes, link narrators</strong><small>Narrator names open the new narrator page. This is the default.</small></label><label class="option-card"><input type="radio" name="ns"><strong>No, show names only</strong><small>You can turn links on later in Settings, General, Display.</small></label></div>
  <div class="actions" style="padding-top:var(--space-4);border-top:1px solid var(--color-divider)"><button class="btn btn--primary" type="button">Continue</button><button class="btn" type="button">Back</button><button class="btn btn--quiet" type="button">Skip this step</button></div>
</section>
{phone_section([("phone=1", "The step list wraps above the step; the buttons wrap under it.", 760)], "The upgrade wizard on a phone.")}
"""
    return page("upgrade", "Upgrade to version 1.10.0", "settings", "system", body, None, "", "", tab_title="Upgrade")


def build():
    return [onboarding(), upgrade()]
