while True:
    try:
        number = int(input("Please enter a number: "))
        break
    except ValueError:
        print("You didn't enter a number")
    except:
        print("An unknown error occurred")

print("Thank you for entering a number")

# Guess a number between 1 and 10 : 1
# Guess a number between 1 and 10 : 3
# Guess a number between 1 and 10 : 5
# Guess a number between 1 and 10 : 7
# You guessed it

guessed = 1
while guessed != 7:
    guessed = int(input("Guess a number between 1 and 10: "))
print("You guessed it")


                  
