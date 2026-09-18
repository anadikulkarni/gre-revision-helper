# Rotations, Angles & Polygons

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

