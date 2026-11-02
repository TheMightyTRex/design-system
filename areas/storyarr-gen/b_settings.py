from shell import *
from b_library import chipbtn

SECTIONS = {
    "general": [("display", "Display", "sun"), ("notifications", "Notifications", "bell")],
    "accounts": [("sign-in", "Sign-in", "key-round"), ("accounts", "Users and access", "users")],
    "sources": [("reading", "Reading accounts", "book-open-text"), ("catalog", "Metadata", "tags")],
    "library": [("libraries", "Libraries", "library"), ("naming", "File naming", "file-pen")],
    "downloads": [("sources", "Download sources", "radar"), ("downloaders", "Download clients", "hard-drive-download"),
                  ("preferences", "Preferences", "sliders-horizontal"), ("automation", "Automation", "zap")],
    "system": [("logs", "Logs", "scroll-text"), ("background-work", "Background work", "timer"), ("upgrades", "Upgrades and backups", "archive-restore")],
}
_n = [0]


def uid(p="s"):
    _n[0] += 1
    return f"{p}{_n[0]}"


def setting(label, hint, control):
    i = uid("lbl")
    control = control.replace("{L}", i)
    return (f'<li class="setting"><div class="setting__text"><span class="setting__label" id="{i}">{label}</span>'
            f'{f"<span class=\"setting__hint\">{hint}</span>" if hint else ""}</div><div class="setting__control">{control}</div></li>')


def opens(label, hint, pid, verb="Edit", extra="", icon="pencil"):
    return (f'<li class="setting setting--opens"><div class="setting__text"><span class="setting__label">{label}</span><span class="setting__hint">{hint}</span></div>'
            f'<div class="setting__control" style="gap:var(--space-2)">{extra}<button class="btn" type="button" data-opens="{pid}">{ic(icon)}{verb}<span class="visually-hidden"> {label}</span></button></div></li>')


def check(on=True):
    return f'<label class="check"><input type="checkbox" aria-labelledby="{{L}}"{" checked" if on else ""}><span class="check__text">{"On" if on else "Off"}</span></label>'


def select(opts, w=240):
    return f'<select class="select" aria-labelledby="{{L}}" style="max-width:{w}px">' + "".join(f"<option>{o}</option>" for o in opts) + "</select>"


def seg(name, opts, checked):
    return (f'<fieldset class="segmented" aria-labelledby="{{L}}">' +
            "".join(f'<label><input type="radio" name="{name}"{" checked" if o == checked else ""}><span>{o}</span></label>' for o in opts) + "</fieldset>")


def unit(value, u, w=160):
    return f'<div class="input-group" style="max-width:{w}px"><input class="input" inputmode="numeric" aria-labelledby="{{L}}" value="{value}"><span class="input-group__unit">{u}</span></div>'


def card(title, hint, rows, action="", h="h2", admin=False):
    i = uid("sec")
    tag = ' <span class="tag">Administrator</span>' if admin else ""
    return (f'<section class="settings-section" aria-labelledby="{i}"><div class="settings-section__head">'
            f'<div style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:var(--space-3)"><div style="display:grid;gap:4px"><{h} id="{i}">{title}{tag}</{h}><p class="small muted">{hint}</p></div>{action}</div></div>'
            f'<ul class="settings-rows">{"".join(rows)}</ul></section>')


def savebar(state="No unsaved changes", dirty=False):
    s = (f'<span class="small" role="status">{ic("circle-alert")} {state}</span>' if dirty else f'<span class="small muted" role="status">{state}</span>')
    return (f'<div role="group" aria-label="Save changes" style="position:sticky;bottom:0;z-index:5;max-width:880px;display:flex;flex-wrap:wrap;align-items:center;gap:var(--space-2) var(--space-4);'
            f'padding:var(--space-3) var(--space-4);border:1px solid var(--color-border);background:var(--color-surface-raised);box-shadow:var(--shadow-raised)">'
            f'<button class="btn btn--primary" type="button">Save changes</button><button class="btn btn--quiet" type="button">Discard changes</button>{s}</div>')


def section_block(first, title, summary, content):
    """The first section is this page (h1); the others are shown below as board parts."""
    # Each section is wrapped so its sticky save bar only sticks while that section is in view.
    wrap = '<div style="display:grid;gap:var(--space-6)">'
    if first:
        return f'{wrap}<div class="page-head"><div class="page-head__text"><h1>{title}</h1><p class="page-head__summary">{summary}</p></div></div>{content}</div>'
    return board_divider(f"{title} (its own page, header row 2)", summary) + wrap + content + "</div>"


def edit_foot(save="Save and test", remove=None, test=False):
    f = f'<button class="btn btn--primary" type="button">{save}</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>'
    if test:
        f += f'<button class="btn" type="button">{ic("zap")}Test</button>'
    if remove:
        f += f'<button class="btn btn--danger" type="button" data-dialog="{remove[1]}">{ic("trash-2")}{remove[0]}</button>'
    return f


def remove_dialog(did, title, body, button):
    return dialog(did, title, f"<p>{body}</p>", f'<button class="btn btn--danger btn--primary" type="button" data-closes>{button}</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>')


COMMON_WHAT = ("<strong>Every section uses the settings rows template</strong>: cards with a heading and one line, label and explanation on the left, the control on the right.",
               "<strong>One save pattern</strong>, modelled on File naming: a save bar that stays in view at the foot of the section, with Save changes, Discard changes and the save state. No more autosave next to explicit saves, or \"Saved\" above the form in one section and below in another.",
               "<strong>Things with several fields open a slide-out</strong> with Save, Cancel, Test and Remove in its footer; removing always asks in a dialog.")


def gpage(group, title, what, blocks, panels="", dialogs="", phone=None):
    secs = SECTIONS[group]
    row2 = (title + " sections", [(sid, name, icon, f"storyarr-settings-{group}.html#{sid}") for sid, name, icon in secs], secs[0][0])
    body = what_changed(list(COMMON_WHAT[:1]) + what + list(COMMON_WHAT[1:])) + "".join(blocks)
    if phone:
        body += phone_section(phone, "Settings rows stack on phones: the control moves under its label, and the save bar stays at the foot of the window.")
    return page(f"settings-{group.lower()}", secs[0][1], "settings", group, body, row2, panels, dialogs, tab_title=f"{secs[0][1]} · Settings")


PHONE_DEFAULT = [("phone=1", "Rows stack; the save bar wraps and stays at the foot of the window.", 760)]


def general():
    display = section_block(True, "Display", "How Storyarr looks for you. Display and accessibility is saved in this browser; the rest is saved to your account.",
        card("Display and accessibility", "Saved in this browser only. The Display button in the header opens the same settings.", [
            setting("Theme", "Match device follows your system's light or dark setting.", seg("th", ["Match device", "Light", "Dark"], "Light")),
            setting("Text size", None, select(["100%", "125%", "150%", "175%"], 160)),
            setting("High contrast", "Stronger borders and colours.", check(False)),
            setting("Reduce motion", "Panels appear without sliding.", check(False)),
            setting("Underline links", None, check(True)),
            setting("Wider text spacing", None, check(False)),
        ]) + card("Covers", "Saved to your account, on every device.", [
            setting("Cover size", "On My library, Following and Discover.", seg("cs", ["Small", "Medium", "Large"], "Medium")),
            setting("Audiobook covers", "Square covers are never cropped.", select(["Letterbox square covers", "Show square"])),
        ]) + card("Saved views", "Views you saved from a section toolbar.", [
            setting("Audiobooks, newest first", "My library", f'<button class="btn" type="button">{ic("trash-2")}Remove<span class="visually-hidden"> Audiobooks, newest first</span></button>'),
            setting("Fantasy winners", "Discover, Browse", f'<button class="btn" type="button">{ic("trash-2")}Remove<span class="visually-hidden"> Fantasy winners</span></button>'),
        ]) + card("Setup wizard", "Go through the first-run questions again. Your current settings are kept.", [
            setting("Run setup again", None, '<a class="btn" href="storyarr-onboarding.html">Open setup wizard</a>'),
        ]) + savebar("Unsaved change: Text size", True))
    notif = section_block(False, "Notifications", "Where Storyarr sends news about requests and downloads.",
        card("Channels", "Each channel sends the events you choose.", [
            opens("Household email", 'Email · everyone · new books and failed downloads · <span class="chip" data-tone="success">Connected</span>', "panel-channel",
                  extra=menu("m-ch1", "More for Household email", [("Send test", "send"), ("Pause channel", "pause"), "hr", ("Delete channel|data-dialog=\"dlg-del-channel\"", "trash-2")], icon="ellipsis", button_class="icon-btn", aria_label="More for Household email")),
            opens("Discord: #books", 'Webhook · administrators · all events · <span class="chip" data-tone="success">Connected</span>', "panel-channel",
                  extra=menu("m-ch2", "More for Discord", [("Send test", "send"), ("Pause channel", "pause"), "hr", ("Delete channel|data-dialog=\"dlg-del-channel\"", "trash-2")], icon="ellipsis", button_class="icon-btn", aria_label="More for Discord: #books")),
            opens("Pushover", 'Push · only me · failed downloads · <span class="chip" data-tone="muted">Paused</span>', "panel-channel"),
        ], action=f'<button class="btn" type="button" data-opens="panel-channel">{ic("plus")}Add channel</button>', h="h3") +
        card("Member events", "What members hear about their own requests.", [
            setting("Tell members when a requested book is in library", None, check(True)),
            setting("Tell administrators about new requests", "Only when a request needs approval.", check(True)),
        ], h="h3", admin=True) + savebar())
    panels = panel("panel-channel", "Discord: #books", f"""
<div class="field"><label for="ch-name">Name</label><input class="input" id="ch-name" value="Discord: #books"></div>
<div class="field"><label for="ch-svc">Service</label><select class="select" id="ch-svc"><option>Discord webhook</option><option>Email</option><option>Pushover</option><option>Other webhook</option></select></div>
<div class="field"><label for="ch-url">Webhook address</label><span class="hint" id="ch-urlh">Saved. Paste a new address to replace it.</span><input class="input" id="ch-url" type="password" aria-describedby="ch-urlh" placeholder="Saved"></div>
<fieldset><legend class="field__label">Who receives it</legend><div class="segmented"><label><input type="radio" name="ch-who"><span>Everyone</span></label><label><input type="radio" name="ch-who" checked><span>Administrators</span></label><label><input type="radio" name="ch-who"><span>Only me</span></label></div></fieldset>
<fieldset><legend class="field__label">Events</legend><label class="check"><input type="checkbox" checked><span class="check__text">Book in library</span></label><label class="check"><input type="checkbox" checked><span class="check__text">Download failed or needs attention</span></label><label class="check"><input type="checkbox" checked><span class="check__text">New request needs approval</span></label></fieldset>
<div class="notice" data-tone="success" role="status">{ic("circle-check")}<div class="notice__body"><span class="notice__title">Test sent</span><p>Discord accepted the message at 14:02.</p></div></div>
<details class="disclosure"><summary>Delivery history <span class="disclosure__meta">last 3</span></summary><div class="disclosure__body"><ul class="rows">
<li class="row row--no-lead"><div><div class="row__title">The Glass Harbour is in library</div><div class="row__meta">1 Nov, 09:14</div></div><div class="row__side"><span class="chip" data-tone="success">Sent</span></div></li>
<li class="row row--no-lead"><div><div class="row__title">Lanterns Under Ice needs attention</div><div class="row__meta">30 Oct, 20:42</div></div><div class="row__side"><span class="chip" data-tone="success">Sent</span></div></li></ul></div></details>""",
        edit_foot("Save channel", ("Delete", "dlg-del-channel"), test=True))
    dialogs = remove_dialog("dlg-del-channel", "Delete the Discord: #books channel?", "Storyarr stops sending to this webhook. Its delivery history is deleted. Other channels are not affected.", "Delete channel")
    return gpage("general", "General", ["<strong>Display is called Display</strong>, not \"General\" like its group. Its three resets and three status lines become one save bar; the card hints say what is saved in this browser and what is saved to your account.",
                                        "<strong>Notification channels are rows</strong>; add, edit, test and delivery history open in a slide-out next to the list instead of a form at the top of the page. <strong>Deleting a channel now asks first</strong> (today it deletes at once)."],
                 [display, notif], panels, dialogs, [("phone=1", "Display rows stack; the save bar stays at the foot of the window.", 760), ("phone=1&open=panel-channel", "Channel editing in the slide-out, full width.", 760)])


def accounts():
    signin = section_block(True, "Sign-in", "How you sign in, and how everyone else can.",
        card("Your sign-in methods", "Methods linked to your account, Alex.", [
            opens("Password", 'Set 4 March 2025 · <span class="chip" data-tone="success">Set up</span>', "panel-password", "Change password", icon="key-round"),
            opens("Household single sign-on", 'Identity provider · linked 2 June 2025 · <span class="chip" data-tone="success">Linked</span>', "panel-oidc", "Manage"),
            setting("Plex", f'<span class="chip" data-tone="muted">Not linked</span>', f'<button class="btn" type="button">{ic("link-2")}Link Plex</button>'),
        ]) + card("Sign-in for everyone", "Which sign-in methods are offered on the sign-in page.", [
            opens("Identity provider (OpenID Connect)", 'Household SSO · <span class="chip" data-tone="success">Connected</span>', "panel-oidc"),
            opens("Plex sign-in", '<span class="chip" data-tone="muted">Off</span>', "panel-oidc", "Set up", icon="plus"),
            setting("New people see the setup wizard", "Moved here from Users and access.", select(["On first sign-in", "Never"])),
        ], admin=True) + savebar())
    users = section_block(False, "Users and access", "People who can sign in, and what each role can do. Was called \"Users &amp; access\".",
        card("People", "3 people", [
            opens("Alex", 'Administrator · signed in today', "panel-user"),
            opens("Robin", 'Member · requests need approval', "panel-user"),
            opens("Sam", 'Member · signed in 3 days ago', "panel-user"),
        ], action=f'<button class="btn" type="button" data-opens="panel-user">{ic("user-plus")}Add person</button>', h="h3") +
        card("Roles", "What each role can do", [
            opens("Administrator", "Everything, including Settings", "panel-role"),
            opens("Member", "Request books, follow authors, manage own lists", "panel-role"),
            opens("Guest", "Browse My library only", "panel-role"),
        ], action=f'<button class="btn" type="button" data-opens="panel-role">{ic("plus")}Add role</button>', h="h3"))
    panels = panel("panel-user", "Robin", f"""
<div class="field"><label for="u-name">Name</label><input class="input" id="u-name" value="Robin"></div>
<div class="field"><label for="u-role">Role</label><select class="select" id="u-role"><option>Member</option><option>Administrator</option><option>Guest</option></select></div>
<label class="check"><input type="checkbox" checked><span class="check__text">Requests need approval<span class="check__hint">An administrator approves each request in Activity, Wanted.</span></span></label>
<fieldset><legend class="field__label">Libraries Robin can use</legend><label class="check"><input type="checkbox" checked><span class="check__text">Fiction audiobooks</span></label><label class="check"><input type="checkbox" checked><span class="check__text">Fiction ebooks</span></label><label class="check"><input type="checkbox"><span class="check__text">Children's audiobooks</span></label></fieldset>
<section aria-labelledby="u-acc-h" style="display:grid;gap:var(--space-2)"><h3 id="u-acc-h">Account details</h3><dl class="facts"><dt>Created</dt><dd>12 May 2025</dd><dt>Last signed in</dt><dd>Yesterday, 21:40</dd><dt>Sign-in methods</dt><dd>Password, Household SSO</dd></dl></section>
<p class="small muted">If you close with unsaved changes, Storyarr asks before discarding them.</p>""",
        edit_foot("Save person", ("Delete account", "dlg-del-user"))) + \
        panel("panel-role", "Member", """<div class="field"><label for="r-name">Role name</label><input class="input" id="r-name" value="Member"></div>
<fieldset><legend class="field__label">Members can</legend><label class="check"><input type="checkbox" checked><span class="check__text">Request books</span></label><label class="check"><input type="checkbox" checked><span class="check__text">Follow authors and series</span></label><label class="check"><input type="checkbox"><span class="check__text">Approve requests</span></label><label class="check"><input type="checkbox"><span class="check__text">Change settings</span></label></fieldset>""",
        edit_foot("Save role", ("Delete role", "dlg-del-role"))) + \
        panel("panel-oidc", "Identity provider", f"""<div class="field"><label for="o-name">Name on the sign-in page</label><input class="input" id="o-name" value="Household SSO"></div>
<div class="field"><label for="o-iss">Issuer address</label><input class="input" id="o-iss" value="https://sso.example.test"></div>
<div class="field"><label for="o-id">Client ID</label><input class="input" id="o-id" value="storyarr"></div>
<div class="field"><label for="o-sec">Client secret</label><span class="hint" id="o-sech">Saved. Type a new secret to replace it.</span><input class="input" id="o-sec" type="password" aria-describedby="o-sech"></div>
<details class="disclosure"><summary>Advanced</summary><div class="disclosure__body"><div class="field"><label for="o-sc">Scopes</label><input class="input" id="o-sc" value="openid profile email"></div></div></details>""",
        edit_foot("Save and test", ("Remove provider", "dlg-del-oidc"))) + \
        panel("panel-password", "Change password", """<div class="field"><label for="p-cur">Current password</label><input class="input" id="p-cur" type="password" autocomplete="current-password"></div>
<div class="field"><label for="p-new">New password</label><span class="hint" id="p-newh">At least 12 characters.</span><input class="input" id="p-new" type="password" autocomplete="new-password" aria-describedby="p-newh"></div>""",
        '<button class="btn btn--primary" type="button">Change password</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>')
    dialogs = dialog("dlg-del-user", "Delete Robin's account?", '<p>Robin can no longer sign in. Their requests and lists are deleted; books in your libraries stay. This cannot be undone.</p><div class="field"><label for="du">Type DELETE to confirm</label><input class="input" id="du" autocomplete="off"></div>',
                     '<button class="btn btn--danger btn--primary" type="button" data-closes>Delete permanently</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>') + \
        remove_dialog("dlg-del-role", "Delete the Member role?", "2 people have this role. Choose another role for them before deleting it.", "Delete role") + \
        remove_dialog("dlg-del-oidc", "Remove the identity provider?", "People who sign in only with Household SSO will need a password. 2 people are affected.", "Remove provider")
    return gpage("accounts", "Accounts", ["<strong>No third tab level</strong>: Users and Roles are two cards on one page instead of a tab switch inside the section. One Edit per person, with Account details merged into the person's slide-out.",
                                         "<strong>Identity provider, Plex sign-in and first-run onboarding move to Sign-in</strong>, from the bottom of Users and access. No ampersand in the section name; no em dashes in its text."],
                 [signin, users], panels, dialogs, [("phone=1", "Sign-in rows stack.", 760), ("phone=1&open=panel-user", "A person's slide-out, full width; Delete account asks with a typed confirmation.", 760)])


def sources():
    reading = section_block(True, "Reading accounts", "Reading sites Storyarr reads your shelves and lists from. Was called \"Sources\", the same as its group and the download sources.",
        card("Goodreads", 'Connected as alex.reads · <span class="chip" data-tone="success">Connected</span>', [
            setting("Want to read", "Shelf · 48 books · checked 2 hours ago", select(["Check every 6 hours", "Check daily", "Do not check"], 220) + f'<button class="btn" type="button" data-opens="panel-list" style="margin-left:8px">Details<span class="visually-hidden"> Want to read</span></button>'),
            setting("Read next", "List · 18 books · checked 2 hours ago", select(["Check daily", "Check every 6 hours", "Do not check"], 220) + f'<button class="btn" type="button" data-opens="panel-list" style="margin-left:8px">Details<span class="visually-hidden"> Read next</span></button>'),
        ], action=f'<button class="btn" type="button" data-opens="panel-reading">{ic("pencil")}Edit connection<span class="visually-hidden"> Goodreads</span></button>') +
        card("StoryGraph", '<span class="chip" data-tone="muted">Not connected</span>', [
            setting("Connect StoryGraph", "Takes 3 steps; the slide-out walks you through them.", f'<button class="btn" type="button" data-opens="panel-storygraph">{ic("plug")}Connect StoryGraph</button>'),
        ]) + card("Hardcover", 'Uses the token in Metadata · <span class="chip" data-tone="success">Connected</span>', [
            setting("Want to read", "Shelf · 21 books", select(["Check daily", "Do not check"], 220)),
        ], action=f'<button class="btn" type="button" data-opens="panel-hardcover">{ic("pencil")}Edit connection<span class="visually-hidden"> Hardcover</span></button>') + savebar())
    meta = section_block(False, "Metadata", "Where book details come from and how Storyarr matches files to books.",
        card("Hardcover connection", "Book details, series and covers.", [
            opens("Hardcover API token", 'Tested today at 08:00 · <span class="chip" data-tone="success">Connected</span>', "panel-hardcover"),
        ], h="h3") + card("Catalogue defaults", "Used when a book has more than one source.", [
            setting("Preferred source", None, select(["Hardcover", "Open Library"])),
            setting("Language", "Books in other languages are hidden from Discover.", select(["English", "Any language"])),
        ], h="h3") + card("Enrichment and matching", None and "" or "How sure Storyarr must be before it matches a file by itself.", [
            setting("Match automatically above", "Below this, the file goes to Library review.", unit("85", "%")),
            setting("Fill in missing descriptions", None, check(True)),
            setting("Replace low-resolution covers", None, check(False)),
        ], h="h3") + card("Field overrides", "What happens to details you edited yourself.", [
            setting("Keep my edits when details refresh", None, check(True)),
        ], h="h3") + savebar())
    panels = panel("panel-hardcover", "Hardcover", f"""<div class="field"><label for="hc-t">API token</label><span class="hint" id="hc-th">Saved. Paste a new token to replace it. <a href="#">Get a token from Hardcover (opens in a new tab)</a></span><input class="input" id="hc-t" type="password" aria-describedby="hc-th"></div>
<div class="notice" data-tone="success" role="status">{ic("circle-check")}<div class="notice__body"><span class="notice__title">Connected</span><p>Tested today at 08:00. Signed in as alex.reads.</p></div></div>
<label class="check"><input type="checkbox" checked><span class="check__text">Read my Hardcover shelves too<span class="check__hint">They appear in Reading accounts.</span></span></label>""",
        edit_foot("Save and test", ("Disconnect", "dlg-disc"))) + panel("panel-reading", "Goodreads", f"""<div class="field"><label for="gr-u">Goodreads profile address</label><input class="input" id="gr-u" value="https://www.goodreads.com/user/show/000000-alex"></div>
<fieldset><legend class="field__label">Shelves to read</legend><label class="check"><input type="checkbox" checked><span class="check__text">Want to read</span></label><label class="check"><input type="checkbox"><span class="check__text">Currently reading</span></label></fieldset>""",
        edit_foot("Save and test", ("Disconnect", "dlg-disc"))) + panel("panel-storygraph", "Connect StoryGraph", f"""<ol class="steps" aria-label="Connection steps"><li aria-current="step">Export</li><li>Upload</li><li>Choose shelves</li></ol>
<p>StoryGraph has no public connection, so Storyarr reads an export file.</p>
<p><strong>Step 1.</strong> In StoryGraph, go to Manage account, then Export StoryGraph library. StoryGraph emails you a CSV file.</p>
<div class="field"><label for="sg-f">Export file</label><input class="input" id="sg-f" type="file" style="padding-top:9px"></div>""",
        '<button class="btn btn--primary" type="button">Continue</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>') + \
        panel("panel-list", "Want to read", """<dl class="facts"><dt>From</dt><dd>Goodreads shelf</dd><dt>Books</dt><dd>48 · 31 in your library</dd><dt>Last checked</dt><dd>Today, 12:00</dd></dl>
<div class="field"><label for="ls-n">Name in Storyarr</label><input class="input" id="ls-n" value="Want to read"></div>
<fieldset><legend class="field__label">New books on this list</legend><div class="option-cards"><label class="option-card"><input type="radio" name="ls-w" checked><strong>Add to Wanted</strong><small>You choose when to search.</small></label><label class="option-card"><input type="radio" name="ls-w"><strong>Request automatically</strong><small>Searched as soon as they appear.</small></label></div></fieldset>
<label class="check"><input type="checkbox"><span class="check__text">Show on Discover, For you</span></label>""", edit_foot("Save list", ("Remove list", "dlg-rm-list")))
    dialogs = remove_dialog("dlg-disc", "Disconnect Hardcover?", "Book details stop updating from Hardcover and its shelves stop being read. Books already in your library keep their details.", "Disconnect") + \
        remove_dialog("dlg-rm-list", "Remove Want to read from Storyarr?", "The list stops being checked. Books in your library and your Goodreads shelf are not changed.", "Remove list")
    return gpage("sources", "Sources", ["<strong>One card per reading site</strong> with its status and its tracked lists as rows, instead of three nested details blocks. Connecting, including the StoryGraph steps, happens in a slide-out; list details move from a modal to a slide-out.",
                                        "<strong>The Hardcover token has one home</strong> (Metadata) and opens the same slide-out from both sections. Catalogue defaults are no longer 70% hidden in an advanced block."],
                 [reading, meta], panels, dialogs, PHONE_DEFAULT + [("phone=1&open=panel-storygraph", "The StoryGraph steps in a slide-out on a phone.", 760)])


def library():
    libs = section_block(True, "Libraries", "Your library servers, who can use each library, and where files are kept.",
        card("Library servers", "Storyarr reads and updates these.", [
            opens("Audiobookshelf", 'http://audiobookshelf:13378 · 2 libraries · <span class="chip" data-tone="success">Connected</span>', "panel-server"),
            opens("Calibre-Web", 'http://calibre-web:8083 · 1 library · <span class="chip" data-tone="danger">Cannot connect</span>', "panel-server"),
        ], action=menu("m-add-server", "Add server", [("Audiobookshelf", None), ("Calibre-Web", None), ("Kavita", None), ("Plex", None)], "Add server", "plus")) +
        card("Library access", "Who can use each library.", [
            opens("Fiction audiobooks", "Everyone", "panel-access"),
            opens("Fiction ebooks", "Everyone", "panel-access"),
            opens("Children's audiobooks", "Alex and Sam", "panel-access"),
        ]) + card("Library folders", "Where imported books are saved.", [
            opens("Fiction audiobooks", '<code>/data/audiobooks</code> · 1.2 TB free', "panel-folder", "Change folder", icon="folder-open"),
            opens("Fiction ebooks", '<code>/data/ebooks</code> · 1.2 TB free', "panel-folder", "Change folder", icon="folder-open"),
        ]))
    naming = section_block(False, "File naming", "How Storyarr names folders and files when it imports a book. This section's save bar is the model for every other section.",
        card("Folder structure", "Folders inside each library folder.", [
            setting("Audiobooks", None, seg("fs-a", ["Author / Series / Book", "Author / Book", "Book"], "Author / Series / Book")),
            setting("Ebooks", None, seg("fs-e", ["Author / Series / Book", "Author / Book", "Book"], "Author / Book")),
        ], h="h3") + card("File names", "Parts of each file name, in order.", [
            setting("1. Series and book number", "For example: The Glass Harbour 02", f'<span class="actions"><button class="icon-btn" type="button" aria-label="Move Series and book number down">{ic("arrow-down")}</button><button class="icon-btn" type="button" aria-label="Remove Series and book number">{ic("x")}</button></span>'),
            setting("2. Title", "For example: Lanterns Under Ice", f'<span class="actions"><button class="icon-btn" type="button" aria-label="Move Title up">{ic("arrow-up")}</button><button class="icon-btn" type="button" aria-label="Move Title down">{ic("arrow-down")}</button></span>'),
            setting("3. Narrator", "For example: read by Sam Oduya", f'<span class="actions"><button class="icon-btn" type="button" aria-label="Move Narrator up">{ic("arrow-up")}</button><button class="icon-btn" type="button" aria-label="Remove Narrator">{ic("x")}</button></span>'),
            setting("Join parts with", None, select(["Space, dash, space ( - )", "Space", "Underscore"], 260)),
        ], action=f'<button class="btn" type="button">{ic("plus")}Add a part</button>', h="h3") +
        card("Preview", "With a book from your library.", [
            '<li style="padding:var(--space-4) 0"><code class="code-block">/data/audiobooks/\n  Mara Ellison/\n    The Glass Harbour/\n      The Glass Harbour 02 - Lanterns Under Ice - read by Sam Oduya.m4b</code></li>',
        ], h="h3") + savebar("Unsaved changes: Ebooks folder structure", True))
    folders = "".join(f'<li class="row row--opens"><span class="app-icon" aria-hidden="true">{ic("folder")}</span><div><div class="row__title"><button type="button">{n}</button></div><div class="row__meta">{m}</div></div><div class="row__side"></div></li>' for n, m in [("audiobooks", "2,104 folders"), ("ebooks", "1,560 folders"), ("downloads", "Downloads in progress"), ("kids", "88 folders")])
    panels = panel("panel-server", "Audiobookshelf", f"""<div class="notice" data-tone="success" role="status">{ic("circle-check")}<div class="notice__body"><span class="notice__title">Connected</span><p>Tested 2 minutes ago, version 2.17.</p></div></div>
<div class="field"><label for="sv-a">Server address</label><input class="input" id="sv-a" value="http://audiobookshelf:13378"></div>
<div class="field"><label for="sv-k">API key</label><span class="hint" id="sv-kh">Saved. Paste a new key to replace it.</span><input class="input" id="sv-k" type="password" aria-describedby="sv-kh"></div>
<fieldset><legend class="field__label">Libraries to use</legend><label class="check"><input type="checkbox" checked><span class="check__text">Fiction audiobooks</span></label><label class="check"><input type="checkbox" checked><span class="check__text">Children's audiobooks</span></label><label class="check"><input type="checkbox"><span class="check__text">Podcasts</span></label></fieldset>""",
        edit_foot("Save and test", ("Remove server", "dlg-rm-server"))) + \
        panel("panel-access", "Access: Children's audiobooks", """<fieldset><legend class="field__label">Who can use this library</legend><label class="check"><input type="checkbox" checked><span class="check__text">Alex</span></label><label class="check"><input type="checkbox"><span class="check__text">Robin</span></label><label class="check"><input type="checkbox" checked><span class="check__text">Sam</span></label></fieldset>""",
              edit_foot("Save access")) + \
        panel("panel-folder", "Choose a folder: Fiction audiobooks", f"""<nav aria-label="Folder path" class="small"><a href="#">/</a> / <a href="#">data</a> / <strong aria-current="location">audiobooks</strong></nav>
<div class="toolbar__search" style="max-width:none"><input class="input" type="search" aria-label="Filter folders" placeholder="Folder name"></div>
<ul class="rows">{folders}</ul><p class="small muted">Only folders Storyarr can write to are shown.</p>""",
              '<button class="btn btn--primary" type="button">Use /data/audiobooks</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>', wide=True)
    dialogs = remove_dialog("dlg-rm-server", "Remove Audiobookshelf?", "Storyarr stops reading its 2 libraries. Files on the disk are not touched, and you can add the server again.", "Remove server")
    return gpage("library", "Library", ["<strong>One way to add and edit</strong> in Libraries: today the section has a popover, an inline form and modals. Now an Add server menu in the card header, and every server, library and folder edits in a slide-out (the folder picker in a wide one).",
                                        "<strong>One status per server</strong> instead of two status widgets and a page notice for the test result. File naming keeps its builder; its join select grows from 22px to 44px."],
                 [libs, naming], panels, dialogs, PHONE_DEFAULT + [("phone=1&open=panel-folder", "The folder picker fills the width on phones.", 760)])


def downloads():
    srcs = section_block(True, "Download sources", "Where Storyarr searches for releases.",
        card("Sources", "Searched in this order. Change the order in Preferences.", [
            opens("MyAnonamouse", 'Torrents · ebooks and audiobooks · <span class="chip" data-tone="success">Connected</span>', "panel-source"),
            opens("Prowlarr", 'Torrents and Usenet · 6 indexers · <span class="chip" data-tone="success">Connected</span>', "panel-source"),
            opens("AudioBook Bay", 'Torrents · audiobooks · <span class="chip" data-tone="danger">Cannot connect</span>', "panel-source"),
            opens("Soulseek", '<span class="chip" data-tone="muted">Not set up</span> · set up here only (not also from Download clients)', "panel-source", "Set up", icon="plus"),
        ]))
    clients = section_block(False, "Download clients", "Where requested books are sent to download.",
        card("Download clients", "Storyarr sends each release to the first client that handles its type.", [
            opens("qBittorrent", 'Torrents · category storyarr · <span class="chip" data-tone="success">Connected</span>', "panel-client"),
            opens("SABnzbd", 'Usenet · category books · <span class="chip" data-tone="success">Connected</span>', "panel-client"),
        ], action=menu("m-add-client", "Add client", [("qBittorrent", None), ("Transmission", None), ("Deluge", None), ("SABnzbd", None), ("NZBGet", None)], "Add client", "plus"), h="h3") +
        card("Release blocklist", "Releases Storyarr will not download again.", [
            opens("14 blocked releases", "Last added 30 October", "panel-blocklist", "Open blocklist", icon="ban"),
        ], h="h3"))
    prefs = section_block(False, "Preferences", "What Storyarr prefers when it chooses a release. Storage reserve and Download recovery moved here from Download clients.",
        f'<div class="toolbar" style="max-width:880px"><div class="toolbar__row"><fieldset class="segmented" aria-label="Applies to"><legend class="visually-hidden">Applies to</legend><label><input type="radio" name="pf-scope" checked><span>Everyone</span></label><label><input type="radio" name="pf-scope"><span>Only me</span></label></fieldset><span class="toolbar__count">Only me: values you do not change are inherited from Everyone.</span></div></div>' +
        card("Formats", "In order of preference.", [
            setting("Ebook formats", None, select(["EPUB, then AZW3, then PDF", "AZW3, then EPUB"], 280)),
            setting("Audiobook formats", None, select(["M4B, then MP3", "MP3, then M4B"], 280)),
        ], h="h3") + card("Ranking and sources", None or "How releases are scored.", [
            setting("Minimum score", "Releases below this wait for you in Activity.", unit("50", "points")),
            setting("Prefer freeleech", None, check(True)),
        ], h="h3") + card("Narrators", "For audiobooks.", [
            setting("Prefer the narrator of earlier books in a series", None, check(True)),
            setting("Skip abridged recordings", None, check(True)),
        ], h="h3") + card("Audiobook processing", "After a download finishes.", [
            setting("Merge MP3 files into one M4B", "Keeps chapters.", check(False)),
        ], h="h3") + card("Storage reserve", "Moved from Download clients.", [
            setting("Keep this much space free", "Downloads wait when the disk has less.", unit("50", "GB")),
        ], h="h3") + card("Download recovery", "Moved from Download clients.", [
            setting("A download has stalled after", None, unit("6", "hours")),
            setting("Then", None, select(["Block it and search again", "Tell me and wait"], 260)),
        ], h="h3") + savebar())
    auto = section_block(False, "Automation", "What Storyarr does by itself. Three open cards instead of three closed rows.",
        card("New follows", "When you follow an author or series.", [setting("Request books already published", None, select(["Add to Wanted", "Request automatically", "Do nothing"])),], h="h3") +
        card("Wanted books", None or "Books waiting for a release.", [setting("Search again every", None, unit("6", "hours")), setting("Give up after", "The request moves to History as Failed.", unit("90", "days"))], h="h3") +
        card("Deleted books", "When a book is deleted from a library server.", [setting("Then", None, select(["Keep it in Storyarr as Not requested", "Request it again"], 300))], h="h3") + savebar())
    panels = panel("panel-source", "MyAnonamouse", f"""<div class="notice" data-tone="success" role="status">{ic("circle-check")}<div class="notice__body"><span class="notice__title">Connected</span><p>Tested 5 minutes ago. Network check passed: IP address matches the session.</p></div></div>
<div class="field"><label for="ma-c">Session cookie</label><span class="hint" id="ma-ch">Saved. Paste a new cookie to replace it.</span><input class="input" id="ma-c" type="password" aria-describedby="ma-ch"></div>
<fieldset><legend class="field__label">Search for</legend><label class="check"><input type="checkbox" checked><span class="check__text">Ebooks</span></label><label class="check"><input type="checkbox" checked><span class="check__text">Audiobooks</span></label></fieldset>
<details class="disclosure"><summary>Advanced</summary><div class="disclosure__body"><div class="field"><label for="ma-r">Minimum seeders</label><input class="input" id="ma-r" value="1" inputmode="numeric"></div></div></details>""",
        edit_foot("Save and test", ("Remove source", "dlg-rm-src"))) + \
        panel("panel-client", "qBittorrent", f"""<div class="notice" data-tone="success" role="status">{ic("circle-check")}<div class="notice__body"><span class="notice__title">Connected</span><p>Tested 2 minutes ago, version 5.0.3.</p></div></div>
<section aria-labelledby="cl-1" style="display:grid;gap:var(--space-3)"><h3 id="cl-1">Connection</h3>
<div class="field"><label for="cl-a">Server address</label><input class="input" id="cl-a" value="http://qbittorrent:8080"></div>
<div class="field"><label for="cl-u">Username</label><input class="input" id="cl-u" value="admin" autocomplete="off"></div>
<div class="field"><label for="cl-p">Password</label><span class="hint" id="cl-ph">Leave blank to keep the saved password.</span><input class="input" id="cl-p" type="password" aria-describedby="cl-ph"></div></section>
<section aria-labelledby="cl-2" style="display:grid;gap:var(--space-3)"><h3 id="cl-2">Download folder</h3>
<div class="field"><label for="cl-c">Category</label><span class="hint" id="cl-ch">Letters, numbers, - and _ only.</span><input class="input" id="cl-c" value="storyarr" aria-describedby="cl-ch"></div>
<dl class="facts"><dt>Folder</dt><dd><code>/data/torrents/storyarr</code></dd></dl></section>
<section aria-labelledby="cl-3" style="display:grid;gap:var(--space-3)"><h3 id="cl-3">Folder mappings</h3><p class="small muted">Only needed when qBittorrent sees the folder under a different path.</p>
<ul class="rows"><li class="row row--no-lead"><div><div class="row__title"><code>/downloads</code> in qBittorrent</div><div class="row__meta">is <code>/data/torrents</code> in Storyarr</div></div><div class="row__side"><button class="icon-btn icon-btn--bare" type="button" aria-label="Remove mapping /downloads">{ic("x")}</button></div></li></ul>
<button class="btn" type="button" style="justify-self:start">{ic("plus")}Add mapping</button></section>""",
        edit_foot("Save and test", ("Remove client", "dlg-rm-client"))) + \
        panel("panel-blocklist", "Release blocklist", f"""<div class="field"><label for="bl-q">Search blocked releases</label><input class="input" id="bl-q" type="search"></div>
<ul class="rows"><li class="row row--no-lead"><div><div class="row__title">Lanterns.Under.Ice.EPUB</div><div class="row__meta">MyAnonamouse · stalled at 62% · 30 Oct</div></div><div class="row__side"><button class="btn btn--compact" type="button" onclick="SharedComponents.toast('Lanterns.Under.Ice.EPUB removed from the blocklist. Undo')">Unblock<span class="visually-hidden"> Lanterns.Under.Ice.EPUB</span></button></div></li>
<li class="row row--no-lead"><div><div class="row__title">Moth.Season.MP3.64kbps</div><div class="row__meta">Prowlarr · below minimum quality · 22 Oct</div></div><div class="row__side"><button class="btn btn--compact" type="button">Unblock<span class="visually-hidden"> Moth.Season.MP3.64kbps</span></button></div></li></ul>
<p class="small muted">Unblocking shows a confirmation with Undo, so a slip is easy to reverse.</p>""", wide=True)
    dialogs = remove_dialog("dlg-rm-src", "Remove MyAnonamouse?", "Storyarr stops searching it. Downloads in progress carry on.", "Remove source") + \
        remove_dialog("dlg-rm-client", "Remove qBittorrent?", "Books already downloaded stay where they are. Downloads in progress stop being tracked.", "Remove client")
    return gpage("downloads", "Downloads", ["<strong>Download clients holds clients only</strong>: rows and one Add client menu instead of six Connect buttons, an inline form and cards five levels deep. Add and edit open a slide-out with Connection, Download folder and Folder mappings sections.",
                                            "<strong>Storage reserve and Download recovery move to Preferences</strong> as open cards; the blocklist opens in a slide-out, and unblocking offers Undo. Every source edits in a slide-out with the same footer; Soulseek is set up in one place.",
                                            "<strong>Preferences scope is a view switch</strong> (Everyone, Only me) at the top, with one help text instead of six identical \"About download preferences\" buttons."],
                 [srcs, clients, prefs, auto], panels, dialogs, PHONE_DEFAULT + [("phone=1&open=panel-client", "A download client's slide-out on a phone.", 760)])


def system():
    logs_rows = [("22:41", ("danger", "Error"), "Download", "SABnzbd did not answer within 10 seconds."),
                 ("22:40", ("", "Info"), "Lists", "Checked 4 reading lists. 2 new books added to Wanted."),
                 ("22:12", ("warning", "Warning"), "Import", "Moth Season part 2 could not be read. Sent to Library review."),
                 ("21:00", ("", "Info"), "Search", "Searched 4 sources for 9 Wanted books.")]
    trs = "".join(f'<tr><td data-label="Time" class="numeric">{t}</td><td data-label="Level"><span class="chip" data-tone="{c[0]}">{c[1]}</span></td><td data-label="Type">{ty}</td><td data-label="Message"><button class="btn btn--quiet btn--compact" type="button" data-opens="panel-log" style="padding:0;white-space:normal;text-align:left;color:inherit;font-weight:400">{m}</button></td></tr>' for t, c, ty, m in logs_rows)
    logs = section_block(True, "Logs", "What Storyarr did in the background, newest first.",
        f"""<div class="toolbar"><div class="toolbar__row">
<div class="toolbar__search"><input class="input" type="search" aria-label="Search logs" placeholder="Message"></div>
<div class="filter-chips" role="group" aria-label="Level">{chipbtn("Errors", "3")}{chipbtn("Warnings", "12")}</div>
{menu("m-log-type", "Type", [("*All types", None, "menuitemradio"), ("Download", None, "menuitemradio"), ("Import", None, "menuitemradio"), ("Lists", None, "menuitemradio"), ("Search", None, "menuitemradio")], "Type: All", None, True)}
<div class="toolbar__end"><span class="toolbar__count">1,208 entries today</span><button class="btn" type="button">{ic("heart-pulse")}Check background worker</button></div></div></div>
<div class="table-wrap" data-stack><table class="table"><thead><tr><th scope="col" aria-sort="descending"><button type="button">Time{ic("arrow-up-down")}</button></th><th scope="col">Level</th><th scope="col">Type</th><th scope="col">Message</th></tr></thead><tbody>{trs}</tbody></table></div>
<div class="load-more"><span>Showing 4 of 1,208 entries</span><button class="btn" type="button">Show 50 more</button></div>""")
    bg = section_block(False, "Background work", "Jobs Storyarr runs on a schedule. The repeated heading and the borrowed checkbox list are gone.",
        card("Scheduled jobs", "Turn a job off to stop it running; it can still be run by hand.", [
            setting("Check followed authors and series", "Every 6 hours · last run 18:00", check(True)),
            setting("Check reading lists", "Every 2 hours · last run 22:40", check(True)),
            setting("Search for Wanted books", "Every 6 hours · last run 21:00", check(True)),
            setting("Back up settings", "Daily at 03:00 · last run today", check(True)),
        ], h="h3") + savebar())
    up = section_block(False, "Upgrades and backups", "The main setting comes first now, instead of last and collapsed.",
        card("Upgrades", 'Version 1.10.0 · <span class="chip" data-tone="success">Up to date</span>', [
            setting("Upgrade automatically", "On: Storyarr backs up your settings first and keeps the defaults for anything new.", check(True)),
            setting("Release notes", "What changed in each version.", f'<button class="btn" type="button" data-opens="panel-release-notes">{ic("file-text")}Read release notes</button>'),
        ], h="h3") + card("Backups", "Made before every upgrade and every night.", [
            setting("Before upgrade to 1.10.0", "28 October 2026 · 4.2 MB", f'<button class="btn" type="button">{ic("download")}Download<span class="visually-hidden"> backup from 28 October</span></button>'),
            setting("Nightly", "Today, 03:00 · 4.3 MB", f'<button class="btn" type="button">{ic("download")}Download<span class="visually-hidden"> nightly backup</span></button>'),
        ], h="h3") + card("Restore previous version", "Goes back to 1.9.2 and its backup. Changes since the upgrade are lost.", [
            setting("Restore version 1.9.2", None, f'<button class="btn btn--danger" type="button" data-dialog="dlg-restore">{ic("rotate-ccw")}Restore 1.9.2</button>'),
        ], h="h3") + savebar())
    panels = panel("panel-log", "Error: Download", f"""<dl class="facts"><dt>Time</dt><dd>2 November 2026, 22:41:07</dd><dt>Type</dt><dd>Download</dd><dt>Book</dt><dd><a href="storyarr-book.html">The Quiet Engine</a></dd><dt>Download client</dt><dd>SABnzbd</dd></dl>
<p>SABnzbd did not answer within 10 seconds. Storyarr tries again in 5 minutes. Check that SABnzbd is running, then select <strong>Test</strong> in Download clients.</p>
<details class="disclosure"><summary>Technical details</summary><div class="disclosure__body"><code class="code-block">GET http://sabnzbd:8080/api?mode=queue
timeout after 10000 ms
attempt 2 of 3</code></div></details>""", '<a class="btn" href="storyarr-settings-downloads.html">Open Download clients</a><button class="btn btn--quiet" type="button" data-copy="SABnzbd timeout 22:41:07">Copy details</button>')
    dialogs = dialog("dlg-restore", "Restore version 1.9.2?", "<p>Storyarr stops, restores the backup from 28 October 2026 and starts version 1.9.2. Requests and settings changed since then are lost. It takes about 2 minutes.</p>",
                     '<button class="btn btn--danger btn--primary" type="button" data-closes>Restore 1.9.2</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>')
    return gpage("system", "System", ["<strong>Logs use the section toolbar and a table</strong>; a log entry opens in a slide-out instead of expanding a row with a 24px button, so rows no longer jump.",
                                      "<strong>Restore is a dialog</strong> instead of an inline confirm, and release notes open in a slide-out."],
                 [logs, bg, up], panels, dialogs, [("phone=1", "Log rows stack into cards on phones.", 760), ("phone=1&open=panel-log", "A log entry in the slide-out.", 760)])


def build():
    return [general(), accounts(), sources(), library(), downloads(), system()]
