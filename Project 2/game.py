import random 
n= random.randint(1,100)
guess=1
a=-1
while (a!=n):
    a= int(input("Enter a number to guess: "))

    if (a>n):
        print("Enter a lower number please !")
        guess+=1
    elif (a<n):
        print("Enter a higher number please !")
        guess+=1

print(f"You guessed the corrected {n} number in {guess} attempts. ")
with open ("best_score.txt","r") as f :
    best= (f.read())

if guess<int(best):
    with open("best_score.txt","w") as f :
        f.write(str(guess))
    best = str(guess)

print (f"The best score :{best}")
print("Thank You!!")
