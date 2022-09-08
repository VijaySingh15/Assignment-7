col=input("Enter your favourite colour name :").lower()
match col:
    case col if 'red' in col:
        print("saturday")
    case col if 'yellow' in col:
        print("Monday")
    case col if 'blue' in col:
        print("Tuesday")
    case col if 'orange' in col:
        print("Wednesday")
    case col if 'white' in col:
        print("Thursday")
    case col if 'black' in col:
        print("Friday")
    case _:
        print("Sunday")
