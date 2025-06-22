import random
print("hello guys welcome to this isnteresting game\n")
print("you will have to chose number between 1 to 100 \n")

x=random.choice(range(0,101))
#print(x)# just for simplicity

chosing_difficulty=input("which difficulty you want to play? 'easy','hard'\n").lower()

game_over=False
guessing_chance=0


if chosing_difficulty=="easy":
    guessing_chance+=10
elif chosing_difficulty=="hard":
    guessing_chance+=5
else:
    print("wrong input")

    
print(f"you will get {guessing_chance} chances ")


while not game_over:

    guess=int(input("guess the number"))

    if x==guess:
        print("you guessed it right")
    elif x>guess:
        print("too low")
    elif x<guess:
        print("too high")


    if guess != x:
        guessing_chance -=1
        print(f"wrong guess you have {guessing_chance} guess left")
        if guessing_chance == 0:
            game_over=True
            print("you lose try again")





