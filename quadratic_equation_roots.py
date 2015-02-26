# Computes the smaller root of a quadratic equation.

import math

def smaller_root (a, b, c):
    d = b ** 2 - 4 * a * c # d - discriminant associated with the given equation
    if d < 0:
        return "Error: No real solutions"
    sqrt_d = math.sqrt(d)
    if d == 0:
        x = (-b + sqrt_d) / (2 * a)
        return "The only solution is " + str(x)
    else:
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        if (x1 > x2):
            return x2
        else:
            return x1

# Test
# Expected results: Error, -2.2360679775, Error, The only solution

print smaller_root(1, 2, 3)
print smaller_root(2, 0, -10)
print smaller_root(6, -3, 5)
print smaller_root (1, -6, 9)


