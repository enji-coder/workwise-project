from tkinter import *
import tkinter.messagebox
import random

root = Tk()
root.geometry("1350x750+0+0")
root.title("Tic Tac Toe")
root.configure(background='#FFAB91')
Tops = Frame(root, bg='blue', pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)
flag = 0

myteam=StringVar()
oppteam=StringVar()
myteamname=""
oppteamname=""


tkinter.messagebox.showinfo("IPL 2020","SELECT YOUR TEAM")

lblTitle = Label(Tops, font=('arial', 50, 'bold'), text="IPL 2020", bd=21, fg='white', bg='#FFAB91',
                 justify=CENTER)
lblTitle.grid(row=0, column=0)

MainFrame = Frame(root, bg='#ffb84d', pady=2, width=1350, height=100, relief=RIDGE)
MainFrame.grid(row=1, column=0)


LeftFrame = Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=10, bg='#8E24AA', relief=RIDGE)
LeftFrame.pack(side=LEFT)


RightFrame = Frame(MainFrame, bd=20, width=750, height=500, padx=10, pady=2, bg='#ffb84d', relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=600, height=200, padx=10, pady=2, bg='#ffb84d', relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=560, height=360, padx=10, pady=2, bg='#ffb84d', relief=RIDGE)
RightFrame2.grid(row=1, column=0)

lbl_myteam = Label(RightFrame1, font=('arial', 40, 'bold'), text="Your Team :", padx=2, pady=2, bg="yellow", fg="black")
lbl_myteam.grid(row=0, column=0, sticky=W)

lbl_opp_team = Label(RightFrame1, font=('arial', 40, 'bold'), text="Opp. Team :", padx=2, pady=2, bg="yellow", fg="black")
lbl_opp_team.grid(row=1, column=0, sticky=W)


e_myteam = Entry(RightFrame1, font=('arial', 40, 'bold'), bd=3, fg="black", width=7,textvariable=myteam,
                  justify=LEFT).grid(row=0, column=1)



e_oppteam = Entry(RightFrame1, font=('arial', 40, 'bold'), bd=3, fg="black", width=7,textvariable=oppteam,
                  justify=LEFT).grid(row=1, column=1)



btnNewGame = Button(RightFrame2, text="Start Game", font=('arial', 40, 'bold'), height=1, width=15, fg='white',
                    bg='dodgerblue',command=lambda :newgame(),state="disabled")

btnNewGame.grid(row=2, column=0, padx=1, pady=11,rowspan=2)



button1 = Button(LeftFrame, text="CSK", font=('arial', 30, 'bold'), height=3, width=8, bg='white',command=lambda: select_team("CSK",button1))
button1.grid(row=1, column=0, sticky=S + N + E + W)

button2 = Button(LeftFrame, text="MI", font=('arial', 30, 'bold'), height=3, width=8, bg='white',command=lambda: select_team("MI",button2))
button2.grid(row=1, column=1, sticky=S + N + E + W)

button3 = Button(LeftFrame, text="RCB", font=('arial', 30, 'bold'), height=3, width=8, bg='white',command=lambda: select_team("RCB",button3))
button3.grid(row=1, column=2, sticky=S + N + E + W)

button4 = Button(LeftFrame, text="DC", font=('arial', 30, 'bold'), height=3, width=8, bg='white',command=lambda: select_team("DC",button4))
button4.grid(row=2, column=0, sticky=S + N + E + W)

button5 = Button(LeftFrame, text="KKR", font=('arial', 30, 'bold'), height=3, width=8, bg='white',command=lambda: select_team("KKR",button5))
button5.grid(row=2, column=1, sticky=S + N + E + W)

button6 = Button(LeftFrame, text="SRH", font=('arial', 30, 'bold'), height=3, width=8, bg='white',command=lambda: select_team("SRH",button6))
button6.grid(row=2, column=2, sticky=S + N + E + W)

button7 = Button(LeftFrame, text="KXIP", font=('arial', 30, 'bold'), height=3, width=8, bg='white',command=lambda: select_team("KXIP",button7))
button7.grid(row=3, column=0, sticky=S + N + E + W)

button8 = Button(LeftFrame, text="RR", font=('arial', 30, 'bold'), height=3, width=8, bg='white',command=lambda: select_team("RR",button8))
button8.grid(row=3, column=1, sticky=S + N + E + W)

team1_sel=0
team2_sel=0


def select_team(teamname,objname):
    global team1_sel,team2_sel,myteamname,oppteamname
    if team1_sel==0:
        objname.configure(background='#90ff0a')
        objname.configure(text='selected')
        objname.configure(state='disabled')
        myteam.set(teamname)
        myteamname=teamname
        team1_sel+=1

    elif team2_sel==0:
        objname.configure(background='#90ff0a')
        objname.configure(text='selected')
        objname.configure(state='disabled')
        oppteam.set(teamname)
        oppteamname=teamname
        team2_sel+=1
        btnNewGame.configure(state="normal")



LeftFrame_new = Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=10, bg='#8E24AA', relief=RIDGE)

heads = Button(LeftFrame_new, text="", font=('arial', 30, 'bold'), height=3, width=14, bg='white',command=lambda: toss("h",heads))
heads.grid(row=1, column=0, sticky=S + N + E + W)

tails = Button(LeftFrame_new, text="", font=('arial', 30, 'bold'), height=3, width=14, bg='white',command=lambda: toss("t",tails))
tails.grid(row=1, column=1, sticky=S + N + E + W)

balls = Button(LeftFrame_new, text="", font=('arial', 30, 'bold'), height=3, width=14, bg='white')
balls.grid(row=0, column=0, sticky=S + N + E + W,columnspan=3)


display = Button(LeftFrame_new, text="", font=('arial', 30, 'bold'), height=3, width=14, bg='white')
display.grid(row=0, column=0, sticky=S + N + E + W,columnspan=3)

# ------------------ scoreboard -----------------------
LeftFrame_scoreboard1 = Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=10, bg='#8E24AA', relief=RIDGE)

display_commentry = Button(LeftFrame_scoreboard1, text="", font=('arial', 30, 'bold'), height=3, width=14, bg='white')
display_commentry.grid(row=0, column=0, sticky=S + N + E + W,columnspan=3)


display_team = Button(LeftFrame_scoreboard1, text="", font=('arial', 30, 'bold'), height=3, width=9, bg='white')
display_team.grid(row=1, column=0, sticky=S + N + E + W)

display_score = Button(LeftFrame_scoreboard1, text="", font=('arial', 30, 'bold'), height=3, width=9, bg='white')
display_score.grid(row=1, column=1, sticky=S + N + E + W)

display_balls = Button(LeftFrame_scoreboard1, text="", font=('arial', 30, 'bold'), height=3, width=9, bg='white')
display_balls.grid(row=1, column=2, sticky=S + N + E + W)


display_game_info = Button(LeftFrame_scoreboard1, text="", font=('arial', 30, 'bold'), height=3, width=14, bg='white')
display_game_info.grid(row=2, column=0, sticky=S + N + E + W,columnspan=3)

game_type=0
score_list=[1,4,2,0,6,"OUT",1,6,0,0,"OUT"]

toss_wining_team=""
ball_value=0
ball_2_value=0

turn1=0
turn2=0


myteam_score=0
wicket=0

oppteam_score=0
o_wicket=0

rem_ball=10
rem_score=0

rem_ball_2=10
rem_score_2=0

def newgame():
    global game_type,score_list,ball_value,myteamname,myteam_score,wicket,ball_2_value,oppteam_score,o_wicket,rem_ball,rem_score,rem_ball_2,rem_score_2
    if game_type==0:
        # game started 
        LeftFrame.destroy()
        LeftFrame_new.pack(side=LEFT)
        heads.configure(text="HEADS")
        tails.configure(text="TAILS")
        #print("------------------------Here")
        game_type+=1
        

    else:
        LeftFrame_new.destroy()
        btnNewGame.configure(text="Next Ball")
        LeftFrame_scoreboard1.pack(side=LEFT)
        #print("display---------------->")
        
        if toss_wining_team==myteamname:
            if ball_value<10:
                ball_value+=1
                print("-----------------> ball 1 ",ball_value)
                s=random.choice(score_list)
                print("------------------> score ",s)
                if s==1:
                    myteam_score+=1
                    display_score_board("it's a Single",myteamname,myteam_score,wicket,ball_value)
                elif s==2:
                    myteam_score+=2
                    display_score_board("it's a double",myteamname,myteam_score,wicket,ball_value)
                elif s==4:
                    myteam_score+=4
                    display_score_board("it's a boundary",myteamname,myteam_score,wicket,ball_value)
                elif s==6:
                    myteam_score+=6
                    display_score_board("it's a SIX ! ",myteamname,myteam_score,wicket,ball_value)
                elif s=="OUT":
                    wicket+=1
                    if wicket == 3:
                        display_score_board("OOPS ! IT'S ALL OUT ! ",myteamname,myteam_score,wicket,ball_value)
                        #print(f"\n\n\t {opp_team} needs {myteam_score} in 10 balls ")
                        defending_score(oppteamname,myteam_score+1,ball_2_value+10)
                        ball_value=11
                    else:
                        display_score_board("OOPS ! IT's a wicket !",myteamname,myteam_score,wicket,ball_value)
                elif s==0:
                    display_score_board("It's DOT BALL",myteamname,myteam_score,wicket,ball_value)     
                rem_score=myteam_score+1        
            else:
                if ball_2_value<10:
                    ball_2_value+=1
                    if rem_score<=0:
                        winningscore(oppteamname+" won the match ")
                        btnNewGame.configure(state="disabled")
                        ball_2_value=11
                    else:
                        rem_ball-=1
                        print("-----------------> ball 2 ",rem_ball)
                        s=random.choice(score_list)
                        if s==1:
                            oppteam_score+=1
                            display_score_board("it's a Single",oppteamname,oppteam_score,o_wicket,ball_2_value)
                            rem_score-=1
                            defending_score(oppteamname,rem_score,rem_ball)
                        elif s==2:
                            oppteam_score+=2
                            display_score_board("it's a double",oppteamname,oppteam_score,o_wicket,ball_2_value)
                            rem_score-=2
                            defending_score(oppteamname,rem_score,rem_ball)
                        elif s==4:
                            oppteam_score+=4
                            display_score_board("it's a boundary",oppteamname,oppteam_score,o_wicket,ball_2_value)
                            rem_score-=4
                            defending_score(oppteamname,rem_score,rem_ball)
                        elif s==6:
                            oppteam_score+=6
                            display_score_board("it's a SIX ! ",oppteamname,oppteam_score,o_wicket,ball_2_value)
                            rem_score-=6
                            defending_score(oppteamname,rem_score,rem_ball)
                        elif s=="OUT":
                            o_wicket+=1
                            if o_wicket == 3:
                                
                                display_score_board("OOPS ! ITS ALL OUT ! ",oppteamname,oppteam_score,o_wicket,ball_2_value)
                                #print(f"\n\n\t {opp_team} needs {myteam_score} in 10 balls ")
                                if oppteam_score>myteam_score:
                                    winningscore(oppteamname+" won the match ")
                                    btnNewGame.configure(state="disabled")
                                    ball_2_value=11
                                else:
                                    winningscore(myteamname+" won the match ")
                                    btnNewGame.configure(state="disabled")
                                    ball_2_value=11
                            else:
                                display_score_board("OOPS ! IT's a wicket !",oppteamname,oppteam_score,o_wicket,ball_2_value)
                                defending_score(oppteamname,rem_score,rem_ball)
                        elif s==0:
                            display_score_board("It's DOT BALL",oppteamname,oppteam_score,o_wicket,ball_2_value)
                            defending_score(oppteamname,rem_score,rem_ball)
                else:
                    if oppteam_score>myteam_score:
                        winningscore(oppteamname+" won the match ")
                        btnNewGame.configure(state="disabled")
                    else:
                        winningscore(myteamname+" won the match ")
                        btnNewGame.configure(state="disabled")
        else:
            if ball_value<10:
                ball_value+=1
                
                print("-----------------> ball 1 ",ball_value)
                s=random.choice(score_list)
                print("------------------> score ",s)
                if s==1:
                    oppteam_score+=1
                    display_score_board("it's a Single",oppteamname,oppteam_score,wicket,ball_value)
                elif s==2:
                    oppteam_score+=2
                    display_score_board("it's a double",oppteamname,oppteam_score,wicket,ball_value)
                elif s==4:
                    oppteam_score+=4
                    display_score_board("it's a boundary",oppteamname,oppteam_score,wicket,ball_value)
                elif s==6:
                    oppteam_score+=6
                    display_score_board("it's a SIX ! ",oppteamname,oppteam_score,wicket,ball_value)
                elif s=="OUT":
                    wicket+=1
                    if wicket == 3:
                        display_score_board("OOPS ! IT'S ALL OUT ! ",oppteamname,oppteam_score,wicket,ball_value)
                        #print(f"\n\n\t {opp_team} needs {myteam_score} in 10 balls ")
                        defending_score(myteamname,oppteam_score+1,ball_2_value+10)
                        
                        ball_value=11
                    else:
                        display_score_board("OOPS ! IT's a wicket !",oppteamname,oppteam_score,wicket,ball_value)
                elif s==0:
                    display_score_board("It's DOT BALL",oppteamname,oppteam_score,wicket,ball_value)     
                rem_score=oppteam_score+1        
            else:
                if ball_2_value<10:
                    ball_2_value+=1
                    if rem_score<=0:
                        winningscore(myteamname+" won the match ")
                        btnNewGame.configure(state="disabled")
                        ball_2_value=11
                    else:
                        rem_ball-=1
                        print("-----------------> ball 2 ",rem_ball)
                        s=random.choice(score_list)
                        if s==1:
                            myteam_score+=1
                            display_score_board("it's a Single",myteamname,myteam_score,o_wicket,ball_2_value)
                            rem_score-=1
                            defending_score(myteamname,rem_score,rem_ball)
                        elif s==2:
                            myteam_score+=2
                            display_score_board("it's a double",myteamname,myteam_score,o_wicket,ball_2_value)
                            rem_score-=2
                            defending_score(myteamname,rem_score,rem_ball)
                        elif s==4:
                            myteam_score+=4
                            display_score_board("it's a boundary",myteamname,myteam_score,o_wicket,ball_2_value)
                            rem_score-=4
                            defending_score(myteamname,rem_score,rem_ball)
                        elif s==6:
                            myteam_score+=6
                            display_score_board("it's a SIX ! ",myteamname,myteam_score,o_wicket,ball_2_value)
                            rem_score-=6
                            defending_score(myteamname,rem_score,rem_ball)
                        elif s=="OUT":
                            o_wicket+=1
                            if o_wicket == 3:
                            
                                display_score_board("OOPS ! ITS ALL OUT ! ",myteamname,myteam_score,o_wicket,ball_2_value)
                                #print(f"\n\n\t {opp_team} needs {myteam_score} in 10 balls ")
                                if oppteam_score>myteam_score:
                                    winningscore(oppteamname+" won the match ")
                                    btnNewGame.configure(state="disabled")
                                    ball_2_value=11
                                else:
                                    winningscore(myteamname+" won the match ")
                                    btnNewGame.configure(state="disabled")
                                    ball_2_value=11
                            else:
                                display_score_board("OOPS ! IT's a wicket !",myteamname,myteam_score,o_wicket,ball_2_value)
                                defending_score(myteamname,rem_score,rem_ball)
                        elif s==0:
                            display_score_board("It's DOT BALL",myteamname,myteam_score,o_wicket,ball_2_value)
                            defending_score(myteamname,rem_score,rem_ball)
                else:
                    if oppteam_score>myteam_score:
                        winningscore(oppteamname+" won the match ")
                        btnNewGame.configure(state="disabled")
                    else:
                        winningscore(myteamname+" won the match ")
                        btnNewGame.configure(state="disabled")


def display_score_board(commentry,teamname,score,wicket,balls):
    display_commentry.configure(text=commentry)
    display_team.configure(text=teamname)
    display_score.configure(text=str(score)+" / "+str(wicket))
    display_balls.configure(text=str(balls)+" ball ")

def defending_score(teamname,score,no_of_ball):
    display_game_info.configure(text=str(teamname)+" needs "+str(score)+" runs in  "+str(no_of_ball)+" balls ")

def winningscore(msg):
    display_game_info.configure(text=str(msg))
toss_list=['h','t']

def toss(selection,objname):
    global toss_wining_team,display

    t_value=random.choice(toss_list)
    print("t_value = ",t_value)
    print("selection value=",selection)
    if selection==t_value:
        heads.configure(state="disabled")
        tails.configure(state="disabled")

        objname.configure(background='#90ff0a')
        objname.configure(text='selected')
        toss_wining_team=myteamname

        display.configure(text=str(myteamname)+" won the toss ! Bat first ")
    
        
    else:
        heads.configure(state="disabled")
        tails.configure(state="disabled")

        objname.configure(background='#90ff0a')
        objname.configure(text='selected')
        toss_wining_team=oppteamname
        display.configure(text=str(oppteamname)+" won the toss ! Bat first ")
        # display = Button(LeftFrame_new, text=str(oppteamname)+" won the toss ! Bat first", font=('arial', 30, 'bold'), height=3, width=14, bg='white',command=lambda: selection("heads"))
        # display.grid(row=0, column=0, sticky=S + N + E + W,columnspan=3)

root.mainloop()
