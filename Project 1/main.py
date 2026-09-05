import random 
'''
1: Snake
-1: Water 
0: Gun
'''
computer = random.choice([-1, 0, 1])
youstr=input("Enter your choice :")
youDict= {"s":1,"w":-1,"g":0}
revDict= {1:"Snake",-1:"Water",0:"Gun"}
you = youDict[youstr]

print(f"You chose {revDict[you]}\nComputer chose {revDict[computer]}")
if (computer == you):
    print("It's a Draw!")
else :
    if (you == 1 and computer == -1):
        print ("You Win!")
    elif (you == -1 and computer == 0):
        print("You Win!")
    elif (you == 0 and computer == 1):
        print("You Win!")
    elif (computer == 1 and you == -1): 
        print("Computer Wins!")
    elif (computer == -1 and you == 0):
        print("Computer Wins!")
    elif (computer == 0 and you == 1):
        print("Computer Wins!")
    else :
        print("Something went wrong !")