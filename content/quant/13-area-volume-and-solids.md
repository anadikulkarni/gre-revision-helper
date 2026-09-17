# Area, Volume & Solids

## Area of an equilateral triangle
covers: 122

For side length `s`, the area is

`area = (sqrt(3) x s^2)/4`

It follows from the 30-60-90 ratios: the height of an equilateral triangle is `s sqrt(3)/2`, and area is half base times height.

### Example
An equilateral triangle of side 6 has area `(sqrt(3) x 36)/4 = 9sqrt(3) ≈ 15.6`. Doubling the side to 12 quadruples the area to `36sqrt(3)`, because area depends on `s^2`.

## Area of a parallelogram
covers: 123

`area = base x height`, where the height is the **perpendicular** distance between the two parallel sides — not the length of the slanted side. A parallelogram is a rectangle that has been pushed over, and pushing it over does not change base or height.

### Example
A parallelogram with base 10 and slant side 6 leaning at 30° has height `6 x sin(30°) = 3`, so its area is 30, not 60. If the question gives you the height directly as 4, the area is simply 40.

### Watch out
Using the slanted side as the height is the classic error, and it always overestimates.

## Area of a trapezoid
covers: 124

`area = ((base1 + base2)/2) x height`: the average of the two parallel sides times the perpendicular distance between them. You are really finding the width of the "average" rectangle.

### Example
A trapezoid with parallel sides 8 and 12 and height 5 has area `((8 + 12)/2) x 5 = 10 x 5 = 50`. If the two bases were equal it would be a parallelogram, and the formula would collapse to base times height.

## Area of a regular polygon
covers: 125

With `n` sides of length `s` and apothem `a` (the perpendicular distance from the centre to the middle of a side):

`area = (n x s x a)/2`

The polygon splits into `n` identical triangles, each with base `s` and height `a`. Since `n x s` is the perimeter, this is also "half perimeter times apothem".

### Example
A regular hexagon of side 6 has apothem `3sqrt(3) ≈ 5.196`, so its area is `(6 x 6 x 5.196)/2 ≈ 93.5`. Cross-check with six equilateral triangles of side 6: `6 x 9sqrt(3) = 54sqrt(3) ≈ 93.5` ✓.

## For a fixed perimeter, regular is biggest
covers: 126, 128

Among all shapes with the same perimeter and the same number of sides, the regular one encloses the most area, and the further from regular the shape gets, the smaller its area. Pushing a square into a long thin rectangle keeps the perimeter but loses area fast.

Across different numbers of sides the same logic continues: more sides means more area for the same perimeter, with the circle as the winner.

### Example
Perimeter 40: a 10 x 10 square gives area 100; a 15 x 5 rectangle gives 75; a 19 x 1 rectangle gives 19. A circle with circumference 40 has radius `40/(2pi) ≈ 6.37` and area ≈ 127, beating every polygon.

### Watch out
This is about a *fixed perimeter*. Two shapes with the same area can have wildly different perimeters, and the comparison reverses.

## A regular hexagon inscribed in a circle
covers: 127

For a regular hexagon inscribed in a circle, the side equals the radius: `s = r`. The hexagon splits into six equilateral triangles meeting at the centre, each with all sides equal to the radius.

The pattern around it is worth knowing: with fewer sides the side is longer than the radius (a square gives `s = r sqrt(2)`), and with more sides the side is shorter.

### Example
A regular hexagon inscribed in a circle of radius 6 has sides of 6, perimeter 36, and area `6 x (sqrt(3) x 36/4) = 54sqrt(3) ≈ 93.5`. The circle's area is `36pi ≈ 113`, so the hexagon fills about 83% of it.

## Cylinder volume and surface area
covers: 129

`volume = pi r^2 h` — the circular base area times the height.

`surface area = 2 pi r^2 + 2 pi r h` — the two circular ends plus the curved side, which unrolls into a rectangle of height `h` and width equal to the circumference `2 pi r`.

### Example
A cylinder with radius 3 and height 10: volume `= pi x 9 x 10 = 90pi ≈ 283`. Surface area `= 2pi(9) + 2pi(3)(10) = 18pi + 60pi = 78pi ≈ 245`.

### Watch out
Doubling the radius quadruples the volume but doubling the height only doubles it — radius appears squared, so questions that change the radius have outsized effects.

## For a fixed volume, regular means less surface area
covers: 130

The three-dimensional partner of the perimeter rule: for a given volume, the more regular (more compact) the solid, the smaller its surface area. Stretch a solid into a long thin shape and the surface area climbs while the volume stays put. The sphere is the extreme winner; among boxes, the cube is.

### Example
Volume 64: a 4 x 4 x 4 cube has surface area 96. A 16 x 2 x 2 box has the same volume but surface area `2(32 + 32 + 4) = 136`. A sphere of volume 64 has surface area about 77.

## The longest diagonal of a shape
covers: 131

The longest diagonal joins the two furthest-apart points, which in a box means travelling across the width, the depth **and** the height at once — a corner to its diametrically opposite corner. It is the answer to "what is the longest rod that fits inside".

### Example
In a rectangular room, the longest straight line is not along the floor but from one bottom corner up to the opposite top corner. A face diagonal of a 3 x 4 x 12 box is only 5, while the true longest diagonal is 13.

## Diagonal of a rectangular solid
covers: 132

`diagonal = sqrt(length^2 + width^2 + depth^2)`

It is Pythagoras applied twice: once across the base to get the floor diagonal, then again vertically using that diagonal and the height.

### Example
A 3 x 4 x 12 box: `sqrt(9 + 16 + 144) = sqrt(169) = 13`. For a cube of side `s` the formula collapses to `s sqrt(3)`, so a cube of side 5 has longest diagonal `5sqrt(3) ≈ 8.66`.

## Fitting boxes inside boxes
covers: 133

If the small box's dimensions divide exactly into the big box's, you may simply divide the volumes. If they do **not** divide exactly, that shortcut overcounts, because the leftover slivers cannot be reassembled. Instead work out how many fit along each dimension, round each down, and multiply.

### Example
How many 2 x 2 x 2 cubes fit in a 10 x 10 x 10 box? Everything divides evenly: `1000/8 = 125`, and `5 x 5 x 5 = 125` agrees. Now try 3 x 3 x 3 cubes in the same box: volume division suggests `1000/27 ≈ 37`, but per dimension you fit only `10/3 → 3`, so the true answer is `3 x 3 x 3 = 27`.

### Watch out
You may also be allowed to rotate the small box. If the dimensions differ, test the orientations — one of them often fits noticeably more.
