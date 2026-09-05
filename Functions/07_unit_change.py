def change(inch):
    return inch*2.54

inch=float(input("enter the length in inches :"))
cm=change(inch)
print(f"The length in centimeters is: {round(cm,2)}")