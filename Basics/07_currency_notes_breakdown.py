# python program to calculate the breakdown of currency notes
while True:
    print("Enter the total amount :")
    amount = int(input())
    original_amount = amount

    if amount <= 0:
        print("Please enter a valid amount.")
        continue

    note_1 = amount // 500
    amount = amount % 500

    note_2 = amount // 200
    amount = amount % 200

    note_3 = amount // 100
    amount = amount % 100

    note_4 = amount // 50
    amount = amount % 50

    note_5 = amount // 20
    amount = amount % 20

    note_6 = amount // 10
    amount = amount % 10

    coin_1 = amount // 5
    amount = amount % 5

    coin_2 = amount // 2
    amount = amount % 2

    coin_3 = amount // 1
    amount = amount % 1

    print(f"\nOriginal Amount entered is = {original_amount}")
    print("\nThe breakdown of the currency notes is :")
    print(f"500 Notes: {note_1}")
    print(f"200 Notes: {note_2}")
    print(f"100 Notes: {note_3}")
    print(f"50 Notes: {note_4}")
    print(f"20 Notes: {note_5}")
    print(f"10 Notes: {note_6}")
    print(f"5 Coins: {coin_1}")
    print(f"2 Coins: {coin_2}")
    print(f"1 Coins: {coin_3}")

    cont = input("Do you want to enter for another amount? (yes/no): ")
    if cont.lower() != 'yes':
        print("Exiting the program. Goodbye!")
        print("Thank you for using the Currency Notes Breakdown Calculator.")
        break