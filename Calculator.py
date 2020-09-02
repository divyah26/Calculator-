class Calc:

    '''def __init__(self):
        pass'''

    def add(x, y):
        return x + y

    def minus(x, y):
        return x - y

    def multiple(x, y):
        return x * y

    def devide(x, y):
        return x/y

a=int(input("Enter first number: "))

b=int(input("Enter second number: "))
choice=1

while choice!=0:
    print("0. Exit")

    print("1. Add")

    print("2. Subtraction")

    print("3. Multiplication")

    print("4. Division")

    choice=int(input("Enter choice: "))

    if choice==1:
        c=Calc.add(a, b)
        print("Result: ",c)

    elif choice==2:
        c=Calc.minus(a, b)
        print("Result: ",c)
        #print("Result: ",minus())

    elif choice==3:
        c=Calc.multiple(a, b)
        print("Result: ",c)

        #print("Result: ",multiple())

    elif choice==4:
        c=Calc.divide(a, b)
        print("Result: ",c)

        #print("Result: ",round(divide(),2))

    elif choice==0:

        print("Exiting!")
