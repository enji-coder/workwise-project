import random
import os 
import time 


os.system("cls")
print("\n\t\t\t\t WELCOME TO IPL 2020 ")

print("\n##################################################################################\n")

team_list=["CSK","MI","KXIP","KKR","RR","RCB","DC","SRH"]
toss_list=['h','t']
score_list=[1,4,2,0,6,"OUT",1,6,0,0,"OUT"]

print("\n\t\t IPL 2020 Team LIST :\n")
for i in team_list:
    print("\t\t\t ",i)

myteam=input("Enter your team name : ")

opp_teamlist=list(team_list)

if myteam in opp_teamlist:
    opp_teamlist.remove(myteam)

opp_team=random.choice(opp_teamlist)
print("\n##################################################################################\n")
print(f"\t\t\t  {myteam}   Vs  {opp_team} ")

input()

print("\n##################################  TOSS  ################################################\n")
t_value=random.choice(toss_list)
t=input("Choose heads or tails for toss(h/t): ")

os.system("cls")

if t_value==t:
    print(f"\n\n\t\t{myteam} won the toss and decided to bat first ! ")
    myteam_score=0
    wicket=0
    ball=0
    for i in range(1,11):
        input()
        ball+=1
        s=random.choice(score_list)
        if s==1:
            print("\n*********************************************  IT IS A SINGLE  **********************************************\n") 
            myteam_score+=1
            print(f"score | {myteam} : {myteam_score}/{wicket}  ({ball} ball )")
        elif s==2:
            print("\n*********************************************  IT IS A Double  **********************************************\n") 
            myteam_score+=2
            print(f"score | {myteam} : {myteam_score}/{wicket}  ({ball} ball )")
        elif s==4:
            print("\n*********************************************  IT IS A FOUR  **********************************************\n") 
            myteam_score+=4
            print(f"score | {myteam} : {myteam_score}/{wicket}  ({ball} ball )")
        elif s==6:
            print("\n*********************************************  IT IS A SIX  **********************************************\n") 
            myteam_score+=6
            print(f"score | {myteam} : {myteam_score}/{wicket}  ({ball} ball )")
        elif s=="OUT":
            print("\n*********************************************  OOPS ! ITS A WICKET  **********************************************\n") 
            
            wicket+=1
            if wicket == 3:
                print("\n*********************************************  OOPS ! ITS ALL OUT  **********************************************\n") 
                print(f"score | {myteam} : {myteam_score}/{wicket}  ({ball} ball )")
                print(f"\n\n\t {opp_team} needs {myteam_score} in 10 balls ")
                break

            print(f"score | {myteam} : {myteam_score}/{wicket}  ({ball} ball )")

        elif s==0:
            print("\n*********************************************  ITS A DOT BALL  **********************************************\n") 
            print(f"score | {myteam} : {myteam_score}/{wicket}  ({ball} ball )")

    print("\n********************************************* END OF 10 BALLS **********************************************\n") 
    print(f"score | {myteam} : {myteam_score}/{wicket}  ({ball} ball )")
    print(f"\n\n\t {opp_team} needs {myteam_score} in 10 balls ")

    input()
    os.system("cls")
    print(f"\n********************************************* {opp_team} Batting **********************************************\n") 


    opp_score=0
    wicket=0
    ball=0
    for i in range(1,11):
        input()
        ball+=1
        s=random.choice(score_list)
        if s==1:
            print("\n*********************************************  IT IS A SINGLE  **********************************************\n") 
            opp_score+=1
            print(f"score | {opp_team} : {opp_score}/{wicket}  ({ball} ball )")
        elif s==2:
            print("\n*********************************************  IT IS A Double  **********************************************\n") 
            opp_score+=2
            print(f"score | {opp_team} : {opp_score}/{wicket}  ({ball} ball )")
        elif s==4:
            print("\n*********************************************  IT IS A FOUR  **********************************************\n") 
            opp_score+=4
            print(f"score | {opp_team} : {opp_score}/{wicket}  ({ball} ball )")
        elif s==6:
            print("\n*********************************************  IT IS A SIX  **********************************************\n") 
            opp_score+=6
            print(f"score | {opp_team} : {opp_score}/{wicket}  ({ball} ball )")
        elif s=="OUT":
            print("\n*********************************************  OOPS ! ITS A WICKET  **********************************************\n") 
            wicket+=1
            if wicket == 3:
                print("\n*********************************************  OOPS ! ITS ALL OUT  **********************************************\n") 
                print(f"score | {opp_team} : {opp_score}/{wicket}  ({ball} ball )")
                if opp_score>myteam_score:
                    print(f"\n*********************************************  {opp_team} WON THE MATCH !  **********************************************\n") 
                    
                elif opp_score==myteam_score:
                    
                    print(f"\n*********************************************  ITS A TIE !  **********************************************\n") 
                else:
                    print(f"\n*********************************************  {myteam} WON THE MATCH !  **********************************************\n") 
                    
                break
            print(f"score | {opp_team} : {opp_score}/{wicket}  ({ball} ball )")

        elif s==0:
            print("\n*********************************************  ITS A DOT BALL  **********************************************\n") 
            print(f"score | {opp_team} : {opp_score}/{wicket}  ({ball} ball )")
        
    if opp_score>myteam_score:
        print(f"\n*********************************************  {opp_team} WON THE MATCH !  **********************************************\n") 
    elif opp_score==myteam_score:
                print(f"\n*********************************************  ITS A TIE !  **********************************************\n") 
    else:
        print(f"\n*********************************************  {myteam} WON THE MATCH !  **********************************************\n") 

else:
    print(f"\n\n\t\t{opp_team} won the toss and decided to bat first ! ")
    opp_score=0
    wicket=0
    ball=0
    for i in range(1,11):
        input()
        ball+=1
        s=random.choice(score_list)
        if s==1:
            print("\n*********************************************  IT IS A SINGLE  **********************************************\n") 
            opp_score+=1
            print(f"score | {opp_team} : {opp_score}/{wicket}  ({ball} ball )")
        elif s==2:
            print("\n*********************************************  IT IS A Double  **********************************************\n") 
            opp_score+=2
            print(f"score | {opp_team} : {opp_score}/{wicket}  ({ball} ball )")
        elif s==4:
            print("\n*********************************************  IT IS A FOUR  **********************************************\n") 
            opp_score+=4
            print(f"score | {opp_team} : {opp_score}/{wicket}  ({ball} ball )")
        elif s==6:
            print("\n*********************************************  IT IS A SIX  **********************************************\n") 
            opp_score+=6
            print(f"score | {opp_team} : {opp_score}/{wicket}  ({ball} ball )")
        elif s=="OUT":
            print("\n*********************************************  OOPS ! ITS A WICKET  **********************************************\n") 
        
            wicket+=1
            if wicket == 3:
                print("\n*********************************************  OOPS ! ITS ALL OUT  **********************************************\n") 
                print(f"score | {opp_team} : {opp_score}/{wicket}  ({ball} ball )")
                print(f"\n\n\t {myteam} needs {opp_score} in 10 balls ")
                break

            print(f"score | {opp_team} : {opp_score}/{wicket}  ({ball} ball )")

        elif s==0:
            print("\n*********************************************  ITS A DOT BALL  **********************************************\n") 
            print(f"score | {opp_team} : {opp_score}/{wicket}  ({ball} ball )")

    print("\n********************************************* END OF 10 BALLS **********************************************\n") 
    print(f"score | {opp_team} : {opp_score}/{wicket}  ({ball} ball )")
    print(f"\n\n\t {myteam} needs {opp_score} in 10 balls ")   

    input()
    os.system("cls")
    print(f"\n********************************************* {myteam} BATTING **********************************************\n") 

    opp_score=0
    wicket=0
    ball=0
    for i in range(1,11):
        input()
        ball+=1
        s=random.choice(score_list)
        if s==1:
            print("\n*********************************************  IT IS A SINGLE  **********************************************\n") 
            myteam_score+=1
            print(f"score | {myteam} : {myteam_score}/{wicket}  ({ball} ball )")
        elif s==2:
            print("\n*********************************************  IT IS A Double  **********************************************\n") 
            myteam_score+=2
            print(f"score | {myteam} : {myteam_score}/{wicket}  ({ball} ball )")
        elif s==4:
            print("\n*********************************************  IT IS A FOUR  **********************************************\n") 
            myteam_score+=4
            print(f"score | {myteam} : {myteam_score}/{wicket}  ({ball} ball )")
        elif s==6:
            print("\n*********************************************  IT IS A SIX  **********************************************\n") 
            myteam_score+=6
            print(f"score | {myteam} : {myteam_score}/{wicket}  ({ball} ball )")
        elif s=="OUT":
            print("\n*********************************************  OOPS ! ITS A WICKET  **********************************************\n") 
            wicket+=1
            if wicket == 3:
                print("\n*********************************************  OOPS ! ITS ALL OUT  **********************************************\n") 
                print(f"score | {myteam} : {myteam_score}/{wicket}  ({ball} ball )")
                if opp_score>myteam_score:
                    print(f"\n*********************************************  {opp_team} WON THE MATCH !  **********************************************\n") 
                    break
                elif opp_score==myteam_score:
                    print(f"\n*********************************************  ITS A TIE !  **********************************************\n") 
                    break
                else:
                    print(f"\n*********************************************  {myteam} WON THE MATCH !  **********************************************\n") 
                    break
                break

            print(f"score | {myteam} : {myteam_score}/{wicket}  ({ball} ball )")

        elif s==0:
            print("\n*********************************************  ITS A DOT BALL  **********************************************\n") 
            print(f"score | {myteam} : {myteam_score}/{wicket}  ({ball} ball )")

    print("\n********************************************* END OF 10 BALLS **********************************************\n") 
    print(f"score | {myteam} : {myteam_score}/{wicket}  ({ball} ball )")
    
    if opp_score>myteam_score:
        print(f"\n*********************************************  {opp_team} WON THE MATCH !  **********************************************\n") 
    elif opp_score==myteam_score:
                    print(f"\n*********************************************  ITS A TIE !  **********************************************\n") 
    else:
        print(f"\n*********************************************  {myteam} WON THE MATCH !  **********************************************\n") 




