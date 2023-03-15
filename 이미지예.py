from tkinter import *
import random
import time,threading
import 최종화면
import 결과
import 문제1

yy=[0,0,0,0,0]
point=0
a=500
life=3
def gamePlay(win):
    global point

    def entryEvent(event) :
        global point
        for i in range(5):
            if entry.get() == str(answer[i]):
                a,b,c=dd()
                answer[i]=answerIndex(a,b,c)
                m=str(a)+b+str(c)
                la[i].config(text=m)
        
                yy[i]=random.randint(-400,-100)
                
                point+=1
                pointLabel.config(text="점수: "+str(point))
                
                break
            
        
        entry.delete(0, 100)
        
    def play():
        global yy
        global point
        global a
        global life
        if(결과.check==False):
            a=200
        cnt=0
        for i in range(5):
            yy[i]+=10
            
                  
            la[i].place(y=yy[i]+40)
            lap[i].place(y=yy[i])
            if(yy[i]>=300):
                yy[i]=random.randint(-400,-100)
                life-=1
                lifeLabel.config(text="목숨: "+str(life))
                if(life==0):
                    최종화면.resultScreen(win,point)
                else:
                    cnt+=1
                    if(cnt==5):
                        win.after(a, play)
                        
            elif(point==20):
                최종화면.resultScreen(win,point)
            else:
                cnt+=1
                if(cnt==5):
                    win.after(a, play)
                    
    def dd():
        symbol=['+','-','*']

        a=random.randint(1,9)
        b=random.randint(0,2)
        c=random.randint(1,9)

        selectSymbol=symbol[b]

        return (a,selectSymbol,c)

    def answerIndex(a,b,c):
        symbol=['+','-','*']
        
        result=0


        if(b=='+'):
            result=a+c
        elif(b=='-'):
            result=a-c
        elif(b=='*'):
            result=a*c
        

        return result

    # 임시 값들
    answer = ['5', '3', '2', '1', '4']
    
    bb=Label(win,bg="white",width=800,height=500)
    bb.place(x=0,y=0)
    
    pointLabel=Label(win,text="점수: "+str(point),font=("Arial",30),bg='white')
    pointLabel.place(x=350,y=200)
    
    lifeLabel=Label(win,text="목숨: "+str(life),font=("Arial",20),bg='white')
    lifeLabel.place(x=670,y=50)

    #문제 출력
    img = PhotoImage(file="그림/sun0.png")
    for i in range(5):
        yy[i]=random.randint(-500,-100)

    lp0=Label(win,image=img)
    lp0.place(x=0,y=yy[0])
    

    lp1=Label(win,image=img)
    lp1.place(x=200,y=yy[1])
    lp1.image=img

    lp2=Label(win,image=img)
    lp2.place(x=400,y=yy[2])
    lp2.image=img

    lp3=Label(win,image=img)
    lp3.place(x=600,y=yy[3])
    lp3.image=img

    lp4=Label(win,image=img)
    lp4.place(x=700,y=yy[4])
    lp4.image=img
    
    

    l0=Label(win,text="3번")
    l0.place(x=35,y=yy[0])
    
    l1=Label(win,text="1번")
    l1.place(x=235,y=yy[1])

    l2=Label(win,text="2번")
    l2.place(x=435,y=yy[2])

    l3=Label(win,text="3번")
    l3.place(x=635,y=yy[3])
    
    l4=Label(win,text="3번")
    l4.place(x=735,y=yy[4])
    
    
    la=[l0,l1,l2,l3,l4]
    lap=[lp0,lp1,lp2,lp3,lp4]
    for i in range(5):
        la[i].config(bg=문제1._from_rgb((255, 213, 79)))
        a,b,c=dd()
        answer[i]=answerIndex(a,b,c)
        m=str(a)+b+str(c)
        la[i].config(text=m)
    

    # 정답 출력 문자
        
    lab = Label(win, text = "정답 입력 :")
    lab.place(x = 300, y = 450)
    

    #정답 입력 창        
    entry = Entry(win, width = 20)
    entry.bind('<Return>', entryEvent)
    entry.place(x = 400, y = 450)

    play()
