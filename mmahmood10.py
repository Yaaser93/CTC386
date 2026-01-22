# Muhammad Mahmood
# Lab 10


#Functions
def temp():
    F = int(input("What is the temperature in Fahrenheit? "))
    C = ((F-32)*(5/9))
    print("The temperature is",C,"degrees Celsius.")

def sneak():
    print("You take a step around...")
    print(" Without realizing it, you stepped on a twig!")
    print(" The guard was alerted to your presence!")
    print(" You have been defeated...")

#Main Code
username = input("What is your name? ")
Option1 = "Why is the new moon heavier than a full moon? Because it's not as light!"
Option2 = username
Option3 = "Hakuna Matata"

print("Hello,",username,". Please select one of the choices below.")
print("Menu")
print("Option 1")
print("Option 2")
print("Option 3")
print("Option 4")
print("Option 5")
print("Option 6")


#Muhammad Mahmood
#Lab 10 (cont.)

choice = int(input())

if choice == 1:
    print(Option1)
elif choice == 2:
    for i in range(15):
        print(Option2)
elif choice == 3:
    repeat = int(input("Select a number. "))
    for i in range(repeat):
        print(Option3)
elif choice == 4:
    answer = 1
    while answer != 24:
        answer = int(input("What number am I thinking of between 0 and 100? "))
        if answer < 24 and answer >= 0:
            print("Your guess was too LOW. Try again.")
        elif answer > 24 and answer <= 100:
            print("Your answer was too HIGH. Try again.")
        elif answer < 0 or answer > 100:
            print("Please select a number within the correct range.")
    print("You win! You guessed it correctly!")
elif choice == 5:
    temp()
elif choice == 6:
    print("You see a bad guy! What do you want to do? ")
    print("Pick 1 to flee. Pick 2 to sneak past. Pick 3 to battle! ")
    choice = int(input())
    if choice == 1:
        for i in range(10):
            print("Get away!")
    elif choice == 2:
        sneak()
    elif choice == 3:
        print(" You defeated the foe!")
    else:
        print("You did not pick a valid choice! You have been defeated.")


else:
    print("Sorry, try again.")
