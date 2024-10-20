DenaryNumber = 200
BinaryNumber = ""
while DenaryNumber>0:
    BinaryNumber = str(DenaryNumber%2) + BinaryNumber
    DenaryNumber //= 2
print(BinaryNumber)