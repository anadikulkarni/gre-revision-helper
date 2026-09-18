# Number Sense & Strategy

## Two quantities given in different units — first move?
covers: 2

### Answer
Convert to a common unit **before** comparing anything. Multiply by a conversion fraction arranged so the unwanted unit cancels.

### Explanation
A question will happily give one speed in km/h and another in m/s and ask which is greater. The numbers are not comparable until they share a unit, and the fastest way to lose a point is to treat 20 > 8 as settling it.

Write the conversion as a fraction that cancels the unit you want gone: to turn m/s into km/h, multiply by `3600 s / 1 hr` and by `1 km / 1000 m`, so seconds and metres both cancel.

### Example
Which is greater: a car at 20 km/h or a runner at 8 m/s? `8 x 3600 = 28,800 m/hr = 28.8 km/h`. The runner is faster, even though "20" looks bigger.

### Watch out
The same trap hides in time (minutes vs hours), money (cents vs dollars) and area (cm² vs m²). If two units appear anywhere in a question, convert first.

## Converting an area or a volume between units — what happens to the factor?
covers: 1

### Answer
Square the conversion factor for an area, cube it for a volume. `1 m² = 3.28² = 10.76 ft²`, `1 m³ = 3.28³ ≈ 35.3 ft³`.

### Explanation
A square metre is not 3.28 square feet — it is a square 3.28 feet on each side, so it holds `3.28 x 3.28` square feet. Forgetting to raise the factor is the most common unit error on the test.

Writing the factor with its unit and raising the whole thing to the power keeps you honest: `(1 m / 3.28 ft)^2 = 1 m² / 10.76 ft²`, and the units then tell you whether to multiply or divide.

### Example
How many square metres is 540 square feet, given 3.28 ft per metre? `3.28^2 = 10.76`, so `540 / 10.76 ≈ 50.2 m²`. Dividing by 3.28 instead gives ≈165 — more than three times too big.

## Quantitative Comparison: how do you prove the answer is D?
covers: 3

### Answer
Find one case where the quantities are **equal** and one where they are **not**. Two different relationships means the relationship is not fixed, so the answer is D.

### Explanation
A QC question does not ask for a value, it asks whether one column is always bigger. That makes D a target rather than a last resort, and the equal/not-equal pair is the quickest proof.

Choose test values deliberately, not randomly. The ones that break intuition are 0, 1, a negative, a fraction between 0 and 1, and something large.

### Example
Quantity A: `x^2`. Quantity B: `x`. Try `x = 1`: both equal 1. Try `x = 2`: A is 4, B is 2. Two different relationships, so **D**. (Told that `x > 1`, the answer would be A.)

### Watch out
One case is never enough. Finding A = B once only rules out "A is always greater"; you still need a second case to choose between C and D.

## When you are about to do heavy arithmetic, what should you do instead?
covers: 4

### Answer
Stop and look for the shortcut: estimate, compare structure, cancel common factors, or test a convenient number. Comparing is easier than computing.

### Explanation
Every comparison and most multiple-choice questions are built so a full calculation is possible but unnecessary. Four-digit multiplication is a sign you have missed the intended route.

To decide whether `17/33` beats `1/2` you do not need the decimal — half of 33 is 16.5, and 17 is more than that.

### Example
Which is greater, `47 x 52` or `48 x 51`? Both pairs sum to 99, and for a fixed sum the product is largest when the numbers are closest together. 48 and 51 are closer, so `48 x 51` wins — no multiplication done.

### Watch out
Estimation is only safe when the quantities are far apart. If your estimate makes them look nearly equal, go back and compute exactly.

## "What is the 50th term / the 200th digit?" — what is the question really about?
covers: 5

### Answer
A repeating cycle. Compute the first few terms, find the cycle length `k`, then take the remainder of `n / k` to see where term `n` lands.

### Explanation
No GRE question wants you to grind out 50 steps. Asking for a far-away term is a signal that the sequence repeats, and the whole job is finding the length of the repeat.

Remainder 0 means you have landed on the **last** item of the cycle, not the first. That off-by-one is where most of the errors live.

### Example
The 50th term of 7, 4, 1, 7, 4, 1, …? The cycle is (7, 4, 1), length 3. `50 / 3` leaves remainder 2, so the 50th term is the 2nd item: **4**.

### Watch out
Write out enough terms to see the cycle repeat *twice*. Two equal terms in a row is not proof of a cycle.

## Unit digit — what is it, and why does it get its own rules?
covers: 6

### Answer
The rightmost digit (the ones place). It is independent of everything to its left: when you add or multiply, the unit digit of the answer depends only on the unit digits of the inputs.

### Explanation
That independence is what makes "last digit of `7^100`" answerable in seconds — the other 84 digits never matter.

### Example
In 3,472 the unit digit is 2. The unit digit of `3,472 x 1,238` comes from `2 x 8 = 16`, so it is **6**, with no long multiplication.

## Even and odd: what do the four operations give you?
covers: new

### Answer
`even ± even = even`, `odd ± odd = even`, `even ± odd = odd`. For products, **anything times an even is even**; only `odd x odd = odd`.

### Explanation
Multiplication is the lopsided one: a single even factor is enough to make the whole product even, which is why the product of consecutive integers is always even.

Division breaks the pattern entirely — an even divided by an even can be either (`8/4 = 2`, `6/4 = 1.5`), so never assume parity survives a division.

### Example
If `n` is odd, is `n^2 + n` odd or even? `odd x odd = odd`, and `odd + odd = even`, so it is always even. Testing `n = 3` gives 12 ✓.

### Watch out
0 is even, and 2 is the only even prime. Both show up in "must be true" questions.

## Signs: what do products and powers do to them?
covers: new

### Answer
Multiplying or dividing: same signs give positive, different signs give negative. Powers: a negative base raised to an **even** power is positive, to an **odd** power stays negative.

### Explanation
Count the negatives in a product — an even number of them cancels out, an odd number leaves the result negative.

The power rule is the source of endless QC traps: `x^2` is never negative, so `x^2 = 9` has two solutions while `x^3 = 27` has one.

### Example
`(-2)^4 = 16` but `(-2)^3 = -8`. And `(-2)(-3)(-4) = -24`: three negatives, so the result is negative.

### Watch out
`-2^4` and `(-2)^4` are different. Without brackets the power binds first, so `-2^4 = -16`.

## Absolute value — what does |x| actually mean?
covers: new

### Answer
The distance from zero on the number line, so it is never negative. `|x| = x` when `x >= 0` and `|x| = -x` when `x < 0`.

### Explanation
Reading it as *distance* rather than "make it positive" is what makes the harder questions easy: `|x - 3|` is the distance between `x` and 3, so `|x - 3| = 5` immediately gives the two points 5 away from 3.

### Example
`|-7| = 7` and `|7| = 7`. `|x - 3| < 5` means "x is less than 5 away from 3", i.e. `-2 < x < 8` — no algebra needed.

### Watch out
`|a + b|` is not `|a| + |b|`: take `a = 3, b = -3`. It is always less than or equal to it.

## Floor of a negative number — which way does it go?
covers: 7

### Answer
Down, always. `floor(-16.7) = -17`, not -16. The floor of a negative non-integer has a **larger** absolute value than the number.

### Explanation
The floor is the greatest integer less than or equal to the number, so it always moves you left on the number line. For positives that looks like "chop off the decimal", which is why negatives catch people out: chopping -16.7 gives -16, which is to the right.

### Example
`floor(16.7) = 16`, `floor(-16.7) = -17`, `floor(-3.01) = -4`, `floor(-3) = -3` (integers are their own floor).

## Quotient and remainder — what is the identity that ties them together?
covers: 8

### Answer
`a = bq + r` with `0 <= r < b`. The quotient `q` is the whole-number part; the remainder `r` is what is left, and it is never negative and always smaller than the divisor.

### Explanation
The constraint on `r` is the important half. A remainder of 7 when dividing by 6 is impossible — it means you did not take out enough copies of 6.

Most remainder questions are solved by writing the number in this form and substituting, not by trying values at random.

### Example
`47 / 5`: quotient 9, remainder 2, since `47 = 5 x 9 + 2`. "n leaves remainder 2 when divided by 5" means `n = 5q + 2`, so n is 2, 7, 12, 17, …

## Quotient and remainder when the number is negative?
covers: 9

### Answer
The quotient goes one step further down, because the remainder must stay non-negative. `-15 / 9` gives quotient **-2**, remainder **3**.

### Explanation
It is tempting to say quotient -1 remainder -6, but remainders cannot be negative. Taking the quotient down to -2 gives `-15 = 9(-2) + 3`, with `0 <= 3 < 9` ✓.

This is the same idea as the floor of a negative: the quotient *is* `floor(a/b)`.

### Example
`-15 / 9` → quotient -2, remainder 3. Compare `15 / 9` → quotient 1, remainder 6. The absolute value of the quotient went up by one.

## Remainder of a sum or a product of huge numbers?
covers: 10

### Answer
Work with the remainders instead: the remainder of a sum is the remainder of the **sum of the remainders**, and the same holds for differences and products. Reduce again if the result is still too big.

### Explanation
This turns enormous arithmetic into single-digit arithmetic. If two numbers each leave remainder 4 on division by 6, their sum leaves `8 mod 6 = 2`, not 8.

### Example
Remainder of `1,234 + 5,678` divided by 5? They leave 4 and 3, and `4 + 3 = 7` leaves remainder **2**. For the product: `4 x 3 = 12`, and `12 mod 5 = 2`.

### Watch out
This does **not** work for division — the remainder of `a/b` has no simple relationship to the remainders of `a` and `b`.
