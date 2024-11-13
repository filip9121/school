def find_absent_digits(mobile_number):
    # Set of all digits from 0 to 9
    all_digits = set("0123456789")

    # Convert the mobile number to a set of its digits
    present_digits = set(mobile_number)

    # Find the digits that are absent by subtracting present digits from all digits
    absent_digits = all_digits - present_digits

    # Return the sorted list of absent digits
    return sorted(absent_digits)

# Example usage
mobile_number = "9876543210"  # Test with a complete set of digits
absent = find_absent_digits(mobile_number)

if absent:
    print("Absent digits:", absent)
else:
    print("All digits are present.")