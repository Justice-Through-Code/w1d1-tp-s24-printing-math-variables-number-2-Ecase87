def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    student_name =  input("Hello, What is your name?")

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    math_score = int(input("what is your Math Score?")) 
    science_score = int(input("what is your Science Score?"))
    english_score = int(input("what is your English Score?"))

    # Calculate the average grade
    average_grade = (math_score + science_score + english_score)/3

    # Return the student's name and their average grade
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    #Used F strings to formate print statment and variables, and used further f string functionality to render only 2 decimal places for scores
    print(f"Hey {student_name}, it look like the average score of your three subjects: Math, science and english; is {average_grade:.2f}")
