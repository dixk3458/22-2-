from tkinter import *
import 제작주문
import pygame
import 문제1



def screenDestroy(win):
    for children in win.winfo_children():
        children.destroy()

def orderBtn(win):
    제작주문.orderScreen(win)

def makeBtn(win):
    문제1.makeScreen(win)

if(__name__=='__main__'):
    win = Tk()
    win.title('시작')
    win.geometry("800x500+370+100")
    win.resizable(width=False, height=False)

    img = PhotoImage(file='프레젠테이션3.png')
    lab = Label(win, image=img)
    lab.place(x=0,y=0)

    btn1 = Button(win, text='PLAY', font=("던파 비트비트체 OTF", 30), width=10, height=2, command=lambda:orderBtn(win))
    btn1.place(x=500, y=350)
    win.mainloop()
