while True :
    string=input("Enter a string :")
    l=len(string)
    palindrome=""
    for i in range (l-1,-1,-1):
        palindrome+=string[i]

    if palindrome==string:
        print(f"The given string '{string}' is palindrome. ")
    else :
        print(f"The given '{string}' string is not palindrome. ")

    cont=input("Do you want to continue ? (yes/no):")
    if cont.lower()!='yes':
        break   