from Tkinter import *
import datetime
now = datetime.datetime.now()



add=Tk()
add.geometry("500x500+0+0")


file=open("Data.txt",'r')
user=file.read()
file.close()
print user


we=Label(add,text="ADD MONEY",fg="white",bg="black",font=("Helvetica",25))
we.pack()
file=open(user+'1.txt','r')
bal=Label(add,text="Your Account balance as of today is:",fg="white",bg="black",font=("Helvetica",15))
bal.pack()
balmon=file.read()

ba=Label(add,text=balmon,fg="white",bg="black",font=("Helvetica",15))
ba.pack()

file.close()
am=Label(add,text="How much money do you want to add?",fg="white",bg="black",font=("Helvetica",15))
am.pack()
mon = Entry(add)
mon.pack()
mon.delete(0, END)
mon.insert(0,"")

def credit():
    money=mon.get()
    file=open(user+'1.txt','w')
    file.write(str(int(balmon)+int(money)))
    su=Label(add,text="You have successfully credited your money!!",fg="white",bg="black",font=("Helvetica",15))
    su.pack()
    file.close()
    file=open(user+'t.txt','a')
    transcreate5="Balance: You have Credited "+money+"$ to your account on "+now.strftime('%d-%B-%y')+" at "+now.strftime('%H:%M:%S %p')
    file.write('\n'+transcreate5)
    file.close()

button=Button(add, text = 'ADD', command = credit)
button.pack()
    

add.mainloop()










