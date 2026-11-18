"""Course detail page renderer."""

LIVE_BASE = "https://theforemostinstitute.com/courses/"

COURSES = {
    "course-quran1": {
        "title": "Our Journey with the Quran <span>(Part 1)</span>",
        "short": "Our Journey with the Quran",
        "category": "Qur’an Studies · Part 1",
        "cover": "assets/img/opt/course-quran2.webp",
        "cover_alt": "Course cover for Our Journey with the Quran, Part 1",
        "lede": "This course is designed for students who have the desire to develop a deeper connection with Allah through His book and are keen to learn and understand the meanings of the Quran.",
        "age": "16+",
        "lessons": "24 lessons",
        "location": "Online",
        "chips": [("i-user", "Ages 16+"), ("i-book", "24 lessons"), ("i-monitor", "Online only")],
        "price": "£28",
        "price_note": "per month, over 8 months",
        "dates": "12 September 2026 – 1 May 2027",
        "schedule": "Saturdays, 11:15am – 12:45pm",
        "format": "Interactive, classwork, group activities, weekly quizzes",
        "overview": [
            "This is year one of a three-year course providing an in-depth and reflective study of the surahs in the 30th Juz of the Quran. It begins by introducing students to the historical, social and cultural context in which the Quran was revealed, before moving into the meanings and tafsir of Surah Al-Fatiha and the last ten surahs.",
            "The course is based on research of traditional tafaseer including Ibn Kathir, Maariful Quran by Mufti Muhammad Shafi, The Noble Quran by Mufti Taqi Uthmani, and tafsir courses delivered by Shaykh Haytham Tamim, Shaykh Akram Nadwi and Ustadh Nouman Ali Khan. Other sources include the Seerah, Hadith and Quran.",
        ],
        "years": [
            ("Year 1", "Introduction to the Quran, Surat Al-Fatiha and Surat An-Naas to Surat Al-Feel", True),
            ("Year 2", "Surat Al-Humazah to Surat Ash-Shams", False),
            ("Year 3", "Surat Al-Balad to Surat An-Naba", False),
        ],
        "objectives": [
            ("Introduction to the Quran",
             "Examine the historical and geographical background of Arabia, the major tribes, the lineage of the Prophet (peace be upon him), and how history shaped Arab beliefs and culture. Review the major religions of sixth-century Arabia, pagan practices in light of authentic narrations, the sources of tafsir, the compilation and preservation of the Quran, and the etiquettes of the student of knowledge."),
            ("Al-Fatiha and the last ten surahs",
             "Study the context in which each surah was revealed and key concepts such as the Hereafter, the oneness of God and the meaning of Rabb in clear, rational terms. Study each surah verse by verse, reflect on its lessons and application, learn the translation of key Arabic words, and practise translating verses into English."),
        ],
        "requirements": [
            "Punctuality and regular attendance are important values of the course.",
            "Students are encouraged to read through their notes after class and be ready for pop quizzes.",
            "Class discussion and participation are rewarded and highly encouraged.",
        ],
        "books": "Students will need a copy of The Majestic Quran (used in the second term) and a Quranic Arabic textbook to be confirmed.",
        "live": LIVE_BASE + "our-journey-with-the-quran-part-1-2/",
        "related": ["course-quran2", "course-prophet", "course-wist"],
    },
    "course-quran2": {
        "title": "Our Journey with the Quran <span>(Part 2)</span>",
        "short": "Our Journey with the Quran",
        "category": "Qur’an Studies · Part 2",
        "cover": "assets/img/opt/course-quran1.webp",
        "cover_alt": "Course cover for Our Journey with the Quran, Part 2",
        "lede": "Starting from Surat Al-Humazah, this course is ideally for students who have completed Part 1 and want to dive deeper into the next set of surahs. It is also open to students with previous knowledge of the early surahs.",
        "age": "16+",
        "lessons": "24 lessons",
        "location": "Harrow",
        "chips": [("i-user", "Ages 16+"), ("i-book", "24 lessons"), ("i-pin", "Harrow")],
        "price": "£32",
        "price_note": "per month, over 8 months",
        "dates": "12 September 2026 – 1 May 2027",
        "schedule": "Saturdays, 3:00pm – 4:30pm",
        "format": "Interactive, classwork, group activities, weekly quizzes",
        "overview": [
            "Part 2 is year two of a three-year course providing an in-depth and reflective study of the surahs in the 30th Juz. It continues from Surat Al-Humazah to Surat Ash-Shams, with a deeper study of context, language and daily application.",
            "The course is based on research of traditional tafaseer including Ibn Kathir, Maariful Quran by Mufti Muhammad Shafi, The Noble Quran by Mufti Taqi Uthmani, and tafsir courses delivered by Shaykh Haytham Tamim, Shaykh Akram Nadwi and Ustadh Nouman Ali Khan. Other sources include the Seerah, Hadith and Quran.",
        ],
        "years": [
            ("Year 1", "Introduction to the Quran, Surat Al-Fatiha and Surat An-Naas to Surat Al-Feel", False),
            ("Year 2", "Surat Al-Humazah to Surat Ash-Shams", True),
            ("Year 3", "Surat Al-Balad to Surat An-Naba", False),
        ],
        "objectives": [
            ("Surat Al-Humazah to Surat Ash-Shams",
             "Study the context in which each surah was revealed and the literary devices used in the Quran — their purpose and placement within each surah."),
            ("Verse by verse, with application",
             "Study each surah verse by verse, reflect on its lessons and application to daily life, learn the root meanings of Arabic words where applicable, and practise translating verses into English."),
        ],
        "requirements": [
            "Punctuality and regular attendance are important values of the course.",
            "Students are encouraged to read through their notes after class and be ready for pop quizzes.",
            "Class discussion and participation are rewarded and highly encouraged.",
        ],
        "books": "Students will need a copy of The Majestic Quran (used in the second term) and a Quranic Arabic textbook to be confirmed.",
        "live": LIVE_BASE + "our-journey-with-the-quran-part-2/",
        "related": ["course-quran1", "course-prophet", "course-wist"],
    },
    "course-prophet": {
        "title": "Life of the Prophet <span>(peace be upon him)</span>",
        "short": "Life of the Prophet",
        "category": "Islamic History · Seerah",
        "cover": "assets/img/opt/course-prophet.webp",
        "cover_alt": "Course cover for Life of the Prophet",
        "lede": "This course is ideal for students who want to immerse themselves in a thorough study of the Prophet’s biography and to reflect and derive inspirational lessons from the significant events around his life.",
        "age": "15+",
        "lessons": "24 lessons",
        "location": "Online",
        "chips": [("i-user", "Ages 15+"), ("i-book", "24 lessons"), ("i-monitor", "Online only")],
        "price": "£26",
        "price_note": "per month, over 8 months",
        "dates": "",
        "schedule": "Saturdays, 1:00pm – 2:15pm",
        "format": "Interactive, classwork, group activities, weekly quizzes",
        "overview": [
            "This is a comprehensive course offering more than a historical narrative of the events surrounding the Prophet’s life and mission. It is an opportunity to delve into and reflect on the deeper meanings of significant events in his prophetic life, and how they can be applied when addressing important challenges Muslims face today.",
            "The primary text is The Sirah of the Prophet (peace be upon him) by Dr. Yasir Qadhi. Supplementary texts include Seerah Ibn Hisham, The Sealed Nectar, and Muhammad Rasul Allah, the Apostle of Mercy by Abul Hasan Ali Hasani Nadwi.",
        ],
        "years": [],
        "objectives": [
            ("The prophetic timeline",
             "Review the important chronological events of the Prophet’s early life, his mission in the early revelatory period in Makkah, and the building of the Muslim community in Madinah."),
            ("Lessons for today",
             "Draw on key lessons from these events and consider how they can inspire a thoughtful response to the contemporary challenges Muslims face."),
            ("Character and humanitarian values",
             "Explore the key humanitarian values the Prophet (peace be upon him) taught and lived, and how they carry universal importance and application."),
        ],
        "requirements": [
            "Punctuality and regular attendance are important values.",
            "Students are encouraged to read through their notes after class and be ready for pop quizzes.",
            "Class discussion and participation are rewarded and highly encouraged.",
            "Students may be assigned extra reading outside of class.",
        ],
        "books": "The primary text is The Sirah of the Prophet by Dr. Yasir Qadhi. Supplementary reading includes Seerah Ibn Hisham, The Sealed Nectar and Muhammad Rasul Allah by Abul Hasan Ali Hasani Nadwi.",
        "live": LIVE_BASE + "life-of-the-prophet-peace-be-upon-him/",
        "related": ["course-quran1", "course-quran2", "course-wist"],
    },
    "course-wist": {
        "title": "Why Islam is True <span>(WIST)</span>",
        "short": "Why Islam is True",
        "category": "Belief · WIST",
        "cover": "assets/img/opt/course-wist.webp",
        "cover_alt": "Course cover for Why Islam is True",
        "lede": "For teenagers seeking certainty in their faith and a rational understanding of why Islam is true.",
        "age": "15+",
        "lessons": "20 lessons",
        "location": "Harrow",
        "chips": [("i-user", "Ages 15+"), ("i-book", "20 lessons"), ("i-pin", "Harrow Arts Centre")],
        "price": "",
        "price_note": "",
        "dates": "Next intake: September 2027",
        "schedule": "Saturdays, 2:00pm – 3:15pm",
        "format": "Discussion, critical thinking and real-life case studies",
        "overview": [
            "Can you explain why you are Muslim? Is Islam the true religion? How can we know there is One God? This course explores these fundamental questions through a structured, evidence-based approach that equips students to understand and articulate the rational foundations of Islamic belief.",
            "Developed and taught by Shaykh Hamza Karamali at Basira Education, the course examines the key arguments for the existence and oneness of God while addressing contemporary challenges raised by atheism and other worldviews. It will be taught by Sabeen Sheikh, a certified instructor.",
        ],
        "years": [],
        "objectives": [
            ("Foundations", "Examine the meaning and foundations of Islam."),
            ("Evidence and reason", "Understand how Islamic belief is grounded in evidence and reason rather than personal preference."),
            ("Arguments for God", "Study the major rational arguments for the existence and attributes of God, including the Argument from Contingency, the Design Argument and the Argument for the Oneness of God."),
            ("Contemporary questions", "Explore questions relating to evolution, evil and suffering through the lens of Islamic rational theology."),
            ("Confident conversation", "Develop confidence in answering common questions about faith, belief and the existence of God."),
        ],
        "requirements": [],
        "books": "",
        "live": LIVE_BASE + "why-islam-is-true-wist/",
        "related": ["course-quran1", "course-prophet", "course-quran2"],
    },
}


def fact_rows(c):
    rows = [
        ("i-user", "Age group", c["age"]),
        ("i-book", "Duration", c["lessons"]),
        ("i-calendar", "Schedule", c["schedule"]),
        ("i-pin", "Location", c["location"]),
        ("i-compass", "Format", c["format"]),
    ]
    if c["dates"]:
        rows.insert(2, ("i-calendar", "Dates", c["dates"]))
    return rows


def render(key):
    c = COURSES[key]
    chips = "\n".join(
        f'<li><svg class="icon" aria-hidden="true"><use href="#{icon}"/></svg> {label}</li>'
        for icon, label in c["chips"]
    )

    years_html = ""
    if c["years"]:
        cards = []
        for label, text, current in c["years"]:
            cls = "year-card is-current" if current else "year-card"
            badge = " <span>Current year</span>" if current else ""
            cards.append(
                f'<div class="{cls}"><strong>{label}{badge}</strong><p>{text}</p></div>'
            )
        years_html = f"""
      <section class="course-section" id="journey">
        <p class="eyebrow">The three-year journey</p>
        <h2>A study of the 30th Juz,<br><em>one year at a time.</em></h2>
        <div class="year-grid">
          {''.join(cards)}
        </div>
      </section>"""

    objectives = "\n".join(
        f"<li><strong>{title}</strong><p>{text}</p></li>"
        for title, text in c["objectives"]
    )

    requirements = ""
    if c["requirements"]:
        req_items = "\n".join(
            f'<li><svg class="icon" aria-hidden="true"><use href="#i-check"/></svg><span>{item}</span></li>'
            for item in c["requirements"]
        )
        books = f'<p class="book-note"><strong>Reading:</strong> {c["books"]}</p>' if c["books"] else ""
        requirements = f"""
      <section class="course-section" id="requirements">
        <p class="eyebrow">Course requirements</p>
        <h2>How to get the most<br><em>from the course.</em></h2>
        <ul class="check-list">{req_items}</ul>
        {books}
      </section>"""

    if c["price"]:
        price_html = f'<p class="enrol-price">{c["price"]} <span>/ month</span></p><p class="enrol-sub">{c["price_note"]}</p>'
        cta_label = "Enrol on the live site"
        note = "Payments are deducted monthly over 8 months from the date of registration."
        hero_fee_label = "Course fee"
        hero_fee_value = f'{c["price"]} <small>/ month</small>'
        hero_fee_note = c["price_note"]
    else:
        price_html = '<p class="enrol-price enrol-price--text">Next intake<br><span>September 2027</span></p>'
        cta_label = "Register your interest"
        note = "This course will next be offered in September 2027. Register your interest on the live course page."
        hero_fee_label = "Next intake"
        hero_fee_value = "September 2027"
        hero_fee_note = "Register your interest on the live course page"

    facts = "\n".join(
        f'<li><svg class="icon" aria-hidden="true"><use href="#{icon}"/></svg><div><span>{label}</span><strong>{value}</strong></div></li>'
        for icon, label, value in fact_rows(c)
    )

    related_cards = []
    for rkey in c["related"]:
        r = COURSES[rkey]
        related_cards.append(f"""
          <a class="related-card" href="{page_for(rkey)}">
            <div class="related-cover"><img src="{r['cover']}" width="820" height="820" alt="{r['cover_alt']}" loading="lazy"></div>
            <div class="related-body">
              <span>{r['category']}</span>
              <h3>{r['short']}</h3>
              <span class="related-link">View course <svg class="icon" aria-hidden="true"><use href="#i-arrow"/></svg></span>
            </div>
          </a>""")

    detail_actions = f"""
        <div class="enrol-actions">
          <a href="{c['live']}" class="btn btn-primary">{cta_label} <svg class="icon" aria-hidden="true"><use href="#i-arrow"/></svg></a>
          <a href="contact.html" class="text-link">Ask a question <svg class="icon" aria-hidden="true"><use href="#i-arrow"/></svg></a>
        </div>"""

    return f"""
<section class="page-hero course-hero">
  <div class="pattern page-hero-pattern" aria-hidden="true"></div>
  <div class="wrap page-hero-grid">
    <div class="page-hero-copy">
      <nav class="breadcrumb reveal" aria-label="Breadcrumb">
        <a href="index.html">Home</a><span aria-hidden="true">/</span><a href="courses.html">Courses</a><span aria-hidden="true">/</span><span>{c['short']}</span>
      </nav>
      <p class="course-tag-inline reveal">{c['category']}</p>
      <h1 class="reveal">{c['title']}</h1>
      <p class="page-hero-lede reveal">{c['lede']}</p>
      <ul class="hero-chips reveal">{chips}</ul>
      <div class="page-hero-actions reveal">
        <a href="#course-details" class="btn btn-primary">Course details <svg class="icon" aria-hidden="true"><use href="#i-arrow"/></svg></a>
        <a href="{c['live']}" class="text-link">{cta_label} <svg class="icon" aria-hidden="true"><use href="#i-arrow"/></svg></a>
      </div>
    </div>
    <div class="course-hero-panel reveal">
      <img src="{c['cover']}" width="820" height="820" alt="{c['cover_alt']}" fetchpriority="high">
      <div class="course-hero-note">
        <span>{hero_fee_label}</span>
        <strong>{hero_fee_value}</strong>
        <p>{hero_fee_note}</p>
      </div>
    </div>
  </div>
</section>

<section class="course-detail" id="course-details">
  <div class="wrap course-layout">
    <article class="course-main">
      <section class="course-section" id="overview">
        <p class="eyebrow">Overview</p>
        <h2>About this course.</h2>
        {''.join(f'<p>{p}</p>' for p in c['overview'])}
      </section>
      {years_html}
      <section class="course-section" id="objectives">
        <p class="eyebrow">What you will study</p>
        <h2>Objectives of<br><em>this course.</em></h2>
        <ol class="number-list">{objectives}</ol>
      </section>
      {requirements}
    </article>

    <aside class="enrol-card" aria-label="Course details and enrolment">
      <p class="eyebrow">Course details</p>
      {price_html}
      <ul class="enrol-facts">{facts}</ul>
      {detail_actions}
      <p class="enrol-note">{note}</p>
    </aside>
  </div>
</section>

<section class="related-courses">
  <div class="wrap">
    <div class="section-head reveal">
      <div>
        <p class="eyebrow">Continue exploring</p>
        <h2 class="h2">Other foundation<br><em>courses.</em></h2>
      </div>
      <p>Each course stands on its own, and together they build a broad foundation in the Islamic sciences.</p>
    </div>
    <div class="related-grid">
      {''.join(related_cards)}
    </div>
  </div>
</section>

<section class="cta">
  <div class="pattern cta-pattern" aria-hidden="true"></div>
  <div class="wrap">
    <p class="eyebrow eyebrow-light reveal">Begin here</p>
    <h2 class="reveal">One course can change<br><em>the way you see everything.</em></h2>
    <p class="reveal">If you would like help choosing, write to us — we will point you in the right direction.</p>
    <div class="cta-actions reveal">
      <a href="courses.html" class="btn btn-gold">See all courses <svg class="icon" aria-hidden="true"><use href="#i-arrow"/></svg></a>
      <a href="contact.html" class="btn btn-outline-light">Talk to us</a>
    </div>
  </div>
</section>
"""


def page_for(key):
    return {
        "course-quran1": "course-our-journey-with-the-quran-part-1-2.html",
        "course-quran2": "course-our-journey-with-the-quran-part-2.html",
        "course-prophet": "course-life-of-the-prophet-peace-be-upon-him.html",
        "course-wist": "course-why-islam-is-true-wist.html",
    }[key]
