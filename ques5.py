a=int(input("Enter number :"))
match a:
    case a if a%2==0:
        print("Saurabh shukla")
    case a if a%2==1 and a>0:
        print("Aditiya Choudhary")
    case a if a%2==1 and a<0 :
        print("Prateek Jain")