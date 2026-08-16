while True :
    weight = float(input("Enter the weight in kilograms :"))
    height =float(input("Enter the height in meters :"))

    bmi =weight/(height**2)

    if bmi<18.5:
        print(f"Your BMI is {bmi:.2f} and you are underweight.")
    elif bmi>=18.5 and bmi<24.9:
        print(f"Your BMI is {bmi:.2f} and you are normal weight.")
    elif bmi>=25 and bmi<29.9:
        print(f"Your BMI is {bmi:.2f} and you are overweight.")
    else:
        print(f"Your BMI is {bmi:.2f} and you are obese.")

    cont =input("Do you want to calculate another setof BMI (yes/no):")
    if cont.lower()!="yes":
        print("Exiting the program ..")
        break