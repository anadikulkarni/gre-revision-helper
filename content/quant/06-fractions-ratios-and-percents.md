# Fractions, Ratios & Percents

## Repeating versus non-repeating decimals — which are rational?
covers: 52

### Answer
Both terminating and **repeating** decimals are rational. Only a decimal that runs forever with **no** repeating block is irrational.

### Explanation
Every ratio of two integers either stops or falls into a repeating block. So `1/3 = 0.333...` is rational despite never terminating, while `sqrt(2) = 1.41421356...` never settles and cannot be written as a fraction.

### Example
`1/3 = 0.333...` (rational, repeating). `1/8 = 0.125` (rational, terminating). `pi` and `sqrt(2)` (irrational).

### Watch out
"Non-terminating" does not mean irrational — that confusion is the whole question.

## Will `a/b` terminate as a decimal?
covers: 53

### Answer
Reduce it first, then factorize the denominator. It terminates **only if the denominator's primes are 2s and 5s**.

### Explanation
Base 10 is `2 x 5`, so only denominators built from 2s and 5s can be rewritten as a power of 10.

### Example
`7/40`: `40 = 2^3 x 5` → terminates (0.175). `7/30`: `30 = 2 x 3 x 5` → repeats (0.2333…). `6/30` looks like it repeats, but reduces to `1/5 = 0.2`.

### Watch out
Always reduce first — the unreduced denominator can hide primes that cancel away.

## Turning a repeating decimal into a fraction?
covers: 54

### Answer
`n` repeating digits sit over `n` nines: `0.444... = 4/9`, `0.373737... = 37/99`, `0.123123... = 123/999`.

### Explanation
The mechanism: set `x` equal to the decimal, multiply by `10^n` where `n` is the block length, and subtract. The infinite tails cancel exactly.

### Example
`x = 0.3737...`; the block is 2 digits so `100x = 37.3737...`. Subtracting gives `99x = 37`, so `x = 37/99`.

### Watch out
A non-repeating head needs an extra step: for `0.1666...`, use `10x = 1.666...` and `100x = 16.66...`, so `90x = 15` and `x = 1/6`.

## Smallest positive integer that turns `a/b` into an integer?
covers: 55

### Answer
`b` — but only once `a/b` is in **lowest terms**.

### Explanation
After reducing, the numerator shares nothing with the denominator, so nothing smaller than `b` can clear it.

### Example
`14/21` reduces to `2/3`, so the answer is **3**, not 21. And `3 x (2/3) = 2` ✓.

### Watch out
Skipping the reduction gives a number that works but is not the smallest — exactly the wrong answer they will offer.

## Setting up a proportion?
covers: 56

### Answer
Put the same kind of quantity in the same position on both sides, then cross-multiply.

### Explanation
Keep units aligned: if the left is km over minutes, the right must be km over minutes too. Then sanity-check the direction — more time should mean more distance.

Check whether the relationship is **direct** (more of one means more of the other, so `a/b = c/d`) or **inverse** (more of one means less of the other, so `a x b = c x d`). Workers and time are inverse: twice the workers, half the time.

### Example
4 km in 30 minutes; how far in 45? `4/30 = a/45` → `30a = 180` → `a = 6 km`.

Inverse case: 6 workers finish a job in 10 days; how long for 15 workers? `6 x 10 = 15 x d`, so `d = 4 days` — not `15/6 x 10`.

## Ratios: what does `a : b` actually let you write down?
covers: new

### Answer
Introduce the multiplier `x`: the parts are `ax` and `bx`, and the whole is `(a + b)x`. Part-to-part is `a : b`; part-to-whole is `a : (a+b)`.

### Explanation
The multiplier is what turns a ratio into an equation. Confusing part-to-part with part-to-whole is the most common ratio error: 2:3 means 2/5 and 3/5 of the total, not 2/3 and 3/3.

To combine two ratios sharing a term, scale them until that term matches — `A:B = 2:3` and `B:C = 4:5` become `A:B:C = 8:12:15`.

### Example
Boys to girls is 3:5 in a class of 40. Total parts `= 8`, so `8x = 40` and `x = 5`: 15 boys and 25 girls. Boys are `3/8` of the class, not `3/5`.

## Percents: converting, and finding "x percent of y"?
covers: new

### Answer
Percent means "per hundred": `x% = x/100`. "Of" means multiply, so `x% of y = (x/100) x y`. Useful ones: `1/8 = 12.5%`, `1/6 ≈ 16.7%`, `1/3 ≈ 33.3%`, `3/8 = 37.5%`, `5/8 = 62.5%`.

### Explanation
Percent questions become easy once you translate word by word: "is" is `=`, "of" is `x`, "what" is the variable.

### Example
"18 is what percent of 45?" → `18 = (p/100) x 45` → `p = 40`. And 15% of 60 is `0.15 x 60 = 9`. Reversing: "12 is 30% of what?" → `12 = 0.3y` → `y = 40`.

### Watch out
`x% of y` always equals `y% of x`, which can turn an awkward computation into an easy one: 8% of 50 is the same as 50% of 8, i.e. 4.

## Percent change — and what happens with two changes in a row?
covers: new

### Answer
`percent change = (new - old)/old x 100`, always over the **original**. Successive changes **multiply**: a 20% rise then a 20% fall is `1.2 x 0.8 = 0.96`, a 4% net loss.

### Explanation
Increases and decreases are not symmetric, because the second change is applied to a different base. A rise of 25% needs a fall of only 20% to undo it.

Multipliers are the fast way through: +30% is `x1.3`, -15% is `x0.85`.

### Example
Price rises from 80 to 100: `(100-80)/80 = 25%` increase. Falling back from 100 to 80 is `(80-100)/100 = -20%`. Two successive 10% rises give `1.1 x 1.1 = 1.21`, a 21% increase, not 20%.

### Watch out
"Increased by 300%" means the result is 4 times the original, not 3 times.

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

## Compound interest formula?
covers: 58

### Answer
`A = p(1 + r)^t`.

### Explanation
Each period's interest is applied to the new balance, so growth is exponential rather than linear. The gap over simple interest is small at first and grows fast — which is why comparison questions love it.

### Example
$300 at 4% compounded annually for 5 years: `300(1.04)^5 ≈ $365.00`, against $360 simple — $5 of interest earning interest.

### Watch out
`(1.04)^5` is not `1 + 5(0.04)`. Powers do not distribute over sums.

## Compound interest when it compounds more than once a year?
covers: 59

### Answer
`A = p(1 + r/n)^(nt)` — divide the rate by `n`, multiply the periods by `n`.

### Explanation
More frequent compounding always yields slightly more, because interest starts earning sooner.

Comparison questions usually only need the direction: for the same nominal rate, more frequent compounding always wins, and the gap widens with time. There is a ceiling, though — compounding infinitely often multiplies by `e^(rt)`, only slightly above monthly.

### Example
$1,000 at 12% for 2 years. Annually: `1000(1.12)^2 = $1,254.40`. Quarterly: `1000(1.03)^8 ≈ $1,266.77`. Monthly: about $1,269.73.

A rate quoted as "12% compounded quarterly" is really 3% four times, which is an effective annual rate of `1.03^4 - 1 ≈ 12.55%`.

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

