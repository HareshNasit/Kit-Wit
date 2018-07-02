from Tkinter import *
from PIL import ImageTk, Image
def thelionandfrog():
    y=Toplevel()
    y.title("The Lion And Frog")
    y.geometry("550x440")
    file=open("story1.txt",'r')
    txt=file.read()
    Label(y,text=txt,bg="blue",fg="green").pack()
    y.configure(bg="blue")
    file.close()
    image=Image.open("The_Lion_and_The_Frog_Story.gif")
    photo=ImageTk.PhotoImage(image)
    label=Label(y,image=photo)
    label.pack()
    label.image=photo

def thethirstycrow():
    y=Toplevel()
    y.geometry("360x485")
    y.title("The Thirsty Crow")
    file=open("story2.txt",'r')
    txt=file.read()
    Label(y,text=txt,bg="blue",fg="green").pack()
    y.configure(bg="blue")
    file.close()
    image=Image.open("thirsty-crow.gif")
    photo=ImageTk.PhotoImage(image)
    label=Label(y,image=photo)
    label.pack(side="top")
    label.image=photo

def TheLionandtheMouse():
    y=Toplevel()
    y.geometry("585x520")
    y.title("The Lion And The Mouse")
    file=open("story3.txt",'r')
    txt=file.read()
    Label(y,text=txt,bg="blue",fg="green").pack()
    y.configure(bg="blue")
    file.close()
    image=Image.open("lion_mouse.gif")
    photo=ImageTk.PhotoImage(image)
    label=Label(y,image=photo)
    label.pack()
    label.image=photo
    
def TheHareandtheTortoise():
    y=Toplevel()
    y.geometry("610x530")
    y.title("The Hare And The Tortoise")
    file=open("story5.txt",'r')
    txt=file.read()
    Label(y,text=txt,bg="blue",fg="green").pack()
    y.configure(bg="blue")
    file.close()
    image=Image.open("The_Tortoise_And_The_Hare.gif")
    photo=ImageTk.PhotoImage(image)
    label=Label(y,image=photo)
    label.pack()
    label.image=photo

def Friends():
    y=Toplevel()
    y.geometry("620x470")
    y.title("Friends")
    file=open("story6.txt",'r')
    txt=file.read()
    Label(y,text=txt,bg="blue",fg="green").pack()
    y.configure(bg="blue")
    file.close()
    image=Image.open("friends.gif")
    photo=ImageTk.PhotoImage(image)
    label=Label(y,image=photo)
    label.pack()
    label.image=photo

def TheFoxandTheGrapes():
    y=Toplevel()
    y.geometry("325x550")
    y.title("The Fox And The Grapes!")
    file=open("story8.txt",'r')
    txt=file.read()
    Label(y,text=txt,bg="blue",fg="green").pack()
    y.configure(bg="blue")
    file.close()
    image=Image.open("The_Fox_and_the_Grapes.gif")
    photo=ImageTk.PhotoImage(image)
    label=Label(y,image=photo)
    label.pack()
    label.image=photo

def CleverThief():
    y=Toplevel()
    y.geometry("550x465")
    y.title("Clever Thief")
    file=open("story9.txt",'r')
    txt=file.read()
    Label(y,text=txt,bg="blue",fg="green").pack()
    y.configure(bg="blue")
    file.close()
    image=Image.open("clever thief.gif")
    photo=ImageTk.PhotoImage(image)
    label=Label(y,image=photo)
    label.pack()
    label.image=photo

def TheCamelandTheJackal():
    y=Toplevel()
    y.geometry("505x515")
    y.title("The Camel and The Jackal")
    file=open("story10.txt",'r')
    txt=file.read()
    Label(y,text=txt,bg="blue",fg="green").pack()
    y.configure(bg="blue")
    file.close()
    image=Image.open("jackalcamel.gif")
    photo=ImageTk.PhotoImage(image)
    label=Label(y,image=photo)
    label.pack()
    label.image=photo

story=Tk()
story.configure(bg="orange")
story.title(" MORAL STORIES ")
story.geometry("260x230")

title=Label(story,text=" ******************MORAL STORIES************** ",bg="red",fg="black")
title.pack()

button_story=Button(story,text=(" The Hare And The Tortoise "),command=TheHareandtheTortoise,bg="black",fg="white")
button_story.pack()

button_story=Button(story,text=(" The Camel And The Jackal "),command=TheCamelandTheJackal,bg="black",fg="white")
button_story.pack()

button_story=Button(story,text=(" The Lion And The Mouse "),command=TheLionandtheMouse,bg="black",fg="white")
button_story.pack()

button_story=Button(story,text=(" The Fox And The Grapes! "),command=TheFoxandTheGrapes,bg="black",fg="white")
button_story.pack()

button_story=Button(story,text=(" The Lion And The Frog "),command=thelionandfrog,bg="black",fg="white")
button_story.pack()

button_story=Button(story,text=(" The Thirsty Crow "),command=thethirstycrow,bg="black",fg="white")
button_story.pack()

button_story=Button(story,text=(" Clever Thief "),command=CleverThief,bg="black",fg="white")
button_story.pack()

button_story=Button(story,text=(" Friends "),command=Friends,bg="black",fg="white")
button_story.pack()

story.mainloop()
