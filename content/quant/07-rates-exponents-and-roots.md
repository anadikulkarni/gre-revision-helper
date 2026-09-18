# Rates, Exponents & Roots

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

## `(a^b)^c` = ?
covers: 63

### Answer
`a^(bc)` — multiply the exponents.

### Explanation
Raising a power to a power repeats the multiplication `c` times, each contributing `b` copies of `a`.

This is the main tool for comparing powers with different bases: rewrite both as powers of the same base and then simply compare exponents.

### Example
`(2^3)^4 = 2^12 = 4,096`, and the long way `8^4` agrees. This is also how you compare ugly powers: `9^10 = (3^2)^10 = 3^20`, which sits neatly beside `27^7 = 3^21`.

Which is bigger, `4^30` or `8^20`? `4^30 = 2^60` and `8^20 = 2^60` — they are equal.

### Watch out
`(a^b)^c` is not `a^(b^c)`. `(2^3)^2 = 64` but `2^(3^2) = 512`.

## `(a^b)(c^b)` = ?
covers: 64

### Answer
`(ac)^b` — same exponent, so multiply the bases and keep the exponent once.

### Explanation
Running it backwards is usually more useful: a messy base splits into friendlier pieces.

It is also how you handle a power of a fraction: `(a/b)^n = a^n/b^n`, so `(2/3)^4 = 16/81`.

### Example
`4^5 x 25^5 = 100^5 = 10^10`. Backwards: `6^8 = (2 x 3)^8 = 2^8 x 3^8`, which is what lets you compare it with `2^10 x 3^8`.

`2^10 x 5^10 = 10^10`, so a question about `2^10 x 5^10 x 3` is really asking about `3 x 10^10` — a 1 followed by ten zeros, tripled.

### Watch out
Mind the brackets: `(ac)^b`, not `ac^b`.

## `(a^b)(a^c)` = ?
covers: 65

### Answer
`a^(b+c)` — same base, so **add** the exponents.

### Explanation
Multiplying gathers all the copies of `a` together, so the counts add.

### Example
`2^3 x 2^5 = 2^8 = 256`. Contrast with a sum: `2^10 + 2^10 = 2 x 2^10 = 2^11`, not `2^20`.

Useful in reverse for comparisons: `3^11` versus `9^5 = 3^10` — same base, so `3^11` is three times larger.

### Watch out
There is no rule for `a^b + a^c`. Factor out the smaller: `2^10 + 2^12 = 2^10(1 + 4) = 5 x 2^10`.

## `(a^b)/(a^c)` = ?
covers: 66

### Answer
`a^(b-c)` — same base, so **subtract**. This is also where `a^0 = 1` and `a^(-n) = 1/a^n` come from.

### Explanation
Division cancels copies of `a`. Subtracting more than you have flips the leftover into the denominator, which is exactly what a negative exponent means.

### Example
`2^8/2^3 = 2^5 = 32`. `3^4/3^7 = 3^(-3) = 1/27`. Note `2^(-3) = 1/8` is positive — a negative exponent is not a negative number.

## Rewriting a root as an exponent?
covers: 67

### Answer
`nth root of a^m = a^(m/n)`. So `sqrt(a) = a^(1/2)` and `cuberoot(a) = a^(1/3)`.

### Explanation
Once roots are exponents, every exponent rule applies to them, and shortcuts that were invisible in radical form appear.

A negative fractional exponent combines both ideas: `a^(-1/2) = 1/sqrt(a)`. And `(a^(1/2))^2 = a`, which is why squaring undoes a square root.

### Example
`sqrt(12)/sqrt(3)` is awkward, but `12^(1/2)/3^(1/2) = (12/3)^(1/2) = 2` is immediate. Likewise `sqrt(sqrt(16)) = 16^(1/4) = 2`.

`8^(2/3)` means "cube root, then square": `cuberoot(8) = 2`, and `2^2 = 4`. Doing the root first keeps the numbers small.

## Is the `n`th root of a number rational?
covers: 68

### Answer
Yes exactly when **every exponent in its prime factorization is divisible by `n`**. Square roots need all even exponents; cube roots need multiples of 3.

### Explanation
Taking an `n`th root divides each exponent by `n`, and you need whole numbers out the other side.

### Example
4th root of 24? `24 = 2^3 x 3`, and 3 and 1 are not multiples of 4 → irrational. `sqrt(144)`? `144 = 2^4 x 3^2`, both even → rational, equal to `2^2 x 3 = 12`.

## Simplifying a radical like `sqrt(24)`?
covers: 69

### Answer
Prime factorize underneath and pull out any prime whose exponent reaches the root's index. `sqrt(24) = sqrt(2^2 x 6) = 2sqrt(6)`.

### Explanation
Each complete group of `n` identical factors escapes an `n`th root as a single factor. If an exponent overshoots, split it: `sqrt(2^9) = sqrt(2^8) x sqrt(2) = 2^4 sqrt(2)`.

### Example
`cuberoot(24) = cuberoot(2^3 x 3) = 2 cuberoot(3)`, because the three 2s form one complete group for a cube root.

### Watch out
`sqrt(a + b)` is not `sqrt(a) + sqrt(b)`: `sqrt(9 + 16) = 5`, not 7. Roots distribute over multiplication and division only.

## Getting a radical out of a denominator?
covers: 70

### Answer
Multiply top and bottom by that radical. For a denominator like `1 + sqrt(2)`, multiply by its **conjugate** `1 - sqrt(2)`.

### Explanation
You are multiplying by 1, so the value is unchanged — but the expression becomes estimable. The conjugate works because the difference of squares kills the root.

### Example
`3/sqrt(2) = 3sqrt(2)/2 ≈ 2.12`. And `1/(1 + sqrt(2)) = (1 - sqrt(2))/(1 - 2) = sqrt(2) - 1`.

## `sqrt(x^2)` = ?
covers: 71

### Answer
`|x|`, **not** `x`. The radical sign always returns the non-negative root. The same applies to any even power under any even root.

### Explanation
Odd roots have no such problem: `cuberoot(x^3) = x` even for negative `x`, because cube roots can return negatives.

### Example
With `x = -5`: `sqrt(x^2) = sqrt(25) = 5 = |x|`. So `sqrt(x^2) = 3` has two solutions, `x = ±3`, while `x^3 = 27` has one.

### Watch out
In a comparison, "`x^2 = 16`" means `x` could be 4 **or** -4. Any question that squares away a sign is usually heading for D.
