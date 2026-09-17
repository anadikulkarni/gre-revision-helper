# Sets & Counting

## Sets versus lists
covers: 143

A **set** is an unordered collection with no duplicates, written in braces `{2, 5, 9}`, and it may be infinite. Its size is written `|S|`. A **list** is ordered, may repeat values, and is always finite.

The distinction decides which counting tool applies: questions about sets lead to combinations and inclusion–exclusion, questions about lists lead to permutations.

### Example
`{1, 2, 3}` and `{3, 2, 1}` are the same set; the lists (1, 2, 3) and (3, 2, 1) are different. `{1, 1, 2}` is really just `{1, 2}` with two elements, whereas the list (1, 1, 2) genuinely has three entries.

## Inclusion–exclusion for two sets
covers: 144

Add the two group sizes and subtract the overlap, which you have otherwise counted twice:

`|A or B| = |A| + |B| - |A and B|`

Rearranged, it also finds the overlap when you know the total, which is the more common exam form.

### Example
In a class of 30, 18 take French and 15 take Spanish, and everyone takes at least one. How many take both? `30 = 18 + 15 - both`, so `both = 3`. If instead 4 students took neither, the equation becomes `30 - 4 = 18 + 15 - both`, giving 7.

### Watch out
Read carefully whether the total includes people in *neither* group. Those have to be removed before the formula applies.

## Inclusion–exclusion for three sets
covers: 145

With three groups the formula extends by adding back the triple overlap, which the pairwise subtractions removed once too often:

`|A or B or C| = |A| + |B| + |C| - |A and B| - |B and C| - |A and C| + |A and B and C|`

There is a second version, used when a question tells you how many are in **exactly** two groups rather than at least two:

`total = |A| + |B| + |C| - (exactly two) - 2 x (all three)`

Which one you need depends entirely on the wording, so identify that first.

### Example
40 students, 20 play football, 18 basketball, 16 tennis, 8 play football and basketball, 6 basketball and tennis, 5 football and tennis, and 3 play all three. Then `20+18+16-8-6-5+3 = 38` play at least one, so 2 play none.

### Watch out
"8 play football and basketball" normally means *at least* those two, including anyone who also plays tennis. If the question says "only football and basketball", use the second formula.

## The multiplication principle
covers: 146

If one choice has `a` options and an independent second choice has `b` options, the pair has `a x b` possible outcomes. Extend it to as many stages as you like by multiplying them all together — this is the backbone of every counting question.

### Example
A menu with 4 starters and 3 mains offers `4 x 3 = 12` two-course meals. Add 2 desserts and it becomes `4 x 3 x 2 = 24`. Likewise a 4-digit PIN using digits 0-9 with repeats allowed has `10^4 = 10,000` possibilities.

## AND means multiply, OR means add
covers: 147

Decide whether the stages happen **together** or **instead** of each other. If both must happen (this *and* that), multiply. If exactly one happens (this *or* that, but not both), add the possibilities.

Most complex counting questions are a tree of these two operations, so label each branch before computing.

### Example
Travel from A to B by 3 roads then B to C by 4 roads: both legs are needed, so `3 x 4 = 12` routes. But if you can travel to C by one of 3 roads **or** by one of 4 different roads, that is `3 + 4 = 7` routes.

### Watch out
If "or" allows both to happen, adding double-counts the overlap — go back to inclusion–exclusion.

## Optional choices, and "at least one"
covers: 148

Something that may be taken or left is a two-way choice: in or out. Give every optional item a factor of 2 and multiply as usual. For `n` optional extras that is `2^n` combinations, including the case where you take none.

To enforce "at least one", count everything and subtract the single case where nothing was chosen.

### Example
4 ice-cream flavours and 4 optional toppings: `4 x 2 x 2 x 2 x 2 = 64` combinations. If at least one topping is compulsory, remove the 4 no-topping cases: `64 - 4 = 60`.

### Watch out
This "count all, subtract the bad case" move is the standard answer to any "at least one" question, and it is almost always faster than counting the good cases directly.

## Combinations: choosing r from n
covers: 149

When order does **not** matter, the number of ways to choose `r` items from `n` is

`nCr = n!/(r!(n - r)!)`

The `r!` on the bottom divides out all the orderings of the same chosen group, which is exactly what "order does not matter" means.

### Example
How many 3-person committees from 10 people? `10C3 = 10!/(3!7!) = (10 x 9 x 8)/(3 x 2 x 1) = 120`. Note the useful symmetry `nCr = nC(n-r)`: choosing 3 to include is the same as choosing 7 to exclude.

### Watch out
The giveaway word is "committee", "group", "handshake" or "selection" — anything where swapping two members changes nothing.

## Permutations: arranging r from n
covers: 150

When order **does** matter, the count is

`nPr = n!/(n - r)!`

It is the combination count times `r!`, since each chosen group can be arranged in `r!` ways.

### Example
How many ways to award gold, silver and bronze among 10 runners? `10P3 = 10!/7! = 10 x 9 x 8 = 720`, six times the 120 committees above — because each group of three can be arranged on the podium in `3! = 6` ways.

### Watch out
Words like "ranking", "order", "podium", "president and treasurer" or "password" signal permutations.

## Permutations by the slot method
covers: 151

Rather than recall the formula, draw a blank for each position and fill in how many options it has, then multiply. Each item used up reduces the choices for the next slot by one.

### Example
How many ways to arrange the letters of ABCDE? Five slots: `5 x 4 x 3 x 2 x 1 = 120`, which matches `5P5 = 5!/0! = 120`. Choosing only the first three letters: `5 x 4 x 3 = 60 = 5P3`.

## Permutations with restrictions
covers: 152

Handle the restricted positions first, then fill in the rest with the slot method. If a restriction splits into separate scenarios, count each scenario fully and **add** them; if the restrictions apply simultaneously, **multiply** the stage counts.

Two standard tricks: to keep items together, glue them into one block and arrange the blocks (then multiply by the arrangements inside the block); to keep items apart, count everything and subtract the arrangements where they are together.

### Example
How many 4-digit numbers can be made from 1-7 with no repeats if the number must be even? The last slot must be 2, 4 or 6 → 3 options; the remaining three slots take any of the leftover 6 digits: `6 x 5 x 4 = 120`. Total `3 x 120 = 360`.
