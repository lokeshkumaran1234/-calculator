a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
for i in range(5):
    print("Calculator menu")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        c=a+b
        print("Sum:",c)
    elif choice==2:
        c=a-b
        print("Difference:",c)
    elif choice==3:
        c=a*b
        print("Product:",c)
    elif choice==4:
        c=a/b
        print("Quotient:",c)
    elif choice==5:
        break
    else:
        print("Invalid choice:")
