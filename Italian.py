# -*- coding: cp1252 -*-
from Tkinter import *
import subprocess
import tkMessageBox
italy=Tk()

italy.geometry('500x700+500+0')

title=Label(italy,text="ITALIAN",fg="red",bg='black',font=("Times",45))
title.pack()

it=Label(italy,text="ITEM",font=("Times",20))
it.place(x=50,y=80)

qua=Label(italy,text="QUANTITY",font=("Times",20))
qua.place(x=350,y=80)


one=Label(italy,text="1)Capicollo (80)",font=("Courier",15))
one.place(x=0,y=120)
ones= Entry(italy,width=10)
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
        file.write('Capicollo (80)x'+value1+' '+':-'+str(int(value1)*80))
        file.write('\n')
        file.close()
        f.write(str(int(value1)*80))
        f.write('\n')
        f.close()
        value1=0
ok1=Button(italy, text = 'OK', command = order1)
ok1.place(x=450,y=120)


two=Label(italy,text="2)Bagna ca uda (50)",font=("Courier",15))
two.place(x=0,y=160)
twos= Entry(italy,width=10)
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
        file.write('Bagna ca uda (50)x'+value2+' '+':-'+str(int(value2)*50))
        file.write('\n')
        file.close()
        f.write(str(int(value2)*50))
        f.write('\n')
        f.close()
        value2=0
ok2=Button(italy, text = 'OK', command = order2)
ok2.place(x=450,y=160)


three=Label(italy,text="3)Buccellato(20)",font=("Courier",15))
three.place(x=0,y=200)
threes= Entry(italy,width=10)
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
        file.write('Buccellato(20)x'+value3+' '+':-'+str(int(value3)*20))
        file.write('\n')
        file.close()
        f.write(str(int(value3)*20))
        f.write('\n')
        f.close()
        value3=0
ok3=Button(italy, text = 'OK', command = order3)
ok3.place(x=450,y=200)


four=Label(italy,text="4)Cibatta (35)",font=("Courier",15))
four.place(x=0,y=240)
fours= Entry(italy,width=10)
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
        file.write('Cibatta (35)x'+value4+' '+':-'+str(int(value4)*35))
        file.write('\n')
        file.close()
        f.write(str(int(value4)*35))
        f.write('\n')
        f.close()
        value4=0
ok4=Button(italy, text = 'OK', command = order4)
ok4.place(x=450,y=240)


five=Label(italy,text="5)Pizza Marinara (90)",font=("Courier",15))
five.place(x=0,y=280)
fives= Entry(italy,width=10)
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
        file.write('Pizza Marinara (90)x'+value5+' '+':-'+str(int(value5)*90))
        file.write('\n')
        file.close()
        f.write(str(int(value5)*90))
        f.write('\n')
        f.close()
        value5=0
ok5=Button(italy, text = 'OK', command = order5)
ok5.place(x=450,y=280)


six=Label(italy,text="6)Pizza Margherita (100)",font=("Courier",15))
six.place(x=0,y=320)
sixs= Entry(italy,width=10)
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
        file.write('Pizza Margherita (100)x'+value6+' '+':-'+str(int(value6)*100))
        file.write('\n')
        file.close()
        f.write(str(int(value6)*100))
        f.write('\n')
        f.close()
        value1=0
ok6=Button(italy, text = 'OK', command = order6)
ok6.place(x=450,y=320)


seven=Label(italy,text="7)Pizza Capricciosa (110)",font=("Courier",15))
seven.place(x=0,y=360)
sevens= Entry(italy,width=10)
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
        file.write('Pizza Capricciosa (110)x'+value7+' '+':-'+str(int(value7)*110))
        file.write('\n')
        file.close()
        f.write(str(int(value7)*110))
        f.write('\n')
        f.close()
        value7=0
ok7=Button(italy, text = 'OK', command = order7)
ok7.place(x=450,y=360)


def calc():
    price_one=80
    price_two=50
    price_three=20
    price_four=35
    price_five=90
    price_six=100
    price_seven=110

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
        italy.destroy()
        #import Main.py
        subprocess.call('Main.py',shell=True)
        
    else:
        italy.destroy()
        #import BILL.py
        subprocess.call('BILL.py',shell=True)
        



pla= Button(italy, text = 'PLACE ORDER', command = calc)
pla.place(x=400, y = 400)

italy.mainloop()
