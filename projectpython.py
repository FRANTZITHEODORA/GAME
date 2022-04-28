# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:17:09 2022

@author: tasar
"""
import random
choosegame = int(input('please choose a game, from one to four :'))

def paperrockcut():
    user1 = [input("please give me a name ")]
    user2 = [input("please give me a name ")]
    gamemoove1 = [input("please give me a moove. rock or cut or paper ")]
    gamemoove2 = [input("please give me a moove, rock or cut or paper ")]

    gamer1 = user1 + gamemoove1
    gamer2 = user2 + gamemoove2


    if gamer1.count("rock") and gamer2.count("paper"):
        print("the winner is ", gamer2)
    if gamer1.count("paper") and gamer2.count("rock"):
        print("the winner is ", gamer1)
    if gamer1.count("paper") and gamer2.count("cut"):
        print("the winner is ", gamer2)
    if gamer1.count("cut") and gamer2.count("paper"):
        print("the winner is ", gamer1)
    if gamer1.count("rock") and gamer2.count("cut"):
        print("the winner is ", gamer1)
    if gamer1.count("cut") and gamer2.count("rock"):
        print("the winner is ", gamer1)
        
def randomnum():
    guessnumb = int(input('please guess a number'))
    life = 1
    randomnumber = random.randint(1, 101)
    while life < 7:
        print(guessnumb)
        if life == 0:
            break
        life += 1
        guessnumbsec = int(input('please guess a number'))
        print(guessnumbsec)
        continue
    if life > 0:
        print('you are out of lifes, sorry')
        if randomnumber != guessnumb:
                    print('the random number was', randomnumber)
        else:
                        print('you won!')
                        print(randomnumber)
                        randomnum()


def mastermind():
    userlist = []
    input_string = input("Enter number of elements by space: ")
    userlist = input_string.split()
    for i in range(len(userlist)):
        userlist[i] = int(userlist[i])
    
    randomlist = []
    for i in range(0,4):
         n = random.randint(1,9)
         randomlist.append(n)
         

    print(userlist)
    print(randomlist)
    compareList(userlist, randomlist)
def compareList(userlist,randomlist):
    res = [x for x in userlist + randomlist if x not in userlist or x not in randomlist]
    print(res)
    if not res:
        print("Lists l1 and l3 are equal")
    else:
        print("Lists l1 and l3 are not equal")


           
if choosegame == 0:
    print('you need to choose a number!')
if choosegame == 1:
    print('you choose the paper - cut- rock game!')
    paperrockcut()
if choosegame == 2:
    print('you choose the random number game!')
    randomnum()
if choosegame == 3:
    print('you choose mastermind!')
    mastermind()
    
