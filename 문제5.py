from tkinter import *
import 시작
import 문제1
import 결과


def clickedBtn(win,snowman,answer):
    snowman['muffler']=answer
    결과.checkSnowman(win,snowman)
    


def quizScreen(win,snowman):
    시작.screenDestroy(win)
    img = PhotoImage(file='그림/목도리.png')
    lab = Label(win, image=img)
    lab.place(x=0,y=0)
    lab.image=img

    #문제 1
    b1=Button(win,text="4(2 x 4) + 12 ÷ 6 x 9  ",bg="yellow",font=("Arial",8),width=18,height=2,command=lambda:clickedBtn(win,snowman,True))
    b1.place(x=375,y=200)
    


    #문제 2
    b2=Button(win,text="1 ÷ 4 + 9 ÷ 2 - 1",bg="yellow",font=("Arial",8),width=16,height=2,command=lambda:clickedBtn(win,snowman,False))
    b2.place(x=500,y=200)
    
    

    #문제 3
    b3=Button(win,text="(-1) x (-2) x (-3) x (-4)",bg="yellow",font=("Arial",8),width=18,height=2,command=lambda:clickedBtn(win,snowman,False))
    b3.place(x=615,y=200)
   
    b1.configure(bg=문제1._from_rgb((227, 242, 253))) 
    b2.configure(bg=문제1._from_rgb((227, 242, 253))) 
    b3.configure(bg=문제1._from_rgb((227, 242, 253))) 

   

