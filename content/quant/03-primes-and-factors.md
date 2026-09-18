# Primes, Factors & GCF

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

## Prime factorization — why is it the first move on so many questions?
covers: new

### Answer
Because every integer above 1 is a unique product of primes, and factor counts, GCF, LCM, divisibility and rational roots are all read straight off that product. Build it by dividing out the smallest prime repeatedly.

### Explanation
`360 / 2 = 180 / 2 = 90 / 2 = 45 / 3 = 15 / 3 = 5 / 5 = 1`, so `360 = 2^3 x 3^2 x 5`. Writing this line before doing anything else is the highest-return habit in the quant section.

### Example
`60 = 2^2 x 3 x 5`. From that one line: divisible by 4 (two 2s), not by 8 (no third 2), not by 9 (only one 3), and it has 12 factors.

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
