# The Foremost Institute — website redesign

A static, multi-page design concept for [theforemostinstitute.com](https://theforemostinstitute.com/), built with the institute's own content, course imagery and brand identity.

Every section of the original site is represented as its own page, with one shared header, navigation and footer.

## Preview

Open `index.html` directly, or serve the folder locally:

```bash
cd /Users/fahadurrehmankhan/Documents/tfi
python3 -m http.server 8080
```

Then visit <http://localhost:8080/>.

## Pages

| Page | File |
| --- | --- |
| Home | `index.html` |
| About (vision, values, teacher, team) | `about.html` |
| Our approach | `our-approach.html` |
| Courses | `courses.html` |
| Our Journey with the Quran — Part 1 | `course-our-journey-with-the-quran-part-1-2.html` |
| Our Journey with the Quran — Part 2 | `course-our-journey-with-the-quran-part-2.html` |
| Life of the Prophet (peace be upon him) | `course-life-of-the-prophet-peace-be-upon-him.html` |
| Why Islam is True (WIST) | `course-why-islam-is-true-wist.html` |
| Contact | `contact.html` |
| Basket | `basket.html` |
| My account | `my-account.html` |

The basket and account pages are styled previews. The contact, newsletter and account forms are front-end only and need a backend, CRM or authentication provider before publishing.

## Project structure

- `assets/css/style.css` — design system, page layouts and responsive rules
- `assets/js/main.js` — mobile menu, course filters, FAQ accordion, scroll reveals, form validation and preview states
- `assets/img/opt/` — optimised WebP imagery used across the pages
- `assets/favicon.png` — favicon
- `_build/base.html` — shared document shell, header, mobile menu and footer
- `_build/pages/` — page content fragments
- `_build/course_data.py` — course facts and course-detail page renderer
- `_build/build.py` — generates every page into the project root
- `_reference/` — original site captures, kept for content reference only

## Rebuilding

The HTML files in the project root are generated. Edit the fragments or course data, then run:

```bash
cd /Users/fahadurrehmankhan/Documents/tfi
python3 _build/build.py
```

## Notes

- Course information, ages, prices, locations, schedules and teacher credentials come from the live site.
- Enrolment and payment actions on the course pages link to the live Foremost Institute site.
- The newsletter, contact and account forms are front-end only. Their code comments mark where a backend or CRM should be connected.
- The layout was checked in Chrome at 360, 390, 768, 1024 and 1440 px, including the mobile menu focus trap, course filtering, FAQ accordion and form states.
