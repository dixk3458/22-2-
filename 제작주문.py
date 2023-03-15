from tkinter import *
import 시작

def orderScreen(win):
    시작.screenDestroy(win)
    img = PhotoImage(file='그림/시작.png')
    lab = Label(win, image=img)
    lab.place(x=0,y=0)
    lab.image=img

    btn1 = Button(win, text='▶',bg="white" ,font=("던파 비트비트체 OTF", 12), width=2, height=1, command=lambda:시작.makeBtn(win))
    btn1.place(x=760, y=460)
        
    # quiz_label = Label(win, text="눈사람의 머리길이는 40, 몸 길이 60,\n 모자 둘레 94.2, 단추 개수 3,\n 목도리 길이 50으로 만들어줘! ", font=("한컴 윤체 B", 16), bg = "white")
    # quiz_label.place(x=310, y=370)
