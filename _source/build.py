"""Build index.html from content.py.

python3 build.py preview  -> images inlined as data URIs (for the private Claude preview)
python3 build.py site OUT -> images as files (for GitHub Pages)
"""
import base64, html, pathlib, sys, re
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import content as C

ASSETS = pathlib.Path("/home/claude/site-assets")
COVERS = ASSETS / "covers"
e = html.escape
MODE = "preview"

ICONS = {
    "instagram": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="17.4" cy="6.6" r="1.4" fill="currentColor"/></svg>',
    "tiktok": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.2 3h3c.3 2.2 1.7 3.6 3.8 3.9v3c-1.5 0-2.8-.4-3.9-1.1v6.3a5.6 5.6 0 1 1-5.6-5.6c.3 0 .6 0 .9.1v3.1a2.6 2.6 0 1 0 1.8 2.4V3z" fill="currentColor"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="3.5" fill="currentColor"/><rect x="6.3" y="10" width="2.6" height="7.6" fill="var(--icon-cut)"/><circle cx="7.6" cy="7.2" r="1.6" fill="var(--icon-cut)"/><path d="M10.9 10h2.5v1.1c.5-.8 1.4-1.3 2.6-1.3 2 0 3 1.2 3 3.5v4.3h-2.6v-3.9c0-1.1-.4-1.7-1.3-1.7s-1.6.6-1.6 1.8v3.8h-2.6z" fill="var(--icon-cut)"/></svg>',
    "pinterest": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9.5" fill="currentColor"/><path d="M12.4 5.6c-3.7 0-5.6 2.6-5.6 4.8 0 1.3.5 2.5 1.6 2.9.2.1.3 0 .4-.2l.2-.6c0-.2 0-.3-.1-.4-.3-.4-.5-.9-.5-1.5 0-2 1.5-3.7 3.8-3.7 2.1 0 3.2 1.3 3.2 3 0 2.2-1 4.1-2.5 4.1-.8 0-1.4-.7-1.2-1.5.2-1 .7-2 .7-2.7 0-.6-.3-1.1-1-1.1-.8 0-1.4.8-1.4 1.9 0 .7.2 1.2.2 1.2l-1 4.1c-.2.9-.1 2.1 0 2.8h.6c.4-.6 1.1-1.9 1.3-2.7l.5-1.9c.3.5 1 .9 1.8.9 2.4 0 4-2.2 4-5.1 0-2.2-1.9-4.3-4.9-4.3z" fill="var(--icon-cut)"/></svg>',
}
PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l10.5-6.5z" fill="currentColor"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h12m-5-6 6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SEARCH = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2.8"/><path d="m15.5 15.5 5 5" stroke="currentColor" stroke-width="2.8" stroke-linecap="round"/></svg>'


def img_src(key):
    if MODE == "preview":
        return "data:image/webp;base64," + base64.b64encode((COVERS / f"{key}.webp").read_bytes()).decode()
    return f"covers/{key}.webp"


def a(href, inner, cls):
    return f'<a class="{cls}" href="{e(href)}" target="_blank" rel="noopener">{inner}</a>'


def peek(url, label="Peek inside my classroom"):
    return a(url, f'<span class="peek-play">{PLAY}</span><span>{e(label)}</span>', "peek")


def cover(p):
    if p.get("img"):
        return f'<div class="cover"><img src="{img_src(p["img"])}" alt="" loading="lazy"></div>'
    return f'<div class="cover cover-text"><span>{e(p.get("cv", p["t"]))}</span></div>'


FOLDER = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6.5A1.5 1.5 0 0 1 4.5 5h4.6l2 2.2h8.4A1.5 1.5 0 0 1 21 8.7v9.8a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 18.5z" fill="currentColor"/></svg>'


def drive_window(title, folders, cls=""):
    rows = "".join(f'<li>{FOLDER}<span>{e(f)}</span></li>' for f in folders)
    return f'''<div class="drive {cls}" role="img" aria-label="Folders inside the {e(title)}">
  <div class="drive-bar"><span></span><span></span><span></span><b>{e(title)}</b></div>
  <ul>{rows}</ul>
</div>'''


def card(p, tone):
    tags = []
    if p.get("best"):
        tags.append('<span class="tag tag-best">Best seller</span>')
    if p.get("free") or p["s"] == "free":
        tags.append('<span class="tag tag-free">Free</span>')
    if p.get("tpt"):
        tags.append('<span class="tag">On TPT</span>')
    cta = "Get it free" if (p.get("free") or p["s"] == "free") else "Shop now"
    reel = peek(p["r"]) if p.get("r") else ""
    inside = ""
    if p.get("inside"):
        folders = getattr(C, p["inside"])
        inside = f'<details class="inside"><summary>See what\'s inside the Drive</summary>{drive_window(p["t"], folders, "drive-small")}</details>'
        p = dict(p, kw=p.get("kw", "") + " " + " ".join(folders))
    search = " ".join([p["t"], p["d"], p.get("kw", ""), "free" if (p.get("free") or p["s"] == "free") else ""]).lower()
    return f'''<article class="card card-{tone}" data-search="{e(search)}">
  {cover(p)}
  <div class="card-body">
    <div class="card-tags">{"".join(tags)}</div>
    <h4>{e(p["t"])}</h4>
    <p>{e(p["d"])}</p>
    <div class="card-actions">{a(p["u"], e(cta) + ARROW, "btn btn-small")}{reel}</div>
    {inside}
  </div>
</article>'''


def socials(cls):
    return "".join(a(url, f'{ICONS[key]}<span>{e(name)}</span>', f"social {cls}") for key, name, url in C.SOCIALS)


def head(title, sub, hid, extra="", eyebrow=""):
    eb = f'<p class="eyebrow">{e(eyebrow)}</p>' if eyebrow else ""
    return f'<div class="block-head">{eb}<h2 id="{hid}" class="section-title">{e(title)}</h2><p class="block-sub">{e(sub)}</p>{extra}</div>'


def build():
    logo_bytes = (ASSETS / "logo-560.webp").read_bytes()
    if MODE == "preview":
        logo_src = "data:image/webp;base64," + base64.b64encode(logo_bytes).decode()
        fav = '<link rel="icon" href="data:image/png;base64,' + base64.b64encode((ASSETS / "favicon.png").read_bytes()).decode() + '">'
    else:
        logo_src = "logo.webp"
        fav = '<link rel="icon" href="favicon.png">'

    by = lambda s: [p for p in C.PRODUCTS if p["s"] == s]
    tones = {"ela": "pink", "history": "blue", "projects": "violet", "setup": "sun"}

    quick = "".join(
        a(url, f'<span class="q-title">{e(t)}</span><span class="q-sub">{e(sub)}</span><span class="q-arrow">{ARROW}</span>', "quick")
        for t, sub, url in C.QUICK_LINKS
    )

    bs = C.BEST_SELLER
    bs_stats = "".join(f"<li>{e(s)}</li>" for s in bs["stats"])
    inside_bits = []
    if bs.get("inside_doc"):
        inside_bits.append(a(bs["inside_doc"], "See everything that's in the Drive", "inside-link"))
    if bs.get("tour_video"):
        inside_bits.append(a(bs["tour_video"], f'<span class="peek-play">{PLAY}</span><span>Watch a video tour of the Drive</span>', "peek"))
    inside_link = f'<div class="inside-row">{"".join(inside_bits)}</div>' if inside_bits else ""

    sp = C.SPOTLIGHT
    sp_buttons = "".join(a(u, e(t) + ARROW, "btn btn-glow" if i == 0 else "btn btn-ghost") for i, (t, u) in enumerate(sp["buttons"]))
    spooky_cards = "".join(card(p, "night") for p in by("spooky"))

    reel_link = f'''<a class="reel hide-on-search" href="{e(sp["reel"])}" target="_blank" rel="noopener">
          <span class="reel-label">Peek inside my classroom</span>
          <span class="reel-play">{PLAY}</span>
          <span class="reel-title">{e(sp["reel_title"])}</span>
          <span class="reel-sub">Watch on Instagram</span>
        </a>'''
    if MODE == "preview":
        reel_block = reel_link
    else:
        reel_block = f'''<div class="reel reel-embed hide-on-search">
          <span class="reel-label">Peek inside my classroom</span>
          <blockquote class="instagram-media" data-instgrm-permalink="{e(sp["reel"])}?utm_source=ig_embed" data-instgrm-version="14">
            <a href="{e(sp["reel"])}" target="_blank" rel="noopener" class="reel-fallback"><span class="reel-play">{PLAY}</span><span class="reel-title">{e(sp["reel_title"])}</span><span class="reel-sub">Watch on Instagram</span></a>
          </blockquote>
        </div>'''

    cs = C.CLAUDE_SITE
    claude_cta = f'''<div class="cta-box cta-claude">
      <div class="cta-copy"><p class="eyebrow">{e(cs["eyebrow"])}</p><h3 class="cta-title">{e(cs["headline"])}</h3><p>{e(cs["body"])}</p>
      {a(cs["url"], "Visit Claude for Teachers" + ARROW, "btn")}</div>
    </div>'''
    bts_cta = f'''<div class="cta-box">
      <a class="cta-cover" href="{e(C.TC + "back-to-school-growing-drive/")}" target="_blank" rel="noopener"><img src="{img_src("bts")}" alt="Back to School Growing Google Drive" loading="lazy"></a>
      <div class="cta-copy"><p><strong>Want ALL my guides in one place?</strong> Grab my Back to School Growing Drive. It's packed with my AI tools and guides, plus everything you need to set up a smooth school year where YOU are in charge of your plans (not the other way around).</p>
      {a(C.TC + "back-to-school-growing-drive/", "Get the Back to School Drive" + ARROW, "btn")}</div>
    </div>'''

    gallery = "".join(f'<figure class="poe-frame"><img src="{img_src(k)}" alt="{e(alt)}" loading="lazy"></figure>' for k, alt in sp.get("gallery", []))
    gallery += '<p class="poe-credit">Portrait and illustrations: Edgar Allan Poe daguerreotype (1848), Gustave Dore\'s The Raven (1884), Harry Clarke (1919). Public domain.</p>'
    BAT = '<svg viewBox="0 0 64 30" aria-hidden="true"><path d="M32 9c-1.6-3.4-3.6-4.6-5.6-4.6.9 1.7.9 3 .1 4.1C23.6 5.6 17.6 4.7 12.4 6.8c3.9 1.8 6.2 4.6 6.3 8.4-3.1-1.9-7-2-10.4-.2 5.8 1.1 9.8 4.2 11.9 9 2.3-3.7 5.9-5.6 9.2-5.6L32 22l2.6-3.6c3.3 0 6.9 1.9 9.2 5.6 2.1-4.8 6.1-7.9 11.9-9-3.4-1.8-7.3-1.7-10.4.2.1-3.8 2.4-6.6 6.3-8.4-5.2-2.1-11.2-1.2-14.1 1.7-.8-1.1-.8-2.4.1-4.1-2 0-4 1.2-5.6 4.6z" fill="currentColor"/></svg>'
    bats = "".join(f'<span class="bat bat-{i}">{BAT}</span>' for i in range(1, 6))

    NAV = [
        ("best-seller", "PBL Drive", []),
        ("spotlight", "Spooky Season", []),
        ("shop", "Shop the Classroom", [(k, n) for k, n in C.SHOP_GROUPS]),
        ("teacher", "For Teachers", []),
        ("free", "Free Resources", []),
        ("find-me", "Find Me Everywhere", []),
        ("about", "About", []),
    ]
    nav_inline = "".join(f'<a href="#{i}">{e(n)}</a>' for i, n, _ in NAV if i in ("best-seller", "spotlight", "shop", "teacher", "free"))
    nav_menu = "".join(
        f'<a class="menu-main" href="#{i}">{e(n)}</a>' + "".join(f'<a class="menu-sub" href="#{si}">{e(sn)}</a>' for si, sn in subs)
        for i, n, subs in NAV)

    ff = C.FAN_FAVORITE
    shop_nav = "".join(f'<a class="chip chip-{tones[k]}" href="#{k}">{e(n)}</a>' for k, n in C.SHOP_GROUPS)
    shop = "".join(
        f'<div class="group" id="{k}"><h3 class="group-title"><span class="dot dot-{tones[k]}"></span>{e(n)}</h3>'
        f'<div class="grid">{"".join(card(p, tones[k]) for p in by(k))}</div></div>'
        for k, n in C.SHOP_GROUPS
    )
    teacher = "".join(card(p, "violet") for p in by("teacher"))
    free = "".join(card(p, "free") for p in by("free"))
    about = "".join(f"<p>{e(t)}</p>" for t in C.ABOUT)
    css = (pathlib.Path(__file__).parent / "style.css").read_text()
    js = (pathlib.Path(__file__).parent / "search.js").read_text()

    return f'''<title>Michaela Arabia: The Balanced Teach</title>
<meta name="description" content="Middle school ELA and history units, PBL, AI tools for teachers, and freebies from Michaela Arabia, The Balanced Teach.">
{fav}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lilita+One&family=Nunito:wght@600;700;800;900&family=Quicksand:wght@700&display=swap">
<style>
{css}
</style>

<nav class="topnav" aria-label="Site sections">
  <div class="wrap topnav-inner">
    <a class="topnav-name" href="#top">Michaela Arabia</a>
    <div class="topnav-links">{nav_inline}</div>
    <details class="topnav-menu" id="topnav-menu">
      <summary>Menu <span aria-hidden="true">&#9662;</span></summary>
      <div class="menu-panel">{nav_menu}</div>
    </details>
  </div>
</nav>

<header class="hero" id="top">
  <div class="wrap hero-inner">
    <img class="logo" src="{logo_src}" alt="Michaela, The Balanced Teach, @Middle_Teacher_Syndrome" width="560" height="561">
    <div class="hero-copy">
      <h1><span>Michaela</span> <span>Arabia</span></h1>
      <p class="tagline">The Balanced Teach</p>
      <p class="bio">{e(C.BIO)}</p>
      <nav class="socials" aria-label="Follow me">{socials("social-hero")}</nav>
    </div>
  </div>
</header>

<main>
  <section class="wrap quick-wrap" aria-label="Search">
    <form class="search" role="search" id="search-form">
      <label for="q" class="search-label">Looking for something?</label>
      <div class="search-box">
        {SEARCH}
        <input id="q" type="search" placeholder="Try Poe, PBL, free, AI, back to school" autocomplete="off">
        <button type="button" id="q-clear" class="search-clear" hidden>Clear</button>
      </div>
      <p class="search-status" id="q-status" aria-live="polite"></p>
    </form>
  </section>

  <section class="wrap best hide-on-search" id="best-seller" aria-labelledby="best-h">
    <div class="best-box">
      <a class="best-cover" href="{e(bs["url"])}" target="_blank" rel="noopener"><img src="{img_src(bs["img"])}" alt="The Growing Project Based Learning Google Drive" loading="lazy"></a>
      <div class="best-copy">
        <p class="eyebrow">{e(bs["eyebrow"])}</p>
        <h2 id="best-h" class="best-title">{e(bs["headline"])}</h2>
        <p>{e(bs["body"])}</p>
        <ul class="best-list">{bs_stats}</ul>
        {inside_link}
        <div class="btn-row">{a(bs["url"], "Get the PBL Drive" + ARROW, "btn btn-big")}{peek(bs["reel"])}</div>
      </div>
    </div>
  </section>

  <section class="spotlight search-zone" id="spotlight" aria-labelledby="spot-h">
    <div class="moon" aria-hidden="true"></div>{bats}
    <div class="wrap">
      <div class="spot-head hide-on-search">
        <p class="eyebrow eyebrow-glow">{e(sp["eyebrow"])}</p>
        <h2 id="spot-h" class="glow-title">{e(sp["headline"])}</h2>
        <p class="spot-body">{e(sp["body"])}</p>
        <div class="btn-row btn-row-center">{sp_buttons}</div>
      </div>
      <div class="spot-feature hide-on-search">
        <div class="spot-reel">{reel_block}</div>
        <div class="poe-gallery" aria-label="Poe portrait and illustrations">{gallery}</div>
      </div>
      <div class="grid grid-night">
        {spooky_cards}
      </div>
    </div>
  </section>

  <section class="wrap fan hide-on-search" id="fan-favorite" aria-labelledby="fan-h">
    <div class="fan-box">
      <img class="fan-cover" src="{img_src(ff["img"])}" alt="" loading="lazy">
      <div class="fan-copy">
        <p class="eyebrow">{e(ff["eyebrow"])}</p>
        <h2 id="fan-h">{e(ff["headline"])}</h2>
        <p>{e(ff["body"])}</p>
        <div class="btn-row">{a(ff["url"], "Shop now" + ARROW, "btn")}{peek(ff["reel"])}</div>
      </div>
    </div>
  </section>

  <section class="wrap block search-zone" id="shop" aria-labelledby="shop-h">
    {head("Shop the Classroom", "The units and projects I actually teach in my own middle school classroom. Tap any one to peek inside and see the price.", "shop-h", f'<nav class="chips hide-on-search" aria-label="Jump to">{shop_nav}</nav>')}
    {shop}
  </section>

  <section class="wrap block search-zone" aria-labelledby="teacher-h" id="teacher">
    {head("For You, the Teacher", "AI, tech, and planning tools to get your time back. Because you deserve your weekends!", "teacher-h", claude_cta + bts_cta)}
    <div class="grid">{teacher}</div>
  </section>

  <section class="wrap block search-zone" aria-labelledby="free-h" id="free">
    {head("Free Resources", "Totally free! Try these first and see if my style works for your kiddos.", "free-h")}
    <div class="grid">{free}</div>
  </section>

  <p class="wrap no-results" id="no-results" hidden>Hmm, nothing matches that yet. Try another word, or check my <a href="https://www.teacherspayteachers.com/store/middle-teacher-syndrome" target="_blank" rel="noopener">TPT store</a>.</p>

  <section class="wrap block more hide-on-search" id="find-me" aria-labelledby="more-h">
    {head("Find Me Everywhere", "My Amazon faves, my TPT store, and even more freebies.", "more-h")}
    <div class="quick-grid">{quick}</div>
  </section>

  <section class="wrap about hide-on-search" id="about" aria-labelledby="about-h">
    <img class="about-logo" src="{logo_src}" alt="" width="560" height="561">
    <div class="about-copy">
      <h2 id="about-h" class="section-title">Hi, I'm Michaela!</h2>
      {about}
      <nav class="socials" aria-label="Follow me">{socials("social-about")}</nav>
    </div>
  </section>
</main>

<footer class="foot">
  <div class="wrap foot-inner">
    <p class="foot-name">Michaela Arabia <span>The Balanced Teach</span></p>
    <nav class="socials" aria-label="Follow me">{socials("social-foot")}</nav>
    <p class="foot-small">@middle_teacher_syndrome &middot; &copy; 2026 Michaela Arabia</p>
  </div>
</footer>
<script>
{js}
</script>
{'' if MODE == "preview" else '<script async src="https://www.instagram.com/embed.js"></script>'}
'''


if __name__ == "__main__":
    MODE = sys.argv[1]
    out = build()
    assert "—" not in out and "–" not in out, "dash found"
    if MODE == "preview":
        p = pathlib.Path("/tmp/preview/balanced-teach.html")
        p.parent.mkdir(exist_ok=True)
        p.write_text(out)
        print(p, len(out))
    else:
        d = pathlib.Path(sys.argv[2])
        page = "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n" + out.replace("<header", "</head>\n<body>\n<header", 1) + "\n</body>\n</html>\n"
        (d / "index.html").write_text(page)
        (d / "logo.webp").write_bytes((ASSETS / "logo-560.webp").read_bytes())
        (d / "favicon.png").write_bytes((ASSETS / "favicon.png").read_bytes())
        (d / "covers").mkdir(exist_ok=True)
        for f in COVERS.glob("*.webp"):
            (d / "covers" / f.name).write_bytes(f.read_bytes())
        print("site written", d)
