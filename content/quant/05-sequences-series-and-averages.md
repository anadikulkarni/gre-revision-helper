# Sequences, Series & Averages

## How many multiples of `r` lie between `a` and `b`?
covers: 44

### Answer
`count = (last - first)/r + 1`, where `first` is the smallest multiple of `r` in range and `last` the largest.

### Explanation
Dividing by `r` converts a distance into a number of steps, and the `+1` is the same fencepost correction as counting integers.

### Example
Multiples of 7 between 50 and 200: first 56, last 196, so `(196 - 56)/7 + 1 = 21`. Cross-check on the multiplier index: `7x8` to `7x28` is `28 - 8 + 1 = 21` ✓.

## Sum of the multiples of `r` between `a` and `b`?
covers: 45

### Answer
Average times count: `((first + last)/2) x ((last - first)/r + 1)`.

### Explanation
The multiples form an evenly spaced list, so the same average-times-count machinery applies.

It works because the multiples of `r` in a range are themselves evenly spaced, with gap `r` — so the average is the midpoint of the first and last, exactly as with consecutive integers.

### Example
Multiples of 7 between 50 and 200: average `= (56 + 196)/2 = 126`, count `= 21`, sum `= 2,646`.

Multiples of 4 between 1 and 100: first 4, last 100, count `(100-4)/4 + 1 = 25`, average 52, sum `= 1,300`.

## How do you tell what kind of sequence you are looking at?
covers: 46

### Answer
Look at what stays constant. **Arithmetic**: constant difference. **Geometric**: constant ratio. **Quadratic**: constant second difference. **Cubic**: constant third difference.

### Explanation
Write the difference rows out. If row one is constant it is arithmetic; if row two is constant it is quadratic; if the *ratio* row is constant it is geometric.

### Example
1, 4, 9, 16, 25 → differences 3, 5, 7, 9 (not constant) → their differences 2, 2, 2 (constant). Quadratic, and indeed the terms are `n^2`.

## nth term of an arithmetic or geometric sequence?
covers: new

### Answer
Arithmetic: `a_n = a_1 + (n - 1)d`. Geometric: `a_n = a_1 x r^(n-1)`.

### Explanation
Both use `n - 1`, not `n`, because the first term has taken zero steps. That off-by-one is the whole difficulty of these formulas.

### Example
Arithmetic 5, 8, 11, …: `a_20 = 5 + 19(3) = 62`. Geometric 5, 10, 20, …: `a_8 = 5 x 2^7 = 640`. Backwards: if an arithmetic sequence has `a_1 = 4` and `a_9 = 36`, then `8d = 32`, so `d = 4`.

## Sum formulas for `1 + 2 + ... + n` and `1^2 + 2^2 + ... + n^2`?
covers: 47

### Answer
`n(n+1)/2` and `n(n+1)(2n+1)/6`.

### Explanation
The first is average-times-count in disguise: the average is `(1+n)/2` and there are `n` terms.

The pairing proof is worth knowing: write `1 + 2 + ... + n` forwards and backwards above each other, and every column sums to `n + 1`. There are `n` columns and you have counted everything twice, hence `n(n+1)/2`.

### Example
`1 + 2 + ... + 100 = 100 x 101/2 = 5,050`. `1^2 + ... + 10^2 = 10 x 11 x 21/6 = 385`. For a sum starting at 11, subtract: `1,275 - 55 = 1,220`.

The first 50 **even** numbers: `2 + 4 + ... + 100 = 2(1 + 2 + ... + 50) = 2 x 1,275 = 2,550`. Factoring the 2 out first is nearly always the quickest route.

## Sum of the first `n` terms of a geometric series?
covers: 48

### Answer
`sum = a(r^n - 1)/(r - 1)`, with `a` the first term and `r` the ratio. If `|r| < 1`, an infinite series sums to `a/(1 - r)`.

### Explanation
Average-times-count fails here because the terms are not evenly spaced — the later terms dominate.

### Example
First 20 terms of 3, 6, 12, 24, …: `3(2^20 - 1)/1 = 3 x 1,048,575 = 3,145,725`. Infinite case: `1 + 1/2 + 1/4 + ... = 1/(1 - 1/2) = 2`.

## Sum of `1 - 2 + 3 - 4 + ...`?
covers: 49

### Answer
Group it in **pairs**. Each pair collapses to the same value, turning the series into a multiplication.

### Explanation
The series has no constant difference or ratio, but pairing consecutive terms creates one that does.

### Example
`1 - 2 + 3 - 4 + ... - 100`: pairs `(1-2), (3-4), ...` each give -1, and there are 50 pairs, so **-50**. Stopping at 101 instead leaves those 50 pairs plus `+101`, giving 51.

### Watch out
Check whether the final term is left unpaired — an odd number of terms always leaves one over, and that is the point of the question.

## A series with no formula and no obvious pattern — what next?
covers: 50

### Answer
Compute the **partial sums** for `n = 1, 2, 3` and look at those instead of the terms. The sums often follow an obvious rule even when the terms do not.

### Explanation
This is how telescoping series give themselves away.

### Example
`1/(1x2) + 1/(2x3) + 1/(3x4) + ...` has partial sums 1/2, 2/3, 3/4 — clearly `n/(n+1)`. So the first 99 terms sum to 99/100, with no algebra.

## Comparing a messy series against another quantity?
covers: 51

### Answer
**Bound it.** Replace every term with the smallest term for a lower bound, then with the largest for an upper bound. If the other quantity falls outside that interval, you are done.

### Explanation
You never needed the exact value, only which side of the other quantity it lies on.

### Example
A: `1/51 + 1/52 + ... + 1/100` (50 terms). B: 1. Every term is at most 1/51, so A ≤ `50/51 < 1`; every term is at least 1/100, so A ≥ 1/2. A is between 0.5 and 0.98, so **B is greater**.

## Arithmetic mean — definition and the trick that matters?
covers: new

### Answer
`mean = sum / count`, so `sum = mean x count`. Most mean questions are really about the **sum**.

### Explanation
When a question changes a list — adds a value, removes one, or reports a new average — convert every average into its total first, adjust the totals, then convert back.

For an evenly spaced list the mean also equals the median, which is a big shortcut.

### Example
Five numbers average 12, so their sum is 60. Add a sixth number, 18: the new sum is 78 and the new mean is `78/6 = 13`. What value would pull the average of the five up to 15? The sum would need to be 90, so the new number must be 30.

### Watch out
The average of two averages is only valid when the groups are the same size — otherwise you need a weighted average.

## Median, mode and range — definitions?
covers: new

### Answer
**Median**: middle value of the sorted list (average the two middle ones if the count is even). **Mode**: the most frequent value. **Range**: `largest - smallest`.

### Explanation
Sorting first is non-negotiable for the median, and it is the step people skip. The median ignores outliers while the mean does not, which is exactly what comparison questions probe.

### Example
For 3, 9, 4, 4, 12: sorted it is 3, 4, 4, 9, 12 → median **4**, mode **4**, range **9**, mean **6.4**. Replace 12 with 120 and the median stays 4 while the mean jumps to 28 — the classic outlier contrast.

## Median of an evenly spaced list, without counting to the middle?
covers: 136

### Answer
`median = (first + last)/2`, and it equals the mean. Works for consecutive integers, consecutive multiples, any arithmetic sequence.

### Explanation
Evenly spaced lists are symmetric about their centre, so the midpoint of the ends is the middle value.

### Example
Median of the multiples of 7 between 50 and 200: `(56 + 196)/2 = 126`. Median of 1 to 100: `(1 + 100)/2 = 50.5`.

### Watch out
Only for even spacing. An arbitrary list must be sorted first.
