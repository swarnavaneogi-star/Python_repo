while True:
    str=input("Enter a string :")
    u=str.upper()
    print(f"The string in upper case is : {u}")

    cont=input("Do you want to continue ? (yes/no :)")
    if cont.lower()!='yes':
        break 