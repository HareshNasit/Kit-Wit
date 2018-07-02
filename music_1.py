import sys
import pygame
pygame.init()
   
from tkinter import *
master = Tk()
from PIL import Image,ImageTk
master.geometry("365x767+778+157")

#background pic and heading
im = Image.open('bg2.png')
tkimage = ImageTk.PhotoImage(im)
myvar=Label(master,image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)
T = Label(master, text="Songs",bg="yellow",fg="red",font=("Agency FB",25))
T.place(x=180,y=20)
#songs as commands
def Blank():
    pygame.mixer.music.load('Blank.wav')
    pygame.mixer.music.play()
    master.geometry("365x767+778+157")
    im = Image.open('Blank.png')
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(master,image = tkimage)
    myvar.place(x=0, y=0, relwidth=1, relheight=1)
    T = Label(master, text="Songs",bg="yellow",fg="red",font=("Agency FB",25))
    T.place(x=180,y=20)
    songs()
    mainloop()
def Faded():
    pygame.mixer.music.load('Faded.wav')
    pygame.mixer.music.play()
    master.geometry("365x767+778+157")
    #changing background image when button is pressed
    im = Image.open('Faded.png')
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(master,image = tkimage)
    myvar.place(x=0, y=0, relwidth=1, relheight=1)
    T = Label(master, text="Songs",bg="yellow",fg="red",font=("Agency FB",25))
    T.place(x=180,y=20)

    songs()
    mainloop()
def Spectre():
    pygame.mixer.music.load('Spectre.wav')
    pygame.mixer.music.play()
    master.geometry("365x767+778+157")
    #changing background image when button is pressed
    im = Image.open('Spectre.png')
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(master,image = tkimage)
    myvar.place(x=0, y=0, relwidth=1, relheight=1)
    T = Label(master, text="Songs",bg="yellow",fg="red",font=("Agency FB",25))
    T.place(x=180,y=20)

    songs()
    mainloop()
def Closer():
    pygame.mixer.music.load('Closer.wav')
    pygame.mixer.music.play()
    master.geometry("365x767+778+157")
    #changing background image when button is pressed
    im = Image.open('Closer.png')
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(master,image = tkimage)
    myvar.place(x=0, y=0, relwidth=1, relheight=1)
    T = Label(master, text="Songs",bg="yellow",fg="red",font=("Agency FB",25))
    T.place(x=180,y=20)

    songs()
    mainloop()
def Spektrem():
    pygame.mixer.music.load('Spektrem.wav')
    pygame.mixer.music.play()
    master.geometry("365x767+778+157")
    #changing background image when button is pressed
    im = Image.open('Spektrem.png')
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(master,image = tkimage)
    myvar.place(x=0, y=0, relwidth=1, relheight=1)
    T = Label(master, text="Songs",bg="yellow",fg="red",font=("Agency FB",25))
    T.place(x=180,y=20)

    songs()
    mainloop()
def CartoonOn():
    pygame.mixer.music.load('CartoonOn.wav')
    pygame.mixer.music.play()
    master.geometry("365x767+778+157")
    #changing background image when button is pressed
    im = Image.open('Cartoon.png')
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(master,image = tkimage)
    myvar.place(x=0, y=0, relwidth=1, relheight=1)
    T = Label(master, text="Songs",bg="yellow",fg="red",font=("Agency FB",25))
    T.place(x=180,y=20)

    songs()
    mainloop()
def Nova():
    pygame.mixer.music.load('Nova.wav')
    pygame.mixer.music.play()
    master.geometry("365x767+778+157")
    #changing background image when button is pressed
    im = Image.open('Ahrix.png')
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(master,image = tkimage)
    myvar.place(x=0, y=0, relwidth=1, relheight=1)
    T = Label(master, text="Songs",bg="yellow",fg="red",font=("Agency FB",25))
    T.place(x=180,y=20)

    songs()
    mainloop()
def Nights():
    pygame.mixer.music.load('Nights.wav')
    pygame.mixer.music.play()
    master.geometry("365x767+778+157")
    #changing background image when button is pressed
    im = Image.open('Nights.png')
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(master,image = tkimage)
    myvar.place(x=0, y=0, relwidth=1, relheight=1)
    T = Label(master, text="Songs",bg="yellow",fg="red",font=("Agency FB",25))
    T.place(x=180,y=20)

    songs()
    mainloop()
def Good():
    pygame.mixer.music.load('FeelGood.wav')
    pygame.mixer.music.play()
    master.geometry("365x767+778+157")
    #changing background image when button is pressed
    im = Image.open('FeelGood.png')
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(master,image = tkimage)
    myvar.place(x=0, y=0, relwidth=1, relheight=1)
    T = Label(master, text="Songs",bg="yellow",fg="red",font=("Agency FB",25))
    T.place(x=180,y=20)

    songs()
    mainloop()
def stop():
    pygame.mixer.music.pause()
def stop1():
    pygame.mixer.music.unpause()
def songs():
    #creating buttons
    blank = Button(master,text="Blank",command=Blank,font=("Ar delany 20 bold",12),bg="green",fg="blue")
    blank.place(x=75,y=80)
    faded = Button(master,text="Faded",command=Faded,font=("Ar delany",12),bg="green",fg="blue")
    faded.place(x=75,y=130)
    spectre = Button(master,text="Spectre",command=Spectre,font=("Ar delany",12),bg="green",fg="blue")
    spectre.place(x=75,y=180)
    closer = Button(master,text="Closer",command=Closer,font=("Ar delany",12),bg="green",fg="blue")
    closer.place(x=75,y=230)
    spektrem = Button(master,text="Spektrem",command=Spektrem,font=("Ar delany",12),bg="green",fg="blue")
    spektrem.place(x=75,y=280)
    cartoon = Button(master,text="Cartoon On and On",command=CartoonOn,font=("Ar delany",12),bg="green",fg="blue")
    cartoon.place(x=75,y=330)
    nova = Button(master,text="Ahrix-Nova",command=Nova,font=("Ar delany",12),bg="green",fg="blue")
    nova.place(x=75,y=380)
    nights = Button(master,text="The Nights",command=Nights,font=("Ar delany",12),bg="green",fg="blue")
    nights.place(x=75,y=430)
    good = Button(master,text="Feel Good",command=Good,font=("Ar delany",12),bg="green",fg="blue")
    good.place(x=75,y=480)
    pause = Button(master,text="| |",command=stop,bg="yellow",fg="blue")
    pause.place(x=175,y=550)
    play = Button(master,text="play",command=stop1,bg="yellow",fg="blue")
    play.place(x=200,y=550)




songs()
mainloop()
print("hi")

