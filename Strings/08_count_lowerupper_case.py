while True :
    str=input("Enter a string :")
    l=len(str)
    upper_count=0
    lower_count=0
    for i in range(l):
        if str[i].isupper():
            upper_count += 1
        elif str[i].islower():
            lower_count += 1

    print(f"The no of upper case characters is {upper_count} amnd lower case is {lower_count} ")
    cont =input("Do you want to continue ? (yes/no) :")
    if cont.lower()!='yes':
        break