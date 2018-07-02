import Tkinter
import random

computer_guess=random.randint(1,10)

def check():
    user_guess=int(text_guess.get())
    if user_guess < computer_guess:
        message = " Higher "
    elif user_guess > computer_guess:
        message = " Lower "
    elif user_guess == computer_guess:
        message = " Correct "
    else:
        message = " Something went wrong "

    result["text"]=message
    text_guess.delete(0,5)

def reset():
    global computer_guess
    computer_guess=random.randint(1,10)
    result["text"]= " Guess Again "

game = Tkinter.Tk()
game.configure(bg="black")
game.title("Guess The Number")
game.geometry("250x75")

title=Tkinter.Label(game,text= " Welcome To The Guess Game ",bg=("black"),fg="orange",font=("arial 12 bold"))
title.pack()

result=Tkinter.Label(game,text= " Good Luck ",bg="black",fg="yellow",font=("arial 12 bold"))
result.pack()

button_check=Tkinter.Button(game,text=("check"),font=("algerian 15 bold"),fg="green",bg="black",command=check)
button_check.pack(side="left")

button_reset=Tkinter.Button(game,text="reset",fg="red",bg="black",font=("algerian 15 bold"),command=reset)
button_reset.pack(side="right")

text_guess=Tkinter.Entry(game,width=15,font=("algerian 15 bold"),bg="WHITE")
text_guess.pack()

game.mainloop()
