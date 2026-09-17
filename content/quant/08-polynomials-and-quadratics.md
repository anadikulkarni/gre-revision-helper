# Polynomials & Quadratics

## Degree of a polynomial
covers: 72

Within each term, add up the exponents of every variable; the biggest of those totals is the degree of the whole polynomial. A single term with several variables counts them all together, which is what people miss.

### Example
In `(2x^2)(4y^3) = 8x^2y^3` the degree is `2 + 3 = 5`. In `x^3 + 5x^2y^2 - 7`, the term degrees are 3, 4 and 0, so the polynomial has degree 4.

## What counts as a polynomial
covers: 75

A polynomial is a sum of terms made only of numbers and variables raised to whole-number powers. That rules out negative exponents (`x^-1`, i.e. variables in a denominator), fractional exponents (roots of variables) and absolute values.

The point of the definition is that polynomials are smooth and predictable, which is what lets the factoring rules below always work.

### Example
`3x^2 - 5x + 7` is a polynomial. `3/x + 2` is not (that is `3x^-1`). `sqrt(x) + 1` is not (that is `x^(1/2)`). `|x| + 4` is not. But `3/4 x^2` is fine — fractional *coefficients* are allowed, only fractional *exponents* are not.

## Linear equations
covers: 74

A linear equation is a polynomial equation of degree 1: every variable appears to the first power only. Graphed on the plane it is a straight line, which is where the name comes from, and it has exactly one solution unless the variable cancels out entirely.

### Example
`3x + 7 = 22` is linear, giving `x = 5`. `y = 2x - 3` is linear in two variables and draws a straight line. `x^2 + 3x = 4` is not linear — it is quadratic, degree 2.

## The three quadratic identities
covers: 73

These three are worth recognising instantly in both directions:

`a^2 + 2ab + b^2 = (a + b)^2`

`a^2 - 2ab + b^2 = (a - b)^2`

`a^2 - b^2 = (a + b)(a - b)`

The third — the difference of squares — is the one that turns awkward arithmetic into mental arithmetic.

### Example
`97 x 103 = (100 - 3)(100 + 3) = 100^2 - 3^2 = 10,000 - 9 = 9,991`. And if a question says `x + y = 10` and `x - y = 4`, then `x^2 - y^2 = 10 x 4 = 40` without ever finding `x` or `y`.

## Spotting an identity to simplify
covers: 76

Before grinding through algebra, scan the expression for the shapes above. A trinomial whose first and last terms are perfect squares and whose middle term is twice the product of their roots is a perfect square trinomial, and collapses into one bracket. A difference of two squares always splits into conjugates.

### Example
`x^2 + 10x + 25 = (x + 5)^2`, because 25 is `5^2` and `10x` is `2 x 5 x x`. `4x^2 - 9 = (2x + 3)(2x - 3)`. And a fraction like `(x^2 - 9)/(x + 3)` simplifies to `x - 3` once you factor the top.

### Watch out
Check the middle term before declaring a perfect square. `x^2 + 7x + 25` is not `(x+5)^2`, because that would need `10x`.

## Find the domain before you simplify
covers: 77

When you cancel a factor from the top and bottom of a fraction, you are quietly dividing by that factor — which is only legal if it is not zero. The restriction it imposes stays with the expression even after the factor has vanished from sight, so work out the domain from the **original** expression.

### Example
`(x^2 - 25)/((x+5)(x-5))`. Cancelling gives 1, but the domain still excludes both `x = 5` and `x = -5`, since either would have made the original denominator zero. Looking only at the simplified answer would lose both restrictions.

### Watch out
This is exactly how a graph ends up with a hole in it. The simplified function is defined there; the original one is not.

## Absolute-value equations split into two
covers: 78

Rearrange until the equation reads `|expression1| = expression2`, then solve it twice: once with `expression1 = expression2` and once with `expression1 = -expression2`. The absolute value hides the sign of what is inside, so both possibilities have to be chased.

### Example
`|4x + 9| = 21`. First: `4x + 9 = 21`, so `x = 3`. Second: `4x + 9 = -21`, so `x = -7.5`. Both check out in the original equation.

### Watch out
Isolate the absolute value before splitting — `2|x| + 3 = 11` must become `|x| = 4` first. And if the right-hand side is negative, there are no solutions at all, since an absolute value can never be negative.

## How many solutions does a quadratic have?
covers: 79

For `ax^2 + bx + c = 0`, compute the discriminant `b^2 - 4ac`. Positive means two distinct real solutions, zero means one (a repeated root), negative means none. You do not need the solutions themselves to answer "how many".

### Example
`x^2 - 4x - 6 = 0`: discriminant `= 16 + 24 = 40 > 0`, so two solutions. `x^2 - 4x + 4 = 0`: discriminant `= 16 - 16 = 0`, so one solution (`x = 2`). `x^2 + x + 5 = 0`: discriminant `= 1 - 20 = -19 < 0`, so no real solutions.

### Watch out
Rearrange to `= 0` before reading off `a`, `b` and `c`, and keep the signs: in `x^2 - 4x - 6`, `c` is -6, not 6.

## Completing the square
covers: 80

When a quadratic does not factor neatly, you can force a perfect square. Take the coefficient of `x`, halve it, square it, and add that to both sides. The left side then folds into a single squared bracket that you can undo with a square root.

### Example
`x^2 - 4x - 6 = 0`. Half of -4 is -2, and `(-2)^2 = 4`, so add 4 to both sides: `x^2 - 4x + 4 - 6 = 4`, which is `(x-2)^2 - 6 = 4`, so `(x-2)^2 = 10` and `x = 2 ± sqrt(10)`.

### Watch out
If the `x^2` term has a coefficient, divide the whole equation through by it first — completing the square only works when the leading coefficient is 1.
