print("Factorial Program")
number = eval(input("Please enter any number ---> "))
factorial = 1
for i in range(number, 0, -1):
    factorial *= i
print("The factorial of", number, " is ", factorial)
