from Tkinter import *

root = Tk()

topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

button1=Button(topFrame,text="Button 1",fg="green")
button2=Button(topFrame,text="Button 2",fg="green")
button3=Button(topFrame,text="Button 3",fg="green")
button4=Button(bottomFrame,text="Button 4",fg="red")
button5=Button(bottomFrame,text="Button 5",fg="red")

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()



root.mainloop()
