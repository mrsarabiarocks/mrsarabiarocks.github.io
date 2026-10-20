"""Build free-claude-guide/index.html (the Free Claude Guide page).

python3 guide.py OUT_SITE_DIR   -> writes OUT_SITE_DIR/free-claude-guide/index.html
Uses the homepage's style.css and helpers so the page matches the rest of the site.
Edit the content in the lists below, then rebuild.
"""
import pathlib, sys, urllib.parse
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import content as C
import build as B

e = B.e
TC = C.TC
HERE = pathlib.Path(__file__).parent

# Where the waitlist form sends signups. Swap this for the ThriveCart $0 product link once it exists.
# PLACEHOLDER: swap in the ThriveCart checkout link for The Teacher Helper Project when it exists.
TEACHER_HELPER_URL = "#teacher-helper"
WAITLIST_URL = ""          # e.g. TC + "claude-waitlist/"
WAITLIST_EMAIL = "mrsarabiarocks@gmail.com"


def ig(code):
    return f"https://www.instagram.com/reel/{code}/"


HL_AI = "https://www.instagram.com/stories/highlights/18204095536248045/"
HL_PBL = "https://www.instagram.com/stories/highlights/17861632432758922/"
HL_POE = "https://www.instagram.com/stories/highlights/17844653230766602/"
HL_TIPS = "https://www.instagram.com/stories/highlights/18121097227699014/"
OUTSIDERS = "https://claude.ai/public/artifacts/2df5f854-953e-4c0c-9c6c-d2101a53b97a"
BTS = TC + "back-to-school-growing-drive/"
PBL = TC + "pbl-growing-drive/"
ASK = "\n\nAsk me some questions to make sure I get the best output possible."

# ---------- Reels that play right on the page ----------
LEAD_REEL = (ig("Desvw-WTv6l"), "Claude builds my workshop boards")  # newest video, shown big at the top
TOP_REELS = [
    (ig("DbBoju3veLA"), "Claude + Canva: a year of slides"),
    (ig("DaGJH9sk1Qn"), "Lots of ways I use Claude"),
    (ig("DZdWKfXh55X"), "Backwards planning with Claude"),
]
MORE_REELS = [
    (ig("DazQIb2zTvd"), "Cowork builds my Canva"),
    (ig("DYD6ujaTbQF"), "Annotation packets with AI"),
    (ig("Dd-vBqSTP80"), "Claude runs my teacher business"),
]
HIGHLIGHTS = [
    (HL_TIPS, "Claude Tips", "Lots of ways I use it"),
    (HL_AI, "AI in the Classroom", "Real examples"),
    (HL_PBL, "PBL", "Project ideas"),
    (HL_POE, "Poe Projects", "Balance in action"),
]

# ---------- Ways I've used Claude in my classroom ----------
# (tone, title, what I did, [(button text, url), ...], reel url or "")
WAYS = [
    ("sun", "Reading workshop boards", "One screen for station rotations: color group schedule, station directions, a built-in timer, and a group points tracker. I made a Raven board and a Tell-Tale Heart board with an escape room station.", [], ig("Desvw-WTv6l")),
    ("pink", "Backwards-planned my PBL units", "I start with the final project and Claude maps the daily lessons backward from it.", [("Get the guide", TC + "pbl-backwards-planning-with-claude/")], ig("DZdWKfXh55X")),
    ("blue", "Made 180 days of agenda slides", "Claude fills the table, Canva Bulk Create spins up the whole year in one go.", [("Agenda Slides + guide", TC + "180-daily-agenda-slides-canvabulkcreate/")], ig("DbBoju3veLA")),
    ("violet", "Built annotation packets for ANY text", "Numbered paragraphs, margin prompts, vocab, and a teacher key in about 10 minutes.", [("Annotation Unlocked", TC + "annotation-unlocked/")], ig("DYD6ujaTbQF")),
    ("sun", "A study tool for my real students", "A student-facing Outsiders coach for theme, motif, conflict, plot, and symbolism. It refuses anything off-topic.", [("Open the live tool", OUTSIDERS)], ""),
    ("pink", "Interactive notebook pages", "Glue-in pages, launch plans, and grading for my comp notebooks.", [("Notebooks Unlocked", TC + "interactive-notebooks-unlocked/")], ig("DaQbqbBBCoc")),
    ("blue", "History graphic organizers", "Cause and Effect, Primary Source Analysis, SOAPSTONE, and notes organizers for 8th grade American History.", [], ""),
    ("violet", "Poe month projects", "Like the House of Usher real estate brochure: students annotate the house, then SELL it.", [("Usher mini unit", TC + "poe-usher-mini-unit-fully-editable/")], ig("DeE_B7VToyi")),
    ("sun", "Three readiness levels of one text", "Same ideas, same thinking, three different reading loads. Saves my prep period.", [], ""),
    ("pink", "Parent emails and newsletters", "The email I've been avoiding since Tuesday, drafted in my voice in 30 seconds.", [], ""),
    ("blue", "Organized my whole PBL Drive", "Claude audited every folder, flagged duplicates, and suggested a cleaner setup before moving a thing.", [("PBL Drive", PBL)], ""),
    ("violet", "Field trip and event logistics", "Roommate lists, buddy schedules, and graduation programs without the spreadsheet headache.", [], ""),
    ("sun", "My whole classroom website", "This site! Claude built it from my product list and keeps it up to date.", [("See the homepage", "/")], ""),
]

# ---------- Prompt sections ----------
# card: (title, use line, prompt, [(btn text, url, soft?)], (watch text, url) or None, note)
BEGINNER = [
    ("Copy-paste prompt", "Lesson and unit planning", "Start from the end and work backward. Claude drafts the plan, you keep the judgment. Build faster so you can teach better.", [
        ("Backwards-design a unit", "When you have a text or topic and a blank calendar staring at you.",
         "You are helping me plan a unit using backwards design. I teach [grade] [subject]. The unit is on [text or topic] and I have [number] class periods of [length] minutes.\n\nStart with the end: give me 3 possible summative assessments students could do to show mastery. For each, tell me what standard or skill it proves.\n\nThen, once I pick one, we will map the daily lessons backward from it. Ask me which assessment I want before you build the calendar.\n\nKeep it real for middle schoolers. No busywork." + ASK,
         [("Get my step-by-step guide here!", TC + "pbl-backwards-planning-with-claude/", False)], ("Watch: Backwards planning with Claude", ig("DZdWKfXh55X")), ""),
        ("Turn a standard into a lesson", "When you know the standard but not the lesson.",
         "I teach [grade] [subject]. Build me a single [length]-minute lesson that hits this standard: [paste standard].\n\nGive me: a hook that takes 5 minutes or less, the main activity, one check for understanding, and an exit ticket. Tell me exactly what I say and what students do.\n\nAssume I have zero prep time and a class that talks a lot." + ASK,
         [("See how I plan with PBL", PBL, False)], ("AI in the classroom", HL_AI), "Want to see how I plan lessons using project-based learning? Peek inside my Project Based Learning Google Drive to see what's inside."),
    ]),
    ("Copy-paste prompt", "Differentiation", "One lesson, three readiness levels, five minutes. This is the one that saves your prep period.", [
        ("Scaffolds for the kids who need them", "When you have IEPs, ELLs, and everyone in between.",
         "I am teaching this assignment to [grade]: [paste assignment].\n\nGive me a support version for: (1) students who need reading support, (2) English language learners, and (3) students who finish early and need a challenge.\n\nFor each, give me the actual modified directions and any sentence stems or word banks. Keep the learning goal identical for all of them." + ASK,
         [], ("See it in action", HL_AI), ""),
        ("Three readiness levels of the same text", "When one reading is too hard for half the room and too easy for the other half.",
         "Here is a reading passage for my [grade] [subject] class: [paste passage].\n\nRewrite it at 3 readiness levels while keeping the same key ideas and vocabulary goals:\n1. Below grade level (shorter sentences, more scaffolding)\n2. On grade level\n3. Above grade level (more complex text, a stretch question)\n\nFor each version, add 2 comprehension questions and 1 discussion question. Do not water down the thinking, just the reading load." + ASK,
         [], ("Claude tips", HL_TIPS), ""),
    ]),
    ("Copy-paste prompt", "Parent and admin emails", "The email you have been avoiding since Tuesday. Draft it in your voice, kind but firm, in 30 seconds.", [
        ("The tricky parent email", "When you need to be honest without starting a war.",
         "Help me write an email to a parent. Here is the situation: [describe what happened, plain and honest].\n\nTone: warm, professional, and clear. I am not apologizing for holding a standard, but I want the parent on my team. Keep it short. Lead with something positive about their kid if there is one. End with a specific next step.\n\nGive me two versions: one softer, one more direct." + ASK,
         [], ("Claude tips", HL_TIPS), ""),
        ("Newsletter or admin update in your voice", "When you have to write it and would rather do literally anything else.",
         "Write a [class newsletter / update to my admin] covering these points: [dump your bullet points here, messy is fine].\n\nMy voice: real, warm, a little dry, no corporate buzzwords, no exclamation-point overload. Short paragraphs. Make it skimmable. Then give me a subject line that people will actually open." + ASK,
         [], ("AI in the classroom", HL_AI), ""),
    ]),
    ("Copy-paste prompt", "PBL and creative projects", "This is my whole thing. Take any text or topic and turn it into a project kids actually want to do.", [
        ("Remix a lesson into a pop-culture project", "Shark Tank, Mythbusters, a newscast, a meme. Same standards, way more buy-in.",
         "I teach [grade] [subject]. We are studying [text or topic]. I want to turn it into a project modeled on [Shark Tank / Mythbusters / a news broadcast / a social media takeover / your idea].\n\nGive me: the project pitch in kid-friendly language, the steps students follow, what they produce, and a simple rubric tied to [standard or skill]. Keep it doable in [number] class periods.\n\nMake it fun but rigorous. I do not do busywork projects." + ASK,
         [("Grab my FREE PBL Prompt Guide", TC + "pblpromptguide/", False)], ("PBL demos", HL_PBL), ""),
        ("Build an annotation set from any text", "Speeches, primary sources, song lyrics, a chapter. Close reading with a purpose.",
         "Here is a text I want my [grade] students to annotate closely: [paste text or name it].\n\nGive me 6 to 8 annotation prompts that push real thinking (tone, word choice, author's purpose, connections to now). Write them as questions students answer in the margins.\n\nThen give me one short project they do after annotating to show they got it. Balance matters to me, so make at least part of this something they do on paper, by hand." + ASK,
         [("Annotation Unlocked: build packets with Claude", TC + "annotation-unlocked/", False), ("Free Annotations Guide (5 to 12)", TC + "annotations-guide-for-grades-5-12/", True)], ("Watch: how I annotate", ig("DX-s1VWzEqv")), ""),
    ]),
    ("Copy-paste prompt", "Workshop and station boards", "Run stations without repeating directions 40 times. One board on the screen shows every group where to go, what to do, and how much time is left.", [
        ("Build a reading workshop board", "When you have color groups rotating through stations and want everything on one screen.",
         "Build me a reading workshop board for my [grade] class as a single web page I can put on my classroom screen. The text is [text or topic].\n\nMy groups are [Blue, Red, Orange, Green] and they rotate through [number] blocks. The stations are: [station 1 and where it is], [station 2 and where it is], [station 3 and where it is]. One station is a teacher meeting with me.\n\nInclude: a schedule tab showing which station each group is at during each block, a directions tab with numbered steps, an example, and a sentence starter for every station, what to bring, a big countdown timer I can start and reset, and a points tracker for each group.\n\nMake it look like [theme, like a spooky Poe vibe], easy to read from the back of the room, and fun." + ASK,
         [], None, "Swap in your own stations. Mine have included an escape room, a choice board, and a teacher meeting."),
    ]),
    ("Copy-paste prompt", "Mastering Claude and Bulk Create", "The move that made me go viral: build the content once with Claude, then let Canva's Bulk Create spin up a whole year of slides in one go. This is how you make 180 things without making 180 things.", [
        ("Fill a Canva Bulk Create template", "Agenda slides, vocab cards, bell ringers, task cards. Anything you'd make one at a time.",
         "I want to mass-produce [180 daily agenda slides / vocab cards / bell ringers] in Canva using Bulk Create. First ask me what fields my template has (like Date, Day, Objective, Agenda, Homework).\n\nThen generate a clean table I can paste straight into Canva Bulk Create: one row per slide, columns matching my fields exactly. Fill it with [my topics and pacing], keep it [grade] appropriate, and do not skip days." + ASK,
         [("Hot Takes: my Bulk Create guide", TC + "guide-bulk-creation-for-teachers/", False), ("Whole-Year Agenda Slides + guide", TC + "180-daily-agenda-slides-canvabulkcreate/", True)], ("Watch: Claude + Canva", ig("DbBoju3veLA")), ""),
    ]),
]

ADVANCED = [
    ("Advanced", "Projects", "Build a Claude that already knows your classroom",
     "<b>New to Projects?</b> A Project is a saved workspace where you upload your files and set your instructions <em>once</em>. Everything you do inside it remembers your grade, your standards, and your voice. Set it up on a Sunday, save hours every week after.",
     "Starter setup", "Copy setup", [
        ("Your \"Classroom HQ\" project", "Stop re-typing your grade, standards, and style every single time. Set it once and every lesson comes out aligned and sounding like you.",
         "Create a new Project called \"Classroom HQ.\" Upload your pacing guide, your standards, one rubric, and one lesson that sounds like you. Then paste this into the project's custom instructions:\n\nYou are my teaching assistant for [grade] [subject]. Everything you make should align to the standards and pacing guide I uploaded and match the voice in my sample lesson: real, clear, a little dry, no busywork. Default to middle school reading levels. When I ask for a lesson or activity, tie it to a standard and keep prep low. Ask me the topic and how many days I have, then build." + ASK,
         [], ("Claude tips", HL_TIPS), ""),
        ("A project per novel or unit", "Reuse everything you built for The Outsiders, Poe, or Night without rebuilding it. The project becomes your unit's memory.",
         "Make a Project named for the text (e.g. \"The Outsiders Unit\"). Upload the reading, your annotation sets, and past projects. Paste into custom instructions:\n\nThis project holds everything for my [text] unit with [grade]. Treat the uploaded reading, annotations, and projects as the source of truth. When I ask for something new (a quiz, a bell ringer, a differentiated version, a project), match the style and rigor of what's already here and keep it aligned to [standard]." + ASK,
         [("PBL Project Drive", PBL, False), ("Poe: Tell-Tale Heart", TC + "poe-tell-tale-heart/", True), ("Poe: House of Usher", TC + "poe-usher-mini-unit-fully-editable/", True), ("Poe: The Raven", TC + "edgar-allan-poe-the-raven-mini-unit/", True)],
         ("See my live Outsiders example", OUTSIDERS), "Need completed novel or short-story projects? Grab mine above."),
        ("Your grading and feedback partner", "Feedback that matches your rubric and still sounds like you, in a fraction of the time. You stay the teacher, it drafts the words.",
         "Create a Project called \"Feedback.\" Upload your rubric and 2 to 3 samples of feedback you have written. Paste into custom instructions:\n\nYou help me draft feedback on student work for [grade] [subject]. Always score against the uploaded rubric and explain it in kid-friendly language. Match the tone of my samples: warm, specific, honest, growth-focused. Give 2 glows and 1 grow. Never rewrite the student's work for them." + ASK,
         [], None, "Keep it FERPA-safe: strip student names or use initials before you paste any work."),
    ]),
    ("Advanced", "Skills", "Teach Claude your signature moves",
     "<b>New to Skills?</b> A Skill is a set of instructions you save once and trigger by name. It is how you teach Claude a move you make all the time, so you never re-type the directions again. Build the skill once, call it forever.",
     "Skill instructions to save", "Copy skill", [
        ("The PBL Remix Machine", "Turn any text or topic into a project kids beg to do, on command. This is my whole brand in one saved skill.",
         "When I give you a text or topic and a format (Shark Tank, Mythbusters, a newscast, a social media takeover, a meme), turn it into a student project. Always output: a kid-friendly pitch, numbered student steps, what they turn in, and a simple 4-row rubric tied to the standard I name. Middle school level. Fun but rigorous. No busywork. If I do not give a format, suggest three." + ASK,
         [("Grab my FREE PBL Prompt Guide", TC + "pblpromptguide/", False)], ("PBL demos", HL_PBL), ""),
        ("The Annotation-Set Generator", "Your exact annotation format from any text in seconds, every time, without re-explaining it.",
         "When I give you a text, create an annotation set in my format: 6 to 8 numbered margin questions that push thinking about tone, word choice, author's purpose, and connections to today. Then add one short after-reading task, and make at least part of it something students do on paper by hand. Keep it [grade] level." + ASK,
         [("Annotation Unlocked: teach Claude to build your packets", TC + "annotation-unlocked/", False), ("Ready-to-go sets (5 to 10 ELA)", PBL, True)], ("Poe demo", HL_POE), ""),
        ("The 3-Level Differentiator", "One passage, three readiness levels, same thinking, on demand. The skill that quietly saves your prep period.",
         "When I paste a passage, rewrite it at 3 readiness levels (below, on, and above grade level) while keeping the same key ideas and vocabulary goals. For each level add 2 comprehension questions and 1 discussion question. Water down the reading load, never the thinking. Label each level clearly." + ASK,
         [], None, ""),
    ]),
    ("Advanced", "Cowork", "Put Claude to work on your actual desktop",
     "<b>New to Cowork?</b> Cowork is Claude on your computer. It can open your files, organize folders, build things, and even run tasks on a schedule. This is where Claude stops giving advice and starts doing the work.",
     "Say this in Cowork", "Copy task", [
        ("Clean up my Drive", "Turn a chaotic resource folder into something you can actually find things in. I did exactly this with my whole PBL Drive.",
         "Connect to my Google Drive and audit my [folder name] folder. Give me a full inventory organized by subfolder, flag duplicates and misfiled items, and suggest a cleaner structure. Do not move anything until I approve it." + ASK,
         [], ("AI in the classroom", HL_AI), ""),
        ("Build me a classroom tool", "Interactive resources built for you, not bought. This whole hub was made with Claude.",
         "Build me an interactive [choice board / review game / student hub] for [grade] on [topic]. Make it a single web page, mobile-friendly, in my brand colors. Include [what you want on it]. Then give me the file so I can share or host it." + ASK,
         [], ("Watch: Cowork builds my Canva while I relax", ig("DazQIb2zTvd")), ""),
        ("My Monday \"week ahead\"", "Start the week already organized without lifting a finger. Set it once and it runs itself.",
         "Every Monday at 6am, pull my calendar for the week and my to-do list, and send me a short \"week ahead\" brief: what is coming, what I need to prep, and the top 3 things to knock out first. Keep it skimmable." + ASK,
         [], None, "This one runs as a scheduled task, so it keeps working every week on its own."),
    ]),
]

OUTSIDERS_PROMPT = """Build me an AI study tool for my students for the novel [The Outsiders]. Cover five sections: theme, motif, conflict, plot diagram, and symbolism.

Students are middle school (6th to 8th grade). Give partial answers with sentence stems and blanks to fill in, and offer a rewrite when they are a little off. Every section requires students to include a quote as support, then write their own analysis, symbolism, or conflict statement.

THEME: Guide them to a universal, non-cliche theme statement (no character names, no plot summary) using the "the author wants us to know..." frame, landing on the big lesson. Focus the theme on being true to yourself and knowing your true identity, inspired by Johnny's line "stay gold." Model statement: The innocence of youth is something we should cherish because nothing stays gold forever, and staying true to yourself as you grow and change helps guide your identity and choices.

MOTIF: Focus on the motif of literature and how it recurs to build the identity theme, using three moments: the poem "Nothing Gold Can Stay," Johnny and Ponyboy reading Gone with the Wind in the church, and the reveal that Ponyboy is the author. Model statement: The motif of literature is present when Ponyboy recites Robert Frost's "Nothing Gold Can Stay," when Ponyboy and Johnny read Gone with the Wind together in the church, and when Ponyboy reveals he is the author telling the story. These moments remind me that embracing your true identity instead of the labels society gives you helps guide your choices and lets you stay true to yourself.

CONFLICT: Main conflict should be person vs. self or person vs. society.

RULES: Refuse to answer anything not related to The Outsiders. Fun, engaging, student-friendly design with a 1960s Outsiders vibe."""

GUIDE_PRODUCTS = [  # titles from content.py, shown as the same cards as the homepage
    "PBL Backwards Planning with Claude", "Annotation Unlocked", "Hot Takes: AI and Canva Magic",
    "Interactive Notebooks Unlocked", "How I Use Claude to Run My Teacher Business",
]
FREE_PRODUCTS = ["PBL Prompt Guide", "Free Annotations Guide, Grades 5 to 12", "Teacher Tools Cheat Sheet"]

TONES = ["pink", "blue", "violet", "sun"]


def rel(url):
    """Homepage-relative asset paths need ../ from this subfolder."""
    return url


def link(href, inner, cls):
    if href.startswith("/"):
        return f'<a class="{cls}" href="{e(href)}">{inner}</a>'
    return B.a(href, inner, cls)


def watch(w):
    if not w:
        return ""
    return B.peek(w[1], w[0])


def prompt_card(c, tone, copy_label, setup_label=None, why=False):
    title, use, prompt, btns, w, note = c
    btn_html = "".join(link(u, e(t) + B.ARROW, "btn btn-small btn-soft" if soft else "btn btn-small") for t, u, soft in btns)
    first = f'<p class="why"><b>Why it\'s powerful:</b> {e(use)}</p>' if why else f'<p class="use">{e(use)}</p>'
    label = f'<p class="setup-label">{e(setup_label)}</p>' if setup_label else ""
    note_html = f'<p class="note">{e(note)}</p>' if note else ""
    return f'''<article class="pcard card-{tone}">
  <h4>{e(title)}</h4>
  {first}
  {label}
  <div class="promptbox">{e(prompt)}</div>
  <div class="pcard-actions"><button class="btn btn-small btn-copy" type="button" data-label="{e(copy_label)}">{e(copy_label)}</button>{btn_html}{watch(w)}</div>
  {note_html}
</article>'''


def bts_strip():
    return f'<div class="bts-strip"><p><strong>All my guides and activities to set up in your classroom, in one place.</strong></p>{B.a(BTS, "Back to School Drive" + B.ARROW, "btn btn-small")}</div>'


def reel(url, title):
    return f'''<div class="spot-reel"><div class="reel reel-embed">
      <blockquote class="instagram-media" data-instgrm-permalink="{e(url)}?utm_source=ig_embed" data-instgrm-version="14">
        <a href="{e(url)}" target="_blank" rel="noopener" class="reel-fallback"><span class="reel-play">{B.PLAY}</span><span class="reel-title">{e(title)}</span><span class="reel-sub">Watch on Instagram</span></a>
      </blockquote>
    </div></div>'''


def waitlist(compact=False):  # not on the page right now; add {waitlist()} back into build_page() to show it
    action = f'action="{e(WAITLIST_URL)}"' if WAITLIST_URL else 'action="#"'
    sub = "" if compact else '<p class="block-sub">Be the first to know when my next Claude guide or lesson drops, get Claude tips for teachers in your inbox, and get subscriber-only discounts.</p>'
    return f'''<div class="waitlist {'waitlist-compact' if compact else ''}">
  <p class="eyebrow">Join the Claude waitlist</p>
  <h3 class="cta-title">Get Claude updates in your inbox</h3>
  {sub}
  <form class="wl-form" {action} data-email="{e(WAITLIST_EMAIL)}">
    <label class="sr-only" for="wl-{1 if compact else 0}">Your email</label>
    <input id="wl-{1 if compact else 0}" type="email" name="email" placeholder="Your email" required autocomplete="email">
    <button class="btn" type="submit">Count me in{B.ARROW}</button>
  </form>
  <ul class="wl-perks"><li>Claude waitlist</li><li>Claude updates</li><li>Discounts on my Claude guides and lessons</li></ul>
  <p class="wl-done" hidden>You're on the list! Watch your inbox.</p>
</div>'''


EXTRA_CSS = """
/* ---------- Free Claude Guide page ---------- */
.sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
.guide-hero .hero-copy { justify-items: start; }
.guide-hero h1 { font-size: clamp(2.5rem, 7.4vw, 4.8rem); }
.guide-hero .logo { width: clamp(160px, 24vw, 250px); }
@media (max-width: 860px) { .hero-inner { flex-direction: column; text-align: center; gap: 22px; } .guide-hero .hero-copy { justify-items: center; } .socials { justify-content: center; } }
.start-grid { margin-top: -44px; position: relative; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; }
.start { background: var(--card); color: var(--text); border: 3px solid var(--line); border-radius: 18px; padding: 18px 20px; box-shadow: var(--shadow); display: grid; gap: 6px; align-content: start; }
.start-n { font-family: var(--f-display); font-size: 1.4rem; line-height: 1.1; }
.start p { color: var(--muted); font-weight: 700; font-size: .95rem; }
.start a { color: var(--text); font-weight: 900; text-decoration: underline; text-decoration-thickness: 2px; text-underline-offset: 3px; }
@media (max-width: 760px) { .start-grid { grid-template-columns: minmax(0, 1fr); } }
.intro { max-width: 760px; margin: 34px auto 0; text-align: center; font-size: 1.08rem; }
.block { margin-top: 64px; }
.block-head { display: grid; gap: 12px; justify-items: center; text-align: center; margin-bottom: 30px; }
.block-sub { max-width: 60ch; color: var(--muted); font-size: 1.05rem; }
.light-frame { background: repeating-linear-gradient(-12deg, rgba(143, 111, 224, .08) 0 14px, transparent 14px 34px), var(--tint-violet); border-color: var(--line); box-shadow: var(--shadow); margin-inline: auto; }
.light-frame .reels-label { border-color: var(--ink); }
.light-frame .reel { color: var(--text); }
.light-frame .reel-sub { color: var(--muted); }
.light-frame .reel-play { box-shadow: none; }
.more-reels { margin-top: 34px; }
.light-frame { width: min(100%, 1100px); }
.light-frame .spot-reels { flex-wrap: wrap; justify-content: center; }
.light-frame .spot-reel { flex: 0 1 330px; min-width: 0; }
.lead-reel { display: flex; flex-wrap: wrap; gap: 28px 40px; align-items: center; justify-content: center; margin-bottom: 44px; }
.lead-frame { width: min(100%, 400px); margin: 0; }
.lead-frame .spot-reel { flex: 1 1 100%; }
.lead-copy { max-width: 36ch; font-size: 1.15rem; font-weight: 700; }
.lead-copy b { font-family: var(--f-display); font-weight: 400; font-size: 1.6rem; line-height: 1.1; display: block; margin-bottom: 8px; }
.lead-copy a { font-weight: 900; color: var(--text); }
@media (max-width: 860px) { .lead-copy { text-align: center; } }
.hl-row { display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; margin-top: 28px; }
.hl { display: inline-flex; align-items: center; gap: 10px; text-decoration: none; background: var(--card); color: var(--text); border: 3px solid var(--line); border-radius: 999px; padding: 8px 18px 8px 8px; box-shadow: var(--shadow-sm); transition: transform .12s, box-shadow .12s; }
.hl:hover { transform: translate(-2px, -2px); box-shadow: 5px 5px 0 var(--ink); }
.hl b { font-family: var(--f-display); font-weight: 400; font-size: 1.1rem; }
.hl small { display: block; color: var(--muted); font-weight: 700; font-size: .8rem; }
.ways { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 250px), 1fr)); gap: 20px; }
.way { background: var(--card); border: 3px solid var(--line); border-top: 12px solid var(--card-accent); border-radius: 18px; box-shadow: var(--shadow); padding: 16px 18px 18px; display: flex; flex-direction: column; gap: 8px; }
.way-n { font-family: var(--f-display); color: var(--card-accent); font-size: 1rem; }
.way h4 { font-family: var(--f-display); font-weight: 400; font-size: 1.28rem; line-height: 1.12; }
.way p { color: var(--muted); font-size: .96rem; flex: 1; }
.way .card-actions { display: flex; flex-wrap: wrap; gap: 10px 14px; align-items: center; margin-top: 4px; }
.way .btn { background: var(--card-accent); }
.card-sun.way .btn, .card-sun .btn-copy { color: #2E2458; }
.level-banner { margin-top: 72px; border: 4px solid var(--ink); border-radius: 26px; padding: 30px 28px; color: #FFFFFF; text-align: center; display: grid; gap: 10px; justify-items: center; box-shadow: 6px 6px 0 var(--ink); background: linear-gradient(135deg, #D86CDB 0%, #9A79E2 48%, #5E83E8 100%); }
.level-banner.adv { background: linear-gradient(135deg, #5E83E8 0%, #8F6FE0 50%, #D86CDB 100%); }
.level-tag { font-family: var(--f-spaced); font-weight: 700; text-transform: uppercase; letter-spacing: .22em; font-size: .85rem; background: rgba(255,255,255,.22); border: 2px solid #FFFFFF; padding: 5px 14px; border-radius: 999px; }
.level-banner h2 { font-family: var(--f-display); font-weight: 400; text-transform: uppercase; font-size: clamp(2.2rem, 6vw, 3.6rem); line-height: 1; text-shadow: 2px 3px 0 rgba(46, 36, 88, .5); }
.level-banner p { max-width: 58ch; font-weight: 700; font-size: 1.08rem; }
.pgrid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 420px), 1fr)); gap: 22px; }
.pcard { background: var(--card); border: 3px solid var(--line); border-radius: 18px; box-shadow: var(--shadow); padding: 18px 20px 20px; display: flex; flex-direction: column; gap: 10px; min-width: 0; border-left: 12px solid var(--card-accent); }
.pcard h4 { font-family: var(--f-display); font-weight: 400; font-size: 1.4rem; line-height: 1.1; }
.pcard .use, .pcard .why { color: var(--muted); font-weight: 700; }
.pcard .why b { color: var(--text); }
.setup-label { font-family: var(--f-spaced); font-weight: 700; text-transform: uppercase; letter-spacing: .16em; font-size: .78rem; color: var(--card-accent); }
.promptbox { white-space: pre-wrap; background: var(--card-tint, var(--tint-violet)); border: 2px dashed var(--card-accent, var(--violet)); border-radius: 12px; padding: 14px 15px; font-size: .95rem; font-weight: 700; line-height: 1.5; color: var(--text); }
.pcard-actions { display: flex; flex-wrap: wrap; gap: 10px 14px; align-items: center; margin-top: 2px; }
.pcard .btn, .btn-copy { background: var(--card-accent, var(--pink)); }
.btn-soft { background: var(--card) !important; color: var(--text) !important; }
.btn-copy.copied { background: var(--free) !important; color: #FFFFFF !important; }
.note { font-size: .88rem; color: var(--muted); font-style: italic; font-weight: 700; }
.bts-strip { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 14px; margin-top: 28px; padding: 14px 20px; background: var(--tint-sun); border: 3px solid var(--line); border-radius: 18px; box-shadow: var(--shadow-sm); }
.bts-strip .btn { background: var(--sun); color: #2E2458; }
.featnote { max-width: 760px; margin: 0 auto 26px; background: var(--tint-blue); border: 3px solid var(--line); border-radius: 16px; padding: 14px 18px; box-shadow: var(--shadow-sm); font-weight: 700; }
.part-badge { font-family: var(--f-spaced); font-weight: 700; text-transform: uppercase; letter-spacing: .2em; font-size: .85rem; color: var(--violet); }
.showcase { margin-top: 40px; display: grid; gap: 14px; justify-items: start; background: var(--tint-sun); border: 3px solid var(--line); border-radius: 24px; padding: 26px 28px; box-shadow: var(--shadow); }
.showcase h3 { font-family: var(--f-display); font-weight: 400; font-size: clamp(1.6rem, 4vw, 2.3rem); line-height: 1.05; }
.showcase .btn { background: var(--sun); color: #2E2458; }
.showcase details { width: 100%; }
.showcase summary { cursor: pointer; font-weight: 900; }
.showcase .promptbox { margin-top: 12px; --card-tint: var(--card); --card-accent: #C98A0E; }
.showcase .pcard-actions { margin-top: 12px; }
.waitlist { max-width: 760px; margin: 56px auto 0; display: grid; gap: 12px; justify-items: center; text-align: center; background: var(--tint-pink); border: 3px solid var(--line); border-radius: 24px; padding: 28px 26px; box-shadow: var(--shadow); }
.waitlist .eyebrow { color: #B0389F; }
.wl-form { display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; width: 100%; max-width: 520px; }
.wl-form input { flex: 1 1 230px; min-width: 0; font: inherit; font-weight: 800; padding: 12px 16px; border-radius: 14px; border: 3px solid var(--ink); background: var(--card); color: var(--text); }
.wl-perks { list-style: none; padding: 0; margin: 2px 0 0; display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; }
.wl-perks li { font-size: .8rem; font-weight: 900; text-transform: uppercase; letter-spacing: .06em; padding: 4px 10px; border-radius: 999px; border: 2px solid var(--line); background: var(--card); }
.wl-done { font-weight: 900; color: var(--free); }
.qrrow { display: flex; flex-wrap: wrap; gap: 18px; justify-content: center; margin-top: 8px; }
.qrcard { background: #FFFFFF; color: #2E2458; border: 3px solid var(--ink); border-radius: 18px; padding: 14px 14px 12px; width: 180px; box-shadow: var(--shadow-sm); text-align: center; }
.qrcard img { width: 136px; height: 136px; display: block; margin: 6px auto 8px; }
.qrcard b { font-family: var(--f-display); font-weight: 400; font-size: 1.2rem; display: block; }
.qrcard small { font-weight: 700; font-size: .8rem; color: #564D7C; }
.qr-scan { font-family: var(--f-spaced); font-weight: 700; text-transform: uppercase; letter-spacing: .14em; font-size: .72rem; color: #5E83E8; }
.webinar { max-width: 760px; margin: 40px auto 0; display: flex; flex-wrap: wrap; gap: 16px; align-items: center; justify-content: space-between; background: var(--tint-blue); border: 3px solid var(--line); border-radius: 20px; padding: 20px 24px; box-shadow: var(--shadow); }
.webinar h3 { font-family: var(--f-display); font-weight: 400; font-size: 1.4rem; line-height: 1.1; }
.webinar p { color: var(--muted); font-weight: 700; }
.webinar .btn { background: var(--blue); }
.topnav-links a.on { border-bottom-color: var(--glow); }
/* video pop-out */
.vmodal { position: fixed; inset: 0; z-index: 100; display: none; align-items: center; justify-content: center; padding: 16px; background: rgba(23, 12, 58, .75); }
.vmodal.open { display: flex; }
.vmodal-box { background: var(--card); border: 3px solid var(--ink); border-radius: 22px; width: 100%; max-width: 420px; max-height: calc(100vh - 32px); overflow: auto; position: relative; padding: 50px 12px 14px; box-shadow: 6px 6px 0 var(--ink); }
.vmodal-close { position: absolute; top: 10px; right: 10px; width: 36px; height: 36px; border-radius: 50%; border: 3px solid var(--ink); background: var(--pink); color: #FFFFFF; font-size: 1.3rem; line-height: 1; cursor: pointer; font-weight: 900; }
.vmodal-body .instagram-media { margin: 0 auto !important; min-width: 0 !important; width: 100% !important; }
.vmodal-alt { display: block; text-align: center; margin-top: 10px; font-weight: 900; color: var(--text); }
body.no-scroll { overflow: hidden; }

/* ---------- Claude orange theme for this page only ---------- */
:root {
  --paper: #FAF4EC; --card: #FFFFFF; --text: #2B1A12; --muted: #6B5246;
  --ink: #2B1A12; --line: #2B1A12;
  --pink: #D97757; --violet: #B85A3A; --blue: #A1492C; --sun: #F0B35B; --glow: #FFD3B6;
  --tint-pink: #FBE3D8; --tint-violet: #F7E6DC; --tint-blue: #FCEEE4; --tint-sun: #FFF0D4;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper: #1C130E; --card: #2A1D16; --text: #F8EEE7; --muted: #D2BBAE; --ink: #050302; --line: #E39A7A;
    --tint-pink: #45261B; --tint-violet: #3B2419; --tint-blue: #3F2A1E; --tint-sun: #3F3018;
  }
}
:root[data-theme="dark"] {
  --paper: #1C130E; --card: #2A1D16; --text: #F8EEE7; --muted: #D2BBAE; --ink: #050302; --line: #E39A7A;
  --tint-pink: #45261B; --tint-violet: #3B2419; --tint-blue: #3F2A1E; --tint-sun: #3F3018;
}
.hero { background: linear-gradient(135deg, #F2A47D 0%, #D97757 52%, #B85A3A 100%); }
.topnav { border-bottom-color: #D97757; }
.hero h1, .level-banner h2 { text-shadow: 2px 3px 0 rgba(43, 26, 18, .45); }
.logo { filter: drop-shadow(5px 5px 0 rgba(43, 26, 18, .4)); }
.topnav-menu summary { background: #D97757; }
.level-banner { background: linear-gradient(135deg, #F2A47D 0%, #D97757 52%, #B85A3A 100%); }
.level-banner.adv { background: linear-gradient(135deg, #8C3F26 0%, #B85A3A 50%, #D97757 100%); }
.light-frame { background: repeating-linear-gradient(-12deg, rgba(217, 119, 87, .09) 0 14px, transparent 14px 34px), var(--tint-violet); }
.reels-label { background: #D97757; }
.eyebrow, .part-badge { color: #B85A3A; }
.qr-scan { color: #B85A3A; }
.webinar .btn { background: #B85A3A; }
.peek-play { color: #FFD3B6; }
.light-frame .reel-title { color: var(--text); }
/* home link */
.home-link { display: inline-flex; align-items: center; gap: 8px; }
.home-arrow { font-family: var(--f-body); font-weight: 900; }
.home-tag { font-family: var(--f-body); font-weight: 900; font-size: .72rem; letter-spacing: .08em; text-transform: uppercase; background: #D97757; color: #FFFFFF; border: 2px solid #FFFFFF; border-radius: 999px; padding: 2px 9px; }
.home-link:hover .home-tag { background: #FFFFFF; color: #2B1A12; }
@media (max-width: 420px) { .home-link { font-size: 1.02rem; gap: 6px; } .topnav-inner { gap: 10px; } }

/* ---------- Teacher Helper Project ---------- */
.hero-helper { width: fit-content; background: #FFFFFF !important; color: #2B1A12 !important; }
@media (max-width: 860px) { .hero-helper { justify-self: center; } }
.helper { display: grid; grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); gap: 40px; align-items: center; background: var(--card); border: 4px solid var(--ink); border-radius: 28px; box-shadow: 8px 8px 0 var(--ink); padding: 34px; }
.helper-covers { position: relative; padding: 0 30px 40px 0; }
.helper-cover { display: block; width: 100%; height: auto; border: 3px solid var(--ink); border-radius: 12px; box-shadow: 6px 6px 0 var(--ink); transform: rotate(-3deg); position: relative; z-index: 2; }
.helper-page { position: absolute; right: 0; bottom: 0; width: 58%; height: auto; border: 3px solid var(--ink); border-radius: 10px; box-shadow: 5px 5px 0 var(--ink); transform: rotate(4deg); z-index: 3; background: #FFF; }
.helper-copy { display: grid; gap: 14px; }
.helper-title { font-family: var(--f-display); font-weight: 400; text-transform: uppercase; font-size: clamp(2.2rem, 5vw, 3.4rem); line-height: 1; }
.helper-lead { font-size: 1.12rem; font-weight: 700; }
.helper-list { margin: 0; padding-left: 1.2em; display: grid; gap: 6px; }
.helper-list li::marker { color: #D97757; }
.helper-btn { background: #D97757 !important; color: #FFFFFF !important; }
.helper-small { font-size: .88rem; color: var(--muted); font-weight: 700; }
@media (max-width: 860px) { .helper { grid-template-columns: minmax(0, 1fr); padding: 22px; gap: 24px; } .helper-covers { max-width: 380px; margin: 0 auto; } }
.more-strip { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 14px; margin-top: 26px; padding: 18px 22px; background: var(--tint-pink); border: 3px solid var(--line); border-radius: 18px; box-shadow: var(--shadow); }
.more-strip p { flex: 1; min-width: 240px; }
.more-strip .btn { background: #D97757; color: #FFF; }
.peek-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 20px; }
.peek-card { background: var(--card); border: 3px solid var(--line); border-top: 12px solid var(--card-accent); border-radius: 18px; box-shadow: var(--shadow); padding: 16px 18px; display: grid; gap: 6px; align-content: start; }
.peek-level { font-family: var(--f-spaced); font-weight: 700; text-transform: uppercase; letter-spacing: .16em; font-size: .78rem; color: var(--card-accent); }
.peek-card h4 { font-family: var(--f-display); font-weight: 400; font-size: 1.45rem; line-height: 1.1; }
.peek-card p { color: var(--muted); font-weight: 700; }
"""

JS = r"""
document.querySelectorAll('.btn-copy').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var box = btn.closest('.pcard, .showcase').querySelector('.promptbox');
    var text = box.innerText;
    function done() { btn.textContent = 'Copied!'; btn.classList.add('copied'); setTimeout(function () { btn.textContent = btn.dataset.label; btn.classList.remove('copied'); }, 1800); }
    if (navigator.clipboard) { navigator.clipboard.writeText(text).then(done, fallback); } else { fallback(); }
    function fallback() { var r = document.createRange(); r.selectNode(box); var s = window.getSelection(); s.removeAllRanges(); s.addRange(r); try { document.execCommand('copy'); done(); } catch (e) {} s.removeAllRanges(); }
  });
});
document.querySelectorAll('.wl-form').forEach(function (f) {
  f.addEventListener('submit', function (ev) {
    if (f.getAttribute('action') && f.getAttribute('action') !== '#') return;
    ev.preventDefault();
    var email = f.querySelector('input').value.trim();
    var body = 'Please add me to the Claude waitlist (updates and discounts on Claude guides and lessons).%0D%0A%0D%0AMy email: ' + encodeURIComponent(email);
    window.location.href = 'mailto:' + f.dataset.email + '?subject=' + encodeURIComponent('Add me to the Claude waitlist') + '&body=' + body;
    var w = f.closest('.waitlist'); w.querySelector('.wl-done').hidden = false;
  });
});
(function () {
  var modal = document.getElementById('vmodal'), body = document.getElementById('vmodal-body'), alt = document.getElementById('vmodal-alt');
  function openReel(id) {
    var url = 'https://www.instagram.com/reel/' + id + '/';
    body.innerHTML = '<blockquote class="instagram-media" data-instgrm-permalink="' + url + '?utm_source=ig_embed" data-instgrm-version="14"><a href="' + url + '" target="_blank" rel="noopener">Watch on Instagram</a></blockquote>';
    alt.href = url; modal.classList.add('open'); document.body.classList.add('no-scroll');
    if (window.instgrm) window.instgrm.Embeds.process();
  }
  function close() { modal.classList.remove('open'); document.body.classList.remove('no-scroll'); body.innerHTML = ''; }
  document.addEventListener('click', function (ev) {
    var link = ev.target.closest('a[href*="instagram.com/reel/"]');
    if (!link || link.closest('.instagram-media') || modal.contains(link)) return;
    if (ev.metaKey || ev.ctrlKey || ev.shiftKey) return;
    var m = link.href.match(/instagram\.com\/reel\/([A-Za-z0-9_-]+)/); if (!m) return;
    ev.preventDefault(); openReel(m[1]);
  });
  modal.addEventListener('click', function (ev) { if (ev.target === modal) close(); });
  modal.querySelector('.vmodal-close').addEventListener('click', close);
  document.addEventListener('keydown', function (ev) { if (ev.key === 'Escape') close(); });
})();
"""


def build_page():
    B.MODE = "site"
    B.img_src = lambda key: f"../covers/{key}.webp"
    by_title = {p["t"]: p for p in C.PRODUCTS}

    start = f'''<section class="wrap start-grid" aria-label="How this page works">
  <div class="start"><span class="start-n">1. Grab it free</span><p>Verified K-12 US teachers get premium Claude free for a year. <a href="https://claude.com/solutions/teachers" target="_blank" rel="noopener">Click here</a>, then hit "Get Verified."</p></div>
  <div class="start"><span class="start-n">2. Watch and try</span><p>Watch my classroom demos, then copy a few of my favorite prompts below. Free, yours to keep.</p></div>
  <div class="start"><span class="start-n">3. Get the whole system</span><p>Ready for Claude to work like your own teacher assistant? <a href="#teacher-helper">Meet The Teacher Helper Project</a>.</p></div>
</section>'''

    hl = "".join(B.a(u, f'<span class="peek-play">{B.PLAY}</span><span><b>{e(t)}</b><small>{e(s)}</small></span>', "hl") for u, t, s in HIGHLIGHTS)
    videos = f'''<section class="wrap block" id="watch" aria-labelledby="watch-h">
  {B.head("Watch Me Use Claude", "Short, no-fluff demos straight from my classroom. Tap play and see what Claude can do.", "watch-h")}
  <div class="lead-reel"><div class="reels-frame light-frame lead-frame"><span class="reels-label">New video</span><div class="spot-reels">{reel(*LEAD_REEL)}</div></div><p class="lead-copy"><b>Station rotations on ONE screen.</b> Watch Claude build my reading workshop board: the group schedule, station directions, a timer, and points. The exact prompt is a move in <a href="#teacher-helper">The Teacher Helper Project</a>.</p></div>
  <div class="reels-frame light-frame"><span class="reels-label">Peek inside my classroom</span><div class="spot-reels">{"".join(reel(u, t) for u, t in TOP_REELS)}</div></div>
  <div class="reels-frame light-frame more-reels"><span class="reels-label">More Claude demos</span><div class="spot-reels">{"".join(reel(u, t) for u, t in MORE_REELS)}</div></div>
  <div class="hl-row">{hl}</div>
</section>'''

    SHOW = {"Reading workshop boards", "Backwards-planned my PBL units", "Made 180 days of agenda slides", "Built annotation packets for ANY text", "A study tool for my real students", "Interactive notebook pages", "Poe month projects", "My whole classroom website"}
    ways = ""
    for i, (tone, t, d, btns, r) in enumerate([w for w in WAYS if w[1] in SHOW], 1):
        acts = "".join(link(u, e(bt) + B.ARROW, "btn btn-small") for bt, u in btns) + (B.peek(r) if r else "")
        ways += f'<article class="way card-{tone}"><h4>{e(t)}</h4><p>{e(d)}</p><div class="card-actions">{acts}</div></article>'
    ways_sec = f'''<section class="wrap block" id="ways" aria-labelledby="ways-h">
  {B.head("Ways I've Used Claude in My Classroom", "The real stuff, from my own 7th and 8th grade ELA and history classes. Tap a video to watch me do it. Every one of these is a move in The Teacher Helper Project.", "ways-h", eyebrow="Straight from my classroom")}
  <div class="ways">{ways}</div>
</section>'''

    by_card = {c[0]: (sec[2], c) for sec in BEGINNER for c in sec[3]}
    teaser_names = ["Backwards-design a unit", "Three readiness levels of the same text", "The tricky parent email"]
    teasers = "".join(prompt_card(by_card[n][1], TONES[i % 4], "Copy prompt") for i, n in enumerate(teaser_names))
    teaser_sec = f'''<section class="wrap block" id="try" aria-labelledby="try-h">
  {B.head("Try These Free", "Three of my favorite prompts, on the house. Copy one, paste it into Claude, and swap the [brackets] for your stuff.", "try-h", eyebrow="Copy, paste, done")}
  <div class="pgrid">{teasers}</div>
  <div class="more-strip"><p><strong>That's 3 of my 36 moves.</strong> The other 33 (workshop boards, study tools, sub plans, rubrics, Projects, Skills, and more) are waiting in The Teacher Helper Project.</p>{link(TEACHER_HELPER_URL, "See what's inside" + B.ARROW, "btn")}</div>
</section>'''

    helper_sec = f'''<section class="wrap block" id="teacher-helper" aria-labelledby="helper-h">
  <div class="helper">
    <div class="helper-covers">
      <img class="helper-cover" src="img/teacher-helper-cover.jpg" alt="The Teacher Helper Project cover" loading="lazy">
      <img class="helper-page" src="img/teacher-helper-page.jpg" alt="How The Teacher Helper Project works page" loading="lazy">
    </div>
    <div class="helper-copy">
      <p class="eyebrow">My ultimate Claude teacher assistant guide</p>
      <h2 id="helper-h" class="helper-title">The Teacher Helper Project</h2>
      <p class="helper-lead">Drop it into Claude and it works the way I work. Make a Project, add the guide, and just say <b>"Do the Workshop Board move for The Raven."</b> Claude asks a few questions, then builds it.</p>
      <ul class="helper-list">
        <li><b>36 ready-to-run moves</b> for planning, differentiation, parent emails, PBL, annotation, and assessments</li>
        <li><b>Build It:</b> workshop boards, student study tools, review games, and Canva Bulk Create</li>
        <li><b>Claude Advanced:</b> Projects, Skills, and letting Claude do the work on your computer</li>
        <li><b>Real screenshots</b> from my classroom, plus links to every demo video</li>
        <li><b>Always up to date:</b> one link that always has the newest version</li>
      </ul>
      <div class="btn-row">{link(TEACHER_HELPER_URL, "Get The Teacher Helper Project" + B.ARROW, "btn btn-big helper-btn")}</div>
      <p class="helper-small">A PDF for your personal classroom use. Works with Claude, including the free verified teacher account.</p>
    </div>
  </div>
</section>'''

    peeks = [
        ("Level 1", "Claude for Beginners", "Copy-paste moves that get your night back: Backwards Unit, Sub Plans, Three Levels, Tricky Parent Email, Quick Rubric, Exit Tickets, and more."),
        ("Level 2", "Build It", "Claude builds things you put on your screen and share with students: Workshop Board, Study Tool, Review Game, Student Hub, Bulk Create Table."),
        ("Level 3", "Claude Advanced", "A Claude that already knows your classroom: Classroom HQ Project, Feedback Partner, PBL Remix Machine Skill, and Monday Week Ahead."),
    ]
    peek_cards = "".join(f'<article class="peek-card card-{TONES[i]}"><span class="peek-level">{e(a)}</span><h4>{e(t)}</h4><p>{e(d)}</p></article>' for i, (a, t, d) in enumerate(peeks))
    peek_sec = f'''<section class="wrap block" id="inside" aria-labelledby="inside-h">
  {B.head("What's Inside", "Three levels, so you can start easy and grow into the advanced stuff.", "inside-h", eyebrow="Sneak peek")}
  <div class="peek-grid">{peek_cards}</div>
  <div class="showcase">
    <p class="eyebrow" style="color:#B07400">See one I actually built</p>
    <h3>The Outsiders study tool, for my real students</h3>
    <p>A student-facing coach for theme, motif, conflict, plot, and symbolism, built from our actual class materials. It refuses anything off-topic, and yes, it has a 1960s vibe. The exact prompt is the Study Tool move in The Teacher Helper Project.</p>
    <div class="btn-row">{B.a(OUTSIDERS, "Open the live tool" + B.ARROW, "btn")}{link(TEACHER_HELPER_URL, "Get the prompt" + B.ARROW, "btn btn-soft")}</div>
  </div>
</section>'''

    guides = "".join(B.card(by_title[t], TONES[i % 4]) for i, t in enumerate(GUIDE_PRODUCTS) if t in by_title)
    frees = "".join(B.card(by_title[t], "free") for t in FREE_PRODUCTS if t in by_title)
    bts_cta = f'''<div class="cta-box">
      <a class="cta-cover" href="{e(BTS)}" target="_blank" rel="noopener"><img src="../covers/bts.webp" alt="Back to School Growing Google Drive" loading="lazy"></a>
      <div class="cta-copy"><p><strong>Want ALL my guides in one place?</strong> My Back to School GROWING Drive is my whole library in one link: AI and Canva prompt guides, a full year of agenda slides, annotation templates, projects, decor, sub plans, and more. Always growing, lifetime access.</p>
      <div class="btn-row">{B.a(BTS, "Get the whole bundle" + B.ARROW, "btn")}{B.a(PBL, "Get the PBL Drive" + B.ARROW, "btn btn-soft")}</div></div>
    </div>'''
    guides_sec = f'''<section class="wrap block" id="guides" aria-labelledby="guides-h">
  {B.head("More of My Guides", "Already built, already pretty, ready for your classroom.", "guides-h", bts_cta, eyebrow="More done-for-you guides")}
  <div class="grid">{guides}</div>
  <h3 class="group-title" style="margin-top:40px">Start free</h3>
  <div class="grid" style="margin-top:18px">{frees}</div>
</section>'''

    qr = "".join(f'<a class="qrcard" href="{e(u)}" target="_blank" rel="noopener"><span class="qr-scan">Scan to follow</span><img src="img/qr-{k}.png" alt="{e(n)} QR code" loading="lazy"><b>{e(n)}</b><small>{e(h)}</small></a>'
                 for k, n, h, u in [("instagram", "Instagram", "@Middle_Teacher_Syndrome", "https://www.instagram.com/middle_teacher_syndrome/"),
                                    ("tiktok", "TikTok", "@middle_teacher_syndrome", "https://www.tiktok.com/@middle_teacher_syndrome"),
                                    ("facebook", "Facebook", "Middle Teacher Syndrome", "https://www.facebook.com/middle_teacher_syndrome")])
    follow = f'''<section class="wrap block" id="follow" aria-labelledby="follow-h">
  {B.head("This Is Just the Start", "I post new prompts, demos, and classroom moves every week. Scan to follow, then come hang out. That is where all the good stuff lives.", "follow-h")}
  <div class="qrrow">{qr}</div>
  <div class="webinar"><div><p class="eyebrow">Webinar handout</p><h3>How to build a novel study with Claude for Education</h3><p>The step-by-step one-pager from the session.</p></div>{B.a("https://docs.google.com/document/d/1_ckXddI9U60CeVE8PTRJhXCbMaMNyUsG/edit?usp=sharing", "Open the one-pager" + B.ARROW, "btn")}</div>
</section>'''

    nav = [("/#best-seller", "PBL Drive"), ("/#spotlight", "Spooky Season"), ("/#shop", "Shop the Classroom"), ("/#teacher", "Teacher Guides"), ("/#free", "Free Resources"), ("/free-claude-guide/", "Free Claude Guide")]
    nav_inline = "".join(f'<a href="{h}"{" class=\"on\"" if "claude" in h else ""}>{e(n)}</a>' for h, n in nav if "spotlight" not in h)
    nav_menu = "".join(f'<a class="menu-main" href="{h}">{e(n)}</a>' for h, n in nav) + \
        "".join(f'<a class="menu-sub" href="#{i}">{e(n)}</a>' for i, n in [("watch", "Watch me use Claude"), ("teacher-helper", "The Teacher Helper Project"), ("ways", "Ways I use Claude"), ("try", "Try these free"), ("inside", "What's inside"), ("follow", "Follow me")])

    css = (HERE / "style.css").read_text() + EXTRA_CSS
    out = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Free Claude Guide for Teachers | Michaela Arabia: The Balanced Teach</title>
<meta name="description" content="How I use Claude in my middle school classroom: demo videos, free prompts, and The Teacher Helper Project, my Claude teacher assistant guide.">
<link rel="canonical" href="https://mrsarabiarocks.com/free-claude-guide/">
<meta property="og:title" content="Free Claude Guide for Teachers">
<meta property="og:description" content="The exact Claude prompts and moves I use in my middle school classroom. Copy, paste, done.">
<meta property="og:image" content="https://mrsarabiarocks.com/logo.webp">
<meta property="og:url" content="https://mrsarabiarocks.com/free-claude-guide/">
<link rel="icon" href="../favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lilita+One&family=Nunito:wght@600;700;800;900&family=Quicksand:wght@700&display=swap">
<style>
{css}
</style>
</head>
<body>
<nav class="topnav" aria-label="Site sections">
  <div class="wrap topnav-inner">
    <a class="topnav-name home-link" href="/" title="Back to my home page"><span class="home-arrow" aria-hidden="true">&larr;</span>Michaela Arabia<span class="home-tag">Home</span></a>
    <div class="topnav-links">{nav_inline}</div>
    <details class="topnav-menu" id="topnav-menu">
      <summary>Menu <span aria-hidden="true">&#9662;</span></summary>
      <div class="menu-panel">{nav_menu}</div>
    </details>
  </div>
</nav>

<header class="hero guide-hero" id="top">
  <div class="wrap hero-inner">
    <img class="logo" src="../logo-orange.webp" alt="Michaela, The Balanced Teach, @Middle_Teacher_Syndrome" width="560" height="561">
    <div class="hero-copy">
      <h1><span>Free Claude</span> <span>Guide</span></h1>
      <p class="tagline">For Teachers</p>
      <p class="bio">See how I use Claude in my real classroom, grab a few free prompts, and meet my teacher assistant guide.</p>
      <nav class="socials" aria-label="Follow me">{B.socials("social-hero")}</nav>
      {link(TEACHER_HELPER_URL, "Get The Teacher Helper Project" + B.ARROW, "btn hero-helper")}
    </div>
  </div>
</header>

<main>
{start}
{videos}
{helper_sec}
{ways_sec}
{teaser_sec}
{peek_sec}
{guides_sec}
{follow}
</main>

<footer class="foot">
  <div class="wrap foot-inner">
    <p class="foot-name">Michaela Arabia <span>The Balanced Teach</span></p>
    <nav class="socials" aria-label="Follow me">{B.socials("social-foot")}</nav>
    <p class="foot-small"><a href="/" style="color:inherit">Back to MrsArabiaRocks.com</a> &middot; @middle_teacher_syndrome &middot; &copy; 2026 Michaela Arabia</p>
  </div>
</footer>

<div class="vmodal" id="vmodal" role="dialog" aria-modal="true" aria-label="Video">
  <div class="vmodal-box">
    <button class="vmodal-close" type="button" aria-label="Close video">&times;</button>
    <div class="vmodal-body" id="vmodal-body"></div>
    <a class="vmodal-alt" id="vmodal-alt" href="#" target="_blank" rel="noopener">Open on Instagram</a>
  </div>
</div>
<script>
{JS}
</script>
<script async src="https://www.instagram.com/embed.js"></script>
</body>
</html>
'''
    assert "—" not in out and "–" not in out, "dash found"
    return out


if __name__ == "__main__":
    d = pathlib.Path(sys.argv[1]) / "free-claude-guide"
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(build_page())
    print("written", d / "index.html")
