while True :
    string=input("Enter a string :")
    checked=""
    words=string.split()
    for word in words :
        if word not in checked:
            count=0

            for w in words:
              if word ==w:
                count+=1
            print(f"The frequency of words {word} is {count}")
            checked+=word +" "

    cont=input("Do you want to continue ? (yes/no):")
    if cont.lower()!='yes':
         break 
     