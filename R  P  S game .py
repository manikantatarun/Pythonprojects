#!/usr/bin/env python
# coding: utf-8

# In[1]:


def takePlayerInput():
    player = "blank"
    while not (player.lower() =="r" or player.lower() =="p" or player.lower() =="s"):
        player = input("Enter Your Choice >> R | P | S =")
    return player.lower()
    


# In[3]:


import random

def getBotInput():
    lst = ['r','p','s']
    return random.choice(lst)


# In[4]:


def checkWinner(player,bot):
    if player == 'r' and bot == "r":
        return "draw"
    elif player == "r" and bot == "p":
        return "bot"
    elif player == "r" and bot == "s":
        return "player"
    elif player == "p" and bot == "s":
        return "bot"
    elif player == "p" and bot == "r":
        return "player"
    elif player == "p" and bot == "p":
        return "draw"
    elif player == "s" and bot == "r":
        return "bot"
    elif player == "s" and bot == "p":
        return "player"
    elif player == "s" and bot == "s":
        return "draw"
    else:
        return "draw"


# In[ ]:


def rockPaperScisser():
    endGame = "n"
    playerScore = 0
    botScore = 0
    while endGame.lower() != "y":
        ply = takePlayerInput()
        bt = getBotInput()
        print("Bot Choice is =",bt)
        winner = checkWinner(player = ply,bot = bt)
        print("Winner is " , winner)
        print (" ")
        if winner == "player":
            playerScore += 2
        elif winner == "bot":
            botScore += 2
        else:
            playerScore += 1
            botScore += 1
        
        print("Player Score =",playerScore)
        print("Bot Score    =",botScore)
        print(" ")
        endGame = input("You want to end Y/N - ")
        


# In[ ]:


rockPaperScisser()


# In[ ]:




