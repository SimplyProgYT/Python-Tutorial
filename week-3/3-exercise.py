# Basic calculator algorithm

num1 = int(input("Please enter an integer: "))
num2 = int(input("Please enter an integer: "))
operation = str(input("Please choose an operaiton (+, -, *, /)"))

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 == 0:
        print("Invalid!")
    else:
        if num1 == num2:
            print("1")
        else:
            print(num1 / num2)
else:
    print("Invalid operation")