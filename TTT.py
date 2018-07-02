from tkinter import*
import tkinter.messagebox as tkm

game=Tk()
game.title( " TIC TAC TOE " )

click=True

def TTT(button):
    global click
    if button["text"]==" " and click==True:
        button["text"]= "X"
        click=False
    elif button["text"]==" " and click==False:
        button["text"]= "O"
        click=True

    elif(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"or
         button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"or
         button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"or
         button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"or
         button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"or
         button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"or
         button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"or
         button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
        tkm.showinfo(" WINNER X "," PLAYER X WON THE GAME ")
        game.destroy()
        

    elif(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"or
         button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"or
         button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"or
         button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"or
         button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"or
         button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"or
         button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"or
         button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" ):
        tkMessageBox.showinfo(" WINNER O "," PLAYER O WON THE GAME ")
        game.destroy()
    else:
        tkm.showinfo("DRAW","The Game Is Draw")
        game.destroy()
button=StringVar()




button1=Button(text=" ",font=("algerian 20 bold"),bg=("orange"),fg=("blue"),height=4,width=8,command=lambda:TTT(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2=Button(text=" ",font=("algerian 20 bold"),bg=("orange"),fg=("blue"),height=4,width=8,command=lambda:TTT(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3=Button(text=" ",font=("algerian 20 bold"),bg=("orange"),fg=("blue"),height=4,width=8,command=lambda:TTT(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4=Button(text=" ",font=("algerian 20 bold"),bg=("blue"),fg=("green"),height=4,width=8,command=lambda:TTT(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)

button5=Button(text=" ",font=("algerian 20 bold"),bg=("blue"),fg=("green"),height=4,width=8,command=lambda:TTT(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)

button6=Button(text=" ",font=("algerian 20 bold"),bg=("blue"),fg=("green"),height=4,width=8,command=lambda:TTT(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7=Button(text=" ",font=("algerian 20 bold"),bg=("green"),fg=("red"),height=4,width=8,command=lambda:TTT(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)

button8=Button(text=" ",font=("algerian 20 bold"),bg=("green"),fg=("red"),height=4,width=8,command=lambda:TTT(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)

button9=Button(text=" ",font=("algerian 20 bold"),bg=("green"),fg=("red"),height=4,width=8,command=lambda:TTT(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)

game.mainloop()
