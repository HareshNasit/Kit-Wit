# -*- coding: cp1252 -*-
from Tkinter import *
import subprocess
import tkMessageBox
america=Tk()

america.geometry('500x700+500+0')

title=Label(america,text="AMERICAN",fg="red",bg='black',font=("Times",45))
title.pack()

it=Label(america,text="ITEM",font=("Times",20))
it.place(x=50,y=80)

qua=Label(america,text="QUANTITY",font=("Times",20))
qua.place(x=350,y=80)


one=Label(america,text="1)American Fried Rice (15)",font=("Courier",15))
one.place(x=0,y=120)
ones= Entry(america,width=10)
ones.place(x=380,y=120)
ones.delete(0, END)
ones.insert(0,"0")
def order1():
    file=open('Final.txt','a')
    f=open('Total.txt','a')
    value1=ones.get()
    if int(value1)==0:
        print"Don't simply press it!!"
    else:
        file.write('American Fried Rice (15)x'+value1+' '+':-'+str(int(value1)*15))
        file.write('\n')
        file.close()
        f.write(str(int(value1)*15))
        f.write('\n')
        f.close()
        value1=0
ok1=Button(america, text = 'OK', command = order1)
ok1.place(x=450,y=120)


two=Label(america,text="2)Dirty Rice (25)",font=("Courier",15))
two.place(x=0,y=160)
twos= Entry(america,width=10)
twos.place(x=380,y=160)
twos.delete(0, END)
twos.insert(0,"0")
def order2():
    file=open('Final.txt','a')
    f=open('Total.txt','a')
    value2=twos.get()
    if int(value2)==0:
        print"Don't simply press it!!"
    else:
        file.write('Dirty Rice (25)x'+value2+' '+':-'+str(int(value2)*25))
        file.write('\n')
        file.close()
        f.write(str(int(value2)*25))
        f.write('\n')
        f.close()
        value2=0
ok2=Button(america, text = 'OK', command = order2)
ok2.place(x=450,y=160)


three=Label(america,text="3)Chaudin (20)",font=("Courier",15))
three.place(x=0,y=200)
threes= Entry(america,width=10)
threes.place(x=380,y=200)
threes.delete(0, END)
threes.insert(0,"0")
def order3():
    file=open('Final.txt','a')
    f=open('Total.txt','a')
    value3=threes.get()
    if int(value3)==0:
        print"Don't simply press it!!"
    else:
        file.write('Chaudin (20)x'+value3+' '+':-'+str(int(value3)*20))
        file.write('\n')
        file.close()
        f.write(str(int(value3)*20))
        f.write('\n')
        f.close()
        value3=0
ok3=Button(america, text = 'OK', command = order3)
ok3.place(x=450,y=200)


four=Label(america,text="4)Half-Smoke (25)",font=("Courier",15))
four.place(x=0,y=240)
fours= Entry(america,width=10)
fours.place(x=380,y=240)
fours.delete(0, END)
fours.insert(0,"0")
def order4():
    file=open('Final.txt','a')
    f=open('Total.txt','a')
    value4=fours.get()
    if int(value4)==0:
        print"Don't simply press it!!"
    else:
        file.write('Half-Smoke (25)x'+value4+' '+':-'+str(int(value4)*25))
        file.write('\n')
        file.close()
        f.write(str(int(value4)*25))
        f.write('\n')
        f.close()
        value4=0
ok4=Button(america, text = 'OK', command = order4)
ok4.place(x=450,y=240)


five=Label(america,text="5)Barbecue (40)",font=("Courier",15))
five.place(x=0,y=280)
fives= Entry(america,width=10)
fives.place(x=380,y=280)
fives.delete(0, END)
fives.insert(0,"0")
def order5():
    file=open('Final.txt','a')
    f=open('Total.txt','a')
    value5=fives.get()
    if int(value5)==0:
        print"Don't simply press it!!"
    else:
        file.write('Barbecue (40)x'+value5+' '+':-'+str(int(value5)*40))
        file.write('\n')
        file.close()
        f.write(str(int(value5)*40))
        f.write('\n')
        f.close()
        value5=0
ok5=Button(america, text = 'OK', command = order5)
ok5.place(x=450,y=280)


six=Label(america,text="6)New American Cuisine (100)",font=("Courier",15))
six.place(x=0,y=320)
sixs= Entry(america,width=10)
sixs.place(x=380,y=320)
sixs.delete(0, END)
sixs.insert(0,"0")
def order6():
    file=open('Final.txt','a')
    f=open('Total.txt','a')
    value6=sixs.get()
    if int(value6)==0:
        print"Don't simply press it!!"
    else:
        file.write('New American Cuisine (100)x'+value6+' '+':-'+str(int(value6)*100))
        file.write('\n')
        file.close()
        f.write(str(int(value6)*100))
        f.write('\n')
        f.close()
        value1=0
ok6=Button(america, text = 'OK', command = order6)
ok6.place(x=450,y=320)


seven=Label(america,text="7)Tex-Mex (30)",font=("Courier",15))
seven.place(x=0,y=360)
sevens= Entry(america,width=10)
sevens.place(x=380,y=360)
sevens.delete(0, END)
sevens.insert(0,"0")
def order7():
    file=open('Final.txt','a')
    f=open('Total.txt','a')
    value7=sevens.get()
    if int(value7)==0:
        print"Don't simply press it!!"
    else:
        file.write('Tex-Mex (30)x'+value7+' '+':-'+str(int(value7)*30))
        file.write('\n')
        file.close()
        f.write(str(int(value7)*30))
        f.write('\n')
        f.close()
        value7=0
ok7=Button(america, text = 'OK', command = order7)
ok7.place(x=450,y=360)


def calc():
    price_one=15
    price_two=25
    price_three=20
    price_four=25
    price_five=40
    price_six=100
    price_seven=30

    user_one=ones.get()
    user_two=twos.get()
    user_three=threes.get()
    user_four=fours.get()
    user_five=fives.get()
    user_six=sixs.get()
    user_seven=sevens.get()
    

    total_one=price_one*int(user_one)
    total_two=price_two*int(user_two)
    total_three=price_three*int(user_three)
    total_four=price_four*int(user_four)
    total_five=price_five*int(user_five)
    total_six=price_six*int(user_six)
    total_seven=price_seven*int(user_seven)

    total=total_one+total_two+total_three+total_four+total_five+total_six+total_seven
    print total


    ask=tkMessageBox.askyesno("Title","Do you want to Order Something else?")
    if ask==True:
        america.destroy()
        #import Main.py
        subprocess.call('Main.py',shell=True)
        
    else:
        america.destroy()
        #import BILL.py
        subprocess.call('BILL.py',shell=True)
        



pla= Button(america, text = 'PLACE ORDER', command = calc)
pla.place(x=400, y = 400)

america.mainloop()
