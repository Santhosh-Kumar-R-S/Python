# Import the string module for constants such as string.ascii_letters, string.digits, and other symbols
# These constants represent sets of characters that include ASCII letters, digits, and various symbols
import string
# Import the random module to shuffle the letters,digits and special charecters 
import random
# Create a list of characters including letters, digits, and special symbols
# string.ascii_letters provides all ASCII letters (both lowercase and uppercase)
# string.digits provides all decimal digits (0-9)
# Additional special characters are added to the list
characters = list(string.ascii_letters + string.digits + ".@_$%^&*()-+")

# Define a function to generate a random password
def generate_password():
    # Get the desired password length from the user
    password_length = int(input("How long would you like your password to be? "))

    # Shuffle the characters list to ensure randomness
    random.shuffle(characters)
    
    # Initialize an empty list to store the password
    password = []
    
    # Generate the password by selecting random characters
    for x in range(password_length):
        password.append(random.choice(characters) )
    # Shuffle the password again for additional randomness
    random.shuffle(password)

    # Convert the list of characters into a string
    password = "".join(password)
    # Print the generated password
    print(password)

# Ask the user if they want to generate a password
option = input("Do you want to generate a password? (Yes/No): ")

# Handle user input
if option == "Yes":
    generate_password()
elif option == "No": 
    print("Program Ended")
    quit()
else: 
    print("Invalid input, Please give input Yes or No")
    quit()
