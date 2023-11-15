import random

def multiplication_practice():
    num = int(input("Enter multiplication table: "))
    num_questions = int(input("Enter number of questions: "))
    
    for _ in range(num_questions):
        factor = random.randint(1, 10)  # Generate a random number between 1 and 10
        result = num * factor
        
        user_answer = int(input(f"What is {num} * {factor}?\nEnter answer: "))
        
        if user_answer == result:
            print(f"Correct answer is {result}.")
        else:
            print(f"Wrong answer. Correct answer is {result}.")

# Call the function to start the multiplication practice
multiplication_practice()
