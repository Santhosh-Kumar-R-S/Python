import random  # Import the random module for generating random numbers
import time    # Import the time module for timing the quiz

OPERATORS = ["+", "-", "*"]  # Define the list of operators used in the quiz
MIN_OPERATORS = 3            # Define the minimum value for the operands
MAX_OPERATORS = 12           # Define the maximum value for the operands
TOTAL_PROBLEMS = 10          # Define the total number of problems in the quiz

# Function to generate arithmetic problems
def generate_problem():
    left = random.randint(MIN_OPERATORS, MAX_OPERATORS)    # Generate a random left operand
    right = random.randint(MIN_OPERATORS, MAX_OPERATORS)   # Generate a random right operand
    operator = random.choice(OPERATORS)                    # Choose a random operator from the list
    
    expr = str(left) + " " + operator + " " + str(right)   # Create the arithmetic expression
    answer = eval(expr)                                    # Calculate the answer
    return expr, answer                                    # Return the expression and the answer

# Ask the user if they are ready to start the quiz
ready = input("Are You Ready for This Quiz? (Yes/No): ")
if ready.capitalize() == "Yes":                                           # Check if the user is ready
    input("Press Enter to Start the Quiz!")                  # Prompt the user to start the quiz
    print("-------------------------------")                 # Print a separator line
    start_time = time.time()                                 # Record the start time of the quiz
elif ready.capitalize() == "No":                                          # Check if the user is not ready
    print("I am waiting for Your Participation in this Quiz...! Please Participate at the next round ")
    print("----------------------------------------------------------------------------------------- ")
    exit()                                                       # Terminate the program
else:
    print("Invalid Input...!, Enter The Valid Input Yes or No")  # Notify the user of an invalid input
    print("--------------------------------------------------")
    exit()                                                       # Terminate the program

# Initialize the variable to count the number of wrong answers
wrong = 0  
right = 0

# Loop through the total number of problems in the quiz
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()                                  # Generate a new arithmetic problem
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + ' = ')  # Prompt the user to solve the problem
        if guess == str(answer):                                       # Check if the user's guess is correct
            right += 1                                                 # Increment the count of correct answers
            break                                                      # Exit the loop if the guess is correct
        else:
            wrong += 1                                                 # Increment the count of wrong answers 
            break                                                      # Break the loop if the guess is incorrect and proceed to the next question


end_time = time.time()                                                 # Record the end time of the quiz
total_time = round(end_time - start_time, 4)                           # Calculate the total time taken for the quiz
time_in_minutes = round(total_time / 60, 2)                            # Calculate the total time in minutes

# Calculate grade based on the number of correct answers
if right == TOTAL_PROBLEMS:
    grade = "Awesome! You got the maximum score of " + str(TOTAL_PROBLEMS) + " out of " + str(TOTAL_PROBLEMS) + "!"
elif right >= TOTAL_PROBLEMS * 0.8: grade = "Great! You got " + str(right) + " out of " + str(TOTAL_PROBLEMS) + "!"
elif right >= TOTAL_PROBLEMS * 0.6:
    grade = "Good! You got " + str(right) + " out of " + str(TOTAL_PROBLEMS) + "!"
else:
    grade = "Try again! You got " + str(right) + " out of " + str(TOTAL_PROBLEMS) + "."


# Display the quiz results
print("-------------------------------")
print("Time taken:", total_time, "seconds")                            # Print the total time taken for the quiz
print("Time taken in minutes", time_in_minutes)                        # Print the total time taken in minute for quize 
print(grade)                                                           # Print the number of right answers count.
print("Number of wrong answers: ", wrong)                              # Print the number of wrong answers.
