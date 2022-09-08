s=input("Enter a string :").strip()
match s:
    case s if ' ' in s:
        print("Multi word String")
    case s if ' ' not in s:
        print("Single word String")