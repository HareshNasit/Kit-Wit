from Tkinter import *
#from PIL import Image, ImageTk
import subprocess
import tkMessageBox
china=Tk()

china.geometry('500x700+500+0')

'''im = Image.open('Back2.jpg')
tkimage = ImageTk.PhotoImage(im)
myvar=Label(china,image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)'''



title=Label(china,text="CHINESE",fg="red",bg='black',font=("Times",45))
title.pack()

it=Label(china,text="ITEM",font=("Times",20))
it.place(x=50,y=80)

qua=Label(china,text="QUANTITY",font=("Times",20))
qua.place(x=350,y=80)



one=Label(china,text="1)Chinese Noodles (20)",font=("Courier",15))
one.place(x=0,y=120)
ones= Entry(china,width=10)
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
        file.write('Chinese Noodles(20) x'+value1+' '+':-'+str(int(value1)*20))
        file.write('\n')
        file.close()
        f.write(str(int(value1)*20))
        f.write('\n')
        f.close()
        value1=0
ok1=Button(china, text = 'OK', command = order1)
ok1.place(x=450,y=120)

two=Label(china,text="2)Noodle Soup     (10)",font=("Courier",15))
two.place(x=0,y=160)
twos= Entry(china,width=10)
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
        file.write('Noodle Soup(10) x'+value2+' '+':-'+str(int(value2)*10))
        file.write('\n')
        file.close()
        f.write(str(int(value2)*10))
        f.write('\n')
        f.close()
        value2=0
ok2=Button(china, text = 'OK', command = order2)
ok2.place(x=450,y=160)

three=Label(china,text="3)Zhajiangmian    (25)",font=("Courier",15))
three.place(x=0,y=200)
threes= Entry(china,width=10)
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
        file.write('Zhajiangmian(25) x'+value3+' '+':-'+str(int(value3)*25))
        file.write('\n')
        file.close()
        f.write(str(int(value3)*25))
        f.write('\n')
        f.close()
        value3=0
ok3=Button(china, text = 'OK', command = order3)
ok3.place(x=450,y=200)

four=Label(china,text="4)Lamian          (15)",font=("Courier",15))
four.place(x=0,y=240)
fours= Entry(china,width=10)
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
        file.write('Lamian(15) x'+value4+' '+':-'+str(int(value4)*15))
        file.write('\n')
        file.close()
        f.write(str(int(value4)*15))
        f.write('\n')
        f.close()
        value4=0
ok4=Button(china, text = 'OK', command = order4)
ok4.place(x=450,y=240)

five=Label(china,text="5)Fried Rice      (30)",font=("Courier",15))
five.place(x=0,y=280)
fives= Entry(china,width=10)
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
        file.write('Fried Rice(30) x'+value5+' '+':-'+str(int(value5)*30))
        file.write('\n')
        file.close()
        f.write(str(int(value5)*30))
        f.write('\n')
        f.close()
        value5=0
ok5=Button(china, text = 'OK', command = order5)
ok5.place(x=450,y=280)

def calc():
    price_one=20
    price_two=10
    price_three=25
    price_four=15
    price_five=30

    user_one=ones.get()
    user_two=twos.get()
    user_three=threes.get()
    user_four=fours.get()
    user_five=fives.get()

    

    total_one=price_one*int(user_one)
    total_two=price_two*int(user_two)
    total_three=price_three*int(user_three)
    total_four=price_four*int(user_four)
    total_five=price_five*int(user_five)


    total=total_one+total_two+total_three+total_four+total_five
    print total


    ask=tkMessageBox.askyesno("Title","Do you want to Order Something else?")
    if ask==True:
        china.destroy()
        #import Main.py
        subprocess.call('Main.py',shell=True)
        
    else:
        china.destroy()
        #import BILL.py
        subprocess.call('BILL.py',shell=True)
        



pla= Button(china, text = 'PLACE ORDER', command = calc)
pla.place(x=400, y = 320)
    
    


china.mainloop()
