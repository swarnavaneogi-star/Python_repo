while True:
        a1=int(input("Enter the first angle of the triangle :"))
        a2=int(input("Enter the second angle of the triangle :"))
        a3=int(input("Enter the third angle of the triangle :"))

        if  a1 > 0 and a2 > 0 and a3 > 0 and a1 + a2 + a3 == 180:
            print("The triangle is valid.")
            if a1 == 90 or a2 == 90 or a3 == 90:
                print("The triangle is a right triangle.")
            elif a1 < 90 and a2 < 90 and a3 < 90:
                print("The triangle is an acute triangle.")
            elif a1 > 90 or a2 > 90 or a3 > 90:
                print("The triangle is an obtuse triangle.")
            elif a1 == a2 == a3:
                print("The triangle is an equilateral triangle.")
            elif a1 == a2 or a2 == a3 or a1 == a3:
                print("The triangle is an isosceles triangle.")

        else:
            print("The triangle is not valid.")

        cont =input("Do you want to enter another set of angles? (yes/no): ")
        if cont.lower()!="yes":
            print("Exiting the program ..")
            break