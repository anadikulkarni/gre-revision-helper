# Averages, Mixtures & Spread

## Mixtures as weighted averages
covers: 134

Mixing two solutions is a weighted average: the concentration of the result sits between the two originals, pulled toward whichever contributes more volume.

If mixture A is `a%` strong with volume `x`, and mixture B is `b%` strong with volume `y`, the final concentration is

`(ax + by)/(x + y)`

The numerator is the total amount of the important substance; the denominator is the total volume.

### Example
30 litres of 20% acid mixed with 10 litres of 60% acid: `(0.20 x 30 + 0.60 x 10)/40 = (6 + 6)/40 = 12/40 = 30%`. Note the answer is much closer to 20% than to 60%, because there is three times as much of the weak solution.

### Watch out
The result must always lie strictly between the two concentrations. If your answer falls outside that range, you have made an arithmetic slip.

## The mixture ratio shortcut
covers: 135

When you know the target concentration and need the **ratio** of the two mixtures, you do not need algebra. Take the distance from each starting concentration to the target, and swap them:

`volume of A : volume of B = |z - b| : |z - a|`

where `z` is the target. The mixture further from the target contributes less, so its distance becomes the *other* one's share.

### Example
Mix 20% acid with 60% acid to get 30%. Distances: from 20 to 30 is 10, from 60 to 30 is 30. Swapping gives `A : B = 30 : 10 = 3 : 1`. Check with the weighted average: `(0.2 x 3 + 0.6 x 1)/4 = 1.2/4 = 30%` ✓.

### Watch out
Take care which distance goes with which mixture. The one nearer the target must get the larger share — sanity-check your ratio against that.

## Median of an evenly spaced list
covers: 136

For any evenly spaced list, the median equals the mean, and both equal the midpoint of the first and last terms:

`median = (first + last)/2`

You never have to count to the middle. This works for consecutive integers, consecutive multiples, or any arithmetic sequence.

### Example
Median of the multiples of 7 between 50 and 200: the first is 56 and the last is 196, so the median is `(56 + 196)/2 = 126`. Median of the integers 1 to 100: `(1 + 100)/2 = 50.5`.

### Watch out
This holds only when the spacing is even. For an arbitrary list you must sort it and find the middle value (or average the two middle values when the count is even).

## Quartiles and measures of position
covers: 137

Quartiles cut an ordered list into four parts: Q1 has a quarter of the data below it, Q2 is the median, Q3 has three quarters below it. The point that trips people up is that the quartile *values* are boundary markers, not members of the quarters — a value sitting exactly on Q1 is not counted inside the first or the second quarter.

The same logic applies to deciles and percentiles: they are dividing lines, and a data point equal to the line belongs to neither side.

### Example
For the list 1, 2, 3, 4, 5, 6, 7, 8 the median Q2 is 4.5 with four values each side; Q1 is 2.5 and Q3 is 6.5. So "how many values are in the third quarter" means those strictly between Q2 and Q3, namely 5 and 6.

### Watch out
Different textbooks compute quartiles slightly differently. On the GRE the interquartile range `Q3 - Q1` is what usually matters, and it is robust to those differences.

## Variance
covers: 138

Variance measures how spread out a list is. Take each term's distance from the mean, square it so that positives and negatives do not cancel, add those up, and divide by how many terms there are.

`variance = sum of (term - mean)^2 / N`

Squaring is what makes outliers count heavily: a term twice as far from the mean contributes four times as much.

### Example
For 2, 4, 6 the mean is 4. Differences are -2, 0, 2; squares are 4, 0, 4; the total is 8; divide by 3 to get a variance of `8/3 ≈ 2.67`.

## Standard deviation step by step
covers: 139

Standard deviation is the square root of the variance, which brings the measure back into the same units as the data. The procedure:

1. Find the mean.
2. Subtract the mean from each term.
3. Square each difference.
4. Add the squares.
5. Divide by `N`.
6. Take the square root.

### Example
For 2, 4, 6: mean 4; differences -2, 0, 2; squares 4, 0, 4; sum 8; divide by 3 → 2.67; square root → **1.63**. For 1, 4, 7 the same procedure gives `sqrt(6) ≈ 2.45` — the same mean but more spread, hence a larger SD.

### Watch out
Most GRE questions only need you to *compare* standard deviations, which you can often do by eye: the list whose values sit further from the mean has the larger SD, regardless of the arithmetic.

## Population versus sample standard deviation
covers: 140

The two differ only in the divisor. Population SD divides by `N`; sample SD divides by `N - 1`. Dividing by a smaller number makes the sample SD slightly larger, which compensates for a sample tending to understate the spread of the population it came from.

### Example
For 2, 4, 6 the population SD is `sqrt(8/3) ≈ 1.63` and the sample SD is `sqrt(8/2) = 2`. The GRE means population SD unless it explicitly says "sample".

## What transformations do to standard deviation
covers: 141

Apply the same change to every term in a list and the spread reacts predictably. **Adding or subtracting** a constant shifts everything together and leaves the standard deviation unchanged. **Multiplying or dividing** by a constant scales the SD by that same factor (by its absolute value, since SD is never negative).

The mean, by contrast, changes under both operations.

### Example
The list 2, 4, 6 has SD ≈ 1.63. Add 100 to each term to get 102, 104, 106: the SD is still 1.63, though the mean jumps from 4 to 104. Multiply the original by 3 to get 6, 12, 18: the SD triples to ≈ 4.90.

### Watch out
Variance scales by the *square* of the factor, so multiplying by 3 multiplies the variance by 9 while multiplying the SD by 3.

## Standardizing a list
covers: 142

Standardizing rewrites each value as the number of standard deviations it sits from the mean — its z-score. Two steps: subtract the mean from every value, then divide each result by the standard deviation. The new list always has mean 0 and standard deviation 1.

`z = (value - mean)/SD`

This is what lets you compare positions across different scales.

### Example
The list 2, 8 has mean 5 and population SD 3. Standardized it becomes `(2-5)/3 = -1` and `(8-5)/3 = 1`, i.e. -1 and 1. So a score of 8 is "one standard deviation above the mean".

## The normal distribution percentages
covers: 162

The bell curve is symmetric about the mean, and the GRE expects you to know how the area splits. Within 1 SD of the mean lies about **68%** of the data (34% each side). The band between 1 and 2 SDs holds about **28%** (14% each side). Beyond 2 SDs lies about **4%** (2% each side).

Cumulatively: about 68% within one SD, about 96% within two. Each half of the curve holds 50%, so `34 + 14 + 2 = 50` on each side — a useful check when you are reconstructing the picture.

### Example
Test scores are normally distributed with mean 500 and SD 100. Between 400 and 600 lie 68% of scores. Above 700 (two SDs up) lie 2%. Between 600 and 700 lie 14%. And a score of 700 is at roughly the 98th percentile, since `50 + 34 + 14 = 98`.

### Watch out
Practise drawing the curve with 2 / 14 / 34 / 34 / 14 / 2 written under the sections. Almost every normal-distribution question is answered by reading numbers off that sketch.
