# All site content lives here. Edit this file, then run build.py.
# img = cover file in /home/claude/site-assets/covers (without .webp); cv = short label for cards without a cover.
# kw = extra search words.

TC = "https://mrsarabiarocks.thrivecart.com/"
T = "https://www.teacherspayteachers.com/Product/"

def ig(code):
    return f"https://www.instagram.com/reel/{code}/"

SOCIALS = [
    ("instagram", "Instagram", "https://www.instagram.com/middle_teacher_syndrome/"),
    ("tiktok", "TikTok", "https://www.tiktok.com/@middle_teacher_syndrome"),
    ("linkedin", "LinkedIn", "https://www.linkedin.com/in/michaela-arabia-a662818b"),
    ("pinterest", "Pinterest", "https://www.pinterest.com/Middle_Teacher_Syndrome"),
]

BIO = "17 years in, and still teaching middle school ELA and history every single day. Tech and AI nerd, here to help you beat burnout. Everything on this page gets tested in my own classroom first!"

QUICK_LINKS = [
    ("Amazon Storefront", "All my classroom faves in one spot", "https://www.amazon.com/shop/middle_teacher_syndrome"),
    ("TPT Store", "Prefer TPT? I'm there too!", "https://www.teacherspayteachers.com/store/middle-teacher-syndrome"),
    ("Free Canva Templates", "Just copy, tweak, and teach", "https://mrsarabiarocks.my.canva.site/canva-templates"),
    ("Free AI Tools", "The ones you MUST try", "https://mrsarabiarocks.my.canva.site/mrs-arabia-rocks-ai-sites-to-try"),
    ("Claude for Teachers", "My free how-to site", "https://thebalancedteach.tiiny.site/?v=beg"),
]

BEST_SELLER = {
    "eyebrow": "My #1 best seller",
    "headline": "The PBL Google Drive",
    "body": "50+ full project based learning units and resources for grades 5 to 12, all in ONE growing Google Drive. Grab it once, and every new project I add is yours too. If you only get one thing from me, make it this one!",
    "stats": ["50+ full units and resources", "Grades 5 to 12", "Grows every year, and new additions are yours free"],
    "inside_doc": "",  # Michaela will send the link to her "what's in the Drive" doc
    "img": "pbl",
    "url": TC + "pbl-growing-drive/",
    "reel": ig("Ddq95n9D9z3"),
}

SPOTLIGHT = {
    "eyebrow": "Spooky Season Spotlight",
    "headline": "Lights off, highlighters out.",
    "body": "This is my FAVORITE MONTH of the whole year. We turn off the lights, pass out the blacklight highlighters, and annotate Poe. Here's what it looks like in my room, plus everything you need to do it in yours!",
    "reel": ig("DeJ8tEED88J"),
    "reel_title": "Blacklight Poe annotating",
    "gallery": [
        ("spooky-poe1848", "Edgar Allan Poe, 1848"),
        ("spooky-dore19", "The Raven, Gustave Dore, 1884"),
        ("spooky-clarke6", "Harry Clarke, 1919"),
        ("spooky-pg33", "The Raven, Gustave Dore, 1884"),
        ("spooky-clarke4", "Harry Clarke, 1919"),
    ],
    "buttons": [
        ("Get the Poe bundle", TC + "edgar-allan-poe-4-week-bundle/"),
        ("Shop my blacklight supplies", "https://urlgeni.us/amazon/ZcwVyW"),
    ],
}

FAN_FAVORITE = {
    "eyebrow": "Fan favorite",
    "headline": "A WHOLE YEAR of agenda slides in minutes",
    "body": "Every day of the school year, already made and fully editable in Canva. Plus I show you how to make your own with Bulk Create. This is my most-loved video ever!",
    "img": "agenda",
    "url": TC + "180-daily-agenda-slides-canvabulkcreate/",
    "reel": ig("DbBoju3veLA"),
}

PRODUCTS = [
    # Spooky (spotlight)
    dict(s="spooky", t="Poe: The Raven Mini Unit", d="A full week of Raven plans, fully editable. Moody, creepy, and SO fun to teach.", u=TC + "edgar-allan-poe-the-raven-mini-unit/", r=ig("Ddy_SyTgYP_"), img="raven", kw="poe halloween october"),
    dict(s="spooky", t="Poe: The Tell-Tale Heart Mini Unit", d="A full week of Tell-Tale Heart plans, fully editable. Heart-pounding in the best way.", u=TC + "poe-tell-tale-heart/", img="telltale", kw="poe halloween october"),
    dict(s="spooky", t="Poe: The Fall of the House of Usher Mini Unit", d="A full week of Usher plans, fully editable. Watch my kids try to SELL the house!", u=TC + "poe-usher-mini-unit-fully-editable/", r=ig("DeE_B7VToyi"), img="usher", kw="poe halloween october"),
    dict(s="spooky", t="Poe: The Cask of Amontillado Mini Unit", d="Annotations, a plot diagram, and a project for Poe's sneakiest revenge story.", u="https://www.teacherspayteachers.com/Product/The-Cask-of-Amontillado-Mini-Unit-Poe-Annotations-Plot-Diagram-PBL-Project-10262608", tpt=True, img="cask", kw="poe halloween october amontillado"),
    dict(s="spooky", t="The Monkey's Paw: 5-Day Foreshadowing Unit", d="Five days of foreshadowing with a story that gives EVERYONE chills.", u=TC + "the-monkeys-paw-5-day-foreshadowing-unit/", r=ig("Ddw6W2JyEWH"), img="monkey", kw="short story halloween october"),
    dict(s="spooky", t="The Lottery: Meme and Lesson Activity", d="A creepy classic plus a meme assessment your students will actually want to do. And it's FREE!", u=TC + "the-lottery-meme--lesson-activity/", r=ig("DZk76x-vo-M"), img="lottery", free=True, kw="short story halloween meme free"),
    dict(s="spooky", t="Free Annotations Guide, Grades 5 to 12", d="Exactly how I teach annotating, step by step. Perfect before blacklight week!", u=TC + "annotations-guide-for-grades-5-12/", r=ig("DX-s1VWzEqv"), free=True, cv="Annotate!", kw="annotation free"),

    dict(s="spooky", t="FREE Poe Unit: 4 Weeks of Ideas", d="My whole month of Poe lesson ideas and plans, totally free. Start here!", u=T+"FREE-Edgar-Allan-Poe-Unit-4-Weeks-of-IDEAS-Lesson-Plans-10254735", tpt=True, free=True, img="tpt10254735", kw="poe halloween october free"),

    # ELA
    dict(s="ela", t="Edgar Allan Poe: 4-Week Bundle", d="ALL my Poe units in one bundle. A whole month of creepy, fully editable lessons.", u=TC + "edgar-allan-poe-4-week-bundle/", img="poebundle", kw="poe halloween october bundle"),
    dict(s="ela", t="The Outsiders Novel Study", d="Three weeks of The Outsiders, ready to teach. Stay gold!", u=TC + "outsiders-novel-study/", r=ig("DZBb8xAvJpS"), img="outsiders", kw="novel"),
    dict(s="ela", t="Novel Choice Project", d="Works with ANY novel or short story. Students make a one-pager and a magazine-style character feature.", u=TC + "novel-choice-project-1-pager--character-feature/", img="novel", kw="one pager novel short story"),
    dict(s="ela", t="ELA Must-Read List", d="My go-to short stories and novels for middle school, all in one list.", u=TC + "ela-must-read-list-short-stories--novels/", r=ig("DdDHMZnBb5C"), cv="Must Reads", kw="books reading list"),

    dict(s="ela", t="Langston Hughes Mini Unit", d="Project based learning with \"Dreams\" and \"Harlem.\" Poetry they'll actually remember.", u=T+"Langston-Hughes-Mini-Unit-Project-Based-Learning-in-Poetry-Dreams-Harlem-11022227", tpt=True, img="tpt11022227", kw="poetry black history month harlem renaissance"),
    dict(s="ela", t="Maya Angelou: I Know Why the Caged Bird Sings", d="A full week of PBL activities with the excerpt. Annotations, art, and Socratic seminar.", u=T+"Maya-Angelou-Excerpt-from-I-Know-Why-The-Caged-Bird-Sings-PBL-Activities-10925165", tpt=True, img="tpt10925165", kw="black history month memoir"),
    dict(s="ela", t="The Lightning Thief Choice Project", d="A Percy Jackson themed choice project, fully editable.", u=T+"Editable-The-Lightning-Thief-Themed-Choice-Project-5616002", tpt=True, img="tpt5616002", kw="percy jackson novel choice"),

    # History
    dict(s="history", t="Dr. King Mini Unit", d="Lessons, readings, annotations, and art for MLK Day and beyond.", u=TC + "dr-king-mini-unit/", img="king", kw="mlk martin luther king january"),
    dict(s="history", t="Malcolm X Mini Unit", d="A ready-to-teach unit, perfect for Black History Month.", u=TC + "malcolm-x-mini-unit/", img="malcolm", kw="black history month february"),
    dict(s="history", t="KOBE Mini Unit", d="Poetry, art, and argument writing built around Kobe's \"Dear Basketball.\"", u=TC + "kobe-mini-unit/", img="kobe", kw="kobe bryant black history month"),

    dict(s="history", t="Black History Month Bundle", d="Malcolm X, Maya Angelou, Langston Hughes, and Kobe. Four weeks of lessons in one bundle!", u=T+"Black-History-Month-Bundle-Malcolm-X-Maya-Angelou-Langston-Hughes-Kobe-11024586", tpt=True, img="tpt11024586", kw="black history month february bundle"),
    dict(s="history", t="MLK and RFK's Speech", d="Dr. King through Robert F. Kennedy's speech the night he died. A full week of plans.", u=T+"Black-Excellence-Month-Martin-Luther-King-Jr-Robert-F-Kennedy-Speech-10841183", tpt=True, img="tpt10841183", kw="mlk martin luther king january rfk"),
    dict(s="history", t="Leaders of West Africa Choice Project", d="Students choose a West African ruler and build a project around them.", u=T+"Leaders-of-West-Africa-Choice-Project-15255445", tpt=True, img="tpt15255445", kw="africa mali mansa musa world history"),
    dict(s="history", t="French Revolution: SLAM Letter or MEME", d="Hamilton vs. Jefferson on the French Revolution. Students pick a side and SLAM it.", u=T+"The-French-Revolution-AHam-vs-TJeff-SLAM-Letter-MEME-10763118", tpt=True, img="tpt10763118", kw="hamilton jefferson american history"),
    dict(s="history", t="MYTHBUSTERS: Ancient Greece", d="Students bust (or confirm!) Greek myths using claim, evidence, reasoning.", u=T+"MYTHBUSTERS-Ancient-Greece-Edition-using-CER-5310535", tpt=True, img="tpt5310535", kw="greece cer pbl myths"),

    # Projects
    dict(s="projects", t="Project Based Learning Google Drive", d="My #1 best seller! 50+ full PBL units and resources for grades 5 to 12 in one growing Drive.", u=TC + "pbl-growing-drive/", img="pbl", best=True, inside="PBL_INSIDE", kw="pbl project based learning drive bundle best seller"),
    dict(s="projects", t="SGN: Some Good News Newscast", d="Students find the GOOD news and broadcast it in their own newscast. A 5-day media literacy project.", u=TC + "some-good-news-sgn-newscast-project/", img="sgn", kw="media literacy pbl"),

    dict(s="projects", t="Shark Tank Inventor Project", d="The editable version of my Shark Tank project. Students invent, pitch, and defend.", u=T+"Editable-SHARK-TANK-Inventor-Project-5381643", tpt=True, img="tpt5381643", kw="pbl shark tank invention"),

    # Classroom setup
    dict(s="setup", t="Back to School Growing Drive", d="Everything I use to start the year, in one Google Drive that keeps growing.", u=TC + "back-to-school-growing-drive/", r=ig("DZsWa_uDBBw"), img="bts", inside="BTS_INSIDE", kw="back to school first week"),
    dict(s="setup", t="Back to School Syllabus", d="An editable syllabus that's ready for your first week.", u=TC + "back-to-school-syllabus/", img="syllabus", kw="back to school"),
    dict(s="setup", t="Back to School Brochure", d="A cute Canva brochure for meet the teacher and back to school night.", u=TC + "backtoschool-brochure/", img="brochure", kw="back to school parents canva"),
    dict(s="setup", t="Editable Upper Grade Classroom Decor", d="Decor made for middle and high school walls. No baby stuff!", u="https://www.teacherspayteachers.com/Product/EDITABLE-Upper-Grade-Classroom-Decor-Middle-Junior-High-High-School-9888991", tpt=True, img="decor", kw="decor posters"),
    dict(s="setup", t="Gen Alpha Slang Posters", d="Slang posters that get a laugh EVERY time. Your students will roast you, in the best way.", u="https://www.teacherspayteachers.com/Product/LIT-Gen-Alpha-Slang-Posters-for-Middle-Junior-High-Classrooms-11945525", tpt=True, img="slang", kw="decor posters slang"),

    dict(s="setup", t="December Agenda and Riddle Slides", d="Morning slides with a riddle a day to get you to winter break.", u=T+"December-Daily-Agenda-Riddle-Slides-Editable-Canva-Google-Slides-14954927", tpt=True, img="tpt14954927", kw="december winter agenda slides riddles"),
    dict(s="setup", t="American History Classroom Posters", d="A history poster set plus my guide to making your own with AI.", u=T+"American-History-Classroom-Poster-Set-AI-Poster-Creation-Guide-17154210", tpt=True, img="tpt17154210", kw="decor posters history ai"),
    dict(s="setup", t="Editable Composition Notebook Tabs", d="Tabs for interactive notebooks. Organized notebooks all year!", u=T+"EDITABLE-Composition-Notebook-Tabs-4806109", tpt=True, img="tpt4806109", kw="interactive notebook inb tabs"),

    # For the teacher
    dict(s="teacher", t="Annotation Unlocked", d="Build annotation packets for ANY text, any grade, in about 10 minutes with AI.", u=TC + "annotation-unlocked/", r=ig("DYD6ujaTbQF"), img="annotunlock", kw="ai annotation"),
    dict(s="teacher", t="Interactive Notebooks Unlocked", d="How to launch, grade, and create interactive notebooks with AI tools.", u=TC + "interactive-notebooks-unlocked/", r=ig("DaQbqbBBCoc"), img="inb", kw="ai inb interactive notebook"),
    dict(s="teacher", t="Hot Takes: AI and Canva Magic", d="My beginner's guide to Bulk Create. Make a year of slides while your coffee is still hot.", u=TC + "guide-bulk-creation-for-teachers/", r=ig("DbYdTMAE6j0"), img="hottakes", kw="canva bulk create ai"),
    dict(s="teacher", t="How to Master AI as a Teacher", d="A step-by-step PDF with the tools and templates I actually use.", u=TC + "how-to-master-ai-pdf/", img="masterai", kw="ai guide"),
    dict(s="teacher", t="Gemini, ChatGPT and Canva Coding Prompts", d="The prompts I can't live without. Copy, paste, done.", u=TC + "geminichatgptcanva-prompts/", img="prompts", kw="ai canva code chatgpt gemini"),
    dict(s="teacher", t="PBL Backwards Planning with Claude", d="Start with the final project and let Claude help you plan backwards.", u=TC + "pbl-backwards-planning-with-claude/", r=ig("DZdWKfXh55X"), img="pblclaude", kw="ai pbl claude"),
    dict(s="teacher", t="Digital Lesson Planner", d="Plan lessons and track accommodations and behavior, all in one place.", u=TC + "ai--digital-tools/", img="planner", kw="planner accommodations behavior google"),
    dict(s="teacher", t="How I Use Claude to Run My Teacher Business", d="For my fellow teacher creators: how I use Claude behind the scenes.", u=TC + "using-claude-to-run-a-teacher-business/", r=ig("Dd-vBqSTP80"), img="claudebiz", kw="ai claude creator business"),
    dict(s="teacher", t="AI and Digital Tools Masterclass", d="My self-paced PD with video tutorials and templates. This is what teacher PD should look like!", u=TC + "aidigital-tools-pd-self-paced/", r=ig("DZsWa_uDBBw"), cv="AI Masterclass", kw="ai pd professional development"),

    # Free
    dict(s="free", t="PBL Prompt Guide", d="AI prompts to plan project based learning fast.", u=TC + "pblpromptguide/", img="pblprompt", kw="ai pbl"),
    dict(s="free", t="Teacher Tools Cheat Sheet", d="The AI tools I tell EVERY teacher to try.", u=TC + "aitoolscheatsheet/", r=ig("DWecIERE0nd"), img="cheat", kw="ai tools"),
    dict(s="free", t="Shark Tank Project", d="Students invent a product and pitch it to the sharks.", u=TC + "free-shark-tank/", cv="Shark Tank", kw="pbl project"),
    dict(s="free", t="Lesson Plan and Sub Plan Template", d="Google Docs. Make a copy and go!", u="https://docs.google.com/document/d/13rkhzs4WCBjGETf5Nv78dnA3HotOSnOS/copy", img="subplan", kw="sub plans lesson plan"),
    dict(s="free", t="AI Prompt-Writing Guide", d="How to write prompts that actually get you what you want.", u="https://drive.google.com/file/d/1CODjXRAXyXIi6JX2XMr4RQbC8eN5IM1Y/view", cv="Prompt Guide", kw="ai prompts"),
    dict(s="free", t="Daily Agenda Slides Template", d="Canva and Google Slides versions.", u="https://www.canva.com/design/DAGJc8K9FtU/rATziqhGmq4r6ZImHRCEsQ/view", img="agendafree", kw="agenda slides canva"),
    dict(s="free", t="Yearly Scope and Sequence Template", d="Map out your whole year in Google Slides.", u="https://docs.google.com/presentation/d/1XFMfXqxMUnQBuGOmCGB_qu6waSAjQ1uWiGI1whN5YqQ/edit", img="scope", kw="planning year"),
    dict(s="free", t="Socratic Seminar Guide", d="My rules and setup for discussions students actually lead.", u="https://drive.google.com/file/d/1-BM_l4P1ayUyQhdX1724t49aSVDyhk2C/view", img="socratic", kw="discussion"),
    dict(s="free", t="Name Tag Template", d="An editable Canva name tag for the first week.", u="https://www.canva.com/design/DAGI-xmdHdg/SLEHcUfRe4r9NGDSqUGr-w/view", img="nametag", kw="back to school canva"),
    dict(s="free", t="Hot Takes First Day Activity", d="An agree or disagree icebreaker that gets EVERYONE talking.", u="https://www.canva.com/design/DAGKxAy270c/oxtsgBim61xrBSggWuitOQ/view", img="hottakes1", kw="back to school icebreaker canva"),
    dict(s="free", t="Morning ClassroomScreen", d="Make a copy of my morning screen setup.", u="https://classroomscreen.com/app/p/3949e989-50a8-4b9d-9cff-0db1f1eb4811/0", cv="Morning Screen", kw="classroomscreen morning"),
    dict(s="free", t="How To Survive", d="A fun end-of-year activity where students write the survival guide.", u="https://drive.google.com/file/d/1IHXOlqylyBcKKFE0Psk6x5Q23kFbv-Gv/view", img="survive", kw="end of year"),
    dict(s="free", t="Indigenous Peoples Day Lesson", d="A primary source discussion lesson. Perfect for October!", u=T+"Indigenous-Peoples-Day-Primary-Source-Document-Discussion-Lesson-7327280", tpt=True, img="tpt7327280", kw="october history primary source"),
    dict(s="free", t="Figurative Language in Music", d="An art assessment where students find figurative language in songs.", u=T+"Figurative-Language-in-MUSIC-ART-Assessment-9746836", tpt=True, img="tpt9746836", kw="figurative language music"),
    dict(s="free", t="Caged Bird Annotations and Art", d="Maya Angelou annotations plus an art assessment.", u=T+"Maya-Angelou-I-Know-Why-The-Caged-Bird-Sings-Annotations-Art-Assessment-5165983", tpt=True, img="tpt5165983", kw="maya angelou annotation"),
    dict(s="free", t="RFK's Speech on Dr. King", d="Annotations and a graphic organizer for RFK's speech.", u=T+"On-the-Death-of-Martin-Luther-King-Jr-RFKs-Speech-6438557", tpt=True, img="tpt6438557", kw="mlk rfk speech january"),
    dict(s="free", t="Most Likely To Awards", d="Peer-voted digital awards with Google Forms. End of year GOLD.", u=T+"Most-Likely-To-Digital-Awards-Created-by-Peers-through-Google-Forms-5528821", tpt=True, img="tpt5528821", kw="end of year awards"),
    dict(s="free", t="Inspirational Quote Posters", d="Quote posters for your classroom walls.", u=T+"Inspirational-Quote-Posters-4782479", tpt=True, img="tpt4782479", kw="decor posters"),
    dict(s="free", t="Step Up to Writing Organizer", d="An 8 to 11 sentence paragraph organizer and rubric.", u=T+"Step-Up-To-Writing-8-11-Sentence-Graphic-Organizer-Rubric-4068940", tpt=True, img="tpt4068940", kw="writing paragraph organizer"),
]

SHOP_GROUPS = [
    ("ela", "ELA Units"),
    ("history", "History Mini Units"),
    ("projects", "Projects"),
    ("setup", "Classroom Setup"),
]

ABOUT = [
    "I've been teaching middle school ELA and American History for 17 years, and I still love it (most days!).",
    "I started making my own resources because I wanted lessons that actually hook middle schoolers, and tech tricks that get me out of school before dark. Now I share all of it with you.",
    "Come say hi on Instagram or TikTok. I post what's really happening in my classroom!",
]

# Real folder names from the Drives (for the "what's inside" previews)
PBL_INSIDE = [
    "1. START HERE",
    "2. Novel & Short Story Annotations & Units",
    "3. Edgar Allan Poe Collection",
    "4. Choice Projects (Any Text)",
    "5. Black Excellence Month & Womens History Month",
    "6. Other Subjects (History & Science)",
    "7. Guides & AI Help",
    "8. Seasonal Slides & Bonuses",
    "9. Interactive Notebooks",
]
BTS_INSIDE = [
    "1. Start Here",
    "Agenda & Daily Slides",
    "Planning Templates",
    "Reading & Annotation",
    "Ice Breakers & Activities",
    "Classroom Setup & Decor",
    "AI Tools & Guides",
]

CLAUDE_SITE = {
    "eyebrow": "Free for teachers",
    "headline": "New to Claude? Start here!",
    "body": "My free Claude for Teachers site walks you through it step by step, with the exact prompts I use to plan faster, differentiate without losing my mind, and get my evenings back. Beginner friendly, with an advanced level when you're ready.",
    "url": "https://thebalancedteach.tiiny.site/?v=beg",
}
