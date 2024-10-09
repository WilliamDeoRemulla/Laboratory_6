age = int(input("Enter your age: "))
member = input("Are you a member?: ")
if age<18:
    if member==str("yes") :
        print("Fee: 450.00 Php")
    if member==str("no") :
        print("Fee: 650.00 Php")
if age>=18 and age<=65:
    if member==str("yes") :
        print("Fee: 550.00 Php")
    if member==str("no") :
        print("Fee: 750 Php")
if age>65:
    if member==str("yes") :
        print("Fee: 400 Php")
    if member==str("no") :
        print("Fee: 600 Php")