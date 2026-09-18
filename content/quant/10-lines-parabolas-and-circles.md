# Lines, Parabolas & Circles

## What do the signs of a line's two intercepts tell you?
covers: 96

### Answer
Through the origin: both are 0. Not through the origin — **positive slope → intercepts have opposite signs** (product negative); **negative slope → same signs** (product positive). Slope 0 has only a y-intercept.

### Explanation
A rising line that misses the origin has to cross one axis on each side of it; a falling line crosses both on the same side. Questions test this without ever giving you an equation.

### Example
`y = 2x - 6`: intercepts -6 and 3, product -18 (negative) ✓. `y = -2x + 6`: intercepts 6 and 3, product 18 (positive) ✓.

### Watch out
A vertical line has **undefined** slope, not zero, and no y-intercept unless it is the y-axis itself.

## Slopes of perpendicular lines?
covers: 97

### Answer
Negative reciprocals: if one is `m`, the other is `-1/m`, and their product is **-1**. (Parallel lines have equal slopes.)

### Explanation
Turning a line 90° swaps rise and run and reverses one of the signs.

### Example
Slope 2/3 is perpendicular to -3/2, and `(2/3)(-3/2) = -1` ✓. So the perpendicular to `y = 4x + 1` through the origin is `y = -x/4`.

### Watch out
Horizontal and vertical lines are perpendicular but break the formula, since `-1/0` is undefined. Treat that pair as a special case.

## A quadratic that is a perfect square — what does its graph do?
covers: 90

### Answer
It **touches** the x-axis at exactly one point instead of crossing. That point is both the only root and the vertex.

### Explanation
This is the graphical face of "discriminant = 0, one solution".

It also tells you the sign of the whole expression: `(x - 3)^2` is never negative, so `y = (x-3)^2 + 4` is always at least 4 — a favourite way to hide a minimum value in a comparison.

### Example
`y = (x - 3)^2` has its only root and its minimum at `(3, 0)`. `y = -(x + 2)^2` opens downward with its maximum at `(-2, 0)`.

`y = x^2 - 6x + 9 = (x-3)^2` touches the axis at `x = 3`; its discriminant is `36 - 36 = 0` ✓.

## `y = (x - h)^2` and `y = (x + h)^2` — which way do they move?
covers: 91, 92

### Answer
Opposite to the sign you see: `(x - h)^2` shifts `h` **right**, `(x + h)^2` shifts `h` **left**.

### Explanation
The vertex sits where the bracket equals zero, so in `(x - 3)^2` that is `x = +3`. Solving "bracket = 0" is more reliable than remembering the rule.

### Example
`y = (x - 4)^2` has vertex `(4, 0)`; `y = (x + 4)^2` has vertex `(-4, 0)`.

### Watch out
This inside-the-bracket sign flip is the single most common graphing error.

## `y = x^2 + k` and `y = x^2 - k` — which way do they move?
covers: 93, 94

### Answer
The way the sign says: `+k` shifts **up**, `-k` shifts **down**. Outside the square, the direction matches.

### Explanation
Combine both kinds of shift and you can place any parabola: `y = (x - h)^2 + k` has vertex `(h, k)`.

### Example
`y = x^2 + 3` has vertex `(0, 3)` and never meets the x-axis. `y = x^2 - 3` has vertex `(0, -3)` and crosses at `±sqrt(3)`. `y = (x - 2)^2 + 5` has vertex `(2, 5)`.

## How do you find a parabola's vertex from an untidy quadratic?
covers: 95

### Answer
Complete the square into **vertex form** `y = (x - h)^2 + k`; the vertex is `(h, k)`. (Or use `h = -b/2a`.)

### Explanation
Vertex form is just the basic parabola shifted `h` right and `k` up, so completing the square doubles as a graphing tool: it converts an unreadable expression into a point you can plot.

### Example
`y = x^2 - 4x - 6` → `(x^2 - 4x + 4) - 4 - 6` → `(x - 2)^2 - 10`. Vertex `(2, -10)`, minimum value -10, y-intercept -6.

### Watch out
Whatever you add inside the bracket must be subtracted outside it, or you have changed the function.

## Equation of a circle?
covers: 98

### Answer
`(x - h)^2 + (y - k)^2 = r^2`, centre `(h, k)`, radius `r`.

### Explanation
It is the distance formula rearranged: every point on the circle is `r` away from the centre. Note the same inside-the-bracket sign flip as parabolas, and that the right-hand side is `r^2`, not `r`.

### Example
`(x - 3)^2 + (y + 2)^2 = 25` is centred at `(3, -2)` with radius **5**. Centred at the origin it simplifies to `x^2 + y^2 = r^2`.

## Does an equation describe a circle?
covers: 99

### Answer
It needs `x^2` and `y^2` added together **with equal coefficients**. Equal coefficients → circle; unequal → ellipse; a minus sign → hyperbola.

### Explanation
Equal coefficients mean the curve stretches by the same amount in both directions, which is what makes it round.

### Example
`3x^2 + 3y^2 = 27` → divide by 3 → `x^2 + y^2 = 9`, a circle of radius 3. `4x^2 + 9y^2 = 36` is an ellipse. `x^2 - y^2 = 9` is neither.

### Watch out
Equal coefficients are required, not coefficients of 1 — divide through before reading off the radius.

## Reflecting a point across an axis, or the origin?
covers: 100

### Answer
Across the x-axis: `(x, -y)`. Across the y-axis: `(-x, y)`. Through the origin: `(-x, -y)`. The coordinate that flips is the one measuring distance from that axis.

### Explanation
Ask what stays the same: reflecting in the x-axis keeps your horizontal position, so `x` is untouched.

The same rules apply to whole shapes: reflect each vertex and rejoin them. Reflection preserves lengths and angles, so the image is congruent to the original.

### Example
`(2, 3)` → x-axis: `(2, -3)`; y-axis: `(-2, 3)`; origin: `(-2, -3)`. Reflecting in both axes in turn is the same as reflecting through the origin.

## Reflecting `(x, y)` across the vertical line `x = k`?
covers: 101

### Answer
`(2k - x, y)` — `y` unchanged.

### Explanation
Rather than memorising it, step the distance twice: from `x` to `k` is `k - x`, so the image sits at `k + (k - x) = 2k - x`.

### Example
Reflect `(2, 3)` across `x = 5`. The point is 3 left of the line, so the image is 3 right: `(8, 3)`. Formula agrees: `2(5) - 2 = 8`.

Another: reflect `(-1, 4)` across `x = 2`. It is 3 units left, so the image is 3 right, at `(5, 4)` — and `2(2) - (-1) = 5` ✓.

## Reflecting `(x, y)` across the horizontal line `y = k`?
covers: 102

### Answer
`(x, 2k - y)` — `x` unchanged.

### Explanation
The mirror image of the previous rule; setting `k = 0` recovers the x-axis rule `(x, -y)`.

### Example
Reflect `(2, 3)` across `y = 1`. The point is 2 above, so the image is 2 below: `(2, -1)`. Formula: `2(1) - 3 = -1` ✓.

Another: reflect `(6, -2)` across `y = 3`. It is 5 below, so the image is 5 above, at `(6, 8)` — and `2(3) - (-2) = 8` ✓.

## Reflecting `(x, y)` across the line `y = x`?
covers: 103

### Answer
Swap the coordinates: `(y, x)`.

### Explanation
`y = x` is the diagonal where the coordinates are equal, so reflecting in it exchanges the roles of horizontal and vertical. This is also why an inverse function's graph is the original reflected in `y = x`.

### Example
`(2, 3)` → `(3, 2)`. Across `y = -x` instead it becomes `(-y, -x)`, so `(2, 3)` → `(-3, -2)`.

So the point `(0, 5)` on the y-axis lands on `(5, 0)` on the x-axis, and any point already on `y = x` stays put.

