"""
Perform a math quiz which generates it's problems by itself.
"""
import random


def generate_random_integer(integerMin, integerMax):
    """
    Generate a random integer between the range of two numbers.

    Args:
        integerMin (int, required): lowest possible number.
        integerMax (int, required): highest possible number.

    Returns:
        ReturnType: int
        generated number
        

    Raises:
        None
    """
    return random.randint(integerMin, integerMax) #pick the mathproblem's numbers


def choose_random_operator():
    """
    Pick a random operator. Excluding /

    Args:
        None

    Returns:
        ReturnType: str
        mathmatical operator 
        

    Raises:
        None
    """
    return random.choice(["+", "-", "*"]) #pick the mathproblem's operator


def generate_problem(number1, number2, operator):
    """
    Generate a mathmatical problem with two numbers and an operator.

    Args:
        number1 (int, required): first number.
        number2 (int, required): second number.
        operator (str, required): The problem`s operator.
    Returns:
        problem: str
        generated problem
        solution: int
        The solution to the problem.
        

    Raises:
        None
    """
    if number2 <0:
        problem = f"{number1} {operator} ({number2})"
    else: 
        problem = f"{number1} {operator} {number2}" #problemstring to show the user
    if operator == "+":                         #generate different solutions depending on the operator
        solution = number1 + number2
    elif operator == "-":
        solution = number1 - number2
    else:
        solution = number1 * number2
    return problem, solution                    #Provide user problem and solution


def math_quiz():
    """
    Performs a math quiz. Picks random numbers. Picks an operator.
    Puts them together to a problem and compares the users answer with the real answer.
    Sums up the correct answers and builds a score.
    

    Args:
        None
    Returns:
        None
    Raises:
        None
    """
    score = 0
    numberOfQuestions = 3

    print("Welcome to the Math Quiz Game!")
    print(
        "You will be presented with math problems, and you need to provide the correct answers."
    )

    for _ in range(numberOfQuestions):              #generate new problem for picked number of Questions
        number1 = generate_random_integer(1, 10)
        number2 = generate_random_integer(1, 5)
        operator = choose_random_operator()

        problem, answer = generate_problem(number1, number2, operator)
        print(f"\nQuestion: {problem}")
        while True:     #get correct userinput
            userAnswer = input("Your answer (n for next question): ")    #user input
            if userAnswer == 'n':
                print("skip")
                break
                
            try:
                userAnswer = int(userAnswer)
            except ValueError:
                print("Only use integer numbers!")
            else:
                break
        if userAnswer == answer:                    #Check User's answer
            print("Correct! You earned a point.")
            score += 1                              #Update score
        else:
            print(f"Wrong answer. The correct answer is {answer}.")
        
    print(f"\nGame over! Your score is: {score}/{numberOfQuestions}")   #Show results


if __name__ == "__main__":
    math_quiz()             #initiate quiz
