#!/usr/bin/env python3
"""Build the static site from _build/base.html and page fragments."""

from pathlib import Path
import html

import course_data

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "_build"

NAV_ITEMS = [
    ("About", "about.html", "about"),
    ("Our approach", "our-approach.html", "approach"),
    ("Courses", "courses.html", "courses"),
    ("Our teacher", "about.html#teacher", "teacher"),
    ("Contact", "contact.html", "contact"),
]

PAGES = {
    "home": {
        "out": "index.html",
        "title": "The Foremost Institute | Rooted in Faith. Rising as Leaders.",
        "description": "The Foremost Institute is an educational and service institute in Harrow, London, nurturing young Muslim leaders through the authentic knowledge of Islam.",
        "canonical": "",
        "active": "",
    },
    "about": {
        "out": "about.html",
        "title": "About | The Foremost Institute",
        "description": "Meet The Foremost Institute: an educational and service institute in Harrow bringing authentic Islamic knowledge to young Muslim adults aged 15 and above.",
        "canonical": "about/",
        "active": "about",
    },
    "approach": {
        "out": "our-approach.html",
        "title": "Our Approach | The Foremost Institute",
        "description": "Knowledge, service and leadership: how The Foremost Institute nurtures young Muslims through authentic learning and real-world action.",
        "canonical": "our-approach/",
        "active": "approach",
    },
    "courses": {
        "out": "courses.html",
        "title": "Courses | The Foremost Institute",
        "description": "Foundation courses in Qur'an studies, Islamic history and belief for young adults aged 15 and above, through university.",
        "canonical": "courses/",
        "active": "courses",
    },
    "course-quran1": {
        "out": "course-our-journey-with-the-quran-part-1-2.html",
        "title": "Our Journey with the Quran (Part 1) | The Foremost Institute",
        "description": "Year one of a three-year reflective study of the 30th Juz: Surah Al-Fatiha and the last ten surahs, grounded in traditional tafsir.",
        "canonical": "courses/our-journey-with-the-quran-part-1-2/",
        "active": "courses",
    },
    "course-quran2": {
        "out": "course-our-journey-with-the-quran-part-2.html",
        "title": "Our Journey with the Quran (Part 2) | The Foremost Institute",
        "description": "Year two of Our Journey with the Quran: Surat Al-Humazah to Surat Ash-Shams, studied in context and applied to daily life.",
        "canonical": "courses/our-journey-with-the-quran-part-2/",
        "active": "courses",
    },
    "course-prophet": {
        "out": "course-life-of-the-prophet-peace-be-upon-him.html",
        "title": "Life of the Prophet (peace be upon him) | The Foremost Institute",
        "description": "A thorough study of the Prophet's life and mission, drawing out timeless lessons for the challenges Muslims face today.",
        "canonical": "courses/life-of-the-prophet-peace-be-upon-him/",
        "active": "courses",
    },
    "course-wist": {
        "out": "course-why-islam-is-true-wist.html",
        "title": "Why Islam is True (WIST) | The Foremost Institute",
        "description": "A structured, evidence-based exploration of why Islam is true, taught by a certified Why Islam is True instructor. Next intake 2027.",
        "canonical": "courses/why-islam-is-true-wist/",
        "active": "courses",
    },
    "contact": {
        "out": "contact.html",
        "title": "Contact | The Foremost Institute",
        "description": "Get in touch with The Foremost Institute in Harrow, London. Ask about courses, enrolment or the institute's work.",
        "canonical": "contact/",
        "active": "contact",
    },
    "basket": {
        "out": "basket.html",
        "title": "Basket | The Foremost Institute",
        "description": "Your basket at The Foremost Institute.",
        "canonical": "basket/",
        "active": "",
    },
    "account": {
        "out": "my-account.html",
        "title": "My Account | The Foremost Institute",
        "description": "Sign in to your Foremost Institute account.",
        "canonical": "my-account/",
        "active": "",
    },
}


def nav_markup(active):
    links = []
    for label, href, key in NAV_ITEMS:
        current = key == active
        classes = "nav-link is-active" if current else "nav-link"
        aria = ' aria-current="page"' if current else ""
        links.append(f'      <a href="{href}" class="{classes}"{aria}>{label}</a>')
    return "\n".join(links)


def mobile_nav_markup(active):
    links = []
    for i, (label, href, key) in enumerate(NAV_ITEMS, start=1):
        current = key == active
        classes = "is-active" if current else ""
        aria = ' aria-current="page"' if current else ""
        links.append(
            f'    <a href="{href}" class="{classes}"{aria}><span>{i:02d}</span>{label}</a>'
        )
    return "\n".join(links)


def main():
    template = (BUILD / "base.html").read_text(encoding="utf-8")

    for key, meta in PAGES.items():
        if key.startswith("course-"):
            content = course_data.render(key).strip()
        else:
            fragment_path = BUILD / "pages" / f"{key}.html"
            if not fragment_path.exists():
                raise SystemExit(f"Missing fragment: {fragment_path}")
            content = fragment_path.read_text(encoding="utf-8").strip()

        page = template
        replacements = {
            "{{TITLE}}": html.escape(meta["title"]),
            "{{DESCRIPTION}}": html.escape(meta["description"]),
            "{{CANONICAL}}": meta["canonical"],
            "{{BODY_CLASS}}": f'page-{key}',
            "{{NAV}}": nav_markup(meta["active"]),
            "{{MOBILE_NAV}}": mobile_nav_markup(meta["active"]),
            "{{CONTENT}}": content,
        }
        for token, value in replacements.items():
            page = page.replace(token, value)

        out_path = ROOT / meta["out"]
        out_path.write_text(page, encoding="utf-8")
        print(f"built {out_path.name}")


if __name__ == "__main__":
    main()
