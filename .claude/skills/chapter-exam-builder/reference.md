# Reference: data schema, markup, layout, known pitfalls

## Content modules

A content module is a Python file imported by name from `config.py` (`module='content_de1'`). It lives next to the config.

### Exam 1 module (`kind='mcq_essay'`): `LETTERS`, `MCQ`, `ESS`

```python
LETTERS = "BDACACBDACDBACBDACBD"      # correct letter of each MCQ; len == len(MCQ); keep A-D balanced

MCQ = [dict(
  q=r"question text with $math$",
  opts=[r"CORRECT", r"wrong 1", r"wrong 2", r"wrong 3"],   # correct option FIRST; builder shuffles to LETTERS[i]
  fig=("file.png", width_cm, "Hình 1"),                      # optional, shown between question and options
  layout="2x2",                                              # optional: "4x1" (one row), "2x2", "1" (one per line)
  sol=[r"solution paragraph", ...],                          # shown only in the solutions file
  wrong=[r"B: why wrong 1", r"C: why wrong 2", r"D: why wrong 3"],   # original order; "B, D: ..." allowed
)]

ESS = [dict(pts=1.25, level="DOK2", stem=r"...", fig=(...), parts=[(r"part text", 0.5), ...],
            sol=[("a", 0.5, [para, ("eq", r"latex"), ("table", tbl)]), ...],
            common=[r"typical mistake"], ans_fig=("a.png", width_cm, "caption"))]
```

Automatic layout: option text of about 5 characters or fewer goes in one row, up to about 14 characters in a 2x2 grid, longer one per line. Use `layout` when a math fraction makes a row taller than expected.

### Exam 2 module (`kind='dok'`): `ESS` only

Optional per-question keys: `passage` (boxed reading text), `stem`, `given` ("Cho biết" block), `table` + `table_caption` (`dict(header=[...], rows=[[...]], widths=[cm,...])`), `fig`, `parts`, `sol`, `common`, `ans_figs` (list of `(file, width_cm, caption)` shown only in the solutions), `level` (printed as [DOK2] in the header of each question).
Points of `parts` must add to `pts`; points of `sol` items must add to `pts` as well.

## Markup inside any string

- `$latex$` inline equation (native Word equation); `$$latex$$` display; in solution lists use `("eq", r"latex")` for a centred display equation.
- `**bold**`, `__italic__`.
- Decimal numbers inside math may be written with a comma (`0,5`); the builder converts to `0{,}5`.
- Multi-letter subscripts such as `v_{max}` are rendered upright automatically.
- A math fragment that starts with `=`, `\approx`, `\ge`, `\le`, `\Rightarrow` is automatically split into a text sign plus the rest.

## Config keys

`EXAMS` items: `kind`, `module`, `out`, `code` (printed "Mã đề thi <code>"), `footer`, `short` ("Đề 1"), `sol_title`, `left`/`right` (header lines as `(text, bold, italic)`, `{N}` becomes the page count), `intro`, `closing`, `extra_math`, `map` (`{question: (topic, revise_section)}`), and for `mcq_essay`: `part1_title`, `part1_sub` (`{n_mcq}`), `part2_title`, `part2_sub` (`{n_ess}`); for `dok`: `sol_note`; optional `show_level`.
`SOL` keys: `out`, `footer`, `left`, `right`, `box`, `intro`, `map_note`, `extra_math`.

## Rendering pitfalls already met (and the fix)

| Symptom | Cause | Fix |
|---|---|---|
| Equations blank in PDF | `libreoffice-math` not installed | `scripts/setup_env.sh` |
| Empty-box glyph next to a unit (m/s then a box then 2) | `$^2$` has an empty base | Write `m/s²` as plain Unicode |
| `¿` after `=` or inside brackets | math starts with an operator, or brackets do not match such as `(a;b]` | Put the operator in text; use `-\pi<\varphi\le\pi` instead of an interval |
| `¿` after a lone `$+$` | one-symbol math | Write the word or plain `+` |
| Spaced `0 , 5` | comma read as a list separator | Already handled by `0{,}5` conversion |
| Italic spaced `m a x` | multi-letter subscript | Already handled (upright) |
| Large gaps between words | justified text with inline math | Builders use left alignment |
| Table column wraps | LibreOffice ignores cell widths | `lib.Doc.table` sets column widths too |
| Page count differs in Word | different line breaking | "Đề có N trang" is a NUMPAGES field |

## Figures

`scripts/figlib.py` helpers: `spring`, `ground`, `block`, `dim`, `blank_axes`, `graph_axes`, `save`. Use `plt` with the STIX font set there. Labels with Vietnamese words use `fontdict=VI` (DejaVu Serif). Name files `d1_*.png` for Exam 1, `d2_*.png` for Exam 2, `a_*.png` for answer-only figures. Width limits: in the two-column part keep figures at 7 cm or less.

## Verification checklist

- `check_numbers_*.py` passes and matches the solutions.
- `verify_docs.py` passes.
- Every PDF page viewed.
- Letters balanced; points: Exam 1 total as stated, Exam 2 total as stated.
- Final report lists what was and was not checked.
