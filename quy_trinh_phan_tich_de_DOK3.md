# Workflow for Analysing a DOK3 Physics Question *Before* Solving It
### (Quy trình phân tích đề DOK3 trước khi giải)

---

## 0. Why this feels hard: what the research says

| Finding | Source | What it means for you |
|---|---|---|
| Novices sort problems by **surface features** ("a tube in a liquid", "a graph"); experts sort by **deep principle** ("restoring force ∝ displacement → SHM"). | Chi, Feltovich & Glaser (1981), *Cognitive Science* | Your first job is to strip the story away and find the principle. |
| Experts spend a long time on a **qualitative representation** (sketch, forces, what changes) before writing any equation; novices jump straight to hunting for formulas containing the unknown. | Larkin, McDermott, Simon & Simon (1980), *Science* | Do not write a formula until you can say in words what is happening physically. |
| "Formula hunting" (means-ends analysis) overloads working memory, so you solve but do not learn the structure. | Sweller (1988), Cognitive Load Theory | A fixed checklist frees memory for thinking. |
| Successful problem solving follows phases: **Focus → Describe physics → Plan → Execute → Evaluate**. | Heller & Heller, University of Minnesota (physics education research); Reif (1995/2008); Pólya, *How to Solve It* (1945) | The workflow below is a compressed version of this. |
| DOK3 = **strategic thinking**: multiple steps, choosing a method, justifying, interpreting data/graphs. Not one recall + one formula. | Webb's Depth of Knowledge | Expect: link between parts, hidden data, data read from a graph, a "show that". |

Key conclusion: the difficulty is not missing knowledge. It is a missing **translation step** between Vietnamese text and physics models.

---

## 1. The 6-pass workflow (Đọc 6 lượt)

### Pass 1 — Skeleton scan (30 seconds)
Do not read the details yet. Answer only:
1. How many parts? What is the **command word** of each part?
2. Which parts depend on each other? (Look for "giả sử biểu thức ở phần (a) đúng", "từ kết quả trên…")

**Command-word dictionary**

| Command word | What it really asks | Typical shape of answer |
|---|---|---|
| Chứng minh / Show that | Start from given facts, arrive at the stated result. The result is given — the *link* is marked. | Definition → compare → conclude |
| Tính / Calculate | Number + unit | Formula → substitution → value |
| Xác định / Determine | Number, possibly read from data/graph | Read data → formula |
| Nêu / State | One short observable fact | One sentence, no derivation |
| Giải thích / Explain | Cause → mechanism → effect | 2–3 linked sentences |
| Nhận xét / Comment on | Compare with expectation / ideal model | Trend + reason |

### Pass 2 — Line-by-line translation (Dịch từng câu sang vật lý)
For every phrase, fill a 3-column table:

| Phrase in the question | Physics meaning | Symbol / consequence |
|---|---|---|

Rule: *every adjective is there for a reason.* Words like "kín", "đường kính **ngoài**", "nhỏ", "thẳng đứng", "chất lỏng **khác**" are almost always hidden data or hidden assumptions.

### Pass 3 — Draw and model (Vẽ và mô hình hoá)
1. Sketch the system at **equilibrium** and at a **displaced** position.
2. List forces / energies. What is constant? What changes?
3. State the idealisations (no friction, small displacement, rigid body…).

### Pass 4 — Classify by principle (Gọi tên nguyên lý)
Ask: *"Which chapter would a textbook put this in, and which single law governs it?"*
Write it as one sentence: "This is ___ because ___."

Trigger patterns (examples for Chương 1 – Dao động):

| You see | Think |
|---|---|
| a = −(constant)·x | SHM, ω² = constant |
| Restoring force ∝ displacement | SHM; find k_eff, then ω = √(k_eff/m) |
| y–t graph | Read T (peak to peak), amplitude, phase at t = 0 |
| Peaks getting smaller | Damping (tắt dần) |
| Floating body | Archimedes: F = ρ g V_displaced |

### Pass 5 — Backward plan (Lập kế hoạch ngược từ ẩn số)
Build a chain from the unknown back to the data:

```
Target  ←  equation that contains it  ←  quantities in that equation
                                             ├─ given directly?
                                             ├─ read from graph?
                                             ├─ hidden in wording?
                                             └─ from a previous part?
```
Stop only when every branch ends in "given", "graph", "wording" or "previous part".

### Pass 6 — Execute, then evaluate (Giải và kiểm tra)
- Units converted to SI before substitution (cm → m, cm² → m²).
- Dimension check of the final formula.
- Order of magnitude: is the answer physically plausible?
- Did you answer **exactly** what the command word asked?

---

## 2. Worked analysis of Câu 7 (analysis only — no final numbers)

### Pass 1 — Skeleton
| Part | Command | Depends on |
|---|---|---|
| (a) | Chứng minh (show that) f = (1/2π)√(Aρg/M) | Given expression a = −(Aρg/M)y |
| (b) | Tính M | Formula from (a) + data from graph 7.2 + new ρ |
| (c) | Nêu đặc điểm | Graph 7.2 only |

### Pass 2 — Translation table
| Phrase | Physics meaning | Consequence |
|---|---|---|
| ống kín một đầu | Liquid cannot enter the tube | Displaced volume is based on the **outer** cross-section |
| diện tích tiết diện không đổi A | Displaced volume changes linearly with depth | ΔV = A·y → buoyancy change ∝ y |
| nổi thẳng đứng | Equilibrium: weight = buoyancy | Only *changes* from equilibrium matter |
| dịch chuyển nhỏ | Linear approximation is valid | Allowed to use SHM |
| a = −(Aρg/M)y | Acceleration ∝ −displacement | Compare with the SHM definition |
| chất lỏng **khác** | ρ in (b) ≠ ρ in (a) | Use 950 kg m⁻³ |
| đường kính **ngoài** 2,4 cm | Hidden data for A | A from diameter (circle), convert cm → m |
| Hình 7.2 | Data source | Period T must be read from the graph |

### Pass 3 — Model
Sketch: tube at equilibrium, then pushed down by y. Ask yourself: which force increases, by how much, in which direction?

### Pass 4 — Principle
"(a) is SHM because acceleration is proportional to displacement and directed opposite to it."
"(b) is the SHM formula used in reverse, with T taken from data."
"(c) is a graph-interpretation question about energy loss."

### Pass 5 — Backward plan for (b) (fill in the blanks yourself)
```
M  ←  f = (1/2π)√(Aρg/M)  ←  f  ←  ?  (from graph: what do you measure?)
                           ←  A  ←  ?  (from which phrase?)
                           ←  ρ  ←  ?
                           ←  g  ←  constant
```

### Guiding questions (hints, in increasing strength)
- (a) Hint 1: What is the *defining* equation of SHM, in terms of a, ω and x?
- (a) Hint 2: Match term by term. What plays the role of ω²? Then how do ω and f relate?
- (b) Hint 1: To read T accurately from a graph, should you measure one cycle or several? Between which kinds of points?
- (b) Hint 2: Why "outer" diameter, not inner? (Which volume of liquid is pushed aside?)
- (c) Hint 1: Compare successive maxima. What changes, and what stays (approximately) constant?
  (Note: "Hình 4.2" in the question is a typo for Hình 7.2.)

---

## 3. One-page checklist (print and keep beside you)

```
□ 1. SKELETON   Parts? Command words? Dependencies?
□ 2. TRANSLATE  Phrase → physics → symbol. Circle every adjective.
□ 3. MODEL      Sketch equilibrium + displaced. Forces. Idealisations.
□ 4. PRINCIPLE  "This is ___ because ___."  (one sentence)
□ 5. PLAN       Unknown ← equation ← each quantity ← source (given/graph/wording/previous)
□ 6. EXECUTE    SI units → substitute → dimension check → plausibility → answers the command?
```

## 4. Training routine
1. For the next 10 questions, do **only Passes 1–5** (no calculation). Time limit: 4 minutes per question.
2. Then solve. Mark which pass would have prevented each mistake.
3. Keep an "error log" with a column *"Which pass failed?"*. After 2 weeks the pattern of your weak pass will be visible.
4. Revisit this sheet at day 1, day 3, day 7.

---

### References
- Chi, M. T. H., Feltovich, P. J., & Glaser, R. (1981). Categorization and representation of physics problems by experts and novices. *Cognitive Science*, 5(2), 121–152.
- Larkin, J., McDermott, J., Simon, D. P., & Simon, H. A. (1980). Expert and novice performance in solving physics problems. *Science*, 208(4450), 1335–1342.
- Sweller, J. (1988). Cognitive load during problem solving. *Cognitive Science*, 12(2), 257–285.
- Heller, P., & Heller, K. *Cooperative Group Problem Solving in Physics*. University of Minnesota.
- Reif, F. (2008). *Applying Cognitive Science to Education*. MIT Press.
- Pólya, G. (1945). *How to Solve It*. Princeton University Press.
- Webb, N. L. (2002). Depth-of-Knowledge levels for four content areas.
