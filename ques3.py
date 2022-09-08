l=int(input("Enter length of first side :"))
b=int(input("Enter length of second side :"))
h=int(input("Enter length of third side :"))
print("\n check given triangle is isosceles triangle enter : a")
print("check given triangle is right triangle enter : b")
print("check given triangle is equilateral triangle enter : c")
print("for exit enter : d")
x=str(input("Enter one option for check :"))
match x:
    case 'a':
        if l is b or l is h or b is h:
            print("This is a isosceles triangle")
        else:
            print("This is not a isosceles triangle")
    case 'b':
        if l**2+b**2==h**2 or l**2==b**2+h**2 or b**2==l**2+h**2:
            print("This is a right angle triangle")
        else:
            print("This is not a right angle triangle")
    case 'c':
        if l==b==h:
            print("This is a equilateral triangle")
        else:
            print("This is not a equilateral triangle")
    case 'd':
        exit()
    case _:
        print("Default value")
            