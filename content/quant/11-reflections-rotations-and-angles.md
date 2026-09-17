# Reflections, Rotations & Angles

## Reflecting across the axes and the origin
covers: 100

Reflecting a point across an axis flips the sign of the **other** coordinate — the one measuring distance from that axis. Across the x-axis, `(x, y)` becomes `(x, -y)`; across the y-axis it becomes `(-x, y)`. Reflecting through the origin flips both: `(x, y)` becomes `(-x, -y)`.

Remember which sign changes by asking what stays the same: reflecting in the x-axis keeps you at the same horizontal position, so `x` is untouched.

### Example
`(2, 3)` reflected in the x-axis is `(2, -3)`; in the y-axis it is `(-2, 3)`; through the origin it is `(-2, -3)`. Reflecting in both axes one after the other gives the same result as reflecting through the origin.

## Reflecting across the vertical line x = k
covers: 101

The y-coordinate is unchanged and the x-coordinate lands as far on the other side of `k` as it started on this side:

`(x, y) → (2k - x, y)`

Rather than memorise it, compute the distance to the line and step that far again: from `x` to `k` is `k - x`, so the image is at `k + (k - x) = 2k - x`.

### Example
Reflect `(2, 3)` across `x = 5`. The point is 3 to the left of the line, so the image is 3 to the right, at `x = 8`: `(8, 3)`. The formula agrees: `2(5) - 2 = 8`.

## Reflecting across the horizontal line y = k
covers: 102

The mirror image of the previous rule: the x-coordinate stays put and the y-coordinate reflects through `k`.

`(x, y) → (x, 2k - y)`

### Example
Reflect `(2, 3)` across `y = 1`. The point is 2 above the line, so the image is 2 below, at `y = -1`: `(2, -1)`. The formula: `2(1) - 3 = -1` ✓. Note `y = 0` recovers the x-axis rule, `(x, -y)`.

## Reflecting across the line y = x
covers: 103

Swap the coordinates: `(x, y)` becomes `(y, x)`. The line `y = x` is the diagonal where the two coordinates are equal, and reflecting in it exchanges the roles of horizontal and vertical.

This is also why the graph of an inverse function is the reflection of the original in `y = x`.

### Example
`(2, 3)` reflected in `y = x` is `(3, 2)`. Reflecting in `y = -x` instead gives `(-y, -x)`, so `(2, 3)` would become `(-3, -2)`.

## Rotating 90° anticlockwise about the origin
covers: 104

`(x, y) → (-y, x)`. Swap the coordinates and then negate the new first one.

You can always check a rotation rule with an easy point instead of trusting memory: `(1, 0)` sits on the positive x-axis, and a quarter turn anticlockwise should carry it to `(0, 1)` on the positive y-axis — which the rule does.

### Example
`(2, 3)` rotated 90° anticlockwise becomes `(-3, 2)`. Sketch it: the point moves from the first quadrant into the second, which is what an anticlockwise quarter turn should do.

## Rotating 90° clockwise about the origin
covers: 105

`(x, y) → (y, -x)`. Swap the coordinates and negate the new second one — the mirror of the anticlockwise rule.

### Example
`(2, 3)` rotated 90° clockwise becomes `(3, -2)`, moving from the first quadrant into the fourth. Check with `(1, 0)`: it should land on `(0, -1)`, and it does. Note that three anticlockwise turns equal one clockwise turn.

## Rotating 180° about the origin
covers: 106

`(x, y) → (-x, -y)`, which is identical to reflecting through the origin. Half a turn sends every point to the opposite side, and the direction of rotation no longer matters.

### Example
`(2, 3)` rotated 180° becomes `(-2, -3)`, moving from the first quadrant to the third. A 270° anticlockwise rotation is the same as 90° clockwise, so `(2, 3)` would become `(3, -2)`.

## Complementary and supplementary angles
covers: 107

Two angles are **complementary** if they add to 90° and **supplementary** if they add to 180°. Supplementary pairs turn up constantly because angles on a straight line always sum to 180°, and so do co-interior angles between parallel lines.

The alphabet trick: C comes before S, and 90 comes before 180.

### Example
The complement of 35° is 55°; its supplement is 145°. In a right triangle the two non-right angles are always complementary, since all three must total 180°.

## Interior angles of a polygon
covers: 108

For a polygon with `n` sides the interior angles add up to `(n - 2) x 180°`. Any polygon can be cut into `n - 2` triangles by drawing diagonals from one vertex, and each triangle contributes 180°.

For a **regular** polygon each interior angle is that total divided by `n`.

### Example
A hexagon has `(6 - 2) x 180 = 720°` in total, so a regular hexagon has interior angles of `720/6 = 120°` each. A pentagon totals 540°, giving 108° per angle when regular.

## Exterior angles always total 360°
covers: 109

Whatever the number of sides, one exterior angle at each vertex always sums to 360°. Walking once around the polygon turns you through one full revolution, and the amount you turn at each corner is exactly the exterior angle.

For a regular polygon, each exterior angle is `360/n` — often a faster route to the interior angle, which is its supplement.

### Example
A regular hexagon: each exterior angle is `360/6 = 60°`, so each interior angle is `180 - 60 = 120°`, matching the other formula. If a question says a regular polygon has exterior angles of 24°, then `n = 360/24 = 15` sides.
