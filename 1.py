from tkinter import *

def entryEvent(event) :
    if entry.get() == answer[0]:
        lab0.destroy()
    if entry.get() == answer[1]:
        lab1.destroy()
    if entry.get() == answer[2]:
        lab2.destroy()
    if entry.get() == answer[3]:
        lab3.destroy()
    if entry.get() == answer[4]:
        lab4.destroy()
    
    entry.delete(0, 100)

answer = ['5', '3', '2', '1', '4'] # 임시 값들

win = Tk()
win.geometry("1000x600+100+100")
lab = Label(win, text = "정답 입력 :")
lab.grid(row = 1, column = 1)

entry = Entry(win, width = 20)
entry.bind('<Return>', entryEvent)
entry.grid(row = 1, column = 2)

img = PhotoImage(file="그림/sun0.png")

lab0 = Label(win, image = img)
lab0.place(x=100, y=50)
lab1 = Label(win, image = img)
lab1.place(x=200, y=50)
lab2 = Label(win, image = img)
lab2.place(x=300, y=50)
lab3 = Label(win, image = img)
lab3.place(x=400, y=50)
lab4 = Label(win, image = img)
lab4.place(x=500, y=50)
mainloop()
