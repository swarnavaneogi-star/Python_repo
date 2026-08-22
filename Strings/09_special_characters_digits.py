while True:
    str=input("Enter a string :")
    l=len(str)
    digits_count=0
    special_characters_count=0
    for i in range(l):
        if (str[i]=='0' or str[i]=='1' or str[i]=='2' or str[i]=='3' or str[i]=='4' or str[i]=='5' or str[i]=='6' or str[i]=='7' or str[i]=='8' or str[i]=='9'):
            digits_count+=1
        elif (str[i]==',' or str[i]=='.' or str[i]=='?' or str[i]=='!' or str[i]=='@' or str[i]=='#' or str[i]=='$' or str[i]=='%' or str[i]=='^' or str[i]=='&' or str[i]=='*'or str[i]=='(' or str[i]==')' or str[i]=='/' or str[i]=='+' or str[i]=='=' or str[i]=='-' ):
            special_characters_count+=1

    print(f"The number of digits present in the string is {digits_count} and the number of special characters presentin the string is {special_characters_count} ")

    cont=input("do you want to continue ? (yes/no) :")
    if cont.lower()!='yes':
        break