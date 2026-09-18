# Triangles & Area

## Given two sides of a triangle, what can the third be?
covers: 115

### Answer
Strictly between their **difference** and their **sum**: `|a - b| < c < a + b`. Any two sides must together exceed the third.

### Explanation
Applied to all three pairs, the triangle inequality pins the missing side into a range — and questions usually ask for the number of integer possibilities.

### Example
Sides 7 and 10: `3 < x < 17`, so an integer third side has **13** possibilities (4 through 16).

### Watch out
The inequality is strict. Sides 3, 7 and 10 make a flat line, not a triangle.

## What proves two triangles congruent?
covers: 116

### Answer
**SSS**, **SAS** (angle *between* the sides), **ASA**, or **AAS**. Notably **SSA does not work** — two different triangles usually fit.

### Explanation
Congruent means identical in size and shape, so three well-chosen pieces pin it down. The exception matters: with two sides and a non-included angle, the third side can swing to two positions.

### Example
Two triangles with sides 5 and 7 and the 40° angle between them are congruent by SAS. With the 40° opposite the 5 instead, nothing is guaranteed.

## What do similar triangles give you?
covers: 120

### Answer
Equal angles and all corresponding lengths in one fixed ratio. **Two** equal angles are enough to prove similarity. Lengths scale by `k`; **areas scale by `k^2`**.

### Explanation
Similar means same shape, different scale — every length (sides, heights, perimeters) uses the same factor, but area uses its square. That squared factor is the part questions target.

### Example
Two triangles with angles 40-60-80; the first has its 40°-side of length 6, the second 9, a ratio of 3:2. If the first has area 20, the second has area `20 x (3/2)^2 = 45`, not 30.

### Watch out
Match sides by the angles they face, not by the order they are written.

## Pythagorean theorem?
covers: new

### Answer
`a^2 + b^2 = c^2`, with `c` the hypotenuse — right triangles only.

### Explanation
It is also the converse: if the three sides satisfy it, the triangle *is* right-angled. And it is the engine behind the distance formula and the diagonal of a box.

### Example
Legs 6 and 8: `36 + 64 = 100`, so `c = 10`. Backwards, hypotenuse 13 with one leg 5: `b^2 = 169 - 25 = 144`, so `b = 12`.

### Watch out
The hypotenuse is always the longest side and always faces the right angle. Plugging it in as a leg is the standard error.

## The 30-60-90 triangle — side ratios?
covers: 117

### Answer
`1 : sqrt(3) : 2`. The short side (`x`) faces 30°, the hypotenuse (`2x`) faces 90°, the middle side (`x sqrt(3)`) faces 60°.

### Explanation
It is half an equilateral triangle cut down the middle, which is also where the height of an equilateral triangle comes from.

### Example
Hypotenuse 10 → short side 5, long leg `5sqrt(3) ≈ 8.66`. So an equilateral triangle of side 10 has height `5sqrt(3)`.

### Watch out
Match sides to angles, not to their position in the picture. Given the **long leg** as 6, the short side is `6/sqrt(3) = 2sqrt(3)`, not 3.

## The 45-45-90 triangle — side ratios?
covers: 118

### Answer
`1 : 1 : sqrt(2)`. Two equal legs, hypotenuse `sqrt(2)` times as long.

### Explanation
It is a square cut along its diagonal, which is why a square of side `s` has diagonal `s sqrt(2)`.

It appears whenever a square's diagonal shows up, and in isosceles right triangles hidden inside larger figures.

### Example
Legs 5 → hypotenuse `5sqrt(2) ≈ 7.07`. Backwards: hypotenuse 10 → legs `10/sqrt(2) = 5sqrt(2)`. So a square with diagonal 10 has area 50.

A square of side 8 has diagonal `8sqrt(2) ≈ 11.3`. A 45-45-90 triangle with hypotenuse `6sqrt(2)` has legs of 6 and area 18.

## A triangle with awkward angles like 30-105-45 — what do you do?
covers: 119

### Answer
Drop a perpendicular to split it into two special right triangles. 105° splits into 45 + 60; 75° splits into 45 + 30.

### Explanation
Once the figure is two known triangles you can use their ratios on both halves and add the areas. Look for angles that decompose into 30/45/60.

### Example
For 30-105-45 with one side given, the height from the 105° vertex creates a 30-60-90 and a 45-45-90 sharing that height. Find the height, use each ratio for its base piece, then add the two areas.

### Watch out
The perpendicular must land inside the triangle for the areas to add. In an obtuse triangle it may fall outside, and you subtract instead.

## Pythagorean triples worth recognising?
covers: 121

### Answer
**3-4-5**, **5-12-13**, **8-15-17**, **7-24-25** — and every multiple of them (6-8-10, 9-12-15, …).

### Explanation
Recognition saves a square root, and recognising a near-miss saves you from assuming a right angle that is not there.

### Example
Legs 8 and 15 → hypotenuse 17 instantly. Legs 9 and 12 → 15, since that is `3 x (3-4-5)`. But sides 5, 12 and 14 are **not** right-angled, however familiar the 5 and 12 look.

### Watch out
The largest number must be the hypotenuse.

## Area of a triangle?
covers: new

### Answer
`area = (1/2) x base x height`, where the height is **perpendicular** to the chosen base.

### Explanation
Any side can be the base, as long as you use the height perpendicular to *that* side. In a right triangle the two legs are base and height already.

### Example
Base 10, height 6 → area 30. A right triangle with legs 6 and 8 has area 24 (the hypotenuse never enters). Two triangles with the same base and the same height have equal areas, however different they look.

### Watch out
In an obtuse triangle the height can fall outside the triangle — it is still the perpendicular distance, not a side.

## Area and perimeter of a rectangle and a square?
covers: new

### Answer
Rectangle: `area = lw`, `perimeter = 2(l + w)`. Square of side `s`: `area = s^2`, `perimeter = 4s`, `diagonal = s sqrt(2)`.

### Explanation
The pairing that questions exploit: a fixed perimeter leaves the area free to vary wildly, and a fixed area leaves the perimeter free — the square is the extreme in both cases.

### Example
Perimeter 40: a 10x10 square has area 100, a 15x5 rectangle 75, a 19x1 rectangle just 19. Conversely, area 36 can be a 6x6 square (perimeter 24) or a 36x1 rectangle (perimeter 74).

## Area of an equilateral triangle of side `s`?
covers: 122

### Answer
`(sqrt(3) x s^2)/4`.

### Explanation
It follows from the 30-60-90 ratios: the height is `s sqrt(3)/2`, and area is half base times height.

Because it depends on `s^2`, the ratio of the areas of two equilateral triangles is the square of the ratio of their sides. And six of them make a regular hexagon, which is how hexagon areas are computed.

### Example
Side 6 → `(sqrt(3) x 36)/4 = 9sqrt(3) ≈ 15.6`. Doubling the side to 12 **quadruples** the area, since it depends on `s^2`.

Given an area of `25sqrt(3)`, solve `(sqrt(3)s^2)/4 = 25sqrt(3)` → `s^2 = 100` → `s = 10`. A regular hexagon of side 10 then has area `6 x 25sqrt(3) = 150sqrt(3)`.

## Area of a parallelogram?
covers: 123

### Answer
`base x height`, where the height is the **perpendicular** distance between the parallel sides — not the slanted side.

### Explanation
A parallelogram is a rectangle pushed over, and pushing it over changes neither base nor height.

### Example
Base 10 with a slant side of 6 leaning at 30°: height `= 6 sin(30°) = 3`, so the area is **30**, not 60.

### Watch out
Using the slanted side as the height always overestimates — it is the most common area error.

## Area of a trapezoid?
covers: 124

### Answer
`((base1 + base2)/2) x height` — the average of the parallel sides times the distance between them.

### Explanation
You are finding the width of the "average" rectangle. If the two bases were equal it would be a parallelogram, and the formula collapses to base times height.

It also runs backwards to find a missing base or height, which is the usual exam form: substitute what you know and solve.

### Example
Parallel sides 8 and 12, height 5 → `10 x 5 = 50`.

A trapezoid of area 60 with bases 7 and 13 has height `60 = 10h`, so `h = 6`.

