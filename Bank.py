from tkinter import *
import subprocess  
#from PIL import Image, ImageTk

root=Tk()
#im = Image.open('back2.jpg')
#tkimage = ImageTk.PhotoImage(im)
#myvar=Label(root,image = tkimage)
#myvar.place(x=0, y=0, relwidth=1, relheight=1)
w = Label(root, text="WELCOME", fg="white", bg="black", font=("Helvetica", 25))
w.place(x=620,y=100)

n= Label(root, text="New here??",fg="white", bg="black", font=("Helvetica", 15))
n.place(x=640,y=400)


u = Entry(root)
u.place(x=640,y=300)
u.delete(0, END)
u.insert(0,"Username")

p = Entry(root, show="*", width=20)
p.place(x=640,y=320)
p.delete(0, END)
p.insert(0,"")


def login():
    pas=p.get()
    user=u.get()
    print (pas)
    print (user)
    f=open("Data.txt",'w')
    f.write(user)
    f.close()
    
    file=open(user+'.txt','r')
    passwrd=file.read()
    file.close()
    file=open(user+'2.txt','r')
    info=file.readlines()
    file.close()
    ch=0
    
    if pas==passwrd:
        subprocess.call('Login.py',shell=True)
    else:
        print ("Wrong Password!!!")
        
       
                        
def Signup():
    import Signup.py
    #subprocess.call('Signup.py',shell=True) 


log = Button(root, text = 'Sign Up', command = Signup)
log.place(x=683, y = 430)
root.geometry('1366x768+0+0')
log = Button(root, text = 'Login', command = login)
log.place(y=350, x = 683)




root.mainloop()


