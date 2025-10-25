name = input("Please enter your name --> ")
print("============\nTHIS IS THE ODD NUMBER SUMMATION, ENTER 0 TO STOP\n========")
sum = 0
odd = ""

while True:
    iya = eval(input("Please enter a random number -->  "))
    if iya == 0:
        print("THE PROGRAM WILL STOP NOW.")
        break
    elif iya % 2 == 1:
        print("ODD NUMBER DETECTED!!! The program will continue.")
        sum += iya
        odd = str(iya) + " "
        continue
    elif iya % 2 == 0:
        print("EVEN NUMBER DETECTED!!! The  program will continue.")
        continue

print(f"Hi, {name}., The sum of all the odd number you provided is: {sum}")
print(f"The odd numbers that had been detected are: {odd}")