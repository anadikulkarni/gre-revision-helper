# Counting Strategy & Probability

## Repeats **and** restrictions together?
covers: 154

### Answer
Split the problem into the sections the restriction creates, count each with the repeats formula, then multiply the sections (or add, if they are alternatives).

### Explanation
Handle one constraint at a time and the hardest-looking counting questions become two small ones.

### Example
Arrangements of TEXTBOOK with all vowels first and all consonants last. Vowels E, O, O → `3!/2! = 3`. Consonants T, X, T, B, K → `5!/2! = 60`. Both blocks are required, so `3 x 60 = 180`.

## An unfamiliar counting question — what do you ask yourself first?
covers: 155

### Answer
Three questions: **how many items**, **how many are being chosen or arranged**, and **does order matter**? Then a fourth: are repeats allowed?

Order matters → permutation. Order does not → combination. Repeats allowed → plain multiplication (`n^r`). Identical items → divide by the repeat factorials.

### Explanation
Nearly every counting question is one of the standard types in disguise. Answering those three questions names the type, and then the formula is mechanical.

### Example
"5 books on a shelf, 2 identical" → arranging 5, order matters, one repeat of 2 → `5!/2! = 60`. "3-topping pizzas from 8 toppings" → choosing 3 of 8, order irrelevant → `8C3 = 56`.

## Seating `n` people around a **circular** table?
covers: 156

### Answer
`(n - 1)!`, not `n!`.

### Explanation
A circle has no fixed starting point, so rotating everyone one seat gives the same arrangement — each distinct seating was counted `n` times, and `n!/n = (n-1)!`. In practice: fix one person, then arrange the rest around them.

### Example
5 people in a row: `5! = 120`. The same 5 around a table: `4! = 24`.

### Watch out
Numbered seats make it a row again, and a flippable arrangement (a bracelet) halves the count. Read the setup carefully.

## For a fixed `n`, which `r` makes `nCr` largest?
covers: 157

### Answer
`r = n/2`. If `n` is odd, the two values either side of the middle tie.

### Explanation
Choosing about half the items gives the most possible groups; the counts fall away symmetrically toward `r = 0` and `r = n`, which each have exactly one.

### Example
`n = 6`: counts run 1, 6, 15, **20**, 15, 6, 1 — maximum at `r = 3`. `n = 7`: 1, 7, 21, **35**, **35**, 21, 7, 1 — `r = 3` and `r = 4` tie.

## Basic probability of an event?
covers: new

### Answer
`P(E) = favourable outcomes / total outcomes`, always between 0 and 1. All the outcomes you count must be **equally likely**.

### Explanation
Most probability questions are really counting questions wearing a hat — build the numerator and denominator with the counting tools you already have.

`P(not E) = 1 - P(E)` is the other half of the toolkit.

### Example
One card from a deck: `P(king) = 4/52 = 1/13`. Two dice: `P(sum of 7) = 6/36 = 1/6`, since 6 of the 36 equally likely pairs total 7. Choosing 2 people from 10 of whom 4 are women, `P(both women) = 4C2 / 10C2 = 6/45 = 2/15`.

### Watch out
Equally likely matters. The sums of two dice are **not** equally likely — 7 comes up six times as often as 2.

## Probability that A **and** B both happen?
covers: 158

### Answer
For **independent** events, `P(A and B) = P(A) x P(B)`. If they are not independent, use `P(A) x P(B given A)`.

### Explanation
Independence means one event does not change the odds of the other. "Without replacement" is the standard flag that it fails.

For three or more independent events, keep multiplying. For dependent ones, each factor is conditioned on everything before it.

### Example
Two coin flips both heads: `1/2 x 1/2 = 1/4`. Two aces drawn without replacement: `4/52 x 3/51 = 1/221`, **not** `(4/52)^2`.

Three heads in a row: `(1/2)^3 = 1/8`. Three aces without replacement: `4/52 x 3/51 x 2/50 = 1/5,525`.

## Probability that A **or** B happens?
covers: 159

### Answer
`P(A or B) = P(A) + P(B) - P(A and B)` — inclusion–exclusion again.

### Explanation
Adding the two probabilities double-counts the outcomes where both occur, so the overlap comes off once.

When the events are mutually exclusive the overlap is 0, so the formula collapses to plain addition — which is why "or" questions about outcomes that cannot co-occur feel so much easier.

### Example
One die: `P(even) = 3/6`, `P(>3) = 3/6`, overlap {4, 6} `= 2/6`. So `P(even or >3) = 3/6 + 3/6 - 2/6 = 2/3`, matching the list 2, 4, 5, 6.

Drawing a king **or** a queen: mutually exclusive, so `4/52 + 4/52 = 2/13`. Drawing a king **or** a heart: they overlap in the king of hearts, so `4/52 + 13/52 - 1/52 = 4/13`.

## Independent versus mutually exclusive — what is the difference?
covers: 160

### Answer
**Independent**: neither affects the other, so `P(A and B) = P(A)P(B)`. **Mutually exclusive**: they cannot both happen, so `P(A and B) = 0` and `P(A or B) = P(A) + P(B)`.

### Explanation
They sound similar and mean opposite things. A consequence worth remembering: for mutually exclusive events `P(A) + P(B) <= 1`, since probabilities summing past 1 would force an overlap.

### Example
Two coin flips are independent (both can be heads). One card being both a king and a queen is mutually exclusive. Two events with non-zero probability can never be both — if they cannot co-occur, knowing one happened tells you a great deal about the other.

## Conditional probability `P(A | B)`?
covers: 161

### Answer
`P(A | B) = P(A and B) / P(B)` — the probability of A **given that** B happened.

### Explanation
Conditioning on B shrinks the world to the outcomes where B occurred, so you rescale by dividing by `P(B)`.

### Example
Roll a die: what is `P(2 | even)`? `P(2 and even) = 1/6`, `P(even) = 1/2`, so `(1/6)/(1/2) = 1/3` — matching the intuition that among 2, 4, 6 exactly one is a 2.

### Watch out
`P(A | B)` and `P(B | A)` are different numbers: the probability of being even **given** a roll of 2 is 1, not 1/3.

## Probability of "at least one" — what is the fast route?
covers: new

### Answer
The complement: `P(at least one) = 1 - P(none)`.

### Explanation
Counting directly means adding the cases for exactly one, exactly two, exactly three … The complement is a single multiplication.

### Example
Four coin flips, at least one head: `P(no heads) = (1/2)^4 = 1/16`, so the answer is **15/16**. Rolling two dice, at least one 6: `1 - (5/6)^2 = 11/36`.

### Watch out
The complement of "at least one" is "none" — and the complement of "at least two" is "zero or one", so both cases must come off.
