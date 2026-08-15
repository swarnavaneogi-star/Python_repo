while True:
    marks = int(input("Enter your marks: "))

    if marks<35:
        print("You failed in the exam!!")
    elif marks>=35 and marks<60:
        print("You passed in the exam!!")
    elif marks>=60 and marks<80:
        print("You passed in the exam with first class!!")
    else:
        print("You passed in the exam with distinction!!")

    cont = input("Do you want to enter another marks? (yes/no): ")
    if cont.lower() != "yes":
        print("Exiting the program. Goodbye!")
        break