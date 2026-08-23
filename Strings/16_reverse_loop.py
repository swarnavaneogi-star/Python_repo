while True :
    string=input("Enter a string :")
    l=len(string)
    rev=""
    for i in range(l-1,-1,-1):
        rev+=string[i]
    print(f"The reversed string  is : {rev}")

    cont=input("Do you want to continue ? (yes/no):")
    if cont.lower()!='yes':
        break 