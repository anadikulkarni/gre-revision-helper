# Inequalities, Functions & Coordinate Basics

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

## `(x + 3)(x - 2) > 0` — what is the solution set?
covers: 84

### Answer
`x < -3` **or** `x > 2`. Mark the critical values on a line and **test a value in each of the three regions** — do not guess from the signs.

### Explanation
For a product of two factors with a positive leading coefficient: positive outside the roots, negative between them.

### Example
Test `x = -4`: `(-1)(-6) = +6` ✓. Test `x = 0`: `(3)(-2) = -6` ✗. Test `x = 3`: `(6)(1) = +6` ✓. So the outside regions win.

### Watch out
Move everything to one side first. Solving `(x+3)(x-2) > 6` by setting each factor against 6 is meaningless — expand, subtract 6, refactor, then test.

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

## Slope of a line, and the equation of a line?
covers: new

### Answer
`slope = (y2 - y1)/(x2 - x1)` = rise over run. Slope-intercept form: `y = mx + b`, where `m` is the slope and `b` the y-intercept.

### Explanation
A positive slope rises left to right, a negative one falls, zero is horizontal, and a vertical line has **undefined** slope (the run is 0). Parallel lines share a slope.

To find a line through two points: compute `m`, then substitute one point into `y = mx + b` to get `b`.

### Example
Through `(2, 3)` and `(6, 11)`: `m = (11-3)/(6-2) = 2`. Then `3 = 2(2) + b` gives `b = -1`, so `y = 2x - 1`.

### Watch out
Keep the points in the same order top and bottom. `(y2 - y1)/(x1 - x2)` flips the sign.

## Distance between two points in the plane?
covers: new

### Answer
`d = sqrt((x2 - x1)^2 + (y2 - y1)^2)` — Pythagoras on the horizontal and vertical gaps.

### Explanation
The two points are opposite corners of a right triangle whose legs are the coordinate differences, so the distance is its hypotenuse.

### Example
From `(1, 2)` to `(4, 6)`: legs 3 and 4, so `d = 5`. Recognising the 3-4-5 saves the square root entirely.

### Watch out
Squaring removes signs, so the order of the points does not matter here — unlike in the slope formula.

## Midpoint of a segment?
covers: new

### Answer
`((x1 + x2)/2, (y1 + y2)/2)` — average each coordinate separately.

### Explanation
The midpoint is the average point, which is also why a question giving you one endpoint and the midpoint lets you solve for the other endpoint.

A line's midpoint is also the centre of the circle that has that line as a diameter, which is how coordinate-geometry questions link the two formulas.

### Example
Midpoint of `(1, 2)` and `(7, 10)` is `(4, 6)`. Backwards: if `(4, 6)` is the midpoint and one endpoint is `(1, 2)`, the other satisfies `(1 + x)/2 = 4`, so it is `(7, 10)`.

If `(2,1)` and `(8,9)` are the ends of a diameter, the centre is `(5,5)` and the radius is half the distance, `= 5`, so the circle is `(x-5)^2 + (y-5)^2 = 25`.

