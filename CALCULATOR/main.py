try:

    a = int(input("Enter the first number:"))
    b= int(input("Enter the number:"))

    print("What kind of operation do you want to perform.Press + for addition\n Press - for subtraction\n Press/ for division\n Press * for multiplication")

    o= input("Enter Operation:")
    match o:
        case"+":
            print(f"The Result id: {a+b}")
        case"-":
            
            print(f"The Result id: {a-b}")

        case"*":
            print(f"The Result id: {a*b}")

        case"/":
            print(f"The Result id: {a/b}")

except Exception as e:
    print("ENter a valid value of a and b")
                        
                        
                        
            