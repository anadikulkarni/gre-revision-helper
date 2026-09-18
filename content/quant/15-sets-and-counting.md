# Sets & Counting

## Set versus list — what is the difference?
covers: 143

### Answer
A **set** is unordered with no duplicates, written `{2, 5, 9}`, and can be infinite; its size is `|S|`. A **list** is ordered, allows duplicates, and is finite.

### Explanation
The distinction decides which tool applies: sets lead to combinations and inclusion–exclusion, lists lead to permutations.

### Example
`{1, 2, 3}` and `{3, 2, 1}` are the same set, but the lists (1, 2, 3) and (3, 2, 1) differ. `{1, 1, 2}` is just `{1, 2}` with two elements, while the list (1, 1, 2) has three entries.

## Inclusion–exclusion for two groups?
covers: 144

### Answer
`|A or B| = |A| + |B| - |A and B|` — add the two, subtract the overlap you counted twice.

### Explanation
The rearranged form is the one exams use: knowing the total and both groups gives you the overlap.

### Example
30 students, 18 take French, 15 Spanish, everyone takes at least one. `30 = 18 + 15 - both` → **3** take both. If 4 took neither, use `30 - 4 = 18 + 15 - both` → 7.

### Watch out
Check whether the total includes people in **neither** group — remove them before applying the formula.

## Inclusion–exclusion for three groups?
covers: 145

### Answer
`|A or B or C| = |A| + |B| + |C| - |A and B| - |B and C| - |A and C| + |A and B and C|`

If instead you are told how many are in **exactly** two groups:
`total = |A| + |B| + |C| - (exactly two) - 2 x (all three)`

### Explanation
The pairwise subtractions remove the triple overlap once too often, so the standard version adds it back. Which formula you need depends entirely on the wording, so settle that first.

### Example
40 students: 20 football, 18 basketball, 16 tennis, 8 football+basketball, 6 basketball+tennis, 5 football+tennis, 3 all three. `20+18+16-8-6-5+3 = 38` play at least one, so 2 play none.

### Watch out
"8 play football and basketball" normally means *at least* those two, including anyone who also plays tennis. "Only football and basketball" is the other formula.

## Several independent choices in a row — how many outcomes?
covers: 146

### Answer
Multiply the options at each stage: `a x b x c ...`

### Explanation
The multiplication principle is the backbone of every counting question; extend it to as many stages as you like.

It also covers repeats: choosing from `n` options `r` times **with** repetition gives `n^r`, because every stage still has all `n` options available.

### Example
4 starters and 3 mains → 12 meals; add 2 desserts → 24. A 4-digit PIN from 10 digits with repeats allowed → `10^4 = 10,000`.

A 3-letter code from 26 letters with repeats allowed: `26^3 = 17,576`. Without repeats: `26 x 25 x 24 = 15,600`.

## When do you add possibilities, and when do you multiply?
covers: 147

### Answer
**AND → multiply** (both stages happen). **OR → add** (one or the other, not both).

### Explanation
Label each branch of the problem before computing; most complex counting questions are just a tree of these two operations.

### Example
A to B by 3 roads then B to C by 4 roads: both legs needed → `3 x 4 = 12` routes. But if you may go to C by one of 3 roads **or** one of 4 others → `3 + 4 = 7`.

### Watch out
If "or" allows both to happen, adding double-counts — go back to inclusion–exclusion.

## Optional extras, and "at least one" — how do you count them?
covers: 148

### Answer
Each optional item is a two-way choice (in or out), so `n` options give `2^n` combinations. For "at least one", count everything and **subtract the case where nothing was chosen**.

### Explanation
Count-all-then-subtract-the-bad-case is the standard move for "at least" questions, and it is almost always faster than counting the good cases.

### Example
4 ice-cream flavours with 4 optional toppings: `4 x 2 x 2 x 2 x 2 = 64`. If at least one topping is compulsory, remove the 4 no-topping cases: **60**.

## Choosing `r` from `n` where order does **not** matter?
covers: 149

### Answer
`nCr = n!/(r!(n - r)!)`

### Explanation
The `r!` divides out the orderings of the same chosen group — which is exactly what "order does not matter" means. Note the symmetry `nCr = nC(n-r)`: choosing 3 to include is choosing 7 to exclude.

### Example
3-person committees from 10 people: `10C3 = (10 x 9 x 8)/(3 x 2 x 1) = 120`.

### Watch out
The giveaway words are committee, group, handshake, selection — anything where swapping two members changes nothing.

## Choosing `r` from `n` where order **does** matter?
covers: 150

### Answer
`nPr = n!/(n - r)!` — which is `nCr` times `r!`.

### Explanation
Each chosen group can be arranged in `r!` ways, so permutations always outnumber combinations by that factor.

The relationship is worth holding onto: `nPr = nCr x r!`. Whenever you can count the groups, multiply by `r!` to get the ordered count.

### Example
Gold, silver, bronze among 10 runners: `10P3 = 10 x 9 x 8 = 720`, six times the 120 committees, because each trio can stand on the podium in `3! = 6` orders.

Arranging 2 of 5 books on a shelf: `5P2 = 20`. Choosing 2 of 5 to take on holiday: `5C2 = 10` — exactly half, since each pair has `2! = 2` orders.

### Watch out
Ranking, order, podium, "president and treasurer", password → permutation.

## Counting arrangements without any formula?
covers: 151

### Answer
The **slot method**: draw a blank for each position, write how many options it has, multiply. Each item used reduces the next slot by one.

### Explanation
It is the formula in disguise, but far harder to misapply — and it extends naturally to restricted positions.

The slot method is also the only practical approach once restrictions appear, because you can fill the constrained slots first and let the rest follow.

### Example
Arranging ABCDE: `5 x 4 x 3 x 2 x 1 = 120`, matching `5P5`. Taking only the first three letters: `5 x 4 x 3 = 60 = 5P3`.

How many 3-digit numbers have no repeated digits? The first slot cannot be 0, so `9 x 9 x 8 = 648`.

## Arrangements with a restriction on some positions?
covers: 152

### Answer
Fill the **restricted slots first**, then the rest by the slot method. Separate scenarios are **added**; simultaneous stages are **multiplied**.

### Explanation
Two standard tricks: to keep items **together**, glue them into one block and arrange the blocks (then multiply by the arrangements inside the block); to keep items **apart**, count everything and subtract the arrangements where they are together.

### Example
4-digit numbers from 1–7, no repeats, must be even. The last slot must be 2, 4 or 6 → 3 options; the other three slots take the remaining digits → `6 x 5 x 4 = 120`. Total `3 x 120 = 360`.

## Arranging `n` items when some are identical?
covers: 41, 153

### Answer
`n!/(a! b! ...)`, dividing by the factorial of each repeat count.

### Explanation
Swapping two identical items produces no new arrangement, so the plain `n!` overcounts by exactly those internal orderings.

### Example
BANANA: `n = 6` with three As and two Ns → `6!/(3! 2!) = 720/12 = 60`. A word with no repeats, like ABCDEF, keeps the full `6! = 720`.

### Watch out
Divide by each repeat's factorial **separately**: three As and two Ns means `3! x 2! = 12`, not `5!`.
