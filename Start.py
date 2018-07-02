import subprocess
import tkinter as tk

button_flag = True


def click2():
    import StartUpScreen.py
    # subprocess.call("StartUpScreen.py",shell=True)
def click():
    print("Hey")
    import AStartUpScreen.py
    #subprocess.call("AStartUpScreen.py",shell=True)
root = tk.Tk()
root.geometry('1000x1000+0+0')
# create a frame and pack it
frame1 = tk.Frame(root)
frame1.pack(side=tk.TOP, fill=tk.X)
# pick a (small) image file you have in the working directory ...
photo1 = tk.PhotoImage(file="Sam.gif")
# create the image button, image is above (top) the optional text
button1 = tk.Button(frame1, compound=tk.TOP, width=365, height=767, image=photo1,bg='green', command=click)
button1.pack(side=tk.LEFT, padx=2, pady=2)
# save the button's image from garbage collection (needed?)
button1.image = photo1
# start the event loop


frame2 = tk.Frame(root)
frame2.pack(side=tk.TOP, fill=tk.X)
# pick a (small) image file you have in the working directory ...
photo2 = tk.PhotoImage(file="Apple.gif")
# create the image button, image is above (top) the optional text
button2 = tk.Button(frame1, compound=tk.TOP, width=365, height=767, image=photo2,bg='green', command=click2)
#button2.pack(side=tk.LEFT, padx=2, pady=2)
button2.place(x=635,y=0)
# save the button's image from garbage collection (needed?)
button2.image = photo2
root.mainloop()
