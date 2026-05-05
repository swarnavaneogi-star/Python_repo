# python program to show a program of calculating bills 
while True:
    print("Enter the total bill amount:")
    bill_amount = float(input())
    og = bill_amount

    print("\nEnter the number of people ....to split the bill:")
    num_people = int(input())

    print("\nEnter the tax percentage:")
    tax_percentage = float(input())

    print("\nDo you want to include tip? (yes/no):")
    include_tip = input().lower()

    tip_percentage = 0
    if include_tip == 'yes':
        print("\nEnter the tip percentage:")
        tip_percentage = float(input())

    # validation
    if bill_amount <= 0 or num_people <= 0 or tax_percentage < 0 or tip_percentage < 0:
        print("Please enter valid inputs to calculate the bill split!!")
        continue

    # calculations (no else needed)
    tax_amount = (bill_amount * tax_percentage) / 100
    tip_amount = (bill_amount * tip_percentage) / 100
    total_bill = bill_amount + tax_amount + tip_amount
    amount_per_person = total_bill / num_people

    print("\n-------BILL SUMMARY-------\n")
    print(f"The original bill amount is : ₹{og}")
    print(f"The tax percentage is : {tax_percentage}%")
    print(f"The tip percentage is : {tip_percentage}%")
    print(f"The total bill amount after adding tax and tip is : ₹{total_bill:.2f}")
    print(f"Each person should pay: ₹{amount_per_person:.2f}")

    cont = input("Do you want to enter for another amount? (yes/no): ")
    if cont.lower() != 'yes':
        print("Thank you for using the Bill Splitter.")
        break