# Unit Digits & Divisibility Rules

## Last digit of a large power — what do you need?
covers: 11

### Answer
The unit digit's **cycle**, which is always length 4 or shorter. Divide the exponent by 4 and use the remainder to pick the entry.

2: 2, 4, 8, 6 · 3: 3, 9, 7, 1 · 7: 7, 9, 3, 1 · 8: 8, 4, 2, 6 · 4: 4, 6 · 9: 9, 1 · 0, 1, 5, 6 never change.

### Explanation
Raise any digit to higher powers and its last digit starts repeating within four steps. Since every cycle length divides 4, dividing the exponent by 4 works for all of them.

### Example
Last digit of `7^103`? The cycle for 7 is (7, 9, 3, 1). `103 / 4` leaves remainder 3, so take the 3rd entry: **3**. Check on a small case: `7^3 = 343` ✓.

### Watch out
Remainder 0 means the **last** entry of the cycle, not the first. `7^100` has remainder 0, so its unit digit is 1.

## Unit digit of `1,234,567^40` — what can you throw away?
covers: 12

### Answer
Everything except the base's last digit: `unitdigit(a^b) = unitdigit(unitdigit(a)^b)`. So `1,234,567^40` ends in the same digit as `7^40`.

### Explanation
Multiplying two numbers only lets their unit digits interact, so the digits further left can never reach the ones place. This is what makes the cycles usable on monstrous numbers.

### Example
Unit digit of `2,468^15`? Keep the 8; its cycle is (8, 4, 2, 6). `15 / 4` leaves remainder 3, so the answer is the 3rd entry, **2**.

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

## Divisibility by 2, 5 and 10?
covers: new

### Answer
Read the last digit: **2** if it is even (0, 2, 4, 6, 8), **5** if it is 0 or 5, **10** only if it is 0.

### Explanation
These are the building blocks the composite rules are made from, so they are worth stating before the clever ones.

### Example
4,938 is divisible by 2 but not 5. 4,935 is divisible by 5 but not 2, so not by 10. 4,930 ends in 0, so it is divisible by all three.

## Divisibility by 3?
covers: 16

### Answer
Add the digits. If the sum is a multiple of 3, so is the number — and you can repeat the test on the sum.

### Explanation
It works because 10, 100, 1000 … all leave remainder 1 on division by 3, so each digit contributes exactly its own value to the remainder.

### Example
4,938 → `4+9+3+8 = 24`, a multiple of 3, so yes. 987,654 → 39 → `3+9 = 12`, so yes.

## Divisibility by 9?
covers: 20

### Answer
The same digit sum, but it must be a multiple of **9**.

### Explanation
Every multiple of 9 is therefore also a multiple of 3, though the reverse fails.

Repeating the digit sum until one digit is left gives the *digital root*, and a digital root of 9 is the same test. It is a quick way to check arithmetic: the digital roots of the inputs must match the digital root of the answer.

### Example
4,938: digits sum to 24, divisible by 3 but not 9 → multiple of 3 only. 4,932: digits sum to 18 → divisible by 9 and by 3.

Digital root of 987,654: `39 → 12 → 3`, so it is divisible by 3 but not 9.

## Divisibility by 4?
covers: 17

### Answer
Look only at the **last two digits**. If that two-digit number is a multiple of 4, so is the whole number.

### Explanation
100 is itself a multiple of 4, so the hundreds and everything above them can never affect the answer. Anything ending in 00 is divisible by 4.

A second shortcut: if the tens digit is even, the number is divisible by 4 exactly when the unit digit is 0, 4 or 8; if the tens digit is odd, the unit digit must be 2 or 6.

### Example
7,318 → 18 is not a multiple of 4, so no. 7,316 → 16 is, so yes.

Squares are a good stress test: every even square is divisible by 4 (`14^2 = 196` → 96 ✓), and every odd square leaves remainder 1.

## Divisibility by 8?
covers: 19

### Answer
Look at the **last three digits**, because 1,000 is a multiple of 8. Anything ending in 000 qualifies.

### Explanation
For a quick check on those three digits, halve three times — if you stay on whole numbers, it divides.

### Example
12,344 → 344, and `344 / 8 = 43` exactly, so yes. Halving: 344 → 172 → 86 → 43 ✓. 12,346 → 346 → 173 → 86.5 ✗.

## Divisibility by 6, 12 or any composite?
covers: 18

### Answer
Split it into **coprime** factors and apply both rules. 6 = 2 x 3, so even **and** digit sum divisible by 3. 12 = 4 x 3, so the last two digits divide by 4 **and** the digit sum by 3.

### Explanation
The factors must share no common factor. `12 = 2 x 6` is useless, because every number divisible by 2 and 6 is just divisible by 6.

### Example
4,938: even ✓, digits sum to 24 ✓ → divisible by 6. 7,316: last two digits 16 divide by 4 ✓, but `7+3+1+6 = 17` is not a multiple of 3 ✗ → not divisible by 12.

## Divisibility by 11?
covers: 21

### Answer
Alternate the digit signs from left to right starting with plus, and add. If that alternating sum is a multiple of 11 (0 counts), so is the number.

### Explanation
10 leaves remainder -1 on division by 11, so each place value flips sign as you move left.

### Example
918,082 → `+9 -1 +8 -0 +8 -2 = 22`, a multiple of 11, so yes (`918,082 / 11 = 83,462`). 4,938 → `+4 -9 +3 -8 = -10` ✗.
