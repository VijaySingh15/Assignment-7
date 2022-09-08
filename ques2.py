print("For addition operation enter 1","For Substraction operation enter 2","For Multiplication operation enter 3","For Division operation enter 4",sep="\n")
x=int(input("Enter operation number :"))
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
match x:
    case 1:
        print("Addition is :",a+b)
    case 2:
        print("Substraction is :",a-b)
    case 3:
        print("Multiplication is :",a*b)
    case 4:
        print("Division is :",a/b)
    case _:
        print("Default value")