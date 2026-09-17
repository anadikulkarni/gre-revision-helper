# Polygons & Triangles

## Regular polygons
covers: 110

A polygon is regular when all its sides are equal **and** all its angles are equal. Equilateral triangles and squares are the familiar cases. Regularity is what lets you divide the angle total by `n` to get a single angle, and it is also the condition behind several maximum-area results later on.

### Example
A regular octagon has 8 equal sides and 8 equal angles of `(8-2) x 180/8 = 135°` each. A rhombus has equal sides but unequal angles, and a rectangle has equal angles but unequal sides — neither is regular; only the square is both.

## The quadrilateral family
covers: 111

They nest inside each other, and knowing the hierarchy answers a lot of "must be true" questions:

- **Parallelogram**: two pairs of parallel sides. Opposite sides and opposite angles are equal; diagonals bisect each other.
- **Rhombus**: a parallelogram with all four sides equal.
- **Rectangle**: a parallelogram with all four angles 90°.
- **Square**: both a rhombus and a rectangle.
- **Trapezoid**: exactly one pair of parallel sides, so it is not a parallelogram at all.

### Example
Every square is a rectangle, but most rectangles are not squares. So "a quadrilateral with four equal sides" could be a square or a non-square rhombus — enough ambiguity to make a comparison question answer D.

## What a trapezoid does and does not guarantee
covers: 112

In a trapezoid all four sides and all four angles can be different; the only structural rule is that the two angles on the same leg (between the parallel sides) add to 180°, because they are co-interior angles across parallel lines.

So do not assume symmetry. Only an *isosceles* trapezoid has equal legs and equal base angles, and the question has to tell you that.

### Example
A trapezoid with parallel sides top and bottom and a base angle of 70° has an angle of 110° directly above it on the same leg. The other leg could carry 50° and 130°, a completely different pair.

## Inscribed and circumscribed
covers: 113

**Inscribed** means drawn inside; **circumscribed** means drawn around the outside. In both cases the touching condition matters: every vertex of the inner shape must sit on the outer shape.

So a square inscribed in a circle has all four corners on the circle, and its diagonal is the circle's diameter. A circle inscribed in a square touches all four sides, and its diameter equals the square's side.

### Example
A square inscribed in a circle of radius 5: the diagonal is the diameter, 10, so the side is `10/sqrt(2) = 5sqrt(2)` and the area is 50. A circle inscribed in a square of side 10 has radius 5 and area `25pi`.

## Bigger angles face bigger sides
covers: 114

In any triangle, the largest angle is opposite the longest side and the smallest angle is opposite the shortest side. The ordering runs both ways, so knowing the order of the angles tells you the order of the sides and vice versa.

### Example
A triangle with angles 30°, 60°, 90° has its shortest side opposite the 30° and its longest (the hypotenuse) opposite the 90°. If a question says `angle A > angle B`, you may conclude that side `a` (opposite A) is longer than side `b` — often all a comparison question needs.

## The triangle inequality
covers: 115

Any two sides of a triangle must together exceed the third. Applied to all three pairs, this pins the missing side into a range: it must be greater than the difference of the other two and less than their sum.

### Example
Two sides are 7 and 10. The third side `x` satisfies `10 - 7 < x < 10 + 7`, so `3 < x < 17`. If `x` must also be an integer, there are 13 possibilities (4 through 16).

### Watch out
The inequality is strict. A "triangle" with sides 3, 7 and 10 is a flat line, not a triangle.

## When two triangles are congruent
covers: 116

Congruent means identical in size and shape. Four combinations of three pieces of information are enough to guarantee it: **SSS** (three sides), **SAS** (two sides and the angle *between* them), **ASA** (two angles and the side between them) and **AAS** (two angles and a side not between them).

The notable exception is **SSA** — two sides and an angle not between them — which does not determine a triangle; there are usually two different triangles that fit.

### Example
Given two triangles with sides 5, 7 and the 40° angle between them, they are congruent by SAS. But given sides 5 and 7 with a 40° angle opposite the 5, two different triangles satisfy the description, so nothing is guaranteed.

## Similar triangles
covers: 120

Similar triangles have the same shape at a different scale: equal angles, and all corresponding lengths in one fixed ratio. Two equal angles are enough to prove similarity (the third follows automatically), which is usually how the GRE sets it up.

Every length scales by the same factor — sides, heights, perimeters. Areas scale by the **square** of that factor.

### Example
Two triangles with angles 40°, 60°, 80°; the first has its 40°-side of length 6, the second 9, a ratio of 3:2. If the first has area 20, the second has area `20 x (3/2)^2 = 45`, not 30.

### Watch out
Match corresponding sides by the angles they sit opposite, not by the order they are written in.

## The 30-60-90 triangle
covers: 117

Its sides are always in the ratio `1 : sqrt(3) : 2`. The shortest side (`x`) faces the 30° angle, the hypotenuse (`2x`) faces the 90°, and the middle side (`x sqrt(3)`) faces the 60°. It is exactly half of an equilateral triangle cut down the middle.

### Example
A 30-60-90 triangle with hypotenuse 10 has a short side of 5 and a long leg of `5sqrt(3) ≈ 8.66`. This also gives the height of an equilateral triangle of side 10: `5sqrt(3)`.

### Watch out
Match sides to angles, not to position in the picture. Given the *long leg* as 6, the short side is `6/sqrt(3) = 2sqrt(3)`, not 3.

## The 45-45-90 triangle
covers: 118

An isosceles right triangle: two equal legs and a hypotenuse `sqrt(2)` times as long, ratio `1 : 1 : sqrt(2)`. It is a square cut along its diagonal, which is why the diagonal of a square with side `s` is `s sqrt(2)`.

### Example
Legs of 5 give a hypotenuse of `5sqrt(2) ≈ 7.07`. Backwards: a hypotenuse of 10 gives legs of `10/sqrt(2) = 5sqrt(2) ≈ 7.07`. So a square with diagonal 10 has side `5sqrt(2)` and area 50.

## Splitting a triangle into special right triangles
covers: 119

When a triangle has awkward angles, drop a perpendicular from a vertex to the opposite side and look for the two special triangles inside it. An angle of 105° splits into 45 + 60, and 75° into 45 + 30 — and suddenly the whole figure is computable with known ratios.

### Example
A triangle with angles 30°, 105°, 45° and one known side. Drop the height from the 105° vertex: it splits into a 30-60-90 and a 45-45-90 sharing that height. Find the height from the known side, use each ratio to get the two base pieces, and add the two areas.

### Watch out
The perpendicular must land inside the triangle for the areas to add. For an obtuse triangle it may fall outside, in which case you subtract instead.

## Pythagorean triples worth memorising
covers: 121

Four sets of whole numbers satisfy `a^2 + b^2 = c^2` often enough to be worth knowing by sight: **3-4-5**, **5-12-13**, **8-15-17** and **7-24-25**. Every multiple of a triple is also a triple, so 6-8-10 and 9-12-15 come free.

Recognising one saves you a square-root calculation, and recognising a *near*-miss saves you from assuming a right angle that is not there.

### Example
A right triangle with legs 8 and 15 has hypotenuse 17 — no calculation needed. Legs of 9 and 12 give 15, since that is `3 x (3-4-5)`. And if a triangle has sides 5, 12 and 14, it is *not* right-angled, however familiar the 5 and 12 look.

### Watch out
The largest number must be the hypotenuse. Sides 3, 4 and 5 make a right triangle; sides 3, 5 and a hypotenuse of 4 are impossible.
