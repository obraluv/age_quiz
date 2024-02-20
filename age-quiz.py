# the following code will ask users to input any number between 1 and 100

age = int(input("please input numbers between 1 and 100:"))


if age > 100: # check if the user input age greater than 100
    print("Sorry, you're dead.")

elif age >= 65:
    print("Enjoy your retirement.")

elif age >= 40:
    print("You're over the hill.") # the following command will check if the age is greater than or equal to 40.

elif age == 21:
    print("Congrats on your 21st!")

elif age < 13:
    print("You qualify for the kiddie discount.")

# the else command will run if the condition of the if and elif statement is False
# if any number out of the specified age in the if and elif statements is input,
# "Age is but a number." will be printed out

else:
    print("Age is but a number.")
