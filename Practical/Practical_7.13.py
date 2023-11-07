# Task 13

# Write some code that iterates over the contents of the roots dictionary
# created within an earlier task. For each entry, print the message -
# “The square root of <num> is <sqrt>”
# Where <num> shows the number, and <sqrt> shows the square root of that number.

import math

roots = {n: math.sqrt(n) for n in range(1, 26)}
for item, level in roots.items():
    print("The square root of ", item, "is", round(level, 3))

# Output:

# The square root of  1 is 1.0
# The square root of  2 is 1.414
# The square root of  3 is 1.732
# The square root of  4 is 2.0
# The square root of  5 is 2.236
# The square root of  6 is 2.449
# The square root of  7 is 2.646
# The square root of  8 is 2.828
# The square root of  9 is 3.0
# The square root of  10 is 3.162
# The square root of  11 is 3.317
# The square root of  12 is 3.464
# The square root of  13 is 3.606
# The square root of  14 is 3.742
# The square root of  15 is 3.873
# The square root of  16 is 4.0
# The square root of  17 is 4.123
# The square root of  18 is 4.243
# The square root of  19 is 4.359
# The square root of  20 is 4.472
# The square root of  21 is 4.583
# The square root of  22 is 4.69
# The square root of  23 is 4.796
# The square root of  24 is 4.899
# The square root of  25 is 5.0