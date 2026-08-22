while True :
    str=input("Enter a string :")
    new=""
    l=len(str)
    print()
    for i in range(l):
        if str[i]!=' ':
            new+=str[i]

    print(f"The new string without the spaces is : {new}")

    cont=input("Do you want to continue ? (yes/no):")
    if cont.lower()!='yes':
        break 