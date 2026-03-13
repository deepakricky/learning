##Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
# f=open("poem.txt")
# c=f.read()
# if ("twinkle" in c):
#     print("Yes it is in the poem")
# else:
#     print("No it is not in the poem")
# f.close()

'''The game() function in a program lets a user play a game and returns the score as an integer.
You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. 
You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.'''

import random
def game():
    print("You are playing a game ")
    score=random.randint(1,100)
    #Fetch the hiscore
    with open("highscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"Your score: {score}")
    if(score>hiscore):
        #write/update this in hiscore to the file
        with open("highscore.txt","w") as f:
            f.write(str(score))
    return score
game()
