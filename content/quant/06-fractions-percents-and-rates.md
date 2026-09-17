# Fractions, Percents & Rates

## Repeating versus non-repeating decimals
covers: 52

Every fraction of two integers turns into a decimal that either stops or eventually repeats forever in a fixed block — that is what makes it rational. A decimal that goes on forever *without* any repeating block cannot be written as a fraction at all; those are the irrational numbers, like `sqrt(2)` and `pi`.

Repeating blocks are usually written with a bar over the repeating part; in plain text, write `0.333...` or say "0.3 repeating", and `0.373737...` for a two-digit block.

### Example
`1/3 = 0.333...` repeats, so it is rational. `1/8 = 0.125` terminates, also rational. `sqrt(2) = 1.41421356...` never settles into a block, so it is irrational and cannot be written as a ratio of integers.

### Watch out
"Non-terminating" does not mean irrational. `1/3` never terminates but is perfectly rational, because it repeats.

## Does a fraction terminate?
covers: 53

Reduce the fraction to lowest terms, then prime factorize the denominator. If the only primes left are 2s and 5s, the decimal terminates; if anything else survives, it repeats. The reason is that our decimal system is base 10 = `2 x 5`, so only denominators built from 2s and 5s can be rewritten as a power of 10.

### Example
`7/40`: `40 = 2^3 x 5`, only 2s and 5s, so it terminates (`0.175`). `7/30`: `30 = 2 x 3 x 5` contains a 3, so it repeats (`0.2333...`). `6/30` looks like it repeats, but reduce it first: `6/30 = 1/5 = 0.2`, which terminates.

### Watch out
Always reduce first. The un-reduced denominator can contain primes that cancel away.

## Turning a repeating decimal into a fraction
covers: 54

Set `x` equal to the decimal, multiply both sides by `10^n` where `n` is the length of the repeating block, then subtract the original equation. The infinite tails are identical so they cancel, leaving a plain equation you can solve.

The shortcut it produces: a block of `n` repeating digits sits over `n` nines. `0.444... = 4/9`, `0.373737... = 37/99`, `0.123123... = 123/999`.

### Example
Convert `0.373737...` to a fraction. Let `x = 0.3737...`; the block is 2 digits, so multiply by 100: `100x = 37.3737...`. Subtract the first from the second: `99x = 37`, so `x = 37/99`.

### Watch out
If the decimal has a non-repeating head, such as `0.1666...`, multiply first to push the head past the point: `10x = 1.666...` and `100x = 16.66...`, so `90x = 15` and `x = 1/6`.

## Smallest multiplier that makes a fraction an integer
covers: 55

Reduce `a/b` to lowest terms; the answer is then simply `b`, the denominator. Once the fraction is reduced, the numerator has nothing left in common with the denominator, so nothing smaller than `b` can clear it.

### Example
Smallest positive integer that turns `14/21` into an integer? Reduce first: `14/21 = 2/3`, so the answer is **3**, not 21. And `3 x (2/3) = 2`, an integer.

### Watch out
Skipping the reduction step gives a number that works but is not the smallest — which is exactly the wrong answer choice they will offer you.

## Proportions and cross-multiplication
covers: 56

A proportion is one fraction set equal to another, usually with a single unknown. Cross-multiply — numerator of one times denominator of the other — and solve. The skill is in setting it up so that the same kind of quantity sits in the same position on both sides.

Keep units aligned: if the left side is km over minutes, the right side must also be km over minutes.

### Example
A man runs 4 km in 30 minutes. How far in 45 minutes at the same rate? Set up `4/30 = a/45`. Cross-multiply: `30a = 4 x 45 = 180`, so `a = 6 km`.

### Watch out
Check the answer makes sense in direction. More time should mean more distance; if your answer went down, you set the proportion up upside down.

## Simple interest
covers: 57

Simple interest is paid on the original principal only, never on interest already earned. The interest itself is `prt`, so the final amount is

`A = p(1 + rt)`

where `p` is the principal, `r` the annual rate as a decimal and `t` the time in years. Because the interest per year never changes, the balance grows in a straight line.

### Example
$300 at 4% simple interest for 5 years: interest `= 300 x 0.04 x 5 = $60`, so `A = $360`. Each year adds exactly $12.

### Watch out
Convert the rate to a decimal (`4% → 0.04`) and the time to years (`18 months → 1.5`) before substituting.

## Compound interest
covers: 58

Compound interest pays interest on interest, so each year's growth is applied to the new balance:

`A = p(1 + r)^t`

The gap between simple and compound is small at first and grows dramatically with time, which is why comparison questions love it.

### Example
$300 at 4% compounded annually for 5 years: `A = 300(1.04)^5 ≈ 300 x 1.21665 = $365.00`, against $360 for simple interest — $5 more, from interest earning interest.

### Watch out
`(1.04)^5` is not `1 + 5(0.04)`. Powers do not distribute over sums, and assuming they do is the error the question is testing.

## Compounding more than once a year
covers: 59

If the interest compounds `n` times a year, each period gets `r/n` of the annual rate and there are `nt` periods in total:

`A = p(1 + r/n)^(nt)`

More frequent compounding always gives a slightly larger amount, because the interest starts earning sooner.

### Example
$1,000 at 12% for 2 years. Annually: `1000(1.12)^2 = $1,254.40`. Quarterly: `n = 4`, so `1000(1 + 0.03)^8 = 1000(1.03)^8 ≈ $1,266.77`. Monthly would give about $1,269.73.

## Compound decrease
covers: 60

Depreciation and decay use the same formula with a minus sign:

`A = p(1 - r)^t`

Each period removes a percentage of whatever is left, so the amount falls quickly at first and then flattens out — it never reaches zero.

### Example
A $20,000 car depreciating 15% a year for 3 years: `A = 20,000(0.85)^3 = 20,000 x 0.614 ≈ $12,282`. Note this is *not* a 45% total drop; three 15% cuts remove about 38.6% in total.

### Watch out
A 20% rise followed by a 20% fall does not return you to the start: `1.2 x 0.8 = 0.96`, a 4% net loss.

## Rate times time
covers: 61

One relationship covers speed, work and production: `amount = rate x time`. For motion it reads `distance = speed x time`; for a job it reads `work = rate x time`. Rearranging gives `rate = amount/time` and `time = amount/rate`.

For combined-work problems, add the rates, not the times: two taps that each fill a tank in 6 and 3 hours fill at `1/6 + 1/3 = 1/2` of a tank per hour, so together they take 2 hours.

### Example
A printer does 20 pages a minute; a second does 30. Together their rate is 50 pages a minute, so a 400-page job takes `400/50 = 8 minutes`.

### Watch out
Average speed for a round trip is total distance over total time, not the average of the two speeds. Driving out at 30 and back at 60 averages 40, not 45.

## Relative speed
covers: 62

When two things move at once, combine their speeds into a single rate before using `distance = rate x time`. Moving toward each other or apart, **add** the speeds, because both are closing or opening the gap. Moving in the same direction, **subtract**, because only the difference changes the gap.

### Example
Two cars start 300 km apart and drive toward each other at 60 and 40 km/h. Closing speed is 100 km/h, so they meet after `300/100 = 3 hours`. If instead the 60 km/h car chases the 40 km/h car from 30 km behind, the gap closes at `60 - 40 = 20 km/h`, taking `30/20 = 1.5 hours`.
