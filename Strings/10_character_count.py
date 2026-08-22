while True:
    str=input("Enter a string :")
    ch_count=0
    print()
    l=len(str)
    ch=input("Enter a character to check the count :")
    for i in range (l):
        if ch==str[i]:
            ch_count+=1

    if ch_count>0:
        print(f"The character {ch} is found !!")
        print(f"It's appeared for {ch_count} times .")

    else:
        print(f"The character {ch} is not found :")

    cont=input("Do you want to continue ? (yes/no) :")
    if cont.lower()!='yes':
        break 