import math
import cmath  # To handle complex numbers when the discriminant is negative

def solve_quadratic(a, b, c):
    # Step 1: Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Step 2: Check the nature of the discriminant
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Two distinct real roots: {root1} and {root2}"
    
    elif discriminant == 0:
        # One real root (repeated root)
        root = -b / (2 * a)
        return f"One real root: {root}"
    
    else:
        # Two complex roots
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return f"Two complex roots: {root1} and {root2}"

# Example usage:
a = 1
b = -3
c = 2
result = solve_quadratic(a, b, c)
print(result)



