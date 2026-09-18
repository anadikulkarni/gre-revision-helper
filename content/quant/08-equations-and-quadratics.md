# Equations & Quadratics

## Degree of a polynomial — how is it measured?
covers: 72

### Answer
Add the exponents **within each term**; the largest of those totals is the degree.

### Explanation
A single term with several variables counts them all together, which is the part people miss.

Degree tells you what to expect: degree 1 graphs as a line with one solution, degree 2 as a parabola with up to two, and in general a polynomial of degree `n` has at most `n` real roots and at most `n - 1` turning points.

### Example
`(2x^2)(4y^3) = 8x^2y^3` has degree `2 + 3 = 5`. In `x^3 + 5x^2y^2 - 7` the term degrees are 3, 4 and 0, so the polynomial has degree **4**.

`(x + 2)(x - 3)(x + 5)` has degree 3 without expanding — just count the brackets.

## What disqualifies an expression from being a polynomial?
covers: 75

### Answer
Negative exponents (variables in a denominator), fractional exponents (roots of variables), and absolute values.

### Explanation
A polynomial is a sum of terms made only of numbers and variables raised to whole-number powers. That restriction is what makes the factoring rules always work.

### Example
`3x^2 - 5x + 7` ✓. `3/x + 2` ✗ (that is `3x^-1`). `sqrt(x) + 1` ✗. `|x| + 4` ✗. But `(3/4)x^2` ✓ — fractional *coefficients* are fine, only fractional *exponents* are not.

## What is a linear equation?
covers: 74

### Answer
A polynomial equation of degree 1 — every variable to the first power only. It graphs as a straight line and has exactly one solution unless the variable cancels out.

### Explanation
Recognising degree tells you what tools apply: linear means isolate and solve, degree 2 means factor, discriminant or the quadratic formula.

### Example
`3x + 7 = 22` → `x = 5`. `y = 2x - 3` is linear in two variables. `x^2 + 3x = 4` is not linear.

## Two equations, two unknowns — how do you solve them?
covers: new

### Answer
**Substitution** (solve one for a variable, put it into the other) or **elimination** (scale one equation so a variable cancels when you add or subtract).

### Explanation
Elimination is usually faster when coefficients line up; substitution is better when one variable is already isolated.

Watch what the question actually asks: it often wants `x + y` or `x - y`, which you can get by adding or subtracting the equations directly — no need to find `x` and `y` at all.

### Example
`2x + 3y = 16` and `x - y = 2`. Substituting `x = y + 2` gives `2y + 4 + 3y = 16`, so `y = 2.4` and `x = 4.4`. But if the question only wanted `3x + 2y`, adding the two equations as they stand gets there faster.

### Watch out
Two equations that are multiples of each other have infinitely many solutions; two with the same slope and different constants have none.

## Expanding brackets, and factoring `x^2 + bx + c`?
covers: new

### Answer
Expand with FOIL: `(x + p)(x + q) = x^2 + (p+q)x + pq`. To factor, find two numbers that **multiply to `c` and add to `b`**.

### Explanation
Factoring is FOIL run backwards, and the multiply-to/add-to search is quick because you only test factor pairs of `c`. If the `x^2` has a coefficient, factor it out first or test pairs on `ac`.

### Example
`x^2 + 7x + 12`: which pair multiplies to 12 and adds to 7? 3 and 4, so it is `(x+3)(x+4)`. `x^2 - 5x + 6` → -2 and -3 → `(x-2)(x-3)`.

### Watch out
Signs are where it goes wrong: a positive `c` with a negative `b` means **both** numbers are negative.

## The three quadratic identities?
covers: 73

### Answer
`a^2 + 2ab + b^2 = (a + b)^2`
`a^2 - 2ab + b^2 = (a - b)^2`
`a^2 - b^2 = (a + b)(a - b)`

### Explanation
The third — difference of squares — is the workhorse, turning awkward arithmetic into mental arithmetic and simplifying fractions in one step.

### Example
`97 x 103 = (100-3)(100+3) = 10,000 - 9 = 9,991`. Given `x + y = 10` and `x - y = 4`, then `x^2 - y^2 = 40` without ever finding `x` or `y`.

## How do you spot that an expression is one of the identities?
covers: 76

### Answer
First and last terms are perfect squares, and the middle term is **twice** the product of their roots → perfect square trinomial. Two squares with a minus between → difference of squares.

### Explanation
Scanning for these shapes before grinding through algebra saves the most time of any habit in this section.

### Example
`x^2 + 10x + 25 = (x+5)^2` (25 is `5^2`, and `10x = 2 x 5 x x`). `4x^2 - 9 = (2x+3)(2x-3)`. `(x^2 - 9)/(x + 3)` simplifies to `x - 3`.

### Watch out
Check the middle term first: `x^2 + 7x + 25` is **not** `(x+5)^2`, which would need `10x`.

## The quadratic formula?
covers: new

### Answer
For `ax^2 + bx + c = 0`:

`x = (-b ± sqrt(b^2 - 4ac)) / 2a`

### Explanation
It always works, so it is the fallback when factoring fails. The quantity under the root is the discriminant, so the formula also tells you the number of solutions.

Rearrange to `= 0` first and keep the signs: in `x^2 - 4x - 6`, `c` is -6.

### Example
`2x^2 + 3x - 2 = 0`: `x = (-3 ± sqrt(9 + 16))/4 = (-3 ± 5)/4`, giving `x = 1/2` and `x = -2`. Factoring confirms it: `(2x - 1)(x + 2)`.

## How many solutions does a quadratic have?
covers: 79

### Answer
Check the discriminant `b^2 - 4ac`: **positive** → 2 solutions, **zero** → 1, **negative** → none.

### Explanation
You do not need the solutions themselves to answer "how many", which is exactly what the question usually wants.

### Example
`x^2 - 4x - 6`: `16 + 24 = 40 > 0` → two. `x^2 - 4x + 4`: `16 - 16 = 0` → one (`x = 2`). `x^2 + x + 5`: `1 - 20 < 0` → none.

## Completing the square — what do you add?
covers: 80

### Answer
Half the coefficient of `x`, squared — add it to **both** sides. `x^2 + bx` becomes a perfect square once you add `(b/2)^2`.

### Explanation
It forces a quadratic that will not factor into a single squared bracket you can undo with a root. It is also how you find a parabola's vertex.

### Example
`x^2 - 4x - 6 = 0`. Half of -4 is -2, squared is 4: `(x^2 - 4x + 4) - 6 = 4`, so `(x-2)^2 = 10` and `x = 2 ± sqrt(10)`.

### Watch out
Divide through by the leading coefficient first — completing the square needs `x^2` to stand alone.

## When you cancel a factor from a fraction, what must you record first?
covers: 77

### Answer
The **domain of the original expression**. Cancelling `(x - 5)` quietly divides by it, so `x = 5` stays excluded even though the factor has vanished.

### Explanation
The restriction belongs to the original expression, not the simplified one, so work the domain out before you simplify. This is exactly how a graph ends up with a hole in it.

### Example
`(x^2 - 25)/((x+5)(x-5))` simplifies to 1, but the domain still excludes **both** `x = 5` and `x = -5`. Reading the simplified form alone would lose both.

## `|expression| = something` — how do you solve it?
covers: 78

### Answer
Isolate the absolute value, then split into two equations: `expression = something` and `expression = -(something)`.

### Explanation
The bars hide the sign of what is inside, so both possibilities must be chased and both checked.

### Example
`|4x + 9| = 21` → `4x + 9 = 21` gives `x = 3`; `4x + 9 = -21` gives `x = -7.5`. Both check out.

### Watch out
Isolate first: `2|x| + 3 = 11` must become `|x| = 4`. And if the right side is negative there are **no** solutions.
