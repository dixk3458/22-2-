from tkinter import *
import 시작
import 결과

def resultScreen(win,point):
    시작.screenDestroy(win)
    
    if(결과.check == False):
        if(point >= 20):
            img = PhotoImage(file='그림/실패눈사람엔딩1.png')
            lab = Label(win, image=img)
            lab.place(x=0,y=0)
            lab.image=img
        elif(20>point>=10):
            img = PhotoImage(file='그림/실패눈사람엔딩2.png')
            lab = Label(win, image=img)
            lab.place(x=0,y=0)
            lab.image=img
        elif(point<10):
            img = PhotoImage(file='그림/실패눈사람엔딩3.png')
            lab = Label(win, image=img)
            lab.place(x=0,y=0)
            lab.image=img
    elif(결과.check == True):
        if(point >= 20):
            img = PhotoImage(file='그림/성공눈사람엔딩1.png')
            lab = Label(win, image=img)
            lab.place(x=0,y=0)
            lab.image=img
        elif(20>point>=10):
            img = PhotoImage(file='그림/성공눈사람엔딩2.png')
            lab = Label(win, image=img)
            lab.place(x=0,y=0)
            lab.image=img
        elif(point<10):
            img = PhotoImage(file='그림/성공눈사람엔딩3.png')
            lab = Label(win, image=img)
            lab.place(x=0,y=0)
            lab.image=img
