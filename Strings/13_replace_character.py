while True :
    str=input("Enter a word  :")
    ch=input("Enter a character to replace :")
    len=len(str)
    pos=int(input("Enter a postion to replace :"))

    if pos>=0 and pos<len:
        str=str[:pos] + ch + str[pos+1:]
        print(f"The new word is {str}:")
    else :
        print("Invalid postion !!")

    cont=input("Do you want to continue ? (yes/no):")
    if cont.lower()!='yes':
        break 