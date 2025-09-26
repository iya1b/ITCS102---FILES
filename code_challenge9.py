print("🦜 PARROT SIMULATOR – THE ECHO CHAMBER")
a = input("What do you want your parrot to say? --> ")
b = eval(input("How many times should your parrot say it? "))
print("Listen to your parrot:")
for c in range(b, 0, -1):
    print("🦜 Squawk!", a)
