while True :
    string=input("Enter a string ")
    new_string=""
    for ch in string :
        if ch not in new_string:
            new_string+=ch

    print(f"The new string without duplictaes elemnets : {new_string} ")

    cont=input("Do you want to continue ? (yes/no):")
    if cont.lower ()!='yes':
        break