# Circles & Solids

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
