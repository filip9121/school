def euclid_gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Replace a with b, and b with the remainder of a divided by b
    return a

# Example usage:
num1 = 56
num2 = 98
gcd = euclid_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd}")
