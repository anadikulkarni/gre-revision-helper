# Inequalities & Functions

## Multiplying or dividing by a negative flips the sign
covers: 81

Inequalities behave like equations for adding and subtracting, but multiplying or dividing both sides by a negative number reverses the direction of the sign. Picture the number line: negating reflects every number through zero, so whatever was on the left ends up on the right.

### Example
`-2x > 6`. Divide by -2 and flip: `x < -3`. Test it: `x = -4` gives `-2(-4) = 8 > 6` ✓, while `x = 0` gives `0 > 6` ✗.

### Watch out
The trap is dividing by a *variable* whose sign you do not know. From `ax > a` you cannot conclude `x > 1` unless you are told `a > 0`.

## Adding and subtracting inequalities
covers: 82

Two inequalities pointing the same way can always be added: if `a > b` and `c > d`, then `a + c > b + d`. Subtracting is only safe when they point in **opposite** directions, and the result keeps the sign of the one you subtract *from*.

Concretely, from `a > b` and `c < d` you may conclude `a - c > b - d`. The intuition: subtracting a smaller thing leaves you with more.

### Example
Given `5 < x < 9` and `1 < y < 4`, what is the range of `x - y`? Flip the second to `-4 < -y < -1` and add: `1 < x - y < 8`.

### Watch out
Never subtract two same-direction inequalities. From `x > 2` and `y > 1` you cannot say `x - y > 1`: take `x = 3, y = 10`.

## Absolute values in inequalities
covers: 83

Isolate the absolute value on the left, then split into two cases exactly as with equations — but when you negate the right-hand side, the inequality sign flips as well.

The two shapes are worth memorising as pictures. `|x| < a` means `-a < x < a`, a single band around zero. `|x| > a` means `x > a` **or** `x < -a`, two pieces heading outwards.

### Example
`|2x - 6| < 4` becomes `-4 < 2x - 6 < 4`, so `2 < 2x < 10`, giving `1 < x < 5`. By contrast `|2x - 6| > 4` gives `2x - 6 > 4` or `2x - 6 < -4`, i.e. `x > 5` or `x < 1`.

### Watch out
`|x - 3| < 5` is best read as "x is less than 5 away from 3", which immediately gives `-2 < x < 8`. Reading absolute value as distance prevents most sign errors.

## Sign charts for factored inequalities
covers: 84

An inequality like `(x + 3)(x - 2) > 0` has two critical values, -3 and 2, but the answer is not simply "x between them" or "x outside them" — you have to check. Mark the critical values on a line, then test one value in each of the three regions and see whether the product is positive or negative.

For a product of two factors: positive outside the roots, negative between them (when the leading coefficient is positive).

### Example
`(x + 3)(x - 2) > 0`. Test `x = -4`: `(-1)(-6) = +6` ✓. Test `x = 0`: `(3)(-2) = -6` ✗. Test `x = 3`: `(6)(1) = +6` ✓. So the solution is `x < -3` or `x > 2`.

### Watch out
Always move everything to one side first. Solving `(x+3)(x-2) > 6` by setting each factor against 6 is meaningless; expand, subtract 6, refactor, then test.

## Functions with an expression inside
covers: 85

When a function is defined as `f(something) = ...`, the rule tells you what happens to whatever the "something" evaluates to. To find `f(7)`, set the inside expression equal to 7, solve for `x`, and substitute that `x` into the right-hand side.

### Example
`f(x + 3) = x^2 + x`. What is `f(7)`? Set `x + 3 = 7`, so `x = 4`. Then the right side is `4^2 + 4 = 20`, so `f(7) = 20`. Substituting 7 directly for `x` would have given 56, the wrong answer the question is fishing for.

## Functions defined in terms of themselves
covers: 86

A recursive definition tells you how to get from one input to the next rather than giving values outright. Read it as a step rule, then walk from the value you are given to the value you want.

### Example
`f(x + 1) = 10 f(x)`, and `f(3) = 5`. What is `f(6)`? Each step up multiplies by 10: `f(4) = 50`, `f(5) = 500`, `f(6) = 5,000`. Three steps, so equivalently `f(6) = 5 x 10^3`.

### Watch out
Count the steps, not the numbers. From `f(3)` to `f(6)` is three steps, not six.

## Finding the range of a function
covers: 87

The range is the set of outputs the function can produce. A reliable method: set `y = f(x)`, rearrange to express `x` in terms of `y`, and then ask what values of `y` are legal in that new expression. Whatever `y` cannot be is missing from the range.

### Example
`y = (3 - x)/(x - 2)`. Multiply out: `y(x - 2) = 3 - x`, so `yx + x = 3 + 2y`, giving `x = (3 + 2y)/(y + 1)`. That is undefined at `y = -1`, so the range of the original function is every real number except -1.

### Watch out
Do not confuse range with domain. Here the *domain* excludes `x = 2` (the original denominator) and the *range* excludes `y = -1`.

## Even functions
covers: 88

A function is even when `f(-x) = f(x)`: feeding in the opposite input gives the same output. For polynomials that happens exactly when every power of `x` is even (a constant counts as `x^0`). Their graphs are mirror images across the y-axis.

### Example
`f(x) = x^2 + 3` is even: `f(-2) = 7 = f(2)`. `cos(x)` and `|x|` are even too. But `f(x) = x^2 + x` is not, because the `x` term is odd-powered: `f(-2) = 2` while `f(2) = 6`.

## Odd functions
covers: 89

A function is odd when `f(-x) = -f(x)`: flipping the input flips the sign of the output. For polynomials that means every power of `x` is odd and there is no constant term. Their graphs have 180° rotational symmetry about the origin.

### Example
`f(x) = x^3 - x` is odd: `f(-2) = -6` and `f(2) = 6`. Adding a constant breaks it — `x^3 + 1` is neither even nor odd, which is the usual state of affairs. Only `f(x) = 0` manages to be both.
