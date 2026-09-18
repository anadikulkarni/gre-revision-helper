# Statistics & Data

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
