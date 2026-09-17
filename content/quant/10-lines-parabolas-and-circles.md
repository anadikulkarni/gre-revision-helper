# Lines, Parabolas & Circles

## What the intercepts tell you about a line
covers: 96

The signs of a line's two intercepts are decided by its slope and whether it passes through the origin, and questions exploit that constantly.

A line through the origin has both intercepts equal to 0, whatever its slope. A horizontal line (slope 0) has only a y-intercept, which can sit anywhere. For a line **not** through the origin: a positive slope forces one intercept positive and the other negative, so their **product is negative**; a negative slope puts both intercepts on the same side, so their **product is positive**.

### Example
`y = 2x - 6` (positive slope): y-intercept -6, x-intercept 3, product -18 — negative, as predicted. `y = -2x + 6` (negative slope): y-intercept 6, x-intercept 3, product 18 — positive.

### Watch out
A vertical line has no slope at all (undefined, not zero) and no y-intercept unless it *is* the y-axis.

## Slopes of perpendicular lines
covers: 97

Perpendicular lines have slopes that are negative reciprocals: if one has slope `m`, the other has slope `-1/m`, and their product is always -1. Parallel lines, by contrast, have equal slopes.

### Example
A line with slope 2/3 is perpendicular to one with slope -3/2, and `(2/3)(-3/2) = -1` ✓. So the line perpendicular to `y = 4x + 1` through the origin is `y = -x/4`.

### Watch out
Horizontal and vertical lines are perpendicular to each other, but the rule fails numerically because `-1/0` is undefined. Treat that pair as a special case.

## Parabolas from perfect squares
covers: 90

A quadratic that is a perfect square, like `y = (x - 3)^2`, touches the x-axis at exactly one point rather than crossing it. That single point is both the root and the vertex — the minimum of the curve if it opens upward, the maximum if it opens downward.

This is the graphical face of "discriminant = 0, one solution".

### Example
`y = (x - 3)^2` has its only root at `x = 3`, and the vertex sits at `(3, 0)`. `y = -(x + 2)^2` opens downward with its maximum at `(-2, 0)`.

## Horizontal shifts of a parabola
covers: 91, 92

Changing `x` inside the bracket slides the curve sideways, and it moves the **opposite** way to the sign you see. `y = (x - h)^2` shifts `h` units **right**; `y = (x + h)^2` shifts `h` units **left**.

The reason is that the vertex sits wherever the bracket equals zero: in `(x - 3)^2` that is `x = +3`.

### Example
`y = (x - 4)^2` is the basic parabola moved 4 right, with vertex `(4, 0)`. `y = (x + 4)^2` is moved 4 left, with vertex `(-4, 0)`.

### Watch out
This inside-the-bracket sign flip is the single most common graphing error. Solve "bracket = 0" every time rather than trusting the sign.

## Vertical shifts of a parabola
covers: 93, 94

Changing the constant *outside* the square moves the curve up or down, and this time the direction matches the sign. `y = x^2 + k` shifts `k` up; `y = x^2 - k` shifts `k` down.

### Example
`y = x^2 + 3` has its vertex at `(0, 3)` and never touches the x-axis. `y = x^2 - 3` has its vertex at `(0, -3)` and crosses at `x = ±sqrt(3)`. Combining both kinds of shift, `y = (x - 2)^2 + 5` has vertex `(2, 5)`.

## Graphing a quadratic by completing the square
covers: 95

Any quadratic can be rewritten as `y = (x - h)^2 + k`, and in that vertex form the graph is simply the basic parabola moved `h` right and `k` up. Completing the square is therefore also a graphing tool: it converts an unreadable expression into a vertex you can plot immediately.

### Example
`y = x^2 - 4x - 6`. Half of -4 is -2, squared is 4, so `y = (x^2 - 4x + 4) - 4 - 6 = (x - 2)^2 - 10`. The vertex is `(2, -10)`, the minimum value is -10, and the y-intercept is still -6 (set `x = 0`).

### Watch out
Whatever you add inside the bracket must be subtracted outside it, or you have changed the function.

## The equation of a circle
covers: 98

A circle of radius `r` centred at `(h, k)` is the set of points at distance `r` from the centre, which the distance formula turns into

`(x - h)^2 + (y - k)^2 = r^2`

Note the same inside-the-bracket sign flip as parabolas: `(x - 3)` means the centre is at `x = +3`. And the right-hand side is `r^2`, not `r`.

### Example
`(x - 3)^2 + (y + 2)^2 = 25` is a circle centred at `(3, -2)` with radius 5. A circle centred at the origin simplifies to `x^2 + y^2 = r^2`.

## Recognising a circle from its equation
covers: 99

If an equation contains both `x^2` and `y^2` added together, it is an ellipse of some kind. It is specifically a **circle** when the coefficients of `x^2` and `y^2` are equal — equal coefficients mean the curve stretches by the same amount in both directions.

### Example
`3x^2 + 3y^2 = 27` is a circle: divide by 3 to get `x^2 + y^2 = 9`, radius 3. `4x^2 + 9y^2 = 36` is an ellipse, since 4 ≠ 9. And `x^2 - y^2 = 9` is neither — a minus sign makes it a hyperbola.

### Watch out
Equal coefficients are required, not coefficients of 1. Divide through before reading off the radius.
