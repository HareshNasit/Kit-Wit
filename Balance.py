from Tkinter import *


balance=Tk()

balance.geometry("500x200+200+50")

file=open("Data.txt",'r')
user=file.read()
file.close()
print user
ac=Label(balance,text="Account Balance",fg="white",bg="black",font=("Helvetica",25))
ac.pack()

file=open(user+'1.txt','r')
bal=Label(balance,text="Your Account balance as of today is:",fg="white",bg="black",font=("Helvetica",15))
bal.pack()
ba=Label(balance,text=file.read(),fg="white",bg="black",font=("Helvetica",15))
ba.pack()



balance.mainloop()
