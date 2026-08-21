while True :
    str=input("Enter a string: ")
    print()
    l=len(str)
    ch=input("Enter a character to check :")
    ch_count=0
    for i in range(l):
        if str[i]==ch:
            ch_count+=1
            print(f"The character '{ch}' is present in the string at index {i} for {ch_count} times :")

    if ch_count==0:
        print(f"The character '{ch}' is no present in the string '{str}'")
    else:
        print(f"The character '{ch}' is present {ch_count} times in the string.")

    cont=input("Do you want to continue (yes/no): ")
    if cont.lower()!="yes":
        break