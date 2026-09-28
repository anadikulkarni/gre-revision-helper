# Statistics, Counting & Probability

## Mixing two solutions — what is the concentration of the result?
covers: 134

### Answer
A weighted average: `(ax + by)/(x + y)`, where mixture A is `a%` strong with volume `x` and B is `b%` with volume `y`.

### Explanation
The numerator is the total amount of the important substance, the denominator the total volume. The result is pulled toward whichever mixture contributes more volume.

### Example
30 litres of 20% acid with 10 litres of 60%: `(6 + 6)/40 = 30%`. Much closer to 20% than 60%, because there is three times as much of the weak one.

### Watch out
The answer must lie strictly **between** the two concentrations. Outside that range means an arithmetic slip.

## What ratio of two mixtures gives a target concentration?
covers: 135

### Answer
Alligation: take each mixture's distance from the target and **swap them**. `A : B = |z - b| : |z - a|`.

### Explanation
The mixture further from the target contributes less, so its distance becomes the *other* one's share. No algebra needed.

### Example
Mix 20% and 60% acid to get 30%. Distances 10 and 30, swapped gives `A : B = 30 : 10 = 3 : 1`. Check: `(0.2 x 3 + 0.6 x 1)/4 = 30%` ✓.

### Watch out
Sanity-check which way round it goes: the mixture **nearer** the target must get the larger share.

## Quartiles — what exactly is Q1, and what sits "inside" a quarter?
covers: 137

### Answer
Quartiles cut an ordered list into four parts: Q1 has a quarter below it, Q2 is the median, Q3 has three quarters below. The quartile **values are boundaries, not members** — a value sitting exactly on Q1 belongs to neither neighbouring quarter.

### Explanation
The same holds for deciles and percentiles: they are dividing lines. The interquartile range `Q3 - Q1` is what the GRE usually wants, and it is robust to the small definitional differences between textbooks.

### Example
For 1, 2, 3, 4, 5, 6, 7, 8: Q2 = 4.5, Q1 = 2.5, Q3 = 6.5, so the interquartile range is 4. "The third quarter" means the values strictly between Q2 and Q3 — 5 and 6.

## Variance — how is it built?
covers: 138

### Answer
`variance = sum of (term - mean)^2 / N`. Distance from the mean, squared, averaged.

### Explanation
Squaring stops positives and negatives cancelling, and it makes outliers count heavily — a term twice as far from the mean contributes four times as much.

Variance is in *squared* units, which is why standard deviation — its square root — is the figure actually quoted. A variance of 0 means every value is identical.

### Example
For 2, 4, 6: mean 4; differences -2, 0, 2; squares 4, 0, 4; total 8; `8/3 ≈ 2.67`.

For 10, 10, 10 the variance is 0. For 8, 10, 12 the mean is 10, the squared differences are 4, 0, 4, and the variance is 8/3 — the same as for 2, 4, 6, since only the spread matters, not the location.

## Standard deviation — the procedure?
covers: 139

### Answer
The square root of the variance: (1) find the mean, (2) subtract it from each term, (3) square the differences, (4) add them, (5) divide by `N`, (6) square root.

### Explanation
Taking the root brings the measure back into the units of the data, which is why SD rather than variance is what questions quote.

### Example
2, 4, 6 → variance 2.67 → SD ≈ **1.63**. The list 1, 4, 7 has the same mean but more spread, giving `sqrt(6) ≈ 2.45`.

### Watch out
Most GRE questions only ask you to **compare** SDs, which you can often do by eye: the list whose values sit further from the mean wins, no arithmetic needed.

## Population versus sample standard deviation?
covers: 140

### Answer
Population divides by `N`; sample divides by `N - 1`. The sample version is slightly larger.

### Explanation
Dividing by a smaller number compensates for a sample tending to understate the spread of the population it came from. The GRE means population SD unless it says "sample".

The intuition for `N - 1`: a sample's own mean sits closer to its points than the true population mean does, so the squared differences come out slightly too small, and the smaller divisor corrects for it.

### Example
For 2, 4, 6: population SD `= sqrt(8/3) ≈ 1.63`; sample SD `= sqrt(8/2) = 2`.

The gap shrinks as the sample grows: with `N = 100` the two divisors differ by 1%, which is why the distinction rarely changes a comparison answer.

## Add 10 to every value, or multiply every value by 3 — what happens to the SD?
covers: 141

### Answer
Adding or subtracting a constant: **no change**. Multiplying or dividing: the SD is multiplied or divided by the same factor.

### Explanation
Adding shifts the whole list without changing the gaps; multiplying stretches the gaps. The mean, by contrast, changes under both.

### Example
2, 4, 6 has SD ≈ 1.63. Adding 100 gives 102, 104, 106 — SD still 1.63, mean now 104. Multiplying by 3 gives 6, 12, 18 — SD ≈ 4.90.

### Watch out
Variance scales by the **square** of the factor: multiplying the list by 3 multiplies the variance by 9.

## Standardizing a list (z-scores)?
covers: 142

### Answer
`z = (value - mean)/SD`. Subtract the mean from every value, then divide by the SD. The new list always has mean 0 and SD 1.

### Explanation
A z-score says how many standard deviations a value sits from the mean, which is what lets you compare positions across different scales.

### Example
The list 2, 8 has mean 5 and population SD 3, so it standardizes to -1 and 1. A score of 8 is "one standard deviation above the mean".

## The normal distribution — what percentages should you be able to draw?
covers: 162

### Answer
**2 / 14 / 34 / 34 / 14 / 2**. So about 68% lies within 1 SD of the mean, about 96% within 2 SDs, and about 4% beyond 2 SDs.

### Explanation
The curve is symmetric, so each half holds 50%: `34 + 14 + 2 = 50` is the check you use when reconstructing the sketch from memory.

### Example
Scores are normal with mean 500, SD 100. Between 400 and 600: 68%. Above 700: 2%. Between 600 and 700: 14%. A score of 700 is roughly the 98th percentile, since `50 + 34 + 14 = 98`.

### Watch out
Draw the curve and write the six numbers under it before answering. Almost every normal-distribution question is then just reading off the sketch.

## Data interpretation questions — what should you do before calculating?
covers: new

### Answer
Read the **axes, units and footnotes** first: what exactly is being measured, in what units, and is the chart showing an amount or a percentage of something.

### Explanation
The arithmetic in a DI set is easy; the traps are in the reading. Percentages of different bases cannot be added or compared directly, and "percent" versus "percentage points" are different questions.

A set of questions shares one chart, so the time spent understanding it pays back three times. Estimate first — answer choices are usually far apart.

### Example
A bar chart shows revenue in **thousands** and a pie chart shows each region's **share**. "Which region grew most?" is about the bars; "which had the largest share?" is about the pie — and a region can gain share while its revenue falls, if the total fell faster.

### Watch out
A percentage increase from 5% to 10% is a rise of 5 percentage **points** but a 100% **increase**.

## Set versus list — what is the difference?
covers: 143

### Answer
A **set** is unordered with no duplicates, written `{2, 5, 9}`, and can be infinite; its size is `|S|`. A **list** is ordered, allows duplicates, and is finite.

### Explanation
The distinction decides which tool applies: sets lead to combinations and inclusion–exclusion, lists lead to permutations.

### Example
`{1, 2, 3}` and `{3, 2, 1}` are the same set, but the lists (1, 2, 3) and (3, 2, 1) differ. `{1, 1, 2}` is just `{1, 2}` with two elements, while the list (1, 1, 2) has three entries.

## Inclusion–exclusion for two groups?
covers: 144

### Answer
`|A or B| = |A| + |B| - |A and B|` — add the two, subtract the overlap you counted twice.

### Explanation
The rearranged form is the one exams use: knowing the total and both groups gives you the overlap.

### Example
30 students, 18 take French, 15 Spanish, everyone takes at least one. `30 = 18 + 15 - both` → **3** take both. If 4 took neither, use `30 - 4 = 18 + 15 - both` → 7.

### Watch out
Check whether the total includes people in **neither** group — remove them before applying the formula.

## Inclusion–exclusion for three groups?
covers: 145

### Answer
`|A or B or C| = |A| + |B| + |C| - |A and B| - |B and C| - |A and C| + |A and B and C|`

If instead you are told how many are in **exactly** two groups:
`total = |A| + |B| + |C| - (exactly two) - 2 x (all three)`

### Explanation
The pairwise subtractions remove the triple overlap once too often, so the standard version adds it back. Which formula you need depends entirely on the wording, so settle that first.

### Example
40 students: 20 football, 18 basketball, 16 tennis, 8 football+basketball, 6 basketball+tennis, 5 football+tennis, 3 all three. `20+18+16-8-6-5+3 = 38` play at least one, so 2 play none.

### Watch out
"8 play football and basketball" normally means *at least* those two, including anyone who also plays tennis. "Only football and basketball" is the other formula.

## Several independent choices in a row — how many outcomes?
covers: 146

### Answer
Multiply the options at each stage: `a x b x c ...`

### Explanation
The multiplication principle is the backbone of every counting question; extend it to as many stages as you like.

It also covers repeats: choosing from `n` options `r` times **with** repetition gives `n^r`, because every stage still has all `n` options available.

### Example
4 starters and 3 mains → 12 meals; add 2 desserts → 24. A 4-digit PIN from 10 digits with repeats allowed → `10^4 = 10,000`.

A 3-letter code from 26 letters with repeats allowed: `26^3 = 17,576`. Without repeats: `26 x 25 x 24 = 15,600`.

## When do you add possibilities, and when do you multiply?
covers: 147

### Answer
**AND → multiply** (both stages happen). **OR → add** (one or the other, not both).

### Explanation
Label each branch of the problem before computing; most complex counting questions are just a tree of these two operations.

### Example
A to B by 3 roads then B to C by 4 roads: both legs needed → `3 x 4 = 12` routes. But if you may go to C by one of 3 roads **or** one of 4 others → `3 + 4 = 7`.

### Watch out
If "or" allows both to happen, adding double-counts — go back to inclusion–exclusion.

## Optional extras, and "at least one" — how do you count them?
covers: 148

### Answer
Each optional item is a two-way choice (in or out), so `n` options give `2^n` combinations. For "at least one", count everything and **subtract the case where nothing was chosen**.

### Explanation
Count-all-then-subtract-the-bad-case is the standard move for "at least" questions, and it is almost always faster than counting the good cases.

### Example
4 ice-cream flavours with 4 optional toppings: `4 x 2 x 2 x 2 x 2 = 64`. If at least one topping is compulsory, remove the 4 no-topping cases: **60**.

## Choosing `r` from `n` where order does **not** matter?
covers: 149

### Answer
`nCr = n!/(r!(n - r)!)`

### Explanation
The `r!` divides out the orderings of the same chosen group — which is exactly what "order does not matter" means. Note the symmetry `nCr = nC(n-r)`: choosing 3 to include is choosing 7 to exclude.

### Example
3-person committees from 10 people: `10C3 = (10 x 9 x 8)/(3 x 2 x 1) = 120`.

### Watch out
The giveaway words are committee, group, handshake, selection — anything where swapping two members changes nothing.

## Choosing `r` from `n` where order **does** matter?
covers: 150

### Answer
`nPr = n!/(n - r)!` — which is `nCr` times `r!`.

### Explanation
Each chosen group can be arranged in `r!` ways, so permutations always outnumber combinations by that factor.

The relationship is worth holding onto: `nPr = nCr x r!`. Whenever you can count the groups, multiply by `r!` to get the ordered count.

### Example
Gold, silver, bronze among 10 runners: `10P3 = 10 x 9 x 8 = 720`, six times the 120 committees, because each trio can stand on the podium in `3! = 6` orders.

Arranging 2 of 5 books on a shelf: `5P2 = 20`. Choosing 2 of 5 to take on holiday: `5C2 = 10` — exactly half, since each pair has `2! = 2` orders.

### Watch out
Ranking, order, podium, "president and treasurer", password → permutation.

## Counting arrangements without any formula?
covers: 151

### Answer
The **slot method**: draw a blank for each position, write how many options it has, multiply. Each item used reduces the next slot by one.

### Explanation
It is the formula in disguise, but far harder to misapply — and it extends naturally to restricted positions.

The slot method is also the only practical approach once restrictions appear, because you can fill the constrained slots first and let the rest follow.

### Example
Arranging ABCDE: `5 x 4 x 3 x 2 x 1 = 120`, matching `5P5`. Taking only the first three letters: `5 x 4 x 3 = 60 = 5P3`.

How many 3-digit numbers have no repeated digits? The first slot cannot be 0, so `9 x 9 x 8 = 648`.

## Arrangements with a restriction on some positions?
covers: 152

### Answer
Fill the **restricted slots first**, then the rest by the slot method. Separate scenarios are **added**; simultaneous stages are **multiplied**.

### Explanation
Two standard tricks: to keep items **together**, glue them into one block and arrange the blocks (then multiply by the arrangements inside the block); to keep items **apart**, count everything and subtract the arrangements where they are together.

### Example
4-digit numbers from 1–7, no repeats, must be even. The last slot must be 2, 4 or 6 → 3 options; the other three slots take the remaining digits → `6 x 5 x 4 = 120`. Total `3 x 120 = 360`.

## Arranging `n` items when some are identical?
covers: 41, 153

### Answer
`n!/(a! b! ...)`, dividing by the factorial of each repeat count.

### Explanation
Swapping two identical items produces no new arrangement, so the plain `n!` overcounts by exactly those internal orderings.

### Example
BANANA: `n = 6` with three As and two Ns → `6!/(3! 2!) = 720/12 = 60`. A word with no repeats, like ABCDEF, keeps the full `6! = 720`.

### Watch out
Divide by each repeat's factorial **separately**: three As and two Ns means `3! x 2! = 12`, not `5!`.

## Repeats **and** restrictions together?
covers: 154

### Answer
Split the problem into the sections the restriction creates, count each with the repeats formula, then multiply the sections (or add, if they are alternatives).

### Explanation
Handle one constraint at a time and the hardest-looking counting questions become two small ones.

### Example
Arrangements of TEXTBOOK with all vowels first and all consonants last. Vowels E, O, O → `3!/2! = 3`. Consonants T, X, T, B, K → `5!/2! = 60`. Both blocks are required, so `3 x 60 = 180`.

## An unfamiliar counting question — what do you ask yourself first?
covers: 155

### Answer
Three questions: **how many items**, **how many are being chosen or arranged**, and **does order matter**? Then a fourth: are repeats allowed?

Order matters → permutation. Order does not → combination. Repeats allowed → plain multiplication (`n^r`). Identical items → divide by the repeat factorials.

### Explanation
Nearly every counting question is one of the standard types in disguise. Answering those three questions names the type, and then the formula is mechanical.

### Example
"5 books on a shelf, 2 identical" → arranging 5, order matters, one repeat of 2 → `5!/2! = 60`. "3-topping pizzas from 8 toppings" → choosing 3 of 8, order irrelevant → `8C3 = 56`.

## Seating `n` people around a **circular** table?
covers: 156

### Answer
`(n - 1)!`, not `n!`.

### Explanation
A circle has no fixed starting point, so rotating everyone one seat gives the same arrangement — each distinct seating was counted `n` times, and `n!/n = (n-1)!`. In practice: fix one person, then arrange the rest around them.

### Example
5 people in a row: `5! = 120`. The same 5 around a table: `4! = 24`.

### Watch out
Numbered seats make it a row again, and a flippable arrangement (a bracelet) halves the count. Read the setup carefully.

## For a fixed `n`, which `r` makes `nCr` largest?
covers: 157

### Answer
`r = n/2`. If `n` is odd, the two values either side of the middle tie.

### Explanation
Choosing about half the items gives the most possible groups; the counts fall away symmetrically toward `r = 0` and `r = n`, which each have exactly one.

### Example
`n = 6`: counts run 1, 6, 15, **20**, 15, 6, 1 — maximum at `r = 3`. `n = 7`: 1, 7, 21, **35**, **35**, 21, 7, 1 — `r = 3` and `r = 4` tie.

## Basic probability of an event?
covers: new

### Answer
`P(E) = favourable outcomes / total outcomes`, always between 0 and 1. All the outcomes you count must be **equally likely**.

### Explanation
Most probability questions are really counting questions wearing a hat — build the numerator and denominator with the counting tools you already have.

`P(not E) = 1 - P(E)` is the other half of the toolkit.

### Example
One card from a deck: `P(king) = 4/52 = 1/13`. Two dice: `P(sum of 7) = 6/36 = 1/6`, since 6 of the 36 equally likely pairs total 7. Choosing 2 people from 10 of whom 4 are women, `P(both women) = 4C2 / 10C2 = 6/45 = 2/15`.

### Watch out
Equally likely matters. The sums of two dice are **not** equally likely — 7 comes up six times as often as 2.

## Probability that A **and** B both happen?
covers: 158

### Answer
For **independent** events, `P(A and B) = P(A) x P(B)`. If they are not independent, use `P(A) x P(B given A)`.

### Explanation
Independence means one event does not change the odds of the other. "Without replacement" is the standard flag that it fails.

For three or more independent events, keep multiplying. For dependent ones, each factor is conditioned on everything before it.

### Example
Two coin flips both heads: `1/2 x 1/2 = 1/4`. Two aces drawn without replacement: `4/52 x 3/51 = 1/221`, **not** `(4/52)^2`.

Three heads in a row: `(1/2)^3 = 1/8`. Three aces without replacement: `4/52 x 3/51 x 2/50 = 1/5,525`.

## Probability that A **or** B happens?
covers: 159

### Answer
`P(A or B) = P(A) + P(B) - P(A and B)` — inclusion–exclusion again.

### Explanation
Adding the two probabilities double-counts the outcomes where both occur, so the overlap comes off once.

When the events are mutually exclusive the overlap is 0, so the formula collapses to plain addition — which is why "or" questions about outcomes that cannot co-occur feel so much easier.

### Example
One die: `P(even) = 3/6`, `P(>3) = 3/6`, overlap {4, 6} `= 2/6`. So `P(even or >3) = 3/6 + 3/6 - 2/6 = 2/3`, matching the list 2, 4, 5, 6.

Drawing a king **or** a queen: mutually exclusive, so `4/52 + 4/52 = 2/13`. Drawing a king **or** a heart: they overlap in the king of hearts, so `4/52 + 13/52 - 1/52 = 4/13`.

## Independent versus mutually exclusive — what is the difference?
covers: 160

### Answer
**Independent**: neither affects the other, so `P(A and B) = P(A)P(B)`. **Mutually exclusive**: they cannot both happen, so `P(A and B) = 0` and `P(A or B) = P(A) + P(B)`.

### Explanation
They sound similar and mean opposite things. A consequence worth remembering: for mutually exclusive events `P(A) + P(B) <= 1`, since probabilities summing past 1 would force an overlap.

### Example
Two coin flips are independent (both can be heads). One card being both a king and a queen is mutually exclusive. Two events with non-zero probability can never be both — if they cannot co-occur, knowing one happened tells you a great deal about the other.

## Conditional probability `P(A | B)`?
covers: 161

### Answer
`P(A | B) = P(A and B) / P(B)` — the probability of A **given that** B happened.

### Explanation
Conditioning on B shrinks the world to the outcomes where B occurred, so you rescale by dividing by `P(B)`.

### Example
Roll a die: what is `P(2 | even)`? `P(2 and even) = 1/6`, `P(even) = 1/2`, so `(1/6)/(1/2) = 1/3` — matching the intuition that among 2, 4, 6 exactly one is a 2.

### Watch out
`P(A | B)` and `P(B | A)` are different numbers: the probability of being even **given** a roll of 2 is 1, not 1/3.

## Probability of "at least one" — what is the fast route?
covers: new

### Answer
The complement: `P(at least one) = 1 - P(none)`.

### Explanation
Counting directly means adding the cases for exactly one, exactly two, exactly three … The complement is a single multiplication.

### Example
Four coin flips, at least one head: `P(no heads) = (1/2)^4 = 1/16`, so the answer is **15/16**. Rolling two dice, at least one 6: `1 - (5/6)^2 = 11/36`.

### Watch out
The complement of "at least one" is "none" — and the complement of "at least two" is "zero or one", so both cases must come off.
