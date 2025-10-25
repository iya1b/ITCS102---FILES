print("HELLO, I WILL BE YOUR ASSISTANT FOR TODAY. I WILL BE LISTING YOUR FAVORITE ANIME.")
print("Type 'ok' to finish collecting.")

list = [ ]
title = " "

while title != "ok":

    title = input("Please enter the title of your favorite anime --> ")

    if title != "ok":
        list.append(title)
        print(f"'{title}' has been added to the list successfully.")
    elif title == "ok":
        print("THIS PROGRAM WILL STOP")
        break

print("LIST OF YOUR FAVORITE ANIME: ")
for anime in list:
     print(f" - {title}")