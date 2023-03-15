from tkinter import *
import 시작
import 게임

check=False

def gameStart(win,checkValue):
    if(checkValue == True):
        시작.screenDestroy(win)
        img = PhotoImage(file='그림/단추.png')
        lab = Label(win, image=img)
        lab.place(x=0,y=0)
        lab.image=img
    else:
        img = PhotoImage(file='그림/머리.png')
        lab = Label(win, image=img)
        lab.place(x=0,y=0)
        lab.image=img




def resultScreen(win,checkedValue):
    시작.screenDestroy(win)
    if(checkedValue == True):
        global check
        check=checkedValue
        img = PhotoImage(file='그림/예쁜눈사람.png')
        lab = Label(win, image=img)
        lab.place(x=0,y=0)
        lab.image=img
        btn1 = Button(win, text='▶',bg="white" ,font=("던파 비트비트체 OTF", 12), width=2, height=1, command=lambda:게임.gameStart(win,checkedValue))
        btn1.place(x=760, y=460)
    else:
        img = PhotoImage(file='그림/망한눈사람.png')
        lab = Label(win, image=img)
        lab.place(x=0,y=0)
        lab.image=img
        btn1 = Button(win, text='▶',bg="white" ,font=("던파 비트비트체 OTF", 12), width=2, height=1, command=lambda:게임.gameStart(win,checkedValue))
        btn1.place(x=760, y=460)



def checkSnowman(win,snowman):
    for key in snowman:
        if(snowman[key] == False):
            checkedValue = False
            break
        else:
            checkedValue = True
    return resultScreen(win,checkedValue)
