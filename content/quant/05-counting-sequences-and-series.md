# Counting, Sequences & Series

## Numbers that are not factors of n!
covers: 40

`n!` contains every integer from 1 to `n` as a factor, so the first number that fails to divide it must involve a prime bigger than `n`. The smallest non-factor is therefore the next prime after `n`, and the next few are that prime's multiples and the primes beyond it.

### Example
What is the smallest integer greater than 1 that is not a factor of `10!`? Every number up to 10 divides it, and so do products built from those primes (12 = 4x3, 14 = 2x7, 15 = 3x5 all divide it). The first failure is **11**, the next prime. After that come 13, 17, 19 and 22 (= 2 x 11, which needs an 11 that `10!` does not have).

### Watch out
Do not stop at "the next number after n". 11 works for `10!` only because 11 happens to be prime; for `12!` the smallest non-factor is 13, not 14 (`14 = 2 x 7`, both present).

## Counting the integers in a range
covers: 42

The number of integers from `a` to `b` **inclusive** is `b - a + 1`. The `+1` is there because subtraction counts the gaps between the numbers, not the numbers themselves, and there is always one more fencepost than fence. If both endpoints are excluded, the count is `b - a - 1`.

### Example
How many integers from 17 to 63 inclusive? `63 - 17 + 1 = 47`. Check with something tiny: from 3 to 5 inclusive there are 3 numbers, and `5 - 3 + 1 = 3`. Strictly between 17 and 63 there are `63 - 17 - 1 = 45`.

### Watch out
"Between" is ambiguous in English but almost always means exclusive on the GRE; "from … to …" and "inclusive" mean both ends count.

## Sum of a range of integers
covers: 43

For any evenly spaced list, the sum is the average times the number of terms, and the average of an evenly spaced list is just the midpoint of the first and last terms. So for the integers from `a` to `b`:

`sum = ((a + b)/2) x (b - a + 1)`

The first bracket is the average, the second is the count. This beats the `n(n+1)/2` formula whenever the list does not start at 1.

### Example
Sum of the integers from 17 to 63. Average `= (17 + 63)/2 = 40`. Count `= 63 - 17 + 1 = 47`. Sum `= 40 x 47 = 1,880`.

### Watch out
The count is `b - a + 1`, not `a - b + 1`. Getting the subtraction backwards gives a negative count and a nonsense answer.

## Counting multiples in a range
covers: 44

Find the smallest multiple of `r` at or above the bottom of the range and the largest at or below the top, then count the steps between them and add one:

`count = (last - first)/r + 1`

Dividing by `r` converts a distance into a number of steps, and the `+1` is the same fencepost correction as before.

### Example
How many multiples of 7 between 50 and 200? The first is 56 (`7 x 8`) and the last is 196 (`7 x 28`). Count `= (196 - 56)/7 + 1 = 20 + 1 = 21`. You can check it against the multiplier index: from `7 x 8` to `7 x 28` is `28 - 8 + 1 = 21` terms.

## Sum of multiples in a range
covers: 45

Same two pieces as any evenly spaced list: average times count. Find the first and last multiples in the range, average them, and multiply by the count you just computed.

`sum = ((first + last)/2) x ((last - first)/r + 1)`

### Example
Sum of the multiples of 7 between 50 and 200. First 56, last 196. Average `= (56 + 196)/2 = 126`. Count `= 21` from above. Sum `= 126 x 21 = 2,646`.

## Types of sequences
covers: 46

Identify a sequence by what stays constant when you look at the differences. **Arithmetic**: constant difference between terms (5, 8, 11, 14). **Geometric**: constant ratio, each term is the last times a fixed number (5, 10, 20, 40). **Quadratic**: the differences are not constant but the differences *of the differences* are. **Cubic**: constant third difference, and so on for higher powers.

Writing out the difference rows is the fastest diagnostic: if row one is constant it is arithmetic, if row two is constant it is quadratic, and if the ratio row is constant it is geometric.

### Example
1, 4, 9, 16, 25: differences are 3, 5, 7, 9 — not constant. Their differences are 2, 2, 2 — constant. So it is quadratic, and indeed the terms are `n^2`.

## The sum formulas worth memorising
covers: 47

Two show up often enough to be worth knowing outright:

`1 + 2 + 3 + ... + n = n(n+1)/2`

`1^2 + 2^2 + 3^2 + ... + n^2 = n(n+1)(2n+1)/6`

The first is just average-times-count in disguise: the average is `(1+n)/2` and there are `n` terms.

### Example
`1 + 2 + ... + 100 = 100 x 101/2 = 5,050`. And `1^2 + 2^2 + ... + 10^2 = 10 x 11 x 21/6 = 385`. If a question asks for `1 + 2 + ... + 50` where the list starts at 11 instead, subtract: `(50 x 51/2) - (10 x 11/2) = 1,275 - 55 = 1,220`.

## Sum of a geometric series
covers: 48

For a geometric sequence with first term `a` and ratio `r`, the sum of the first `n` terms is

`sum = a(r^n - 1)/(r - 1)`

Unlike an arithmetic series you cannot use average-times-count, because the terms are not evenly spaced — the later terms dominate.

### Example
Sum of the first 20 terms of 3, 6, 12, 24, … Here `a = 3` and `r = 2`, so `sum = 3(2^20 - 1)/(2 - 1) = 3 x (1,048,576 - 1) = 3 x 1,048,575 = 3,145,725`.

### Watch out
When `|r| < 1` the terms shrink and the sum converges; an infinite geometric series then sums to `a/(1 - r)`. For example 1 + 1/2 + 1/4 + … = `1/(1 - 1/2) = 2`.

## Alternating series: group them in pairs
covers: 49

A series like `1 - 2 + 3 - 4 + ...` has no constant difference or ratio, but pairing consecutive terms turns it into one that does. Each pair collapses to the same value, so the sum becomes a simple multiplication.

### Example
`1 - 2 + 3 - 4 + ... - 100`. Pair them as `(1-2) + (3-4) + ... + (99-100)`: each pair is -1 and there are 50 pairs, so the sum is **-50**. If the series stopped at 101 instead, you would have those 50 pairs plus a leftover `+101`, giving 51.

### Watch out
Check whether the last term is left unpaired. An odd number of terms always leaves one over, and forgetting it is the whole point of the question.

## When there is no formula, find the pattern
covers: 50

For an unfamiliar series `a1 + a2 + ... + an`, compute the sum for `n = 1`, `n = 2`, `n = 3` and look at the results rather than the terms. The partial sums very often follow an obvious rule even when the terms do not, and that rule is the answer.

### Example
`1/(1x2) + 1/(2x3) + 1/(3x4) + ...` Partial sums: 1/2, then 2/3, then 3/4. The pattern is `n/(n+1)`, so the sum of the first 99 terms is 99/100 — no algebra required.

## Bounding a series to compare it
covers: 51

Some comparison questions give a series with no clean pattern at all. You do not need its exact value, only whether it is bigger or smaller than the other quantity. Replace every term with the smallest term to get a lower bound, then with the largest term to get an upper bound. If the other quantity sits outside that interval, you have your answer.

### Example
Quantity A: `1/51 + 1/52 + ... + 1/100` (50 terms). Quantity B: 1. Every term is at most 1/51, so A is at most `50/51 < 1`. Every term is at least 1/100, so A is at least `50/100 = 1/2`. A lies between 0.5 and 0.98, so B is greater.
