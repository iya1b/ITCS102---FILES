name = input("Hi! What is your name ? --> ")
fare = eval(input("How much is your fare fee --> "))
isStudent = input("Are you currently a student? (yes or no) ")

if isStudent == 'yes' :
    discount = fare * 0.2
    #fare -= discount
    newf = fare - discount 
    print("Hi, ", name)
    print("Your total discount is ", discount)
    print("Your new fare is ", newf)

else:
    print("Sorry,", name, "You are not eligible for a discount")


