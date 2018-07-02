from Tkinter import *
import datetime
now = datetime.datetime.now()
withdraw=Tk()

withdraw.geometry('500x500+0+0')

w = Label(withdraw, text="Withdraw Money", fg="white", bg="black", font=("Helvetica", 25))
w.pack()

file=open("Data.txt",'r')
user=file.read()
file.close()
print user

file=open(user+'1.txt','r')
balmon=file.read()
file.close()
bal=Label(withdraw,text="Your Account balance as of today is:",fg="white",bg="black",font=("Helvetica",15))
bal.pack()
ba=Label(withdraw,text=balmon,fg="white",bg="black",font=("Helvetica",15))
ba.pack()



def withdrawl():
    h= Label(withdraw, text="How much money do you want to withdraw?", fg="white", bg="black", font=("Helvetica", 15))
    h.pack()

    money = Entry(withdraw)
    money.pack()
    money.delete(0, END)
    money.insert(0,"")
    
    def debit():
        money1=money.get()
        print money1
        print type(money1)
        file=open(user+'1.txt','r')
        balmon=file.read()
        file.close()
        print balmon
        print type(balmon)
        if int(money1)>int(balmon):
            er= Label(withdraw, text="Insufficient funds,please check your balance!", fg="white", bg="black", font=("Helvetica", 15))
            er.pack()
        else:
            file=open(user+"1.txt",'w')
            file.write(str(int(balmon)-int(money1)))
            file.close()
            n= Label(withdraw, text="Your money is successfully been debited!!", fg="white", bg="black", font=("Helvetica", 15))
            n.pack()
            file=open(user+'t.txt','a')
            transcreate4="Balance: You have Debitted "+str(money1)+"$ from your account on "+now.strftime('%d-%B-%y')+" at "+now.strftime('%H:%M:%S %p')
            file.write('\n'+transcreate4)
            file.close()
            
    deb= Button(withdraw, text = 'DEBIT', command = debit)
    deb.pack()

proceed= Button(withdraw, text = 'PROCEED', command = withdrawl)
proceed.pack()

        
withdraw.mainloop()
    
