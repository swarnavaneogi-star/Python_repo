name=input("Enter your name: ")
l=len(name)
print(f"Length of your name is: {l}")
print()
print("Accessing each character in the name:")
for i in range(l):
    print(f"Character at index {i} is : {name[i]}")