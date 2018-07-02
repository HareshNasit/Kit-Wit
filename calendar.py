from Tkinter import *

import calendar as cd
root = Tk()
root.geometry('500x500+0+0')

year = 2016
month = 7    

str1 = cd.month(year, month)


root.title("Monthly Calendar")


year=Entry(root)
year.pack()
year.delete(0, END)
year.insert(0,"Year")

mo=Entry(root)
mo.pack()
mo.delete(0, END)
mo.insert(0,"Month")

def go():
    
    month=mo.get()
    yr=year.get()
    str1 = cd.month(int(yr), int(month))
    label1 = Label(root, text=str1, font=('courier', 14, 'bold'), bg='green')
    label1.pack(padx=6, pady=10)


done= Button(root, text = 'PROCEED', command = go)
done.pack()


root.mainloop()



