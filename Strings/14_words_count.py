while True :
    s= input("Enter a sentences  :")
    l=len(s)
    words_count=0
    for i in range(l):
        if s[i]!=" ":
            if i==0 or s[i-1]==" ":
                words_count+=1

    print(f"The number of words present in the sentence are {words_count} ")

    cont=input("Do you want to continue :(yes/no) :")
    if cont.lower()!='yes':
        break 