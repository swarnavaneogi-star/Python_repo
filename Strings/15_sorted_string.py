while True :
    string = input("Enter a string :")
    sorted_string = ''.join(sorted(string))
    print(f"The sorted string is {sorted_string}")

    cont=input("Do you want to continue ? (yes/no):")
    if cont.lower()!='yes':
        break 
    