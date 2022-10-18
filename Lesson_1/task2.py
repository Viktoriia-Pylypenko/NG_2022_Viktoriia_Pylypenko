#calculator

firstNumber = int(input("Enter the first value:"))
secondNumber = int(input("Enter the second value:"))

operationsOnNumbers = input("Select actions on numbers: +, -, *, /." )

#action on numbers
if operationsOnNumbers == "+":
    print("Sum:" + str(firstNumber + secondNumber))
elif operationsOnNumbers == "-":
    print("Minus:" + str(firstNumber - secondNumber))
elif operationsOnNumbers == "*":
    print("Multiplication:" + str(firstNumber * secondNumber))
elif operationsOnNumbers == "/":
    print("Division:" + str(firstNumber / secondNumber))
else:
    print("Please, select an mathematical sign for action on numbers.")

#end)
