# GCF, LCM & Factorials

## Greatest common factor from prime factorizations
covers: 28

The GCF is the largest number that divides all of them. Prime factorize every number, then for each prime that appears in *all* of them take the **lowest** power. Multiply those together and you have the GCF. A prime missing from any one number cannot appear in the GCF at all.

Think of it as "what do they all have in common" — you can only share as many copies of a prime as the stingiest number has.

### Example
GCF of 60 and 72. `60 = 2^2 x 3 x 5` and `72 = 2^3 x 3^2`. Shared primes are 2 and 3. Lowest power of 2 is `2^2`, lowest power of 3 is `3^1`, and 5 is missing from 72 so it is out. GCF `= 4 x 3 = 12`.

### Watch out
If two numbers share no prime at all, their GCF is 1 and they are called coprime — not zero.

## Factors shared by a group are the factors of their GCF
covers: 29

"How many factors do 60 and 72 have in common?" is the same question as "how many factors does their GCF have". Build the GCF, then apply the exponent-plus-one counting rule to it. There is no need to list anything.

This is worth internalising because it converts a vague-sounding question into two steps you already know cold.

### Example
Common factors of 60 and 72: the GCF is `12 = 2^2 x 3`, so the count is `(2+1)(1+1) = 6`. They are 1, 2, 3, 4, 6, 12 — and you can see each one divides both 60 and 72.

## Least common multiple from prime factorizations
covers: 30

The LCM is the smallest number all of them divide into. Prime factorize, then for each prime that appears in *any* of them take the **highest** power, and multiply. Where the GCF asks what they share, the LCM asks what is needed to satisfy everyone.

### Example
LCM of 60 and 72. `60 = 2^2 x 3 x 5`, `72 = 2^3 x 3^2`. Highest power of 2 is `2^3`, of 3 is `3^2`, of 5 is `5^1`. LCM `= 8 x 9 x 5 = 360`. Sanity check: `360/60 = 6` and `360/72 = 5`, both whole.

### Watch out
The LCM of two numbers is never smaller than the larger of them, and the GCF is never bigger than the smaller. If your answer breaks that, you have swapped the rules.

## Divisible by a and by b means divisible by their LCM
covers: 31

If a number is a multiple of `a` and also a multiple of `b`, then it is a multiple of `LCM(a, b)` — not necessarily of `a x b`. This is the rule people get wrong: a number divisible by 4 and by 6 must be divisible by 12, not by 24.

Only when `a` and `b` are coprime does `LCM(a, b) = a x b`, which is why "divisible by 3 and by 5" does safely mean "divisible by 15".

### Example
`n` is divisible by 8 and by 12. `LCM(8, 12) = 24`, so `n` must be a multiple of 24. `n = 24` works and is not a multiple of `8 x 12 = 96`, which proves the product version is wrong.

## GCF times LCM equals the product
covers: 32

For any two positive integers, `GCF(a, b) x LCM(a, b) = a x b`. Every prime appears in the pair with a lower and a higher exponent, and the GCF takes the lower one while the LCM takes the higher, so between them they use up exactly the exponents in `a x b`.

This gives you a free shortcut whenever a question hands you three of the four quantities.

### Example
`a = 60`, `b = 72`, `GCF = 12`. Then `LCM = (60 x 72)/12 = 4,320/12 = 360`, matching the direct computation. And if a question says two numbers multiply to 1,200 with a GCF of 10, the LCM is `1,200/10 = 120` with no factorization needed.

### Watch out
This identity holds for two numbers only. For three or more it breaks down.

## Simplifying a quotient of factorials
covers: 33

`n!` means `n x (n-1) x (n-2) x ... x 1`, so a bigger factorial contains a smaller one whole. When you divide `m!` by `n!` with `m > n`, everything up to `n!` cancels and you are left with the handful of terms in between — never compute the factorials themselves.

`m!/n! = m x (m-1) x ... x (n+1)`.

### Example
`8!/5! = (8 x 7 x 6 x 5!)/5! = 8 x 7 x 6 = 336`. Similarly `100!/98! = 100 x 99 = 9,900`, which you can do in your head, while `100!` has 158 digits.

### Watch out
`0! = 1` by definition, which keeps formulas like `nPn = n!/0!` working.

## Legendre's method: the prime factorization of n!
covers: 35

`n!` is far too big to factorize by multiplying out, but you can count each prime directly. For a prime `p`, count how many multiples of `p` are at or below `n`, then how many multiples of `p^2`, then `p^3`, and so on until the count reaches zero. The total is the exponent of `p` in `n!`.

The reason for the extra rounds is that a number like 9 contributes *two* 3s to the product, so it has to be counted once as a multiple of 3 and again as a multiple of 9.

### Example
Exponent of 3 in `10!`: multiples of 3 up to 10 are 3, 6, 9 → 3 of them; multiples of 9 are just 9 → 1; multiples of 27 → 0. Total `3 + 1 = 4`, so `10!` contains `3^4`. Doing the same for 2 (5 + 2 + 1 = 8), 5 (2) and 7 (1) gives `10! = 2^8 x 3^4 x 5^2 x 7`.

## Legendre's shortcut: keep dividing
covers: 36

You do not have to list multiples. Divide `n` by `p` and drop the decimal, then divide that result by `p` again, and keep going until you hit 0. Adding up everything you wrote down gives the exponent.

Each division is asking the same question one level deeper, which is exactly what counting multiples of `p`, `p^2`, `p^3` does.

### Example
Exponent of 5 in `100!`: `100/5 = 20`, `20/5 = 4`, `4/5 = 0`. Total `20 + 4 = 24`. Exponent of 2 in `100!`: 50, 25, 12, 6, 3, 1, 0 → `50+25+12+6+3+1 = 97`.

## How many factors does a factorial have
covers: 34

Use Legendre's method to get the prime factorization of `n!`, then apply the ordinary exponent-plus-one rule. There is no separate formula — it is the two techniques stacked.

### Example
How many factors does `10!` have? From above, `10! = 2^8 x 3^4 x 5^2 x 7^1`, so the count is `(8+1)(4+1)(2+1)(1+1) = 9 x 5 x 3 x 2 = 270`.

## How many copies of r are inside n!
covers: 37

If `r` is prime, run Legendre's method for `r` and you are done. If `r` is composite, factorize it first, run Legendre separately for each of its primes, then see which prime runs out first — that bottleneck is your answer.

The bottleneck logic is the point: making one copy of `r` uses one of each of its primes, so you can only make as many copies as the scarcest ingredient allows.

### Example
How many copies of 15 are inside `20!`? `15 = 3 x 5`. Exponent of 3: `20/3 = 6`, `6/3 = 2`, `2/3 = 0` → 8. Exponent of 5: `20/5 = 4`, `4/5 = 0` → 4. The 5s run out first, so `20!` contains 4 copies of 15.

## Largest power of r that divides n!
covers: 38

This is the same machinery in its most common exam form: "if `n!/r^x` is an integer, what is the largest `x`?" Run Legendre for each prime in `r`. If a prime appears in `r` with an exponent of its own, divide that prime's Legendre total by the exponent and drop the decimal. The smallest result across all the primes is the answer.

### Example
If `30!/3^x` is an integer, what is the largest `x`? Legendre for 3: `30/3 = 10`, `10/3 = 3`, `3/3 = 1`, `1/3 = 0`. Total `10 + 3 + 1 = 14`, so `x = 14`.

Harder: if `100!/24^x` is an integer, what is the largest `x`? `24 = 2^3 x 3`. Legendre for 2 gives 97, but each 24 needs three 2s, so `97/3 = 32.3 → 32`. Legendre for 3 gives `33 + 11 + 3 + 1 = 48`, and each 24 needs one 3, so 48. The minimum is **32**.

### Watch out
Take the floor *after* dividing by the exponent, and take the minimum across primes at the very end — swapping those two steps gives the wrong answer.

## Trailing zeros of a factorial
covers: 39

A trailing zero comes from a factor of 10, and `10 = 2 x 5`. In any factorial the 2s vastly outnumber the 5s, so the number of trailing zeros is just the number of 5s: run Legendre for 5 and stop.

### Example
How many zeros does `100!` end in? Legendre for 5: `100/5 = 20`, `20/5 = 4`, `4/5 = 0`, total **24**. Note that counting `100/5 = 20` alone is the classic mistake — 25, 50, 75 and 100 each contribute a second 5.
