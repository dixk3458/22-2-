from tkinter import *
import 시작
import 문제1
import 문제3



def clickedBtn(win,snowman,answer):
    snowman['body']=answer
    문제3.quizScreen(win,snowman)
    


def quizScreen(win,snowman):
    시작.screenDestroy(win)
    img = PhotoImage(file='그림/몸.png')
    lab = Label(win, image=img)
    lab.place(x=0,y=0)
    lab.image=img

    #문제 1
    b1=Button(win,text="10 + 5 x 4",font=("Arial",8),width=14,height=2,command=lambda:clickedBtn(win,snowman,False))
    b1.place(x=80,y=120)
    


    #문제 2
    b2=Button(win,text="32 + 2 x 4^2",font=("Arial",8),width=14,height=2,command=lambda:clickedBtn(win,snowman,False))
    b2.place(x=200,y=120)
    
    

    #문제 3
    b3=Button(win,text="20(12 ÷ 4)",font=("Arial",8),width=14,height=2,command=lambda:clickedBtn(win,snowman,True))
    b3.place(x=320,y=120)
   
    b1.configure(bg=문제1._from_rgb((227, 242, 253))) 
    b2.configure(bg=문제1._from_rgb((227, 242, 253))) 
    b3.configure(bg=문제1._from_rgb((227, 242, 253))) 

