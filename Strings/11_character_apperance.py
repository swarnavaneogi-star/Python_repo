while True :
    str=input("enter a string:")
    max=0
    min=len(str)
    for i in str:
        ch_count=0
        for j in str:
            if i==j:
                ch_count+=1

        if max<ch_count:
            max=ch_count
            maxchar=i
        elif min>ch_count:
            min=ch_count
            minchar=i

    print(f"The maximum apperead is character is {maxchar} for {ch_count} times .")
    print(f"The minimum appeared character is {minchar} for {ch_count} times .")

    cont=input("Do you want to continue ? (yes/no):")
    if cont.lower()!='yes':
        break 
