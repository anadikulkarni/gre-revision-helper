# Unit Digits & Divisibility Rules

## Unit digits of powers run in cycles
covers: 11

Raise any digit to higher and higher powers and its unit digit starts repeating, always within four steps. That is the whole trick behind "what is the last digit of `7^103`" questions: work out the cycle, then find where 103 lands inside it.

The cycles worth knowing: 2 goes 2, 4, 8, 6; 3 goes 3, 9, 7, 1; 7 goes 7, 9, 3, 1; 8 goes 8, 4, 2, 6 (all length 4). 4 goes 4, 6 and 9 goes 9, 1 (length 2). 0, 1, 5 and 6 never change at all. Since every cycle length divides 4, dividing the exponent by 4 is enough for all of them.

### Example
Last digit of `7^103`. The cycle for 7 is (7, 9, 3, 1), length 4. `103 / 4` leaves remainder 3, so we want the 3rd entry: **3**. Check the logic on a small case: `7^3 = 343`, and 3 is indeed the 3rd entry.

### Watch out
Remainder 0 means the *last* item of the cycle, not the first. `7^100` has remainder 0, so its unit digit is 1, the 4th entry.

## Only the base's unit digit matters
covers: 12

`unitdigit(a^b) = unitdigit(unitdigit(a)^b)`. Everything to the left of the base's last digit is irrelevant to the answer, because multiplying two numbers only lets the unit digits talk to each other. This is what makes the cycles above usable on monstrous numbers.

So `1,234,567^40` has the same unit digit as `7^40`, and you can throw the other six digits away the moment you see the question.

### Example
Unit digit of `2,468^15`? Keep only the 8: the cycle for 8 is (8, 4, 2, 6). `15 / 4` leaves remainder 3, so the answer is the 3rd entry, **2**.

## Unit digit of a sum or product
covers: 13

The unit digit of a sum is the unit digit of the sum of the unit digits, and the same holds for products. This is just the remainder rule for division by 10, and it lets you collapse a long expression into single digits before doing anything else.

If the digits add to more than 9, keep only the last digit of that total and carry on.

### Example
Unit digit of `327 + 4,589 + 62`? Add only the last digits: `7 + 9 + 2 = 18`, so the unit digit is **8**. For a product, `327 x 4,589` has unit digit from `7 x 9 = 63`, so **3**.

## Worked example: unit digit of a long power sum
covers: 14

Combine the last three ideas and a question like "what is the unit digit of `3 + 3^2 + 3^3 + ... + 3^50`?" becomes a counting exercise. Each power of 3 contributes its own unit digit from the cycle (3, 9, 7, 1), those four digits sum to 20, and 20 contributes a unit digit of 0. So every complete block of four terms adds nothing to the unit digit, and only the leftover terms matter.

### Example
`3 + 3^2 + ... + 3^50`: 50 terms is 12 complete blocks of 4 (48 terms, contributing unit digit 0) plus 2 leftover terms, `3^49` and `3^50`. `49 / 4` leaves remainder 1, so `3^49` ends in 3; `50 / 4` leaves remainder 2, so `3^50` ends in 9. `3 + 9 = 12`, so the unit digit of the whole sum is **2**.

### Watch out
Count the leftovers from the *end* of the series, and check whether the series starts at `3^1` or `3^0` — an extra first term changes the answer.

## Remainder of a huge power
covers: 15

The same cyclicity idea works for remainders by any divisor, not just 10. To find the remainder of `a^b` divided by `n`, compute the remainders of `a^1, a^2, a^3, ...` divided by `n` until the pattern repeats, then use the exponent's position in that cycle.

If a step of the pattern gives you a number bigger than the divisor, reduce it again. When dividing by 6, a running value of 7 is really a remainder of 1.

### Example
Remainder of `4^35` divided by 6. `4^1 = 4` → 4. `4^2 = 16` → 4. `4^3 = 64` → 4. The cycle has length 1, so the answer is **4** for any positive power. A richer case: `3^20` divided by 7 gives remainders 3, 2, 6, 4, 5, 1 then repeats (length 6); `20 / 6` leaves remainder 2, so the answer is the 2nd entry, 2.

## Divisibility by 2, 5 and 10
covers: new

Before the clever rules, the three that come straight off the last digit: a number is divisible by 2 if its unit digit is even (0, 2, 4, 6, 8), by 5 if its unit digit is 0 or 5, and by 10 if its unit digit is 0. These are the building blocks that the composite rules below are made from.

### Example
4,938 is divisible by 2 (ends in 8) but not by 5. 4,935 is divisible by 5 but not by 2, so not by 10. 4,930 ends in 0 so it is divisible by 2, 5 and 10.

## Divisibility by 3
covers: 16

Add up the digits. If that sum is a multiple of 3, so is the original number — and if the sum is still too big to judge, add its digits again and repeat.

The rule works because 10, 100, 1000 … all leave remainder 1 when divided by 3, so each digit contributes exactly its own value to the remainder.

### Example
Is 4,938 divisible by 3? `4 + 9 + 3 + 8 = 24`, and 24 is a multiple of 3, so yes. For 987,654: `9+8+7+6+5+4 = 39`, and `3+9 = 12`, a multiple of 3, so yes.

## Divisibility by 9
covers: 20

Exactly the same digit-sum test, but the sum must be a multiple of 9. Every number divisible by 9 is therefore also divisible by 3, though the reverse is not true.

### Example
4,938: digits sum to 24, which is divisible by 3 but not 9, so 4,938 is a multiple of 3 and not of 9. 4,932: digits sum to 18, a multiple of 9, so it is divisible by 9 (and by 3).

## Divisibility by 4
covers: 17

Ignore everything except the last two digits: if the two-digit number they form is divisible by 4, so is the whole number. This works because 100 is itself a multiple of 4, so the hundreds and everything above them can never affect the answer.

Two handy corollaries: any number ending in 00 is divisible by 4, and any even number whose tens digit is even needs only its unit digit to be 0, 4 or 8.

### Example
Is 7,318 divisible by 4? Look at 18 — not a multiple of 4, so no. Is 7,316? Look at 16 — yes, so 7,316 is divisible by 4.

## Divisibility by 8
covers: 19

Same idea one place further: check the last *three* digits, because 1,000 is a multiple of 8. If the three-digit number they form is divisible by 8, so is the original.

Anything ending in 000 is divisible by 8, which is why questions about round numbers often collapse immediately.

### Example
Is 12,344 divisible by 8? Check 344: `344 / 8 = 43` exactly, so yes. Is 12,346? Check 346: `346 / 8 = 43.25`, so no. For a faster check on the three digits, halve three times: 344 → 172 → 86 → 43, all whole numbers, so it is a multiple of 8.
