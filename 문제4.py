from tkinter import *
import 시작
import 문제1
import 문제5


def clickedBtn(win,snowman,answer):
    snowman['hat']=answer
    문제5.quizScreen(win,snowman)
    


def quizScreen(win,snowman):
    시작.screenDestroy(win)
    img = PhotoImage(file='그림/모자.png')
    lab = Label(win, image=img)
    lab.place(x=0,y=0)
    lab.image=img

    #문제 1
    b1=Button(win,text="4 + 6 x 5π",bg="yellow",font=("Arial",8),width=14,height=2,command=lambda:clickedBtn(win,snowman,False))
    b1.place(x=375,y=200)
    


    #문제 2
    b2=Button(win,text="5 x 6 x 2π",bg="yellow",font=("Arial",8),width=14,height=2,command=lambda:clickedBtn(win,snowman,True))
    b2.place(x=500,y=200)
    
    

    #문제 3
    b3=Button(win,text="12 + 9 x 9 x 6π",bg="yellow",font=("Arial",8),width=14,height=2,command=lambda:clickedBtn(win,snowman,False))
    b3.place(x=625,y=200)
   

    b1.configure(bg=문제1._from_rgb((227, 242, 253))) 
    b2.configure(bg=문제1._from_rgb((227, 242, 253))) 
    b3.configure(bg=문제1._from_rgb((227, 242, 253))) 


