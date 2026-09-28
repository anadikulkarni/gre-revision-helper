# Coordinate Geometry & Angles

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

## Rotating `(x, y)` 90° anticlockwise about the origin?
covers: 104

### Answer
`(-y, x)` — swap, then negate the new first coordinate.

### Explanation
Check any rotation rule with an easy point instead of trusting memory: `(1, 0)` sits on the positive x-axis and a quarter turn anticlockwise must take it to `(0, 1)`, which this rule does.

Rotations preserve distance from the origin, so a point 5 units out stays 5 units out — a quick sanity check on any answer.

### Example
`(2, 3)` → `(-3, 2)`, moving from the first quadrant into the second — exactly what an anticlockwise quarter turn should do.

## Rotating `(x, y)` 90° clockwise about the origin?
covers: 105

### Answer
`(y, -x)` — swap, then negate the new second coordinate.

### Explanation
The mirror of the anticlockwise rule. Three anticlockwise turns equal one clockwise turn, which is a handy check for 270° questions.

Clockwise by 90° is the same as anticlockwise by 270°, and doing either four times returns you to the start. If a question rotates by 450°, subtract 360° first.

### Example
`(2, 3)` → `(3, -2)`, first quadrant to fourth. Test with `(1, 0)`: it should land on `(0, -1)` ✓.

Rotating `(0, 4)` clockwise gives `(4, 0)`: the point travels from the positive y-axis to the positive x-axis ✓.

## Rotating `(x, y)` 180° about the origin?
covers: 106

### Answer
`(-x, -y)` — identical to reflecting through the origin, and the direction of rotation no longer matters.

### Explanation
Half a turn sends every point to the diametrically opposite side.

Because it equals reflection through the origin, a 180° rotation is the only rotation that is also a reflection — which is why questions can describe the same transformation in two ways.

### Example
`(2, 3)` → `(-2, -3)`, first quadrant to third. A 270° anticlockwise turn equals 90° clockwise, so it would give `(3, -2)`.

A shape with 180° rotational symmetry, such as a parallelogram, maps onto itself — its centre is the point you rotate about.

## Complementary and supplementary angles?
covers: 107

### Answer
**Complementary** add to 90°, **supplementary** add to 180°. C before S, 90 before 180.

### Explanation
Supplementary pairs appear constantly because angles on a straight line total 180°. In any right triangle the two non-right angles are complementary.

Two more facts close most diagram questions: angles on a straight line sum to 180°, and angles around a point sum to 360°. Vertical (opposite) angles are always equal.

### Example
The complement of 35° is 55°; its supplement is 145°.

If two angles on a line are `3x` and `2x`, then `5x = 180`, so they are 108° and 72°. In a right triangle with one angle 35°, the third is 55°.

## Two parallel lines cut by a transversal — which angles are equal?
covers: new

### Answer
Only **two** values appear, and every angle is one or the other. Corresponding, alternate interior and alternate exterior angles are **equal**; co-interior (same-side) angles are **supplementary**. Vertical (opposite) angles are always equal, parallel or not.

### Explanation
Rather than memorising names, look at the picture: all the "acute-looking" angles are equal to each other, all the "obtuse-looking" ones are equal to each other, and one of each pair adds to 180°.

### Example
If one angle is 70°, then every angle in the figure is 70° or 110°. Angles around a point total 360°, and angles on a line total 180° — those two facts close most diagram questions.

## Sum of the interior angles of an `n`-sided polygon?
covers: 108

### Answer
`(n - 2) x 180°`. For a **regular** polygon, divide that by `n` for one angle.

### Explanation
Diagonals from a single vertex cut the polygon into `n - 2` triangles, each worth 180°.

The formula also runs backwards: given the angle total, `n = total/180 + 2`. And for a *regular* polygon each interior angle is `180 - 360/n`, which is often the faster route.

### Example
Hexagon: `(6-2) x 180 = 720°`, so a regular hexagon has angles of `720/6 = 120°`. A pentagon totals 540°, giving 108° each.

A polygon whose interior angles sum to 1,080° has `1080/180 + 2 = 8` sides. A regular decagon has angles of `180 - 36 = 144°`.

## Sum of the exterior angles of any polygon?
covers: 109

### Answer
Always **360°**, whatever the number of sides. For a regular polygon each exterior angle is `360/n`.

### Explanation
Walking once round the polygon turns you through one full revolution, and at each corner you turn by the exterior angle.

### Example
Regular hexagon: each exterior angle is `360/6 = 60°`, so each interior angle is `180 - 60 = 120°` ✓. If a regular polygon has exterior angles of 24°, it has `360/24 = 15` sides.

A regular polygon with interior angles of 150° has exterior angles of 30°, so it has 12 sides.

## What makes a polygon regular?
covers: 110

### Answer
All sides equal **and** all angles equal. Both conditions are required.

### Explanation
Regularity is what lets you divide the angle total by `n`, and it is the condition behind the maximum-area results later.

For a regular polygon everything follows from `n`: each interior angle is `180 - 360/n`, each exterior angle is `360/n`, and the number of diagonals is `n(n-3)/2`.

### Example
A regular octagon has angles of 135°. A rhombus has equal sides but unequal angles; a rectangle has equal angles but unequal sides — neither is regular. Only the square is both.

A hexagon has `6(3)/2 = 9` diagonals; a pentagon has 5.

## The quadrilateral family — how do they nest?
covers: 111

### Answer
- **Parallelogram**: two pairs of parallel sides; opposite sides and angles equal; diagonals bisect each other.
- **Rhombus**: parallelogram with four equal sides.
- **Rectangle**: parallelogram with four right angles.
- **Square**: both a rhombus and a rectangle.
- **Trapezoid**: exactly one pair of parallel sides, so not a parallelogram.

### Explanation
The hierarchy answers "must be true" questions directly: every square is a rectangle, but most rectangles are not squares.

### Example
"A quadrilateral with four equal sides" could be a square or a non-square rhombus — ambiguous enough to make a comparison question answer D.

## What does a trapezoid actually guarantee?
covers: 112

### Answer
Only that the two angles on the same leg add to **180°**. All four sides and all four angles can otherwise be different.

### Explanation
Those co-interior angles are supplementary because the other two sides are parallel. Symmetry is not implied — only an *isosceles* trapezoid has equal legs and equal base angles, and the question must say so.

### Example
A base angle of 70° forces 110° directly above it on the same leg. The other leg could carry 50° and 130°, a completely different pair.

## Inscribed versus circumscribed?
covers: 113

### Answer
**Inscribed** is drawn inside, **circumscribed** is drawn around — and in both cases every vertex of the inner shape must touch the outer shape.

### Explanation
The touching condition is what turns the words into measurements: a square inscribed in a circle has its **diagonal** equal to the diameter; a circle inscribed in a square has its **diameter** equal to the side.

### Example
Square inscribed in a circle of radius 5: diagonal 10, so side `10/sqrt(2) = 5sqrt(2)` and area 50. Circle inscribed in a square of side 10: radius 5, area `25pi`.

## In a triangle, how do angles and opposite sides relate?
covers: 114

### Answer
Largest angle faces the longest side, smallest angle faces the shortest side — and the ordering works both ways.

### Explanation
Knowing the order of the angles gives you the order of the sides for free, which is often all a comparison question needs.

Two immediate corollaries: equal angles face equal sides (so an isosceles triangle's base angles are equal), and in a right triangle the hypotenuse is always the longest side because 90° is the largest angle.

### Example
In a 30-60-90 triangle the shortest side faces the 30° and the hypotenuse faces the 90°. If `angle A > angle B`, then side `a` (opposite A) is longer than side `b`.

A triangle with angles 50°, 60°, 70° has its sides in that same order of size, so the side opposite the 50° is the shortest.
