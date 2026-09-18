# LCM, Factorials & Ranges

## `n` is divisible by `a` and by `b` — what else must it be divisible by?
covers: 31

### Answer
`LCM(a, b)` — **not** `a x b`. A number divisible by 4 and by 6 must be divisible by 12, not 24.

### Explanation
Only when `a` and `b` are coprime does `LCM(a, b) = a x b`, which is why "divisible by 3 and by 5" safely means "divisible by 15".

### Example
`n` divisible by 8 and 12 → `LCM = 24`, so `n` is a multiple of 24. And `n = 24` itself is not a multiple of `8 x 12 = 96`, which kills the product version.

## What is the relationship between GCF, LCM and the numbers themselves?
covers: 32

### Answer
`GCF(a, b) x LCM(a, b) = a x b` — for **two** numbers only.

### Explanation
Each prime appears in the pair with a lower and a higher exponent; the GCF takes the lower, the LCM the higher, so together they use up exactly the exponents in `a x b`.

### Example
`a = 60, b = 72, GCF = 12` → `LCM = (60 x 72)/12 = 360` ✓. If two numbers multiply to 1,200 with GCF 10, the LCM is `1,200/10 = 120` with no factorization at all.

### Watch out
The identity breaks for three or more numbers.

## `m!/n!` with `m > n` — how do you simplify it?
covers: 33

### Answer
Cancel the smaller factorial: `m!/n! = m x (m-1) x ... x (n+1)`. Never compute the factorials themselves.

### Explanation
`n!` sits inside `m!` whole, so everything up to `n!` cancels and only the handful of terms in between survive.

### Example
`8!/5! = (8 x 7 x 6 x 5!)/5! = 336`. And `100!/98! = 100 x 99 = 9,900` in your head, while `100!` has 158 digits.

### Watch out
`0! = 1` by definition, which keeps formulas like `nPn = n!/0!` working.

## How do you find the prime factorization of `n!`?
covers: 35

### Answer
Legendre's method: for each prime `p`, count the multiples of `p` up to `n`, then the multiples of `p^2`, then `p^3`, until the count hits 0. The total is the exponent of `p`.

### Explanation
The extra rounds exist because a number like 9 contributes *two* 3s, so it must be counted once as a multiple of 3 and again as a multiple of 9.

### Example
Exponent of 3 in `10!`: multiples of 3 are 3, 6, 9 → 3; multiples of 9 → 1; multiples of 27 → 0. Total **4**. Doing all the primes gives `10! = 2^8 x 3^4 x 5^2 x 7`.

## Legendre's method without listing multiples?
covers: 36

### Answer
Divide `n` by `p` and drop the decimal, divide that result by `p` again, and keep going until you reach 0. Add up everything you wrote.

### Explanation
Each division asks the same question one level deeper, which is exactly what counting multiples of `p`, `p^2`, `p^3` does.

### Example
Exponent of 5 in `100!`: `100/5 = 20`, `20/5 = 4`, `4/5 = 0` → **24**. Exponent of 2 in `100!`: 50, 25, 12, 6, 3, 1 → **97**.

## How many factors does `n!` have?
covers: 34

### Answer
Legendre for the prime factorization, then the ordinary exponent-plus-one rule. No separate formula — two techniques stacked.

### Explanation
The only work is being systematic about every prime up to `n`.

The counts grow startlingly fast, which is why these questions always name a small factorial: `10!` has 270 factors, but `15!` has 4,032.

### Example
`10! = 2^8 x 3^4 x 5^2 x 7^1`, so the count is `(8+1)(4+1)(2+1)(1+1) = 270`.

For `6! = 720 = 2^4 x 3^2 x 5`: `(4+1)(2+1)(1+1) = 30` factors. Legendre gives the exponents: 2 → `3+1 = 4`, 3 → `2`, 5 → `1`.

## How many copies of `r` are inside `n!`?
covers: 37

### Answer
If `r` is prime, run Legendre for `r`. If `r` is composite, factorize it, run Legendre for each prime, and take the **minimum** — the scarcest prime is the bottleneck.

### Explanation
Making one copy of `r` uses one of each of its primes, so you can build only as many as the rarest ingredient allows.

### Example
Copies of 15 inside `20!`? `15 = 3 x 5`. 3s: `20/3 = 6`, `6/3 = 2` → 8. 5s: `20/5 = 4` → 4. The 5s run out first, so **4**.

## If `n!/r^x` is an integer, what is the largest `x`?
covers: 38

### Answer
Legendre each prime of `r`; if a prime carries an exponent inside `r`, divide that prime's total by the exponent and drop the decimal; then take the **minimum** across primes.

### Explanation
The floor comes *after* dividing by the exponent, and the minimum comes at the very end. Swapping those two steps gives the wrong answer.

### Example
`30!/3^x`: Legendre for 3 gives `10 + 3 + 1 = 14`, so **x = 14**.

Harder — `100!/24^x`, where `24 = 2^3 x 3`. Legendre for 2 gives 97, but each 24 needs three 2s: `97/3 = 32.3 → 32`. Legendre for 3 gives `33+11+3+1 = 48`, one per 24 → 48. Minimum: **32**.

## How many zeros does `n!` end in?
covers: 39

### Answer
Count the **5s** — run Legendre for 5 and stop. A trailing zero needs a `2 x 5`, and the 2s always outnumber the 5s.

### Explanation
The only work is remembering the higher powers: 25, 50, 75 and 100 each contribute a second 5.

The reverse question is common too: "for which `n` does `n!` first end in 6 zeros?" Walk the counts up — `20!` has 4, `25!` has 6 (25 contributes two 5s), so the answer is 25.

### Example
`100!` ends in `20 + 4 = 24` zeros. Answering 20 is the classic mistake.

`50!`: `50/5 = 10`, `10/5 = 2` → 12 zeros. `200!`: `40 + 8 + 1 = 49` zeros.

## Smallest integer that is **not** a factor of `n!`?
covers: 40

### Answer
The next **prime** after `n`. Every integer up to `n` divides `n!`, so the first failure must need a prime bigger than `n`.

### Explanation
After that first prime come its multiples and the primes beyond it. Do not just take "the next number after n" — that only works when it happens to be prime.

### Example
Smallest non-factor of `10!` is **11**. Next come 13, 17, 19 and 22 (`= 2 x 11`). For `12!` it is 13, not 14, since `14 = 2 x 7` and both are present.

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
