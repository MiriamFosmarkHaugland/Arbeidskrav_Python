login_information_dict = {
    "Username": "PGR107",
    "Password": "Python"
}

quiz_dict = {
    "Q1. What is the capital of Norway?": {
        "a. Bergen": False,
        "b. Oslo": True,
        "c. Stavanger": False,
        "d. Trondheim": False
    },
    "Q2. What is the currency of Norway?": {
        "a. Euro": False,
        "b. Pound": False,
        "c. Krone": True,
        "d. Deutsche Mark": False
    },
    "Q3. What is the largest city in Norway?": {
        "a. Oslo": True,
        "b. Stavanger": False,
        "c. Bergen": False,
        "d. Trondheim": False
    },
    "Q4. When is constitution day (the national day) of Norway?": {
        "a. 27th May": False,
        "b. 17th May": True,
        "c. 17th April": False,
        "d. 27th April": False
    },
    "Q5. What color is the background of the Norwegian flag?": {
        "a. Red": True,
        "b. White": False,
        "c. Blue": False,
        "d. Yellow": False
    },
    "Q6. How many countries does Norway Border?": {
        "a. 1": False,
        "b. 2": False,
        "c. 3": True,
        "d. 4": False
    },
    "Q7. What is the name of the university in Trondheim?": {
        "a. UiS": False,
        "b. UiO": False,
        "c. NMBU": False,
        "d. NTNU": True
    },
    "Q8. How long is the border between Norway and Russia?": {
        "a. 96 km": False,
        "b. 196 km": True,
        "c. 296 km": False,
        "d. 396 km": False
    },
    "Q9. Where in Norway is Stavanger?": {
        "a. North": False,
        "b. South": False,
        "c. South-west": True,
        "d. South-east": False
    },
    "Q10. From which Norwegian city did the worlds famous composer Edvard Grieg come?": {
        "a. Oslo": False,
        "b. Bergen": True,
        "c. Stavanger": False,
        "d. Tromsø": False
    }
        
}

wrong_answers_dict = {}

def login_info(login_information, username, password):
    if login_information["Username"] == username and login_information["Password"] == password:
        print("Login was Successful!\n")
    else:
        print("Invalid username and/or password\n")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        login_info(login_information, username, password)


current_correct_answer = ""
correct_answer_count = 0
wrong_answer_count = 0

username = input("Please enter your username: ")
password = input("Please enter your password: ")

login_info(login_information_dict, username, password)

for question, options in quiz_dict.items():
    option_letter = ""
    print(question)
    for option in options.keys():
        print(option)
    
    for option, isCorrect in options.items():
        if isCorrect == True:
            current_correct_answer = option
            option_letter = option.split(". ")[0]
    
    userInputAnswer = input("Enter your answer by the letter assigned to it (ex: a): ").lower()
    
    if option_letter == userInputAnswer:
        correct_answer_count = correct_answer_count + 1
        print("The answer is correct!\n")
    else: 
        wrong_answer_count = wrong_answer_count + 1
        wrong_answers_dict.update({
            question: {
                "user_answer": userInputAnswer,
                "correct_answer": current_correct_answer
            }
        })
        print("The answer is wrong.\n")

print("----- The quiz is now done, here are the results -----\n")
print("- Number of correct answers:", correct_answer_count)
print("- Number of wrong answers:", wrong_answer_count, "\n")

if len(wrong_answers_dict) != 0:
    print("These questions were answered wrong: \n")
    for question, answers_dict in wrong_answers_dict.items():
        print("The question was:", question)
        print("The user answered:", answers_dict["user_answer"])
        print("Correct answer was:", answers_dict["correct_answer"], "\n")