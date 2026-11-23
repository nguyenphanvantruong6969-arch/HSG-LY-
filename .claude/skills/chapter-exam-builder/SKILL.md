---
name: chapter-exam-builder
description: Build a practice-exam set from a chapter document (PDF, HTML, notes) as Word files in Vietnamese exam layout - Exam 1 (multiple choice with ascending difficulty plus a few long questions), Exam 2 (real-exam style DOK2/DOK3 problems), and one combined answer-and-solution file. Use when the user asks for "đề luyện tập", "đề kiểm tra", "bài tập chương", "make exercises/practice exam from this chapter", "output docx like a Vietnamese test", or wants the same three-file package made for another chapter or subject.
---

# chapter-exam-builder

Turns one chapter of study material into three `.docx` files that look like a Vietnamese exam paper:

1. **Exam 1** - Part I: multiple choice A-D in two columns, ascending difficulty, each question linking several topics. Part II: a few long (tự luận) questions.
2. **Exam 2** - "real deal" problems in the style of the source document's DOK2 / DOK3 exercises (reading graphs, reading a passage, data analysis, new situations, derive your own formula), with the needed formulas given when the source does so.
3. **Answers and solutions** - one combined file: answer table, worked solutions, point breakdown, common mistakes, and a map from each question to the section to revise.

Equations are native Word equations (OMML). No emoji, A4, Times New Roman, neutral header. The Chương 1 "Dao động điều hoà" set built with this skill lives in `examples/chuong1_dao_dong/` and is the reference for style and difficulty.

## Layout of this skill

- `scripts/` - `lib.py` (Word layout, LaTeX to OMML via pandoc), `render.py` (MCQ/essay rendering, option shuffling), `figlib.py` (matplotlib helpers), `build_exam.py`, `build_solutions.py`, `verify_docs.py`, `setup_env.sh`.
- `templates/` - `config_template.py`, `content_exam1_template.py`, `content_exam2_template.py`, `figs_template.py`, `check_numbers_template.py`. These run as a working demo.
- `examples/chuong1_dao_dong/` - the full real example (content, figures, config).
- `reference.md` - data schema, markup, layout options, rendering pitfalls. Read it before writing content.

## Workflow

Paths below are relative to the skill directory `.claude/skills/chapter-exam-builder/`. Use a working directory outside the skill (for example the session scratchpad) for content, figures and generated files; write the final `.docx` files into the user's repo folder (default `de_luyen_tap/`).

1. **Environment.** Run `bash scripts/setup_env.sh` once per fresh container. `libreoffice-math` is required to preview equations; without it equations render blank in the PDF preview (the `.docx` is still fine).
2. **Read the source.** PDF: Read with `pages` (at most 20 pages per call). HTML or Markdown: extract text. List the sections, formulas, existing exercise types and difficulty levels (DOK1-3). If no source document was given, ask for it.
3. **Ask quick options** with one AskUserQuestion call, defaults first (these were the user's choices last time):
   - Exam 1: 20 multiple-choice questions plus 4 long questions, 60 minutes.
   - Exam 2: 9 questions = 3 DOK2 + 6 DOK3, 20 points, 180 minutes.
   - Math level of DOK3: derivatives, second-order differential equations and centre of mass allowed, with the solution form or formulas given in the statement.
   - Header: neutral ("ĐỀ LUYỆN TẬP - <exam name>"). Never write a ministry name or "Đề thi chính thức", never imitate an official emblem.
   - Output: 3 files (Exam 1, Exam 2, combined answers), saved in the repo, not committed unless the user asks (or a stop hook asks).
   Skip any question the user already answered in the request.
4. **Compute first.** Copy `templates/check_numbers_template.py` to the working directory and compute every data value and answer independently of the written solution. Choose data so results are clean. Only after the numbers agree write the solutions.
5. **Write content** (`content_*.py`, schema in `reference.md`):
   - Multiple choice rises through four levels: recall (1 topic), comprehension (2 topics), application (2-3 topics, graphs, "n-th time", cross-topic), advanced (3 topics). Each wrong option maps to a real student mistake and has a one-line explanation. Correct letters balanced (equal counts of A-D).
   - Long questions: a, b, c parts with points; the last is the hardest.
   - Exam 2: new situations, not copies of the source exercises. DOK2 = reading a graph/passage/data table. DOK3 = new situation, derive the formula, connect topics. Give "Cho biết" when the source does. Points per part must sum to the question total; total of the exam must match the header.
6. **Figures.** Copy `templates/figs_template.py`; draw graphs black and white, grid like exam paper, STIX font, 300 dpi, labels as symbols and units only. Check each PNG by viewing it.
7. **Config.** Copy `templates/config_template.py` to the working directory, set titles, codes, time, `OUT_DIR`, `FIG_DIR`, the content module names, and the `map` of question to revision section.
8. **Build.** `python3 scripts/build_exam.py <config.py>` then `python3 scripts/build_solutions.py <config.py>` (both loop to settle the page count in "Đề có N trang"). Environment variable `EXAM_OUT_DIR` sets the output folder.
9. **Look at every page.** The build leaves PDFs in the `--tmp` folder; render with `pdftoppm -r 70 -png` and view the images. Fix gaps, split figures, wrapped option rows, stray glyphs (a `¿` means a math fragment the renderer cannot handle; see `reference.md`).
10. **Verify.** `python3 scripts/verify_docs.py --exam <exam files> --solutions <solutions file>` must pass (no emoji, no stray glyph, no solution text inside exam files). Also confirm: letters balanced, exam 1 points add to 10, exam 2 points add to 20, question counts match.
11. **Report** honestly: files, page counts, what was checked, what the user should double check (open once in Word; page count may differ by one). Do not claim a Word check that was not done.
12. **Git.** Commit and push only when the user asks or a stop hook requires it, to the branch the session was assigned. Never open a pull request unless asked.

## Quality rules

- Vietnamese throughout; decimal comma; units as plain Unicode (m/s², cm³).
- Never paste solutions into exam files. Exam files must not contain "Lời giải" or "Đáp án".
- Every numeric answer is recomputed independently; show the check in the final report.
- Keep the user's tutoring preferences from the conversation (address "em", name, formal tone). If the user asks for exams, do not also restart a Socratic Q&A.
- Content is new: do not copy exercises from the source document. Adapting a type of exercise is fine.
- Keep the set honest about difficulty: DOK3 questions should need several steps and a derivation, not just a formula.

## When something fails

- Equations blank in PDF preview: install `libreoffice-math` (`scripts/setup_env.sh`).
- `¿` in text: rewrite that math fragment as text plus a simpler formula (details in `reference.md`).
- Figure splits from its question: reduce its width or reorder; check in the PDF.
- `AssertionError` about `LETTERS`: the answer-letter string must have one letter per multiple-choice question.
