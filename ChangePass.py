from Tkinter import *
import datetime
now = datetime.datetime.now()
import tkMessageBox
password=Tk()
password.geometry("1000x600+0+0")
file=open("Data.txt",'r')
user=file.read()
file.close()
print user



w= Label(password, text="Change Password", fg="white", bg="black", font=("Helvetica", 25))
w.pack()

age=Label(password, text="Please enter your age for security reasons:", fg="white", bg="black", font=("Helvetica", 15))
age.pack()

age1 = Entry(password)
age1.pack()
age1.delete(0, END)
age1.insert(0,"Age")

def change():
    file=open(user+'2.txt','r')
    ageof=file.readlines()
    file.close()
    age2=age1.get()
    if age2==ageof[1]:
        thanks= Label(password, text="Thank you for confirming your age.", fg="white", bg="black", font=("Helvetica", 15))
        thanks.pack()
        file=open(user+".txt",'w')
        n=Label(password, text="Enter your name:", fg="white", bg="black", font=("Helvetica", 15))
        n.pack()
        name=Entry(password)
        name.pack()
        name.delete(0, END)
        name.insert(0,"Name")

        new=Label(password, text="Enter new password:", fg="white", bg="black", font=("Helvetica", 15))
        new.pack()
        newpass=Entry(password)
        newpass.pack()
        newpass.delete(0, END)
        newpass.insert(0,"")

        def done():
            file=open(user+".txt",'w')
            newpass1=newpass.get()
            name1=name.get()

            file.write(newpass1)
            file.close()
            file=open(user+'2.txt','w')
            file.write(name1)
            file.write('\n')
            file.write(age2)

            done1=Label(password, text="You have successfully changed your password!!", fg="white", bg="black", font=("Helvetica", 15))
            done1.pack()
            file.close()

            transcreate6="Account: You have Changed your account Password on "+now.strftime('%d-%B-%y')+" at "+now.strftime('%H:%M:%S %p')
            file.write('\n'+transcreate6)
            file.close()

        changebutt=Button(password, text = 'CHANGE', command = done)
        changebutt.pack()
    else:
        if tkMessageBox.showinfo("ERROR", "Incorrect AGE!!!"):
            print "CLOSED!!!!!!"
        
cont=Button(password, text = 'CONTINUE', command = change)
cont.pack()
       
password.mainloop()










            


        

