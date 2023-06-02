# This imports the class from another file

from Question import Question

# These are the questions/inputs for the quiz

question_prompts = [
    "What is a cat?\n(a) A predator\n(b) A perpetrator\n\n",
    "What is a Singapura?\n(a) A country\n(b) A cat\n\n",
    "Which month is associated with cats?\n(a) June\n(b) March\n\n",
] 

# This is the correct answers for the questions/prompts

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),
    ]

# This function loops through the questions to keep score and prints the result


def run_test(questions):
    print("Welcome to the ultimate crazy-cat-person quiz. First question:\n")
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got:\n" + str(score) + "/" + str(len(questions)) + " correct")


# This function runs the test itself

run_test(questions)
