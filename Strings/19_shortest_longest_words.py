while True :
    string=input("Enter a string :")
    words=string.split()
    longest=words[0]
    shortest=words[0]
    for word in words:
        if len(word)>len(longest):
            longest=word
        elif len(word)<len(shortest):
            shortest=word

    print(f"The Longest word is : {longest}")
    print(f"The shortest word is :{shortest}")

    cont=input("Do you want to continue ? (yes/no):")
    if cont.lower()!='yes':
        break 
