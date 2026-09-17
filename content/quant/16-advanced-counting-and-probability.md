# Advanced Counting & Probability

## Arrangements with repeated items
covers: 41, 153

Arranging `n` items where some are identical gives fewer distinct results than `n!`, because swapping two identical items changes nothing. Divide by the factorial of each repeat count:

`arrangements = n!/(a! b! ...)`

where `a`, `b`, … are how many times each repeated item appears.

### Example
How many arrangements of the letters in BANANA? `n = 6`, with three As and two Ns, so `6!/(3! 2!) = 720/12 = 60`. For a word with no repeats, like ABCDEF, the division disappears and you get the full `6! = 720`.

### Watch out
Divide by the factorial of each repeat *separately*; do not add the repeat counts together first. Three As and two Ns means `3! x 2! = 12`, not `5! = 120`.

## Repeats plus restrictions
covers: 154

Combine the two ideas: split the problem into the sections the restriction creates, count each with the repeats formula, then multiply the sections together (or add, if they are alternative scenarios).

### Example
How many arrangements of TEXTBOOK have all vowels first and all consonants last? The vowels are E, O, O → `3!/2! = 3` arrangements. The consonants are T, X, T, B, K → `5!/2! = 60`. The two blocks are both required, so multiply: `3 x 60 = 180`.

## Turning a word problem into a counting problem
covers: 155

Most counting questions are one of the standard types wearing a disguise. Before calculating, answer three questions: how many items are there, how many are being chosen or arranged, and does order matter? Add a fourth if needed: are repeats allowed?

Order matters → permutation. Order does not → combination. Repeats allowed → plain multiplication (`n^r`). Identical items in a fixed arrangement → divide by the repeat factorials.

### Example
"How many ways can 5 books be placed on a shelf if 2 are identical?" Items: 5, all being arranged, order matters, with one repeat of 2 → `5!/2! = 60`. "How many 3-topping pizzas from 8 toppings?" Choosing 3 of 8, order irrelevant, no repeats → `8C3 = 56`.

## Circular arrangements
covers: 156

Seating `n` people around a circle gives `(n - 1)!` arrangements rather than `n!`. A circle has no fixed starting point, so rotating everyone by one seat produces the same arrangement — which means each distinct seating has been counted `n` times, and `n!/n = (n - 1)!`.

The practical method: fix one person in place, then arrange the remaining `n - 1` around them.

### Example
5 people in a row: `5! = 120`. The same 5 around a round table: `4! = 24`. If the seats are numbered — or if the arrangement can be flipped over, as with a bracelet — the count changes again, so read the question carefully.

## When is nCr largest?
covers: 157

For a fixed `n`, the number of combinations peaks when `r` is half of `n`. Choosing about half the items gives the most possible groups, and the counts fall away symmetrically toward `r = 0` and `r = n`, which each have exactly one.

If `n` is odd there is no exact half, so two neighbouring values of `r` tie for the maximum.

### Example
With `n = 6`, the counts run 1, 6, 15, 20, 15, 6, 1 — the maximum is 20 at `r = 3`. With `n = 7` they run 1, 7, 21, 35, 35, 21, 7, 1, so `r = 3` and `r = 4` tie at 35.

## Probability that both A and B happen
covers: 158

For **independent** events — where one happening does not change the odds of the other — multiply:

`P(A and B) = P(A) x P(B)`

If the events are not independent, use the conditional version `P(A) x P(B given A)`.

### Example
Two fair coin flips both landing heads: `1/2 x 1/2 = 1/4`. But drawing two aces from a deck *without replacement* is not independent: `4/52 x 3/51 = 1/221`, not `(4/52)^2`.

### Watch out
"Without replacement" is the flag for dependence. The second probability must account for what the first draw removed.

## Probability that A or B happens
covers: 159

`P(A or B) = P(A) + P(B) - P(A and B)`. It is inclusion–exclusion again: adding the two probabilities double-counts the outcomes where both occur, so subtract that overlap once.

### Example
Rolling a die, `P(even) = 3/6` and `P(greater than 3) = 3/6`. The overlap (4 or 6) is `2/6`. So `P(even or greater than 3) = 3/6 + 3/6 - 2/6 = 4/6 = 2/3` — matching the list 2, 4, 5, 6.

## Independent versus mutually exclusive
covers: 160

These sound similar and mean opposite things. **Independent** events do not affect each other's chances, so `P(A and B) = P(A) x P(B)`. **Mutually exclusive** events cannot both happen, so `P(A and B) = 0` and `P(A or B) = P(A) + P(B)`.

A consequence worth remembering: for mutually exclusive events `P(A) + P(B) <= 1`, because probabilities summing past 1 would force an overlap.

### Example
Two coin flips are independent (both can be heads). Drawing one card that is both a king and a queen is mutually exclusive. Note that two events with non-zero probability cannot be both independent and mutually exclusive — if they cannot co-occur, knowing one happened tells you a great deal about the other.

## Conditional probability
covers: 161

`P(A | B) = P(A and B)/P(B)` — the chance of A *given that* B has happened. Conditioning on B shrinks the world to just the outcomes where B occurred, so you re-scale by dividing by `P(B)`.

### Example
Roll a die; what is the probability it is a 2 given that it is even? `P(2 and even) = 1/6`, `P(even) = 1/2`, so `P(2 | even) = (1/6)/(1/2) = 1/3`. That matches intuition: among 2, 4, 6, one of the three is a 2.

### Watch out
`P(A | B)` and `P(B | A)` are different numbers. The probability of being even given a roll of 2 is 1, not 1/3.

## "At least one" via the complement
covers: new

Questions asking for the probability of "at least one" are almost always faster backwards: compute the probability that it never happens and subtract from 1.

`P(at least one) = 1 - P(none)`

Counting the direct way means adding the cases for exactly one, exactly two, exactly three … whereas the complement is a single multiplication.

### Example
Flip a coin 4 times; what is the probability of at least one head? `P(no heads) = (1/2)^4 = 1/16`, so the answer is `15/16`. The direct route would have needed four separate cases.

### Watch out
The complement of "at least one" is "none", not "exactly one". Likewise the complement of "at least two" is "zero or one" — both of which you must subtract.
