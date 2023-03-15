from tkinter import *
import 시작
import 문제1
import 문제4


def clickedBtn(win,snowman,answer):
    snowman['snowBtn']=answer
    문제4.quizScreen(win,snowman)
    


def quizScreen(win,snowman):
    시작.screenDestroy(win)
    img = PhotoImage(file='그림/단추.png')
    lab = Label(win, image=img)
    lab.place(x=0,y=0)
    lab.image=img

    #문제 1
    b1=Button(win,text="48 x 8 ÷ 6 - 51",bg="yellow",font=("Arial",8),width=14,height=2,command=lambda:clickedBtn(win,snowman,False))
    b1.place(x=380,y=200)
    


    #문제 2
    b2=Button(win,text="12 + 2 x 16 ÷ 4",bg="yellow",font=("Arial",8),width=14,height=2,command=lambda:clickedBtn(win,snowman,False))
    b2.place(x=500,y=200)
    
    

    #문제 3
    b3=Button(win,text="-2(3 + 100 x 0 - 5)-1",bg="yellow",font=("Arial",8),width=16,height=2,command=lambda:clickedBtn(win,snowman,True))
    b3.place(x=615,y=200)
   

    b1.configure(bg=문제1._from_rgb((227, 242, 253))) 
    b2.configure(bg=문제1._from_rgb((227, 242, 253))) 
    b3.configure(bg=문제1._from_rgb((227, 242, 253))) 
