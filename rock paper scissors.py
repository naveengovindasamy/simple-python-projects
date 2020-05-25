import sys
user1 = input("what is your name?: ")
user2 = input("and your name?: ")
user1_answer = input("%s, do you want to choose rock, paper or scissors?: "% user1)
user2_answer = input("%s, do you want to choose rock, paper, scissors?: "% user2)
def compare(u1, u2):
    if u1 == u2:
        return("it's a tie")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return(user1,"wins!")
        else:
            return(user2,"wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return(user1,"wins")
        else:
            return(user2,"wins")
    elif u1 == 'rock':
        if u2 == 'rock':
            return(user1,"wins!")
        else:
            return(user2,"win!")
    else:
        return("invalid input! you have not entered rock, paper, scissors,try again,")
    sys.exit()
print(compare(user1_answer, user2_answer))