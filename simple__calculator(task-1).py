print("welcome to calculator")

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x//y

print("select an operation")
print("1 for add")
print("2 for sub")
print("3 for mul")
print("4 for div")
print("5 for mod")

while True:
    choice=input("enter choice")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        if choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))
        if choice == '3':
            print(num1, "*", num2, "=", mul(num1, num2))
        if choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))
        if choice == '5':
            print(num1, "//", num2, "=", mod(num1, num2))
    else:
        print("invalid input")