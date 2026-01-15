# Muhammad Mahmood
# Lab 9
# github test comment


#Functions
def temp():
    F = int(input("What is the temperature in Fahrenheit? "))
    C = ((F-32)*(5/9))
    print("The temperature is",C,"degrees Celsius.")


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


#Muhammad Mahmood
#Lab 8 (cont.)

choice = int(input("Select 1, 2, 3, 4, or 5. "))

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

else:
    print("Sorry, try again.")
