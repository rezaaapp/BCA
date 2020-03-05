from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg='blue',bg = 'red')
button2 = Button(topFrame, text="Button 2", fg='pink')
button3 = Button(topFrame, text="Button 3", fg='red')
button4 = Button(topFrame, text="Button 4", fg='yellow')

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack()
button4.pack()

root.mainloop()
