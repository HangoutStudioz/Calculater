Num1 = int(input("Enter Your Number:"))
Num2 = int(input("Enter Your Second Number:"))
Symbol = input("Enter Your Symbol:")
def Addition(a , b):
    print(a+b)
    return Addition
def Subtract(a , b):
    print(a-b)
    return Addition
def Multiply(a , b):
    print(a*b)
    return Multiply
def Division(a , b):
    print(a/b)
    return Division
if Symbol == "+":
    Addition(Num1, Num2)
elif Symbol == "-":
    Subtract(Num1, Num2)
elif Symbol == "*":
    Multiply(Num1, Num2)
elif Symbol == "/":
    Division(Num1, Num2)