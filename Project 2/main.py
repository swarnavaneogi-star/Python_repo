import random 
n= random.randint(1,100)
guess=1
a=-1
while (a!=n):
    a= int(input("Enter a numnber to guess: "))

    if (a>n):
        print("Enter a lower number please !")
        guess+=1
    elif (a<n):
        print("Enter a higher number please !")
        guess+=1

print(f"You guessed the corrected {n} number in {guess} attempts. ")
print("Thank You!!")
