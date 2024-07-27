def addition(x,y):
    print(x+y)
    
def subtraction(x,y):
    print(x-y)
    
def multiplication(x,y):
    print(x*y)
    
def division(x,y):
    if y==0:
        print("Y should be greater then zero")
    else:
        print(x/y)
    
def calculator():
    print("--------------------Simple Calculator--------------------")
    print("Choose which operation want to operate:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
calculator()

choice=input("Enter Your Choice: \t")

x= float(input("Enter the value for the x:\t"))
y= float(input("Enter the value for the y:\t"))  

if  choice=="1":
    addition(x,y)
elif choice=="2":
    subtraction(x,y)
elif choice=="3":
    multiplication(x,y)
elif choice=="4":
    division(x,y)
else:
    print("Invalid Input...! Please Enter the valid Input 1/2/3/4?\t")
    
again=input("If you want calculate again? (yes/no):\t")

if again.lower()=="yes":
    calculator()
    choice=input("Enter Your Choice: \t")

    x= float(input("Enter the value for the x:\t"))
    y= float(input("Enter the value for the y:\t"))  

    if  choice=="1":
        addition(x,y)
    elif choice=="2":
        subtraction(x,y)
    elif choice=="3":
        multiplication(x,y)
    elif choice=="4":
        division(x,y)
    else:
        print("Invalid Input...! Please Enter the valid Input 1/2/3/4?\t")
else:
    print("Thank You...! Have a nice day...! :)")