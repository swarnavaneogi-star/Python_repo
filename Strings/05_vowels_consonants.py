while True:
    str=input("Enter a string : ")
    print()
    vowels_count=0
    consonants_count=0
    l=len(str)
    for i in range(l):
        if (str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u' or str[i]=='A' or str[i]=='E' or str[i]=='I' or str[i]=='O' or str[i]=='U'):
            vowels_count+=1
        else:
            consonants_count+=1

    print(f"The number of vowels is - {vowels_count} and the number of consnonants is - {consonants_count} ")

    cont=input("Do you want to continue ? (yes/no):")
    if cont.lower()!='yes':
      break