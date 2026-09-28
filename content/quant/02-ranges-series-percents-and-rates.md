# Ranges, Series, Percents & Rates

## How many integers are there from `a` to `b`?
covers: 42

### Answer
Inclusive: `b - a + 1`. Exclusive at both ends: `b - a - 1`. Subtraction counts gaps, and there is always one more fencepost than fence.

### Explanation
"Between" on the GRE almost always means exclusive; "from … to …" and "inclusive" mean both ends count.

### Example
From 17 to 63 inclusive: `63 - 17 + 1 = 47`. Sanity check on a tiny case: 3 to 5 inclusive is 3 numbers ✓. Strictly between: 45.

## Sum of all the integers from `a` to `b`?
covers: 43

### Answer
`sum = ((a + b)/2) x (b - a + 1)` — the average of the endpoints times the count. True for any evenly spaced list.

### Explanation
Evenly spaced lists are symmetric, so their average is exactly the midpoint of the first and last terms. This beats `n(n+1)/2` whenever the list does not start at 1.

### Example
Sum from 17 to 63: average `= 40`, count `= 47`, so `40 x 47 = 1,880`.

### Watch out
The count is `b - a + 1`, not `a - b + 1`. Reversing the subtraction gives a negative count and nonsense.

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

## Simple interest formula?
covers: 57

### Answer
`A = p(1 + rt)` — interest is `prt`, added once to the principal. `r` is the annual rate as a decimal, `t` the time in years.

### Explanation
Interest is paid on the original principal only, never on interest already earned, so the balance grows in a straight line.

### Example
$300 at 4% for 5 years: interest `= 300 x 0.04 x 5 = $60`, so `A = $360` — exactly $12 a year.

### Watch out
Convert the rate to a decimal and the time to years (18 months → 1.5) before substituting.

## Compound interest formula — annually, and more often than that?
covers: 58, 59

### Answer
Once a year: `A = p(1 + r)^t`.

`n` times a year: `A = p(1 + r/n)^(nt)` — divide the rate by `n`, multiply the periods by `n`.

### Explanation
Each period's interest is applied to the new balance, so growth is exponential rather than linear. The gap over simple interest is small at first and widens fast, which is why comparison questions like it.

More frequent compounding always yields slightly more, because the interest starts earning sooner. There is a ceiling: compounding infinitely often multiplies by `e^(rt)`, only a little above monthly.

### Example
$300 at 4% compounded annually for 5 years: `300(1.04)^5 ≈ $365.00`, against $360 simple.

$1,000 at 12% for 2 years — annually `1000(1.12)^2 = $1,254.40`; quarterly `1000(1.03)^8 ≈ $1,266.77`; monthly about $1,269.73. A rate quoted as "12% compounded quarterly" is really 3% four times, an effective annual rate of `1.03^4 - 1 ≈ 12.55%`.

### Watch out
`(1.04)^5` is not `1 + 5(0.04)`. Powers do not distribute over sums, and assuming they do is the error being tested.

## Formula for something that shrinks by a percentage each period?
covers: 60

### Answer
`A = p(1 - r)^t`.

### Explanation
Each period removes a percentage of whatever remains, so the amount falls quickly at first and then flattens — it never quite reaches zero.

Halving is the case to recognise: `r = 0.5` gives `p(0.5)^t`, so the quantity halves every period — and after `t` periods, `t` halvings.

### Example
A $20,000 car depreciating 15% a year for 3 years: `20,000(0.85)^3 ≈ $12,282`. Note that is a 38.6% total drop, not 45%.

A population falling 10% a year takes about 7 years to halve: `0.9^7 ≈ 0.478`. And a 50% fall followed by a 50% rise leaves you at `0.5 x 1.5 = 0.75` — down 25%, not back where you started.

## The one formula behind speed, work and production?
covers: 61

### Answer
`amount = rate x time`. Distance = speed x time; work = rate x time. For combined work, **add the rates, never the times**.

### Explanation
Rearranging gives `rate = amount/time` and `time = amount/rate`. Two taps filling a tank in 6 and 3 hours work at `1/6 + 1/3 = 1/2` of a tank per hour, so together they take 2 hours.

### Example
One printer does 20 pages a minute, another 30. Combined rate 50 per minute, so a 400-page job takes `400/50 = 8 minutes`.

### Watch out
Average speed is total distance over total time, not the average of the speeds. Out at 30 and back at 60 averages **40**, not 45.

## Two objects moving at once — what do you do with their speeds?
covers: 62

### Answer
Combine them into one rate. Toward each other or apart: **add**. Same direction: **subtract**.

### Explanation
Only the rate at which the gap changes matters. Two cars approaching each other close the gap at the sum of their speeds; a chase closes it at the difference.

### Example
300 km apart, driving toward each other at 60 and 40 km/h: closing speed 100, so they meet after 3 hours. If instead the 60 chases the 40 from 30 km back, the gap closes at 20 km/h, taking 1.5 hours.
