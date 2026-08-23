while True:
    string=input("Enter a string :")
    words=string.split()
    new_sentence=""
    for word in words :
        reversed_word = word[::-1]
        new_sentence += reversed_word + " "
    print(f"The new string is : {new_sentence}")

    cont=input("Do you want to continue ? (yes/no):")
    if cont.lower()!='yes':
       break