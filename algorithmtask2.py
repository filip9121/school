import cmath  # To handle complex roots

def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c  # Discriminant
    root1 = (-b + cmath.sqrt(d)) / (2*a)
    root2 = (-b - cmath.sqrt(d)) / (2*a)
    return root1, root2

# Example usage
a, b, c = map(float, input("Enter coefficients a, b, c: ").split())
print("Roots:", solve_quadratic(a, b, c))
