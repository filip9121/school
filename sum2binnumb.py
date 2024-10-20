def sum_binary(bin1, bin2):
    # Step 1: Convert binary strings to integers
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    
    # Step 2: Add the two integers
    total = num1 + num2
    
    # Step 3: Convert the result back to binary (bin() returns a string with '0b' prefix)
    binary_result = bin(total)[2:]  # [2:] to remove the '0b' prefix
    
    # Step 4: Return the binary result
    return binary_result

# Example usage:
bin1 = "1010101010101010101010101010101"
bin2 = "1111111111111111111111111111111"

result = sum_binary(bin1, bin2)
print(result)  # Output: 11010101010101010101010101010110
