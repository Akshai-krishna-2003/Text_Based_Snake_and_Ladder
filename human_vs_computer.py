if __name__=='__main__':
    print("File not meant for execution!")

import random
import sqlite3 as sql

def get_player_name():
    player=input("Enter name of player : ")
    return player
    
def throw_dice1(player):
    print()
    enter=input("{},Press 'ENTER' to roll the Die: ".format(player))
    n1=random.randint(1,6)
    print('Face of the die came: ',n1)
    return n1

def throw_dice2():
    print()
    print("It's my turn to roll the die")
    n2=random.randint(1,6)
    print('Face of the die came: ',n2)
    return n2

def process(player):
    snake_bite={35:4,
                54:12,
                74:45,
                86:19,
                92:51,
                98:41}

    ladder={9:29,
            24:84,
            27:73,
            42:79,
            67:96}


    sum1=0
    sum2=0
    print()
    print("Let's start the game")

    while sum1<100 and sum2<100:
        
        value1=throw_dice1(player)
        if value1==1 or sum1>=1:
            if sum1+value1<100:
                sum1+=value1
                print(player,'your score is',sum1)
                if sum1 in snake_bite:
                    print('".....Bitten by snake....."')
                    sum1=snake_bite[sum1]
                    print('Your current score is',sum1)
                elif sum1 in ladder:
                    print('".....Gained access to ladder....."')
                    sum1=ladder[sum1]
                    print('Your current score is',sum1)
            elif sum1+value1>100:
                sum1=sum1
                num1=100-sum1
                print('Come-on, get "{}" to win the game'.format(num1))
                print('Your current score is',sum1)
            elif sum1+value1==100:
                print('You got to that 100!')
                print('"Congrats you won the game"')

                print()
                print('Saving game details')
                dbname='Game_details.db'
                table='Save_hvc_details'
                conn=sql.connect(database=dbname)
                cursor=conn.cursor()
                query='INSERT INTO {} VALUES("{}",CURRENT_DATE,CURRENT_TIME)'.format(table,player)
                cursor.execute(query)
                conn.commit()
                break
        else:
            print("Get '1' to get into the board")
            
        
        value2=throw_dice2()
        if value2==1 or sum2>=1:
            if sum2+value2<100:
                sum2+=value2
                print('My score is',sum2)
                if sum2 in snake_bite:
                    print('".....Bitten by snake....."')
                    sum2=snake_bite[sum2]
                    print('My current score is',sum2)
                elif sum2 in ladder:
                    print('".....Gained access to ladder....."')
                    sum2=ladder[sum2]
                    print('My current score is',sum2)
            elif sum2+value2>100:
                sum2=sum2
                num2=100-sum2
                print('Come-on, get "{}" to win the game'.format(num2))
                print('My current score is',sum2)
            elif sum2+value2==100:
                print('I got to that 100!')
                print('"I won the game!"')

                print()
                print('Saving game details')
                dbname='Game_details.db'
                table='Save_hvc_details'
                conn=sql.connect(database=dbname)
                cursor=conn.cursor()
                query='INSERT INTO {} VALUES("Computer",CURRENT_DATE,CURRENT_TIME)'.format(table)
                cursor.execute(query)
                conn.commit()
                break
        else:
            print("Get '1' to get into the board")

