from art import logo
import random

print(logo)
# Tell the user welcome to the number guessing game
print("Welcome to the guessing game!")
# Ask the user if they would like to play the easy game or the hard game+
difficuly = input("What difficulty would you like to play? Type 'easy' for easy and 'hard' for hard: ")

# Generate a random number by creating a function get_number that selects a random integer between 1 and 100. 
def get_number():
    random_integer = random.randint(1, 100)
    return random_integer
# Pass the get_number function into a variable called selected_number
selected_number = get_number()

# Create a variable called user_guess which takes an input of the user with a number 1 - 100
def get_user_guess():
    user_guess = int(input("Please select a number between 1 and 100: "))
    return user_guess

#calling get_user_guess()
user_guess = get_user_guess()


# play_game function is used to check 
def play_game(lives):
    global selected_number
    global user_guess
    
    
    while lives > 1:
        if user_guess == selected_number:
            lives = 0
            print(f"You win! The random number was {selected_number}!")
            return
            
        elif user_guess > selected_number:
            print("The random number is lower!")
            lives -= 1
            print(f"You have {lives} lives remaining!")
            user_guess = get_user_guess()
            
        elif user_guess < selected_number:
            print("The random number is higher!")
            lives -= 1
            print(f"You have {lives} lives remaining!")
            user_guess = get_user_guess()
            
       
    print(f"You lost! The random number was {selected_number}!")
            
#if user says 'easy' call play_game(10)        
if difficuly == 'easy':
    play_game(10)
# if user says 'hard' > call play_game(5)
elif difficuly == 'hard':
    play_game(5)
# else > invalid input
else:
    print("Invalid selection!")


