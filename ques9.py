print("a.Non century leap year","b.Century leap year","c.Non century non leap year","d.Century non leap year",sep="\n")
x=input("Enter one option to check :")
year=int(input("Enter year :"))
match x:
    case 'a' if year%400!=0:
        print(year,"Non century leap year")
    case 'b' if year%400==0:
        print(year,"Century leap year")
    case 'c' if year%100!=0 and year%4!=0:
        print(year,"Non century non leap year")
    case 'd' if year%100==0 and year%4!=0:
        print(year,"Century non leap year")
        

