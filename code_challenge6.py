print("Please enter 7 numbers")

result = 0
for odd in range(1, 8, 1):
    number = eval(input("Please enter any number ---> "))
    if number % 2:
        result += number
    
print("The total sum of all odd number is:", total)
