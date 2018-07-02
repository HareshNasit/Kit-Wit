from Tkinter import *
import subprocess
#from PIL import Image, ImageTk
main=Tk()

main.geometry('500x700+0+0')

'''im = Image.open('Back.jpg')
tkimage = ImageTk.PhotoImage(im)
myvar=Label(main,image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)'''


def close():
    main.destroy()

title=Label(main,text="The Square Oriental",fg="red",bg='black',font=("Times",45))
title.pack()

n=Label(main,text="Enter your name:",font=("Times",20))
n.place(x=0,y=100)


name= Entry(main,width=25)
name.place(x=200,y=110)
name.delete(0, END)
name.insert(0,"")

def cont():
    name1=name.get()
    we=Label(main,text="Welcome "+name1+'!!!',font=("Times",20))
    we.place(x=0,y=180)
    qu=Label(main,text="What would you like to order?",font=('Times',20))
    qu.place(x=0,y=210)
    
    def china():
        main.destroy()
        #import Chinese.py
        subprocess.call('Chinese.py',shell=True)
                
    def india():
        main.destroy()
        #import India.py
        subprocess.call('Indian.py',shell=True)

    def italy():
        main.destroy()
        #import Italian.py
        subprocess.call('Italian.py',shell=True)

    def america():
        main.destroy()
        subprocess.call('American.py',shell=True)

    def france():
        main.destroy()
        subprocess.call('French.py',shell=True)
    
             



    chi= Button(main, text = 'CHINESE',command=china,font=('Courier',20))
    chi.place(x=200, y =270)
    ind=Button(main,text="INDIAN",command=india,font=('Courier',20))
    ind.place(x=200,y=350)
    ita=Button(main,text='ITALIAN',command=italy,font=('Courier',20))
    ita.place(x=200,y=430)
    ame=Button(main,text='AMERICAN',command=america,font=('Courier',20))
    ame.place(x=200,y=510)
    fre=Button(main,text='FRENCH',command=france,font=('Courier',20))
    fre.place(x=200,y=590)



co= Button(main, text = 'CONTINUE', command = cont)
co.place(x=200, y = 150)







main.mainloop()
