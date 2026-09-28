# Exponents, Algebra & Functions

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

## Cancelling a factor from a fraction — what happens to the domain?
covers: 77

### Answer
The **domain is fixed by the original expression, not the simplified one**. Cancelling `(x - 5)` is dividing by it, so `x = 5` stays out of the domain even after the factor disappears from the page. Work the domain out **before** you simplify.

### Explanation
The domain of an expression is the set of inputs it is allowed to take — everything that does not make a denominator zero or put a negative under an even root. When you cancel, you have quietly assumed the factor you cancelled is not zero, and that assumption has to be carried forward as a domain restriction.

This is exactly how a graph ends up with a hole in it: the simplified function is defined at that point, the original one is not, so the domain says "undefined" where the picture looks continuous.

### Example
`(x^2 - 25)/((x + 5)(x - 5))` simplifies to 1, but the domain still excludes **both** `x = 5` and `x = -5`, since either would have made the original denominator zero. Reading the domain off the simplified expression would lose both restrictions.

Another: `(x^2 - 4)/(x - 2)` simplifies to `x + 2`, whose domain looks like every real number — but the original is undefined at `x = 2`, so the domain is "all reals except 2" and the graph of `x + 2` has a hole at `(2, 4)`.

### Watch out
The same care applies to multiplying both sides of an equation by an expression containing the variable: you may introduce a solution the original equation never had, so check every answer against the **original**.

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

## The one rule that makes inequalities different from equations?
covers: 81

### Answer
Multiplying or dividing both sides by a **negative** number flips the inequality sign.

### Explanation
Negating reflects every number through zero on the number line, so whatever was on the left ends up on the right. Adding and subtracting are safe.

### Example
`-2x > 6` → divide by -2 and flip → `x < -3`. Test: `x = -4` gives `8 > 6` ✓; `x = 0` gives `0 > 6` ✗.

### Watch out
The real trap is dividing by a **variable** of unknown sign. From `ax > a` you cannot conclude `x > 1` unless you know `a > 0`.

## Can you add or subtract two inequalities?
covers: 82

### Answer
Add freely when they point the **same** way. Subtract only when they point **opposite** ways, and the result keeps the sign of the one you subtract from.

### Explanation
From `a > b` and `c < d` you may conclude `a - c > b - d` — subtracting a smaller thing leaves you with more. The safest habit is to flip the second inequality and add.

### Example
Given `5 < x < 9` and `1 < y < 4`, find the range of `x - y`. Flip the second to `-4 < -y < -1` and add: `1 < x - y < 8`.

### Watch out
Never subtract two same-direction inequalities: from `x > 2` and `y > 1` you cannot say `x - y > 1` — take `x = 3, y = 10`.

## `|x| < a` and `|x| > a` — what do they look like on the line?
covers: 83

### Answer
`|x| < a` is one band: `-a < x < a`. `|x| > a` is two pieces heading outwards: `x > a` **or** `x < -a`. When you negate the right-hand side, the sign flips too.

### Explanation
Reading the bars as distance prevents most sign errors: `|x - 3| < 5` says "x is less than 5 away from 3".

### Example
`|2x - 6| < 4` → `-4 < 2x - 6 < 4` → `1 < x < 5`. But `|2x - 6| > 4` → `x > 5` **or** `x < 1`.

## A factored inequality like `(x + 3)(x - 2) > 0` — how do you get the solution set?
covers: 84

### Answer
Move everything to one side, find the critical values where each factor is zero, mark them on a number line, and **test one value in every region**. Never guess the signs from the inequality.

### Explanation
The critical values split the line into regions, and the expression cannot change sign inside a region — so one test value settles the whole region. For two factors with a positive leading coefficient the pattern is positive outside the roots and negative between them, but testing takes two seconds and works for any number of factors, for `>=` versus `>`, and for a negative leading coefficient, where the pattern reverses.

The habit matters more than the pattern: as soon as there are three factors, or a squared factor that touches zero without crossing, memorised patterns fail and testing does not.

### Example
`(x + 3)(x - 2) > 0`. Critical values -3 and 2. Test `x = -4`: `(-1)(-6) = +6` ✓. Test `x = 0`: `(3)(-2) = -6` ✗. Test `x = 3`: `(6)(1) = +6` ✓. So the solution is `x < -3` **or** `x > 2`.

Same method with a sign flip: `-(x - 1)(x - 4) > 0` tests positive only between 1 and 4, so the answer is `1 < x < 4` — the opposite shape, caught by testing rather than recall.

### Watch out
Rearrange to "something > 0" first. Solving `(x+3)(x-2) > 6` by setting each factor against 6 is meaningless — expand, subtract 6, refactor, then test.

## `f(x + 3) = x^2 + x`. What is `f(7)`?
covers: 85

### Answer
**20.** Set the inside expression equal to 7: `x + 3 = 7`, so `x = 4`, and then evaluate the right-hand side at `x = 4`: `16 + 4 = 20`.

### Explanation
The rule describes what happens to whatever the inside expression evaluates to, so you must solve for the `x` that produces the input you want.

The same care is needed for composite functions: `f(g(x))` means run `g` first, then feed its output into `f`. Work from the inside out.

### Example
Substituting 7 directly for `x` would give 56 — the wrong answer the question is fishing for.

With `f(x) = 2x + 1` and `g(x) = x^2`: `f(g(3)) = f(9) = 19`, but `g(f(3)) = g(7) = 49`. Order matters.

## A function defined in terms of itself — how do you use it?
covers: 86

### Answer
Read it as a **step rule** and walk from the value you are given to the value you want.

### Explanation
Recursive definitions tell you how to move from one input to the next rather than giving values outright.

### Example
`f(x + 1) = 10 f(x)` with `f(3) = 5`. Each step multiplies by 10: `f(4) = 50`, `f(5) = 500`, `f(6) = 5,000` — three steps, so `5 x 10^3`.

### Watch out
Count steps, not numbers: from `f(3)` to `f(6)` is three steps, not six.

## How do you find the range of a function?
covers: 87

### Answer
Set `y = f(x)`, rearrange to get `x` in terms of `y`, and ask which `y` values are legal. Whatever `y` cannot be is missing from the range.

### Explanation
Solving for `x` converts a question about outputs into a question about a domain, which you already know how to answer.

### Example
`y = (3 - x)/(x - 2)` → `y(x-2) = 3-x` → `x(y+1) = 3+2y` → `x = (3+2y)/(y+1)`, undefined at `y = -1`. So the range is every real number except **-1**.

### Watch out
Do not confuse the two: here the *domain* excludes `x = 2` and the *range* excludes `y = -1`.

## What makes a function even?
covers: 88

### Answer
`f(-x) = f(x)`. For polynomials that means every power of `x` is **even** (a constant counts as `x^0`). The graph is symmetric about the y-axis.

### Explanation
Feeding in the opposite input gives the same output, so the two halves of the graph mirror each other.

### Example
`f(x) = x^2 + 3` is even: `f(-2) = 7 = f(2)`. `f(x) = x^2 + x` is not, because of the odd-powered term: `f(-2) = 2` but `f(2) = 6`.

## What makes a function odd?
covers: 89

### Answer
`f(-x) = -f(x)`. For polynomials that means every power is **odd** and there is no constant term. The graph has 180° rotational symmetry about the origin.

### Explanation
Flipping the input flips the sign of the output.

A quick test that avoids algebra: if the graph looks the same after turning the page 180°, it is odd; if it looks the same after folding along the y-axis, it is even.

### Example
`f(x) = x^3 - x` is odd: `f(-2) = -6`, `f(2) = 6`. Adding a constant breaks it — `x^3 + 1` is neither. Only `f(x) = 0` is both even and odd.

For any odd function `f(0) = 0`, because `f(-0) = -f(0)` forces it. That single fact answers many "which could be odd" questions immediately.
