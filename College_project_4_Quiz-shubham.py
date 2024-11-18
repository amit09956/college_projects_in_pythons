def ask_Questions(question,options,correct_answer):
    print(question)
    for i,option in enumerate(options,1):
        print(f'{i} . {option}')
    try:
        answer=int(input("please choose the correct number (1/2/3/4):"))
       
        if options[answer-1].lower() == correct_answer.lower():
            print("correct!\n")
            return True
        else:
            print(f"Wrong! The correct answer is: {correct_answer}\n")
            return False 
    except(ValueError,IndexError):
        print("Enter the currect option between( 1 to 4)")
        return False
    

def quiz():
    questions=[{
        "question":"Which of the following is not a valid data type in Python?",
        "option":['int',"float","char","string"],
        "correct_answer":"char"
    }
    ,
    {
        "question":"x = 5\n y=3\n print(x // y)",
        "option":['1.667',"1","2","1.6"],
        "correct_answer":"1"  
    },
    {
        "question":"Which keyword is used to define a function in Python?",
        "option":["function","def","define","fun"],
        "correct_answer":"def" 
    },
    {
        "question":"which type of sequence is imutable?",
        "option":["list","tuple","dictionary","set"],
        "correct_answer":"tuple" 
    },
    {
        "question":"Which of the following is used to create a loop that executes a specific number of times?",
        "option":["while-loop","do whille-loop","for-loop","repeat until-loop"],
        "correct_answer":"for-loop" 
    }]
    score=0
    total_questions=len(questions)
    for quest in questions:
        if ask_Questions(quest["question"],quest["option"],quest["correct_answer"]):
            score+=1
            
    print("You score:",(score/total_questions)*100)       
quiz()

