from tkinter import*
from random import randint , choice

root = Tk()
root.geometry("600x500")
root.title("Maths Quiz")

question = StringVar()
answer = StringVar()
givenAnswer = StringVar()
score = IntVar()
questionNumber = IntVar()
current_question= 0

questionLabel= Label(root , textvariable=f"question: {question}", font=('arial' , 20)) 
questionLabel.grid(row=2 , column=0)

resultLabel = Label(root, text="", font=('arial', 20))
resultLabel.grid(row=4, column=0, columnspan=2)

scoreLabel = Label(root, text=f"Score : {score.get()}", font=('arial', 20), fg="blue")
scoreLabel.grid(row=5, column=0 )

questionScale = Scale(root , from_=0 , to =10 , orient=HORIZONTAL , length=400, variable=questionNumber)
questionScale.grid(row=1 , column=0)

completeQuestionLable= Label(root, text="10th Question", )
completeQuestionLable.grid(row=1 , column=1)


def generateQuestion():
    global current_question
    current_question += 1
    questionNumber.set(current_question)
    
    number1 = randint(1 , 10)
    number2 = randint(1,  10)

    operator = choice(['+' , '-' , '*' , '//'])

    question.set(str(number1) + operator + str(number2))
    answer.set(eval(question.get()))
    resultLabel.config(text="")


def checkAnswer(): 

    global scoreLabel     
    if str(answer.get()) == givenAnswer.get():
        score.set(score.get() + 1)
        resultLabel.config(text="Correct!", fg="green")
        scoreLabel = Label(root, text=f"Score : {score.get()}", font=('arial', 20), fg="blue")
        scoreLabel.grid(row=5, column=0 )

    else:
        resultLabel.config(text=f"Incorrect! Answer: {answer.get()}", fg="red")
    

    if current_question < 10:
        root.after(1000, generateQuestion)
    else:
        resultLabel.config(text="Quiz Finished!", fg="purple")
        scoreLabel.config(text=f"Final Score : {score.get()}")
        submitButton.config(state=DISABLED) 
   

def restart():

    global scoreLabel ,current_question
    current_question = 0   
    scoreLabel.destroy()
    score.set(0)
    questionNumber.set(0)
    generateQuestion()

    scoreLabel = Label(root, text=f" Score : {score.get()}", font=('arial', 20), fg="blue")
    scoreLabel.grid(row=5, column=0 ) 
    

headingLabel1 = Label(root , text="Maths Quiz" , font=('arial' , 25) )
headingLabel1.grid(row=0 , column=0 )

questionLabel= Label(root , textvariable=question, font=('arial' , 20)) 
questionLabel.grid(row=2 , column=0)

answerEntry = Entry(root , textvariable=givenAnswer , font=('arial' ,20), width = 25)
answerEntry.grid(row=3 , column=0)

submitButton = Button(root , text="submit " , font=('arial' , 13) ,command=checkAnswer )
submitButton.grid(row=3 , column=1)

RestartButton = Button(root , text="Restart " ,fg= "red",  font=('arial' , 15) ,command=restart , width = 33)
RestartButton.grid(row=6 , column=0)

generateQuestion()
root.mainloop()  