# Exponents & Roots

## Power of a power: multiply the exponents
covers: 63

`(a^b)^c = a^(bc)`. Raising a power to another power means repeating the multiplication `c` times, and each repetition contributes `b` copies of `a`, so you end up with `bc` of them.

### Example
`(2^3)^4 = 2^12 = 4,096`. Check the long way: `2^3 = 8`, and `8^4 = 4,096`. This is also how you compare ugly powers — `9^10` is `(3^2)^10 = 3^20`, which sits neatly beside `3^19` or `27^7 = 3^21`.

### Watch out
`(a^b)^c` is not `a^(b^c)`. `(2^3)^2 = 64` while `2^(3^2) = 2^9 = 512`. Brackets decide which one you have.

## Same exponent, different bases
covers: 64

`(a^b)(c^b) = (ac)^b`. When two powers share an exponent you may multiply the bases and keep the exponent once. It also runs backwards, which is usually the more useful direction: a messy base can be split into friendlier pieces.

### Example
`4^5 x 25^5 = (4 x 25)^5 = 100^5 = 10^10`. Backwards: `6^8 = (2 x 3)^8 = 2^8 x 3^8`, which is what lets you compare it with `2^10 x 3^8`.

### Watch out
Note the brackets: `(ac)^b`, not `ac^b`. Without them the exponent would only apply to `c`.

## Same base, multiplying: add the exponents
covers: 65

`(a^b)(a^c) = a^(b+c)`. Multiplying means putting all the copies of `a` together, so the counts add.

### Example
`2^3 x 2^5 = 2^8 = 256`. This is the move that rescues expressions like `2^10 + 2^10`: that is not `2^20` but `2 x 2^10 = 2^11`. Adding powers is completely different from multiplying them.

### Watch out
There is no rule for `a^b + a^c`. When you see a sum of powers, factor out the smaller one instead: `2^10 + 2^12 = 2^10(1 + 4) = 5 x 2^10`.

## Same base, dividing: subtract the exponents
covers: 66

`(a^b)/(a^c) = a^(b-c)`. Division cancels copies of `a`, so the counts subtract. This is also where the two definitions that look strange come from: `a^0 = 1` (because `a^b/a^b = 1`) and `a^(-n) = 1/a^n` (because subtracting more than you have flips it into the denominator).

### Example
`2^8/2^3 = 2^5 = 32`. And `3^4/3^7 = 3^(-3) = 1/27`. A negative exponent is not a negative number — `2^(-3)` is 1/8, comfortably positive.

## Roots as fractional exponents
covers: 67

A root is a power with a fractional exponent: `sqrt(a) = a^(1/2)`, `cuberoot(a) = a^(1/3)`, and in general `n-th root of a^m = a^(m/n)`. Rewriting roots this way lets you use every exponent rule you already know, and shortcuts that were invisible in radical form become obvious.

### Example
`sqrt(12)/sqrt(3)` looks awkward, but as `12^(1/2)/3^(1/2) = (12/3)^(1/2) = 4^(1/2) = 2` it is immediate. Similarly `sqrt(sqrt(16)) = (16^(1/2))^(1/2) = 16^(1/4) = 2`.

## Is the nth root rational?
covers: 68

Prime factorize the number under the root. The root is rational exactly when every exponent in that factorization is divisible by the root's index — because taking an `n`-th root divides each exponent by `n`, and you need whole numbers out the other side.

For square roots that means every exponent must be even; for cube roots, every exponent a multiple of 3.

### Example
Is the 4th root of 24 rational? `24 = 2^3 x 3`. The exponents 3 and 1 are not multiples of 4, so no. Is `sqrt(144)` rational? `144 = 2^4 x 3^2`, both exponents even, so yes — it is `2^2 x 3 = 12`.

## Simplifying radicals
covers: 69

Prime factorize what is under the root and pull out any prime whose exponent reaches the index of the root. Each group of `n` identical factors under an `n`-th root escapes as a single factor outside.

If an exponent overshoots, split it: `sqrt(2^9) = sqrt(2^8) x sqrt(2) = 2^4 x sqrt(2)`.

### Example
`sqrt(24) = sqrt(2^3 x 3) = sqrt(2^2) x sqrt(2 x 3) = 2sqrt(6)`. And `cuberoot(24) = cuberoot(2^3 x 3) = 2 x cuberoot(3)`, because the three 2s form one complete group for a cube root.

### Watch out
`sqrt(a + b)` is not `sqrt(a) + sqrt(b)`. Roots distribute over multiplication and division only — `sqrt(9 + 16) = 5`, not `3 + 4`.

## Radicals in the denominator
covers: 70

A fraction with a root on the bottom is considered unsimplified and is harder to compare or estimate. Multiply top and bottom by that root to move it upstairs — you are multiplying by 1, so the value does not change.

When the denominator is a sum like `1 + sqrt(2)`, multiply by its conjugate `1 - sqrt(2)` instead, and the difference-of-squares identity clears the root.

### Example
`3/sqrt(2) = (3 x sqrt(2))/(sqrt(2) x sqrt(2)) = 3sqrt(2)/2 ≈ 2.12`, which you can now estimate at a glance. With a conjugate: `1/(1 + sqrt(2)) = (1 - sqrt(2))/((1)^2 - (sqrt(2))^2) = (1 - sqrt(2))/(-1) = sqrt(2) - 1`.

## Even exponents under even roots need absolute values
covers: 71

`sqrt(x^2)` is **not** `x` — it is `|x|`. The square root symbol always returns the non-negative root, so if `x` were negative the plain answer would have the wrong sign. The same applies to any even power under any even root.

Odd roots have no such problem: `cuberoot(x^3) = x` even when `x` is negative, because cube roots can return negatives.

### Example
If `x = -5`, then `sqrt(x^2) = sqrt(25) = 5 = |x|`, not -5. So an equation like `sqrt(x^2) = 3` has two solutions, `x = 3` and `x = -3`, while `x^3 = 27` has only one.

### Watch out
In a quantitative comparison, "`x^2 = 16`" means `x` could be 4 or -4. Any question that squares away a variable's sign is usually heading for answer D.
