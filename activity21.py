print("HI! I AM YOUR WASHING MACHINE. PLEASE ANSWER THE QUESTIONS BELOW.")

dirty = True

while dirty == True:
    confirm = input("Do you still want to continue washing? (yes or no) ")

    if confirm == "yes":
        print("This machine will continue to wash your clothes.")
        continue

    else:
        print("Alright! This machine will stop washing your clothes.")
        break