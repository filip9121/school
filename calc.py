while True:
    try:
        Num1 = int(input("Please state the first number"))
        Operator = input("Please state the operation")
        Num2 = int(input("Please state the second number"))
    except: 
        print("Please give only numbers!")
        pass
    if Operator == "+":
        print(Num1 + Num2)
    elif Operator == "-":
        print(Num1-Num2)
    elif Operator == "*":
        print(Num1*Num2)
    elif Operator == "/":
        print(Num1/Num2)
    else: print("Wrong operator")
