number1 = input("введи число:\n")
sign = input("введи знак:\n")
number2 = input("введи второе число:\n")

number1 = int(number1)
number2 = int(number2)

if sign == '+':
    answer = number1 + number2

if sign == '-':
    answer = number1 - number2

if sign == '*':
    answer = number1 * number2

if sign == '/':
    answer = number1 / number2

print(number1, sign, number2, " = ", answer)

