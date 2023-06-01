from question import Question

#This is an introdiction to the quiz
print("Welcome to the ultimate flowerpower-quiz - a game to enhance your knowledge of saving plants.")

#This is the questions for the quiz
question_prompts = [
    "Your plant is hanging, what do you do?\n(A) Throw it out\n(B) Water it\n(C) Put it in the sun\n\n"
    "Your plant is not growing, what do you do?\n(A) Give it to your mom\n(B) Give it plant nutrition\n(C) Give it more water\n\n"
    "Your plant is getting too big, what do you do?\n(A) Cut it down\n(B) Put it in the shadows \n(C) Give it a bigger pot\n\n"
    "Your plant got lice, what do you do?\n(A) Kill the plant and the lice with it\n(B) Spraying the plant with soapwater\n(C) \n\n"
    "Your plant has mold, what do you do?\n(A) Wash the plant with dishwasher\n(B) Water it\n(C) Change the soil\n\n

] 

questions = [
    Question(question_prompts[0], "B")
    Question(question_prompts[1], "B")
    Question(question_prompts[2], "C")
    Question(question_prompts[3], "B")
    Question(question_prompts[4], "C")
    ]