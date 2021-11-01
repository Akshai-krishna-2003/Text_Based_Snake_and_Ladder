ans='y'

x=1

import sqlite3 as sql

while ans=='y' or ans=='Y':
    choice=int(input('''
Menu of the game:
~~~~~~~~~~~~~~~~~

1.For reading rules of the game
2.For reading the Readme file of game
3.For playing against human
4.For playing against computer
5.For viewing your past game details

Enter your choice here: '''))
    
    if choice==1:
        if x==1:
            import Game_rules as gr
            gr.game_rules()
            x+=1
        elif x>1:
            gr.game_rules()
        ans=input('''Press (y/Y) to continue the menu
Press any other key to leave the menu

Enter your choice :''')
        if ans=='y' or ans=='Y':
            continue
        else:
            print()
            print("Thank you for playing this game ... see you soon")
            break
        
    elif choice==2:
        print()
        file=open('Readme.txt','r')
        content=file.read()
        print(content)
        print()
        ans=input('''Press (y/Y) to continue the menu
Press any other key to leave the menu

Enter your choice :''')
        if ans=='y' or ans=='Y':
            continue
        else:
            print()
            print("Thank you for playing this game ... see you soon")
            break

    elif choice==3:
        print()
        print("HUMAN VS HUMAN GAME")
        print()
        import human_vs_human as hvh
        x,y=hvh.get_player_name()
        hvh.process(x,y)
        ans=input('''Press (y/Y) to continue the menu
Press any other key to leave the menu

Enter your choice :''')
        if ans=='y' or ans=='Y':
            continue
        else:
            print()
            print("Thank you for playing this game ... see you soon")
            break
    
    elif choice==4:
        print()
        print("HUMAN VS COMPUTER GAME")
        print()
        import human_vs_computer as hvc
        x=hvc.get_player_name()
        hvc.process(x)
        ans=input('''Press (y/Y) to continue the menu
Press any other key to leave the menu

Enter your choice :''')
        if ans=='y' or ans=='Y':
            continue
        else:
            print()
            print("Thank you for playing this game ... see you soon")
            break

    elif choice==5:
        print()
        print("Your past game details here")
        print()
        ch=int(input('''
From which game you want to see the details

Press 1 to see the details of human vs human game
Press 2 to see the details of human vs computer game

Enter your choice here:'''))
        if ch==1:
            print()
            print('Details of human vs human game')
            print()
            dbname='Game_details.db'
            table='Save_hvh_details'
            conn=sql.connect(database=dbname)
            cursor=conn.cursor()
            query='SELECT * FROM {}'.format(table)
            cursor.execute(query)
            lot=cursor.fetchall()
            for el in lot:
                print('''
Winner name = {}
Date of winning game = {}
Time of winning game = {}'''.format(el[0],el[1],el[2]))
                print()
        elif ch==2:
            print()
            print('Details of human vs computer game')
            print()
            dbname='Game_details.db'
            table='Save_hvc_details'
            conn=sql.connect(database=dbname)
            cursor=conn.cursor()
            query='SELECT * FROM {}'.format(table)
            cursor.execute(query)
            lot=cursor.fetchall()
            for el in lot:
                print('''
Winner name = {}
Date of winning game = {}
Time of winning game = {}'''.format(el[0],el[1],el[2]))
                print()
        else:
            print()
            print('This choice is invalid')
            print()
        ans=input('''Press (y/Y) to continue the menu
Press any other key to leave the menu

Enter your choice :''')
        if ans=='y' or ans=='Y':
            continue
        else:
            print()
            print("Thank you for playing this game ... see you soon")
            break
    else:
        print()
        print('This choice is invalid')
        print()
        ans=input('''Press (y/Y) to continue the menu
Press any other key to leave the menu

Enter your choice :''')
        if ans=='y' or ans=='Y':
            continue
        else:
            print()
            print("Thank you for playing this game ... see you soon")
            break
        print()
