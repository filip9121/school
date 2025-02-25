number = 2
power = 10

def RecursePower(number, power):
    if power > 1:
        return(number *RecursePower(number,power-1))
    else:
        return(number)


print(RecursePower(number,power))