from random import sample as random
import time
import getpass
import os
import mysql.connector

mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql",
  database="game"
)

cursor = mydb.cursor()

brc=0
while True:
    print('_______________BULLS AND COWS_________________')
    print()
    print('1. NEW GAME')
    print('2. HIGHSCORES')
    print('3. QUIT',end='\n\n')
    print('enter your option:- ',end='')
    opt=input(' ')

    if opt=='2':
        print('on what basis do you want the view the scoreboard- (T)ries/(t)ime/(B)oth- ',end='')
        sc_c=input('')
        print('\n\n')

       
        if sc_c=='T':
            cursor.execute('select * from bandc order by tries')
            scores=cursor.fetchall()
            usernames=[]
            Tries=[]
            diffs=[]
           
            print('USERNAME\t-    TRIES\t\t    - DIFFICULTY')
            for f in scores:
                usernames.append(f[0])
                Tries.append(f[1])
                diffs.append(f[2])
            for s in range(0,len(scores)-1):
                print(usernames[s],'\t\t-   ',Tries[s],'\t\t-\t',diffs[s])

        elif sc_c=='t':
            cursor.execute('select * from bandct order by time')
            scores=cursor.fetchall()
            usernames=[]
            Times=[]
            diffs=[]
           
            print('USERNAME\t-    TIME\t\t   - DIFFICULTY')
            for f in scores:
                usernames.append(f[0])
                Times.append(f[1])
                diffs.append(f[2])
            for s in range(0,len(scores)-1):
                print(usernames[s],'\t\t-   ',Times[s],'\t\t-\t',diffs[s])

        else:
            cursor.execute('select * from bandc order by tries')
            scores=cursor.fetchall()
            usernames1=[]
            Tries=[]
            diffs1=[]
           
            print('USERNAME\t-    TRIES\t\t    - DIFFICULTY')
            for f in scores:
                usernames1.append(f[0])
                Tries.append(f[1])
                diffs1.append(f[2])
            for s in range(0,len(scores)-1):
                print(usernames1[s],'\t\t-   ',Tries[s],'\t\t-\t',diffs1[s])

            print('\n\n------------------------------------------------------------------------------------------\n\n')


            cursor.execute('select * from bandct order by time')
            scores=cursor.fetchall()
            usernames2=[]
            Times=[]
            diffs2=[]
           
            print('USERNAME\t-    TIME\t\t   - DIFFICULTY')
            for f in scores:
                usernames2.append(f[0])
                Times.append(f[1])
                diffs2.append(f[2])
            for s in range(0,len(scores)-1):
                print(usernames2[s],'\t\t-   ',Times[s],'\t\t-\t',diffs2[s])

            print('\n\n------------------------------------------------------------------------------------------\n\n')


           
           
        print('\n\n\n')
        print('press any key to return to main menu:-',end='')
        input2main=input('')
        os.system('cls')
        continue

    if opt=='3':
        quit()

    if opt=='1':
        print('choose number of players(1/2):- ',end='')
        pl=input('')
    while True:
        authcheck=0
        login=0
        if pl=='1':
            os.system('cls')
            print('1.LOGIN/REGISTER')
            print('2.GUEST(stats wont be saved)',end='\n\n')
            print('enter your option:- ',end='')
            lrorg=input('')
            print('----------------------------------------------------')
           
            if lrorg=='1':
                os.system('cls')
                print('1.LOGIN')
                print('2.REGISTER',end='\n\n')
                print('enter your option:- ',end='')
                lorr=input('')
                print()
                print('-----------------------------------------------')
                if lorr=='1':
                    os.system('cls')
                    username=input('USERNAME:- ')
                    password=input('PASSWORD:- ')
                    ch=username,'=',password
                    check=''
                    for m in ch:
                        check+=m
                    f=open('test.txt','a+')
                    f.seek(0)
                    r=f.read()
                    if check in r:
                        print('login successful')
                        login=1
                    else:
                        print('incorrect username/password')
                        f.close()
                        authcheck=1
                else:
                    os.system('cls')
                    f=open('test.txt','a+')
                    username=input('USERNAME= ')
                    password=input('PASSWORD= ')
                    cpassword=input('CONFIRM PASSWORD= ')
                    r=f.read()
                    if username in r:
                        print('username already exists')
                        authcheck=1
                        break
                    elif password!=cpassword:
                        print('passwords dont match')
                        authcheck=1
                        break
                    else:
                        f=open('test.txt','a+')
                        write=username,'=',password,'\n'
                        wr=''
                        for k in write:
                            wr+=k
                        w=f.write(wr)
                        authcheck=1
                        f.close()
                        print('registration successful')
           
        while True:
            if authcheck==0:
                time.sleep(3)
                os.system('cls')
                print('------------------------------BULLS AND COWS-----------------------------------',end='\n\n')
                   
                   
                if pl=='1':
                    diff_c=input('choose difficulty(e/m/h)  -')
                    if diff_c=='h':
                        diff=6
                    elif diff_c=='m':
                        diff=5
                    else:
                        diff=4
                    numbers=[1,2,3,4,5,6,7,8,9,0]
                    n=random(numbers,diff)
                    while n[0]==0:
                        n=random(numbers,diff)
                    num=''
                    print('a random,',diff,'digit number has been generated!(without repetition)')
                    for i in n:
                        num+=str(i)
                else:
                    num=getpass.getpass('enter the number:-')
                tries=0
                guess=None
                start=time.time()
                while guess!=num:
                        tries+=1
                        print()
                        guess=input('guess-')
                        if guess=='chakka':
                            print(num)
                           
                        cows=0
                        bulls=0
                        for y in range(len(num)):                                                  #BULLS
                            x=num[y]
                            v=guess[y]
                            if x==v:
                                bulls+=1
                        for i in range(len(num)):                                                    #COWS
                            n=guess[i]
                            c=n in num
                            if c:
                                cows+=1
                                   
                        cows-=bulls
                        print('cows=',cows)
                        print('bulls=',bulls)

                stop=time.time()
                t=int(stop-start)

                if login==1:
                    utd=(username,tries,diff_c)
                    utid=(username,t,diff_c)
                    cusername=(username,)
                    cursor.execute('select * from bandc where username= %s',cusername)
                    res=cursor.fetchall()
                    if res==[]:
                        cursor.execute('insert into bandc values( %s, %s, %s)',utd)
                        cursor.execute('insert into bandct values( %s, %s, %s)',utid)
           
                    else:
                        tu=(tries,username)
                        tiu=(t,username)
                        du=(diff_c,username)
                        cusername=(username,)
                       
                        cursor.execute('select tries from bandc where username= %s',cusername)
                        prevhtrt=cursor.fetchall()
                        prevhtrt=prevhtrt[0]
                        prevhtr=0
                       
                        for t in prevhtrt:
                            prevhtr+=t
                        prevtr=int(prevhtr)
                        if prevtr>tries:
                            cursor.execute('update bandc set tries= %s where username= %s',tu)
                            cursor.execute('update bandc set difficulty= %s where username= %s',du)
                       

                        cursor.execute('select time from bandct where username= %s',cusername)
                        prevhtt=cursor.fetchall()
                        prevhtt=prevhtt[0]
                        prevht=0

                        for ts in prevhtt:
                            prevht+=ts
                        prevt=int(prevht)
                        if prevt>t:
                            cursor.execute('update bandc set time= %s where username= %s',tiu)
                            cursor.execute('update bandc set difficulty= %s where username= %s',du)
                           
                mydb.commit()      
                print('Congrats , you won the game using',tries,'tries and within',t,'seconds')
                a=input('Do you want to play again?(y/n)')
                if a=='n' or a=='N':
                    os.system('cls')
                    brc=1
                    break
                else:
                    print()
                    print('===================================================')
           
            else:
                time.sleep(4)
                os.system('cls')
                break
           
        if brc!=0:
            wwww-=1
            time.sleep(3)
            os.system('cls')
            break
