GivenNumber = 125
AmountOfZeroes = 0
while GivenNumber > 4:
    AmountOfZeroes += GivenNumber // 5
    GivenNumber //= 5
print (AmountOfZeroes)