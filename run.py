# This imports the class from another file

from Question import Question

# These are the questions/inputs for the quiz

question_prompts = [
    "What is a cat?\n(A) A predator\n(B) A perpetrator\n\n"
    "What is a Singapura?\n(A) A country\n(B) A cat\n\n"
    "Which month is associated with cats?\n(A) June\n(B) March\n\n"
] 

# This is the correct answers for the questions/prompts

questions = [
    Question(question_prompts[0], "A")
    Question(question_prompts[1], "B")
    Question(question_prompts[2], "B")
    ]

# This function loops thru the questions to keep score and prints the result


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")


# This function runs the test itself

run_test(questions)