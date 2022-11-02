# File: quadratic.py

import math

def quadratic_roots(a, b, c):
    d = b**2 - (4 * a * c)  # discriminant
    if d < 0:
        print('Error: Roots are imaginary')
        return None, None
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    return x1, x2

if __name__ == '__main__':
    # Test the function quadratic_roots()
    x1, x2 = quadratic_roots(2, 5, 1)
    print('Real unequal roots:', x1, x2)
    x1, x2 = quadratic_roots(1, 2, 1)
    print('Real equal roots:', x1, x2)
    x1, x2 = quadratic_roots(5, 1, 2)
    print('Imaginary roots:', x1, x2)
