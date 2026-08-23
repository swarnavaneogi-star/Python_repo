while True :
    string_1=input("Enter a string : ")
    string_2=input("Enter another string : ")
    l_s_1=string_1.lower()
    l_s_2=string_2.lower()
    sorted_string=''.join(sorted(l_s_1))
    sorted_string_1=''.join(sorted(l_s_2))

    if sorted_string==sorted_string_1:
        print(f"The strings are anagrams: {string_1},{string_2}")
    else:
       print(f"The strings are not anagrams: {string_1},{string_2}") 

    cont=input("Do you want to continue ? (yes/no):")
    if cont.lower()!='yes':
         break