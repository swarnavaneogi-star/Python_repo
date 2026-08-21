str=input("Enter a string: ")
print()
l=len(str)
print(f"Length of the string is :{l}")
count_spaces=0
count_ch=0
for i in range(l):
    if str[i]==" ":
        count_spaces+=1
    if str[i].isalpha():
        count_ch+=1
print(f"The number of spaces in the string is : {count_spaces}")
print(f"The number of characters in the string is : {count_ch}")