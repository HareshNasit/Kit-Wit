from Tkinter import *
import os
bill=Tk()

bill.geometry('500x700+0+0')

file=open('Final.txt','r')

order=file.readlines()
file.close()

f=open('Total.txt','r')

tot=f.readlines()
f.close()

SUM=0
for i in tot:
    SUM=SUM+int(i)
    print SUM
    

title=Label(bill,text="BILL!!",fg="red",bg='black',font=("Times",45))
title.pack()

for i in order:
    items=Label(bill,text=i,font=("Times",20))
    items.pack()

total=Label(bill,text='TOTAL='+str(SUM),font=('Times',20))
total.pack()

os.remove('Total.txt')
os.remove("Final.txt")
bill.mainloop()
