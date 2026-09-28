# Triangles, Area & Solids

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

## Circumference and area of a circle?
covers: new

### Answer
`circumference = 2 pi r = pi d`, `area = pi r^2`. Radius is half the diameter.

### Explanation
Nearly every circle question is "find `r` first". Whatever you are given — area, circumference, a chord, an inscribed square — convert it to the radius and the rest follows.

Scaling: doubling the radius doubles the circumference but **quadruples** the area.

### Example
Radius 6: circumference `12pi ≈ 37.7`, area `36pi ≈ 113`. Given an area of `49pi`, the radius is 7 and the circumference is `14pi`.

### Watch out
Read whether you are given radius or diameter. Using `d` where the formula wants `r` doubles or quadruples the answer.

## Arc length and sector area for a central angle of `n` degrees?
covers: new

### Answer
Take that fraction of the whole circle:
`arc = (n/360) x 2 pi r` and `sector area = (n/360) x pi r^2`.

### Explanation
A sector is a slice of pizza: the central angle tells you what fraction of the full 360° you have, and both the boundary and the area scale by that same fraction.

### Example
Radius 6, central angle 60°: that is `1/6` of the circle, so the arc is `(1/6)(12pi) = 2pi` and the sector area is `(1/6)(36pi) = 6pi`. Backwards: an arc of `3pi` on a radius-6 circle is `3pi/12pi = 1/4` of the circle, so the angle is 90°.

### Watch out
Arc length is a distance and sector area is an area — do not use one where the other is asked.

## Inscribed angles, and the angle in a semicircle?
covers: new

### Answer
An inscribed angle is **half** the central angle standing on the same arc. So an angle inscribed in a semicircle (standing on a diameter) is always **90°**.

### Explanation
The semicircle case is the one the GRE uses most: any triangle with the diameter as one side and its third vertex on the circle is right-angled at that vertex.

### Example
A central angle of 80° gives an inscribed angle of 40° on the same arc. And if `AB` is a diameter and `C` is anywhere else on the circle, `angle ACB = 90°`, so `AC^2 + BC^2 = AB^2`.

## Area of a regular polygon?
covers: 125

### Answer
`area = (n x s x a)/2`, where `a` is the **apothem** — the perpendicular distance from the centre to the middle of a side. Since `n x s` is the perimeter, this is "half perimeter times apothem".

### Explanation
The polygon splits into `n` identical triangles, each with base `s` and height `a`.

### Example
Regular hexagon of side 6: apothem `3sqrt(3) ≈ 5.196`, so area `= (6 x 6 x 5.196)/2 ≈ 93.5`. Cross-check with six equilateral triangles: `6 x 9sqrt(3) = 54sqrt(3) ≈ 93.5` ✓.

## A regular hexagon inscribed in a circle — how do side and radius compare?
covers: 127

### Answer
`s = r`, exactly. Fewer sides → `s > r` (a square gives `s = r sqrt(2)`); more sides → `s < r`.

### Explanation
The hexagon splits into six equilateral triangles meeting at the centre, each with every side equal to the radius.

It makes several figures computable at a glance: the hexagon's perimeter is `6r`, its area is six equilateral triangles of side `r`, and its longest diagonal is the circle's diameter `2r`.

### Example
Hexagon in a circle of radius 6: sides 6, perimeter 36, area `54sqrt(3) ≈ 93.5`. The circle's area is `36pi ≈ 113`, so the hexagon fills about 83% of it.

## Same perimeter, different shapes — which has the most area?
covers: 126, 128

### Answer
The most **regular** one, and the further from regular, the less area. Across different side counts, more sides is better, with the circle the overall winner.

### Explanation
Stretching a shape while keeping its perimeter loses area fast, which is what makes these comparison questions answerable without computing anything.

### Example
Perimeter 40: a 10x10 square gives 100, a 15x5 rectangle 75, a 19x1 rectangle 19. A circle of circumference 40 has area ≈127, beating every polygon.

### Watch out
This is about a **fixed perimeter**. With a fixed area the comparison reverses.

## Volume and surface area of a rectangular solid and a cube?
covers: new

### Answer
Box: `volume = lwh`, `surface area = 2(lw + lh + wh)`. Cube of side `s`: `volume = s^3`, `surface area = 6s^2`.

### Explanation
A box has three pairs of identical faces, which is where the 2 and the three products come from. For a cube all six faces match.

Scaling: double every edge and the volume goes up **8 times**, the surface area **4 times**.

### Example
A 3x4x5 box: volume 60, surface area `2(12 + 15 + 20) = 94`. A cube of side 4: volume 64, surface area 96.

## Volume and surface area of a cylinder?
covers: 129

### Answer
`volume = pi r^2 h`. `surface area = 2 pi r^2 + 2 pi r h` — two circular ends plus the curved side.

### Explanation
The curved side unrolls into a rectangle of height `h` and width equal to the circumference `2 pi r`, which is where the second term comes from.

### Example
Radius 3, height 10: volume `= 90pi ≈ 283`; surface area `= 18pi + 60pi = 78pi ≈ 245`.

### Watch out
Radius appears squared in the volume, so changing it has an outsized effect: doubling `r` quadruples the volume, while doubling `h` only doubles it.

## Same volume, different shapes — which has the least surface area?
covers: 130

### Answer
The most **regular** one. Elongate a solid and the surface area climbs while the volume stays put. The sphere wins overall; among boxes, the cube.

### Explanation
The three-dimensional partner of the perimeter rule, and it is tested the same way — as a comparison you answer by reasoning, not calculating.

### Example
Volume 64: a 4x4x4 cube has surface area 96; a 16x2x2 box has the same volume but surface area `2(32 + 32 + 4) = 136`. A sphere of volume 64 has about 77.

## What is the longest straight line that fits inside a box?
covers: 131

### Answer
The **space diagonal** — corner to diametrically opposite corner, crossing length, width and height at once. Not a face diagonal.

### Explanation
This is the "longest rod that fits" question. The two furthest-apart points of a box are opposite corners, so both the width and the depth get "diagonalled".

### Example
In a room, the longest line runs from a bottom corner to the opposite top corner. In a 3x4x12 box the best face diagonal is only 5, while the true longest is 13.

## Formula for the diagonal of a rectangular solid?
covers: 132

### Answer
`d = sqrt(l^2 + w^2 + h^2)`. For a cube of side `s` it collapses to `s sqrt(3)`.

### Explanation
Pythagoras applied twice: once across the base to get the floor diagonal, then again vertically using that diagonal and the height.

It is also the 3-D distance formula: the diagonal is the distance between opposite corners, exactly as `sqrt(dx^2 + dy^2 + dz^2)` measures distance in space.

### Example
3x4x12 box: `sqrt(9 + 16 + 144) = sqrt(169) = 13`. Cube of side 5: `5sqrt(3) ≈ 8.66`.

A 6x6x7 box: `sqrt(36 + 36 + 49) = sqrt(121) = 11`. And "will a 12-inch rod fit in a 4x6x9 box?" → `sqrt(16+36+81) = sqrt(133) ≈ 11.5`, so no.

## How many small boxes fit inside a big one?
covers: 133

### Answer
Divide **per dimension** and round each down, then multiply. Dividing the volumes only works when every dimension divides exactly.

### Explanation
Volume division silently assumes the leftover slivers can be reassembled, which they cannot.

### Example
2x2x2 cubes into a 10x10x10 box: everything divides, so `1000/8 = 125`, matching `5 x 5 x 5`. But 3x3x3 cubes: volume division suggests 37, while per dimension you fit `10/3 → 3`, giving `3 x 3 x 3 = 27`.

### Watch out
You may be allowed to rotate the small box. When the dimensions differ, test the orientations — one often fits noticeably more.
