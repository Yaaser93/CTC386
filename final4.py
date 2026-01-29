#Muhammad Mahmood
#Final Question 4

def celebrate():
    print("Happy New Year!")

number = int(input("Pick a number between 1 and 10. "))
if number < 1 or number > 10:
    print("Sorry, please try again.")
else:
    for i in range(number):
        celebrate()


