from tkinter import *
import 시작
import 문제2

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb   

snowman = {
        'head': None,
        'body': None,
        'snowBtn' : None,
        'hat':None,
        'muffler':None,
}

def clickedBtn(win,answer):
    snowman['head']=answer;
    문제2.quizScreen(win,snowman)
    
    


def makeScreen(win):
    시작.screenDestroy(win)
    img = PhotoImage(file='그림/머리.png')
    lab = Label(win, image=img)
    lab.place(x=0,y=0)
    lab.image=img
    
  
    buttonImage = PhotoImage(file='그림/woodskin.png')

    #문제 1
    b1=Button(win,text="10 + 5 x 6",bg=_from_rgb((227, 242, 253)),font=("Arial",8),width=14,height=2,command=lambda:clickedBtn(win,True))
    b1.place(x=380,y=120)
    


    #문제 2
    b2=Button(win,text="20 - 10 x 4",bg=_from_rgb((227, 242, 253)),font=("Arial",8),width=14,height=2,command=lambda:clickedBtn(win,False)) 
    b2.place(x=500,y=120)
    
    

    #문제 3
    b3=Button(win,text="6 x 3 + 32",bg=_from_rgb((227, 242, 253)),font=("Arial",8),width=14,height=2,command=lambda:clickedBtn(win,False))
    b3.place(x=620,y=120)

    b1,b2,b3.configure(bg=_from_rgb((227, 242, 253))) 