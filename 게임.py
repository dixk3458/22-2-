from tkinter import *
import 시작
import time
from threading import Thread
import 이미지예

def startTimer(win):
    timer = 3
    timeLabel = Label(win,text="3초뒤에 게임이 시작됩니다.",font=("Arial",20))
    timeLabel.place(x = 300,y = 150)
    time.sleep(2)
    timeLabel.place(x = 400,y=200)
    while True:   
        if timer < 1:
            print("끝")
            timeLabel.destroy()
            시작.screenDestroy(win)
            이미지예.gamePlay(win)
            break
        else:
            timeLabel.configure(text=timer)
            timer = timer - 1
            time.sleep(1)

def setTimer(win):
    timerThread = Thread(target=startTimer,args=(win,))
    timerThread.start()


def gameStart(win,checkValue):
    if(checkValue == True):
        시작.screenDestroy(win)
        img = PhotoImage(file='그림/성공눈사람지키기.png')
        lab = Label(win, image=img)
        lab.place(x=0,y=0)
        lab.image=img
        setTimer(win)
    else:
        시작.screenDestroy(win)
        img = PhotoImage(file='그림/실패눈사람지키기.png')
        lab = Label(win, image=img)
        lab.place(x=0,y=0)
        lab.image=img
        setTimer(win)





   
    
        

