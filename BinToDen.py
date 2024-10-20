BinaryNumber = "101011011"
DenaryNumber = 0
exponent = 1

for bit in BinaryNumber[::-1]: #[::-1] will itterate through the BinaryNumber right to left (inverted itteration)
    if bit == "1":
        DenaryNumber += exponent
    exponent *= 2

print(DenaryNumber)