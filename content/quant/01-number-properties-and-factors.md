# Number Properties & Factors

## Converting an area or a volume between units — what happens to the factor?
covers: 1

### Answer
Square the conversion factor for an area, cube it for a volume. `1 m² = 3.28² = 10.76 ft²`, `1 m³ = 3.28³ ≈ 35.3 ft³`.

### Explanation
A square metre is not 3.28 square feet — it is a square 3.28 feet on each side, so it holds `3.28 x 3.28` square feet. Forgetting to raise the factor is the most common unit error on the test.

Writing the factor with its unit and raising the whole thing to the power keeps you honest: `(1 m / 3.28 ft)^2 = 1 m² / 10.76 ft²`, and the units then tell you whether to multiply or divide.

### Example
How many square metres is 540 square feet, given 3.28 ft per metre? `3.28^2 = 10.76`, so `540 / 10.76 ≈ 50.2 m²`. Dividing by 3.28 instead gives ≈165 — more than three times too big.

## Floor of a negative number — which way does it go?
covers: 7

### Answer
Down, always. `floor(-16.7) = -17`, not -16. The floor of a negative non-integer has a **larger** absolute value than the number.

### Explanation
The floor is the greatest integer less than or equal to the number, so it always moves you left on the number line. For positives that looks like "chop off the decimal", which is why negatives catch people out: chopping -16.7 gives -16, which is to the right.

### Example
`floor(16.7) = 16`, `floor(-16.7) = -17`, `floor(-3.01) = -4`, `floor(-3) = -3` (integers are their own floor).

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

## Last digit of a huge power like `7^103`?
covers: 6, 11, 12

### Answer
Two steps. **Keep only the base's last digit** — `unitdigit(a^b) = unitdigit(unitdigit(a)^b)` — then use that digit's **cycle**, which is never longer than 4. Divide the exponent by 4 and the remainder picks the entry.

2: 2, 4, 8, 6 · 3: 3, 9, 7, 1 · 7: 7, 9, 3, 1 · 8: 8, 4, 2, 6 · 4: 4, 6 · 9: 9, 1 · 0, 1, 5, 6 never change.

### Explanation
The unit digit is the rightmost digit, and it behaves independently of everything to its left: multiplying two numbers only lets their unit digits interact. That is why `1,234,567^40` ends in the same digit as `7^40`, and why you can answer questions about 80-digit numbers in seconds.

Raise any digit to higher powers and the last digit starts repeating within four steps. Since every cycle length divides 4, dividing the exponent by 4 works for all of them.

### Example
`7^103`: the cycle for 7 is (7, 9, 3, 1), and `103 / 4` leaves remainder 3, so the answer is the 3rd entry, **3**. Check on a small case: `7^3 = 343` ✓.

`2,468^15`: keep the 8, whose cycle is (8, 4, 2, 6); `15 / 4` leaves remainder 3, so the answer is **2**.

### Watch out
Remainder 0 means the **last** entry of the cycle, not the first. `7^100` leaves remainder 0, so it ends in 1.

## Unit digit of a sum or of a product?
covers: 13

### Answer
Add or multiply just the unit digits, then keep the last digit of that result.

### Explanation
It is the remainder rule for division by 10, and it lets you collapse a long expression into single digits before doing anything else.

### Example
`327 + 4,589 + 62`: add `7 + 9 + 2 = 18`, so the unit digit is **8**. For `327 x 4,589`: `7 x 9 = 63`, so **3**.

## Unit digit of `3 + 3^2 + 3^3 + ... + 3^50`?
covers: 14

### Answer
**2.** Each block of four powers contributes `3+9+7+1 = 20`, so complete blocks add 0 to the unit digit. Only the leftover terms count.

### Explanation
50 terms is 12 complete blocks of four (48 terms, unit digit 0) plus two leftovers, `3^49` and `3^50`. `49 / 4` leaves 1 so `3^49` ends in 3; `50 / 4` leaves 2 so `3^50` ends in 9. `3 + 9 = 12` → unit digit 2.

### Example
Same method on `2 + 2^2 + ... + 2^22`: the cycle (2, 4, 8, 6) sums to 20, so ignore the 20 complete-block terms; the leftovers are `2^21` (ends in 2) and `2^22` (ends in 4), giving unit digit **6**.

### Watch out
Count the leftovers from the **end** of the series, and check whether it starts at `3^1` or `3^0` — one extra first term changes everything.

## Remainder of `a^b` divided by a small number `n`?
covers: 15

### Answer
Find the cycle of remainders of `a^1, a^2, a^3, ...` divided by `n`, then use `b`'s position in that cycle. Reduce any running value that grows past `n`.

### Explanation
Cyclicity is not just a base-10 trick — remainders by any divisor repeat too. Compute until the pattern comes back round, then jump.

### Example
Remainder of `4^35` divided by 6? `4, 16, 64` give remainders 4, 4, 4 — a cycle of length 1, so the answer is **4** for every positive power. Richer case: `3^n` divided by 7 gives 3, 2, 6, 4, 5, 1 (length 6); `20 / 6` leaves 2, so `3^20` leaves remainder **2**.

## How far do you test before declaring `n` prime?
covers: 22

### Answer
Divide by the primes up to `sqrt(n)` and stop. In practice 2, 3, 5, 7, 11, 13 settles everything below 289.

### Explanation
If `n` had a factor larger than its square root, that factor would be paired with one *smaller* than the square root — which you would already have found. So there is nothing above the square root left to check.

### Example
Is 191 prime? `sqrt(191) ≈ 13.8`. It is odd; digits sum to 11 (not a multiple of 3); it does not end in 0 or 5; `191/7 ≈ 27.3`, `191/11 ≈ 17.4`, `191/13 ≈ 14.7`. None divide, so **yes**.

### Watch out
1 is not prime, and 2 is the only even prime — the source of most "all primes are odd" errors.

## Which squares, cubes and roots should you know cold?
covers: new

### Answer
Squares to 20: 121, 144, 169, 196, 225, 256, 289, 324, 361, 400. Cubes to 6: 8, 27, 64, 125, 216. Powers of 2 to 10: 1024. And `sqrt(2) ≈ 1.41`, `sqrt(3) ≈ 1.73`, `sqrt(5) ≈ 2.24`.

### Explanation
Recognition is speed. Seeing that 196 is `14^2`, or that 1.73 is `sqrt(3)` in disguise, turns a 40-second question into a 5-second one, and it is what lets you estimate radical answers without a calculator.

### Example
Simplify `sqrt(288)`. Recognising `288 = 144 x 2` gives `12sqrt(2) ≈ 16.97` at once. And a triangle side of `8.66` should immediately read as `5sqrt(3)`.

## Three consecutive integers — what is guaranteed?
covers: 23 (split)

### Answer
Exactly one is a multiple of 3, at least one is even, so the **product is always divisible by 6** and the **sum is always a multiple of 3**. If the middle one is odd, the product is also divisible by 8, hence by 24.

### Explanation
The bonus case works because an odd middle forces both outer numbers to be even, and one of any two consecutive evens is a multiple of 4.

The same reasoning extends to three consecutive *multiples* of a number: the sum is three times the middle one.

### Example
`5 x 6 x 7 = 210 = 6 x 35` ✓. `6 x 7 x 8 = 336 = 24 x 14` — middle number 7 is odd, so the divisible-by-24 bonus applies.

## How do you name consecutive numbers in algebra?
covers: 23 (split)

### Answer
Integers: `n, n+1, n+2`. Evens: `2n, 2n+2, 2n+4`. Odds: `2n+1, 2n+3, 2n+5`. Multiples of 7: `7n, 7n+7, 7n+14`. Or centre them: `n-1, n, n+1`, whose sum is just `3n`.

### Explanation
Naming them properly turns a sentence into one equation, and centring on the middle term usually halves the algebra.

### Example
Three consecutive odd integers sum to 87; what is the largest? `(2n+1)+(2n+3)+(2n+5) = 87` → `6n + 9 = 87` → `n = 13`, giving 27, 29, 31. Or: the sum is 3 times the middle, so the middle is 29 and the largest is **31**.

## `a` is divisible by `p^m` and `b` by `p^n` — what about `ab`?
covers: 24

### Answer
`ab` is divisible by `p^(m+n)`. Factors accumulate when you multiply; they never disappear.

### Explanation
This is the rule behind nearly every "must be divisible by" question. It also works in reverse: to show a product is divisible by 12, find a 4 in one factor and a 3 in another — neither factor needs to be divisible by 12 itself.

### Example
`a` divisible by 4 (`2^2`), `b` divisible by 6 (`2 x 3`) → `ab` divisible by `2^3 x 3 = 24`. Taking `a = 8, b = 18` gives 144, and `144 / 24 = 6` ✓.

## How many factors does a number have?
covers: 25

### Answer
Prime factorize, **add 1 to every exponent, and multiply**. For `60 = 2^2 x 3^1 x 5^1` that is `3 x 2 x 2 = 12`.

### Explanation
Building a factor means choosing how many copies of each prime to take, and a prime with exponent `e` gives you `e + 1` choices: none, one, …, up to `e`.

### Example
60's twelve factors: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60 ✓.

### Watch out
The count includes 1 and the number itself. A perfect square always has an **odd** number of factors, since its square root pairs with itself.

## How many **odd** factors does a number have?
covers: 26

### Answer
Delete the whole power of 2 from the prime factorization, then use the same exponent-plus-one rule on what is left.

### Explanation
The 2s were the only thing capable of making a factor even, so removing them counts exactly the odd ones.

### Example
Odd factors of 60? Drop the `2^2` from `2^2 x 3 x 5` to get `3 x 5`, giving `(1+1)(1+1) = 4`: 1, 3, 5, 15.

Another: `360 = 2^3 x 3^2 x 5` → drop the `2^3` → `(2+1)(1+1) = 6` odd factors: 1, 3, 5, 9, 15, 45.

## How many **even** factors does a number have?
covers: 27

### Answer
Total factors minus odd factors. (Or: with `2^a` in the factorization, use `a` choices for the power of 2 instead of `a + 1`.)

### Explanation
Every factor is either odd or even, so the subtraction is exact.

A number with no 2 in its factorization is odd, so it has *zero* even factors — worth checking before you start subtracting.

### Example
60 has 12 factors and 4 odd ones, so **8** are even: 2, 4, 6, 10, 12, 20, 30, 60. The other route: `2 x (1+1)(1+1) = 8` ✓.

For 360: 24 factors in total, 6 odd, so 18 even. The direct route agrees: `3 x (2+1)(1+1) = 18`.

## Greatest common factor of a group of numbers?
covers: 28

### Answer
Prime factorize them all, then for each prime that appears in **every** number take the **lowest** power, and multiply.

### Explanation
You can only share as many copies of a prime as the stingiest number has, and a prime missing from any one number cannot appear at all.

### Example
GCF of 60 (`2^2 x 3 x 5`) and 72 (`2^3 x 3^2`): shared primes 2 and 3, lowest powers `2^2` and `3^1`, and 5 is out. GCF `= 12`.

### Watch out
Numbers sharing no prime have a GCF of **1**, not 0 — they are called coprime.

## How many factors do two numbers have in common?
covers: 29

### Answer
Count the factors of their **GCF**. Build the GCF, then apply the exponent-plus-one rule to it.

### Explanation
Any number dividing both must divide their greatest common factor, so the shared factors are exactly the GCF's factors. No listing required.

### Example
60 and 72 have GCF `12 = 2^2 x 3`, so `(2+1)(1+1) = 6` common factors: 1, 2, 3, 4, 6, 12 ✓.

Another: 84 (`2^2 x 3 x 7`) and 126 (`2 x 3^2 x 7`) have GCF `2 x 3 x 7 = 42`, so `(1+1)(1+1)(1+1) = 8` common factors.

## Least common multiple of a group of numbers?
covers: 30

### Answer
Prime factorize, then for each prime appearing in **any** of them take the **highest** power, and multiply.

### Explanation
Where the GCF asks what they share, the LCM asks what it takes to satisfy everyone.

### Example
LCM of 60 (`2^2 x 3 x 5`) and 72 (`2^3 x 3^2`): `2^3 x 3^2 x 5 = 360`. Check: `360/60 = 6` and `360/72 = 5` ✓.

### Watch out
The LCM is never smaller than the largest number and the GCF never bigger than the smallest. If that fails, you have swapped the rules.

## `n` is divisible by `a` and by `b` — what else must it be divisible by?
covers: 31

### Answer
`LCM(a, b)` — **not** `a x b`. A number divisible by 4 and by 6 must be divisible by 12, not 24.

### Explanation
Only when `a` and `b` are coprime does `LCM(a, b) = a x b`, which is why "divisible by 3 and by 5" safely means "divisible by 15".

### Example
`n` divisible by 8 and 12 → `LCM = 24`, so `n` is a multiple of 24. And `n = 24` itself is not a multiple of `8 x 12 = 96`, which kills the product version.

## What is the relationship between GCF, LCM and the numbers themselves?
covers: 32

### Answer
`GCF(a, b) x LCM(a, b) = a x b` — for **two** numbers only.

### Explanation
Each prime appears in the pair with a lower and a higher exponent; the GCF takes the lower, the LCM the higher, so together they use up exactly the exponents in `a x b`.

### Example
`a = 60, b = 72, GCF = 12` → `LCM = (60 x 72)/12 = 360` ✓. If two numbers multiply to 1,200 with GCF 10, the LCM is `1,200/10 = 120` with no factorization at all.

### Watch out
The identity breaks for three or more numbers.
