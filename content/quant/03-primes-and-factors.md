# Primes & Factors

## Divisibility by 6 and other composites
covers: 18

There is no separate digit trick for 6. Instead, split 6 into `2 x 3` and apply both rules: a number is divisible by 6 exactly when it is even *and* its digits sum to a multiple of 3. The same method builds a test for any composite number out of the tests you already know.

The one condition is that the factors you split into must be **coprime** (share no factor). `12 = 4 x 3` works, because 4 and 3 are coprime. `12 = 2 x 6` does not, because 2 and 6 share a factor, and every multiple of 2 that is also a multiple of 6 is really just a multiple of 6.

### Example
Is 4,938 divisible by 6? It is even, and `4+9+3+8 = 24` is a multiple of 3, so yes. Is 7,316 divisible by 12? It is divisible by 4 (last two digits 16) but `7+3+1+6 = 17` is not a multiple of 3, so no.

## Divisibility by 11
covers: 21

Alternate the signs of the digits from left to right, starting with plus, then add them up. If that alternating sum is a multiple of 11 (including 0), the number is divisible by 11.

The rule comes from the fact that 10 leaves remainder -1 on division by 11, so each place value flips sign as you move left.

### Example
Is 918,082 divisible by 11? `+9 -1 +8 -0 +8 -2 = 22`, which is a multiple of 11, so yes. Is 4,938? `+4 -9 +3 -8 = -10`, not a multiple of 11, so no.

## Testing whether a number is prime
covers: 22

To check whether `n` is prime, try dividing by the primes up to `sqrt(n)` and stop there. You do not need to go further, because if `n` had a factor larger than its square root, it would have to be paired with one smaller than the square root, which you would already have found.

In practice that means testing 2, 3, 5, 7, 11, 13 — enough to settle every number below 289.

### Example
Is 191 prime? `sqrt(191) ≈ 13.8`, so test 2, 3, 5, 7, 11, 13. It is odd; digits sum to 11 so not divisible by 3; does not end in 0 or 5; `191/7 ≈ 27.3`; `191/11 ≈ 17.4`; `191/13 ≈ 14.7`. None divide it, so 191 is prime.

### Watch out
1 is not prime, and 2 is the only even prime — the single most common source of "all primes are odd" errors in comparison questions.

## Prime factorization is the master key
covers: new

Every integer greater than 1 breaks down into a unique product of primes, and almost every factor, GCF, LCM, divisibility and root question on the GRE is really asking you to look at that breakdown. Getting into the habit of writing a number as its prime factorization before doing anything else is the highest-return habit in the quant section.

Build it by dividing out the smallest prime repeatedly: `360 / 2 = 180 / 2 = 90 / 2 = 45 / 3 = 15 / 3 = 5 / 5 = 1`, giving `360 = 2^3 x 3^2 x 5`.

### Example
`60 = 2^2 x 3 x 5`. From that one line you can read off that 60 is divisible by 4 (there are two 2s), not by 8 (there is no third 2), not by 9 (only one 3), and that it has 12 factors in total.

## What three consecutive integers guarantee
covers: 23 (split)

Consecutive integers hand you divisibility facts for free. Among any three consecutive integers exactly one is a multiple of 3, so the product is always divisible by 3; at least one is even, so the product is divisible by 2; together that makes the product always divisible by 6. Their sum is also always a multiple of 3 (it equals three times the middle number).

There is a bonus case: if the middle number is odd, then the outer two are both even and one of them is a multiple of 4, so the product is divisible by 8 as well — and therefore by 24.

The same reasoning extends to three consecutive *multiples* of a number: their sum is three times the middle one, and the product keeps the divisibility of the base.

### Example
`5 x 6 x 7 = 210 = 6 x 35`, divisible by 6. `7 x 8 x 9 = 504`, and because the middle number 8 is even the "divisible by 8" bonus does not apply here — check instead `6 x 7 x 8 = 336 = 24 x 14`, where the middle number 7 is odd, so 336 is divisible by 8 and by 24.

## Writing consecutive integers algebraically
covers: 23 (split)

When a problem describes consecutive numbers, naming them properly turns the words into one equation. Three consecutive integers are `n, n+1, n+2`. Three consecutive even numbers are `2n, 2n+2, 2n+4`. Three consecutive odd numbers are `2n+1, 2n+3, 2n+5`. Three consecutive multiples of 7 are `7n, 7n+7, 7n+14`.

Centring on the middle term is often faster still: writing them as `n-1, n, n+1` makes the sum `3n` immediately.

### Example
The sum of three consecutive odd integers is 87; what is the largest? Write `(2n+1) + (2n+3) + (2n+5) = 87`, so `6n + 9 = 87`, `n = 13`, and the integers are 27, 29, 31. Or use the centre trick: the sum is 3 times the middle number, so the middle is 29 and the largest is 31.

## Divisibility travels through products
covers: 24

If `a` is divisible by `p^m` and `b` is divisible by `p^n`, then `ab` is divisible by `p^(m+n)`. Factors do not disappear when you multiply; they accumulate. This is the rule behind almost every "must be divisible by" question.

The reverse also matters: to prove a product is divisible by 12, find a 4 in one factor and a 3 in another — you do not need either factor to be divisible by 12 on its own.

### Example
If `a` is divisible by 4 (`2^2`) and `b` is divisible by 6 (`2 x 3`), then `ab` is divisible by `2^3 x 3 = 24`. So `a = 8, b = 18` gives `ab = 144`, and `144 / 24 = 6` exactly.

## Counting the factors of a number
covers: 25

Prime factorize, add 1 to every exponent, and multiply those results together. The rule works because building a factor means choosing how many copies of each prime to take, and for a prime with exponent `e` you have `e + 1` choices: none, one, two, …, up to `e`.

### Example
How many factors does 60 have? `60 = 2^2 x 3^1 x 5^1`, so the count is `(2+1)(1+1)(1+1) = 3 x 2 x 2 = 12`. Listing them confirms it: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60.

### Watch out
This counts *all* factors including 1 and the number itself. A perfect square always has an odd number of factors, because one of its exponents-plus-one pairings is the square root pairing with itself.

## Counting the odd factors
covers: 26

An odd number can have no even factors, so delete the whole power of 2 from the prime factorization and apply the same exponent-plus-one rule to what is left. The 2s were the only thing making factors even, so removing them counts exactly the odd factors.

### Example
Odd factors of 60? `60 = 2^2 x 3 x 5`; drop the `2^2` to get `3 x 5`, so the count is `(1+1)(1+1) = 4`. Those are 1, 3, 5 and 15.

## Counting the even factors
covers: 27

Every factor is either odd or even, so the even count is simply total factors minus odd factors. (Equivalently: an even factor must contain at least one 2, so with `2^a` in the factorization you have `a` choices for the power of 2 instead of `a + 1`.)

### Example
60 has 12 factors, 4 of which are odd, so 8 are even: 2, 4, 6, 10, 12, 20, 30, 60. The other route gives the same thing: `2 x (1+1)(1+1) = 8`.
