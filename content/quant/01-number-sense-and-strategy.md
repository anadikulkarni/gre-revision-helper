# Number Sense & Strategy

## Always convert units before comparing
covers: 2

A GRE question will happily give you one speed in kilometres per hour and another in metres per second, then ask which is greater. The numbers are not comparable until they are in the same unit, and the test writers know that the fastest way to lose a point is to compare 20 km/h against 8 m/s as if 20 > 8 settled it.

Make converting the first thing you do, not the last. Write the conversion as a fraction that cancels the unit you want to get rid of: to turn 8 m/s into km/h, multiply by `3600 s / 1 hr` and by `1 km / 1000 m`, and the seconds and metres cancel, leaving 28.8 km/h.

### Example
Which is greater: a car at 20 km/h or a runner at 8 m/s? Convert the runner: `8 m/s x 3600 s/hr = 28,800 m/hr = 28.8 km/h`. The runner is faster, even though "20" looks bigger than "8".

### Watch out
The same trap appears with time (minutes vs hours), money (cents vs dollars) and area (cm² vs m²). If a question mentions two different units anywhere, convert before you do anything else.

## Converting squared and cubed units
covers: 1

When you convert an *area* you must square the conversion factor, and when you convert a *volume* you must cube it. A square metre is not 3.28 square feet — it is a square that is 3.28 feet on each side, so it is `3.28^2 = 10.76` square feet. Forgetting this is one of the most common unit mistakes on the test.

The safe way is to write the conversion factor with its unit and raise the whole thing to the power you need: `(1 m / 3.28 ft)^2 = 1 m² / 10.76 ft²`. Then the units tell you whether to multiply or divide.

### Example
How many square metres is 540 square feet, given 3.28 ft per metre? Square the factor first: `3.28^2 = 10.76`. Then `540 / 10.76 ≈ 50.2 square metres`. Dividing by 3.28 instead would have given ≈165, which is more than three times too big.

### Watch out
Cubic units need the cube: 1 m³ = `3.28^3 ≈ 35.3` ft³. The bigger the power, the bigger the error if you skip this step.

## Quantitative Comparison: hunt for equal, then unequal
covers: 3

In a Quantity A / Quantity B question you are not asked for a value, you are asked whether one column is always bigger. That makes answer choice D ("cannot be determined") a genuine target rather than a last resort. The fastest route to D is to find one case where the two quantities are equal and one case where they are not — two cases is all it takes to prove the relationship is not fixed.

Pick your cases deliberately rather than randomly. The values worth trying are 0, 1, a negative number, a fraction between 0 and 1, and a large number, because those are exactly where the usual intuitions break.

### Example
Quantity A: `x^2`. Quantity B: `x`. Try `x = 1`: both are 1, so they can be equal. Try `x = 2`: A is 4, B is 2, so A can be bigger. Two different relationships, so the answer is D. (If the question had said `x > 1`, the answer would be A.)

### Watch out
One case is never enough. Finding that A = B once only rules out "A is always greater"; you still need a second case to choose between C and D.

## Do the least maths you can get away with
covers: 4

Every quantitative comparison and most multiple-choice questions are built so that a full calculation is possible but unnecessary. If you find yourself about to multiply four-digit numbers, stop: there is almost certainly a shortcut. Estimate, compare structure, cancel common factors, or test a convenient number instead.

Comparing is easier than computing. To decide whether `17/33` is bigger than `1/2`, you do not need the decimal — you need to notice that half of 33 is 16.5 and 17 is more than that.

### Example
Which is greater, `47 x 52` or `48 x 51`? No multiplication needed. Both are products of pairs that sum to 99, and for a fixed sum the product is biggest when the two numbers are closest together. 48 and 51 are closer than 47 and 52, so `48 x 51` is greater.

### Watch out
Estimation is only safe when the quantities are far apart. If your estimate makes them look nearly equal, go back and calculate exactly.

## Find the repeating pattern
covers: 5

When a question asks for the 50th term, the 200th digit, or the remainder of a huge power, it is never asking you to grind out 50 steps. It is telling you that the thing repeats. Compute the first four or five cases by hand, spot the cycle length, and then use division to jump to the term you want.

Once you know the cycle length `k`, the position of term `n` inside the cycle is given by the remainder of `n / k`. A remainder of 0 means you have landed on the last item of the cycle, not the first — that off-by-one is where most errors happen.

### Example
What is the 50th term of 7, 4, 1, 7, 4, 1, …? The cycle is (7, 4, 1) with length 3. `50 / 3` leaves remainder 2, so the 50th term is the 2nd item of the cycle: 4.

### Watch out
Always write out enough terms to see the cycle repeat *twice*. Two identical terms in a row is not proof of a cycle.

## The unit digit
covers: 6

The unit digit is the rightmost digit of a number — the ones place. It gets its own section of GRE arithmetic because it behaves independently of everything to its left: when you add or multiply, the unit digit of the answer depends only on the unit digits of the inputs.

That independence is what makes questions about the last digit of `7^100` answerable in seconds. You never need the other 84 digits.

### Example
In 3,472 the unit digit is 2. The unit digit of `3,472 x 1,238` is the unit digit of `2 x 8 = 16`, which is 6 — and you never had to do the full multiplication.

## Floor of a negative number
covers: 7

The floor of a number is the greatest integer that is less than or equal to it, so flooring always moves you *left* on the number line, never right. For positive numbers that feels like "chop off the decimal", which is why negatives catch people out: chopping the decimal off -16.7 gives -16, but -16 is to the *right* of -16.7, so it cannot be the floor.

Say it out loud as "round down, always" and the negatives take care of themselves: the floor of a negative non-integer has a *larger* absolute value than the number itself.

### Example
`floor(16.7) = 16` but `floor(-16.7) = -17`, because -17 is below -16.7 and -16 is above it. Likewise `floor(-3.01) = -4` and `floor(-3) = -3` (integers are already their own floor).

## Quotient and remainder
covers: 8

Dividing one integer by another splits it into a whole-number part and a leftover. If `a` is divided by `b`, the quotient `q` is the whole part and the remainder `r` is what is left, and the three are tied together by one identity worth memorising:

`a = bq + r`, where `0 <= r < b`

That constraint on `r` is the important half. The remainder is never negative and is always strictly less than the divisor, which is why a remainder of 7 when dividing by 6 is impossible — it means you did not take out enough copies of 6.

### Example
`47 / 5`: the quotient is 9 and the remainder is 2, since `47 = 5 x 9 + 2` and `0 <= 2 < 5`. If a question says "n leaves remainder 2 when divided by 5", that means `n = 5q + 2`, so n could be 2, 7, 12, 17, …

### Watch out
A remainder question is usually best answered by writing `n = bq + r` and substituting, not by trying numbers at random.

## Quotient and remainder with negative numbers
covers: 9

The rule `0 <= r < b` also holds when the number being divided is negative, and it forces the quotient to go one step further down than you would expect. Because the remainder must be non-negative, the quotient has to be *smaller* than the naive answer — in absolute terms, one bigger.

Concretely: the quotient of a negative number is `-(1 + |quotient of the positive equivalent|)` whenever the division is not exact.

### Example
`-15 / 9`. It is tempting to say the quotient is -1 with remainder -6, but remainders cannot be negative. Take the quotient down to -2: `-15 = 9 x (-2) + 3`, giving quotient -2 and remainder 3, with `0 <= 3 < 9`. Compare `15 / 9`, where the quotient is 1 and the remainder is 6.

### Watch out
This is the same idea as the floor of a negative number: the quotient *is* `floor(a/b)`, and floors of negatives always round away from zero.

## Remainders add, subtract and multiply
covers: 10

You can work with remainders the same way you work with the numbers themselves: the remainder of a sum is the remainder of the sum of the remainders, and the same is true for differences and products. That turns enormous arithmetic into single-digit arithmetic.

The one extra step is that the result may still be too big, in which case you take the remainder again. If two numbers each leave remainder 4 on division by 6, their sum leaves remainder `8 mod 6 = 2`, not 8.

### Example
What is the remainder when `1,234 + 5,678` is divided by 5? `1,234` leaves 4 and `5,678` leaves 3. `4 + 3 = 7`, and `7` leaves remainder 2 on division by 5. So the answer is 2 — no need to add the numbers at all. The same works for products: `1,234 x 5,678` leaves `4 x 3 = 12`, and `12 mod 5 = 2`.

### Watch out
This does **not** work for division: the remainder of `a/b` divided by n has no simple relationship to the remainders of a and b.
