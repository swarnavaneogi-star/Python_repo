while True:
    str=input("Enter a string :")
    u=str.lower()
    print(f"The string in lower case is : {u}")

    cont=input("Do you want to continue ? (yes/no :)")
    if cont.lower()!='yes':
        break 