print("THE MULTIPLICATION TABLE MAKER")
number = eval(input("Please enter any number --> "))

print("Multiplication table for: ", number)

for m in range(1, 11, 1):
    result = number * m
    print(number, "×", m, "=", result)
