#Muhammad Mahmood
#Final Question 1

print("Option 1")
print("Option 2")
print("Option 3")

choice = int(input("Choose one of the above options. Only type the number. "))

if choice == 1:
    name = input("What's your name? ")
    print("Hey,",name, "! Working hard or hardly working, eh?")
if choice == 2:
    food = input("Pick a food. ")
    for i in range (20):
        print(food)
if choice == 3:
    number = 1
    while number > 0 or number < 0:
        number = int(input("Pick any number. "))
        if number != 0:
            print("Warning! Try again! ")
    print("Nice job.")
