"""Hand-curated day-by-day grouping for the Quant mountain.

The Quant Notes sheet is only loosely ordered by topic, so the 16 daily groups
below were assembled by hand: each day is a coherent block of concepts, and
consecutive days flow from one topic into the next (number properties ->
factors/factorials -> series -> fractions/percents -> exponents -> algebra ->
coordinate geometry -> plane geometry -> statistics -> counting -> probability).

Concepts are referenced by their title in column A of the sheet (normalised:
lower-cased, whitespace collapsed), so the mapping survives rows being moved
around.  Any concept in the sheet that is not listed here is reported by
scripts/build_data.py and appended to the smallest day, so nothing is ever
silently dropped.
"""

QUANT_GROUPS = [
    (
        "Strategy & Number Basics",
        [
            "How much is 540 sq feet in sq meters? (3.28 ft to a meter)",
            "Always keep in mind units",
            "Equal/Not Equal strategy for comparison",
            '"No Math Needed" strategy',
            "Pattern Recognition Strategy",
            "Unit digit?",
            "Note: floor of negative numbers",
            "Quotient and remainder",
            "Quotient and remainder for negative numbers",
            "Remainder of sums is sum of remainders",
        ],
    ),
    (
        "Unit Digits & Divisibility Rules",
        [
            "Unit digits from exponents",
            "unitdigit(a^b) = unitdigit((unitdigit(a))^b)",
            "Unit digit of exponent sums",
            "Unit digit of 3 + 3^2 + 3^3 + ... + 3^50?",
            "Find remainder of large exponent a^b divided by small number n",
            "Divisibility rule of 3",
            "Divisibility rule of 4",
            "Divisibility rule of 6",
            "Divisibility rule of 8",
            "Divisibility rule of 9",
        ],
    ),
    (
        "Primes, Factors & GCF",
        [
            "Divisibility rule of 11",
            "Test whether a number n is prime",
            "Three consecutive integers",
            "Divisibility derivation",
            "How many factors does have a number have?",
            "How many odd factors of a number?",
            "How many even factors of a number?",
            "Find GCF of group of numbers",
            "How many shared factors of group of numbers",
            "Find LCM of group of numbers",
        ],
    ),
    (
        "LCM, Factorials & Legendre's Method",
        [
            "LCM Divisibility rule",
            "GCF and LCM relation",
            "Factorial division m!/n!",
            "How many factors does a factorial have?",
            "How to do Legendres method for n!",
            "Legendres trick",
            "How many of a certain number r in a factorial n!?",
            "Largest factor r of factorial n!",
            "How many trailing zeroes at the end of factorial?",
            "Smallest non-prime numbers that are not factor of factorial n!",
            "Number of combinations from n numbers",
        ],
    ),
    (
        "Intervals, Sequences & Series",
        [
            "# of integers in interval",
            "Sum of integers in an interval",
            "Number of multiples of r in a interval (a, b)",
            "Sum of multiples of r in an interval (a, b)",
            "Types of sequences: arithmetic, geometric, quadratic, cubic",
            "Series formulas for exponents",
            "Series formula for geometric sequence sums",
            'Sum of "trick" series like 1, -2, 3, -4 ...',
            "Sum of complicated series: a1 + a2 + ... + an",
            "Trick series comparison",
        ],
    ),
    (
        "Fractions, Decimals, Percents & Rates",
        [
            "Difference between repeating and non-repeating decimals",
            "How to know if a decimal terminates",
            "How to convert repeating decimal to a fraction",
            "Smallest positive integer to multiply with a/b to result in an integer",
            "Proportions and cross-multiplications of proportions",
            "Simple Interest formula",
            "Compound Interest formula",
            "Compound Interest formula (compounds multiple times a year)",
            "Compound decrease formula",
            "Speed and time formulas.",
            "Relative speeds",
        ],
    ),
    (
        "Exponents, Roots & Radicals",
        [
            "Exponent rule: exponent of an exponent.",
            "Exponent rule: multiplied exponents when exponents are the same",
            "Exponent rule: multiplied exponents when bases are the same.",
            "Exponent rule: division when bases are the same",
            "Instead of radicals, represent roots as fraction exponents to solve problems",
            "How to check if root(n) is rational",
            "Simplifying roots",
            "Radicals (roots) in denominators",
            "Trickiness: even exponent under even radical (root)",
        ],
    ),
    (
        "Polynomials & Quadratic Equations",
        [
            "Polynomial degree",
            "Algebraic Identities: Quadratic",
            "Linear equation",
            "Requirements for polynomials",
            "Perfect square trinomial to simplify polynomial expressions",
            "When simplifying algebraic expressions, calculate the domain pre-simplification",
            "Absolute value equations should be split into 2 equations",
            "How many solutions does a quadratic equation have?",
            "Completing the square",
        ],
    ),
    (
        "Inequalities & Functions",
        [
            "Inequality rule",
            "Subtracting inequalities",
            "Absolute values and inequalities",
            "Inequality scope confusion",
            "Function that has expression in input",
            "Function that references itself in output",
            "How to find range of function",
            "Even functions",
            "Odd functions",
        ],
    ),
    (
        "Graphing: Parabolas, Lines & Circles",
        [
            "Graphing perfect square quadratics",
            "Shifting parabola rules: y = (x - h)^2",
            "Shifting parabola rules: y = (x+ h)^2",
            "Shifting parabola rules: y = x^2 + k",
            "Shifting parabola rules: y = x^2 - k",
            "Graphing quadratics by completing the square",
            "Intercept signs",
            "Slope of perpendicular lines",
            "Circle equations",
            "How to know if equation makes a circle",
        ],
    ),
    (
        "Reflections, Rotations & Angles",
        [
            "Reflecting point on axes/origin.",
            "Reflecting point (x, y) on line x = k.",
            "Reflecting point (x, y) on line y = k.",
            "Reflecting point (x, y) on line y = x.",
            "Rotating point (x, y) about origin: 90 degrees anti-clockwise",
            "Rotating point (x, y) about origin: 90 degrees clockwise",
            "Rotating point (x, y) about origin: 180 degrees",
            "Complementary and supplementary angles",
            "Sum of interior angles of a polygon with no of sides n",
            "Sum of exterior angles of any polygon",
        ],
    ),
    (
        "Polygons, Quadrilaterals & Triangles",
        [
            "Regular polygons",
            "Types of quadrilaterals: parallelogram, rhombus, rectangle, square, trapezoid",
            "Trapezoid rule",
            "Inscribed and circumscribed shapes",
            "Relationship between angles and side length",
            "Triangle Inequality",
            "When are 3 triangles congruent",
            "30-60-90 triangles (ie. the 3 angles are 30, 60, 90)",
            "45-45-90 trianges (isosceles right triangles)",
            "Look to split triangles up into 30-60-90 and 45-45-90 to solve",
            "Similar triangles (AAA)",
            "Common pythagorean triplets (remember: all multiples are triplets too)",
        ],
    ),
    (
        "Area, Perimeter, Volume & Surface Area",
        [
            "Area of equilateral triangle with side length s",
            "Area of parallelogram",
            "Area of trapezoid",
            "Area of a regular polygon with number of sides n",
            "Comparing area of two shapes with same sides same perimeter",
            "The regular hexagon with side length s inscribed in a circle with radius r rule",
            "Relationship between perimeter and area and regular shapes",
            "Volume and surface area of a cylinder",
            "Relationship between volume and surface area and regular shapes",
            "Longest diagonal",
            "Longest diagonal of a rectangular solid",
            "Trick related to shapes stacking in other shapes",
        ],
    ),
    (
        "Averages, Mixtures & Standard Deviation",
        [
            "Mixture problems: Find % of important substance in final mixture",
            "The mixture trick: finding ratio of 2 mixtures",
            "Finding the median of a symmetrical sequence",
            "Measures of positions of sequences",
            "Variance",
            "Standard deviation",
            "Population vs Sample standard deviation",
            "How standard deviation changes with sequence transformations",
            "Standardization of a sequence",
        ],
    ),
    (
        "Sets & Counting Principles",
        [
            "Sets vs Lists",
            "Inclusion-Exclusion principle",
            "Inclusion-Exclusion principle for 3 sets",
            "Multiplication method for choice in combos",
            "When to add in permutations/combinations and when to multiply?",
            "Optional choice in combos",
            "Number of correct combinations pick r out of n options",
            "Number of correct permutations (order matters) pick r out of n",
            "Permutations using the multiplication method",
            "Permutations with restrictions",
        ],
    ),
    (
        "Advanced Counting & Probability",
        [
            "Permutations with repeats, n slots, a and b repeats.",
            "Permutations with repeats with restrictions",
            "Combinatorics Problems",
            "Permutations in a circle with n options",
            "Highest possible combinations given n options and r choices",
            "P(A n B): Intersect aka probability both A and B occur",
            "P(A u B): Union aka probability at least one of A or B occur",
            "Independent events and mutually exclusive events",
            "Conditional probability P(A | B)",
            "Memorize standard deviation probability under normal distribution (should be able to draw given chart from memory)",
        ],
    ),
]

VOCAB_GROUP_COUNT = 16
QUANT_GROUP_COUNT = len(QUANT_GROUPS)
