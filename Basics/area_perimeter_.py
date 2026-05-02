# python program to check and find the area and perimeter of different shapes 
import math 
print("Select a shape to calculate the area and the perimeter \n:")
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Circle")
print("5.Equilateral Triangle")
print("6.Parallelogram")
print("7.Trapezium")
print("8.Rhombus")
print("Enter your choice:\n")
choice=int(input())
if choice==1:
    side =int(input("Enter the side of the sqaure : "))
    area =side**2
    perimeter = 4*side
    print("The area of the sqaure is =",area,"\n and the perimeter of the square is =",perimeter)
elif choice ==2:
    length =int(input("Enter the length of the rectangle : "))
    breadth =int(input("Enter the breadth of the rectangle : "))
    area =length*breadth
    perimeter = 2*(length+breadth)
    print("The area of the rectangle is =",area,"\n and the perimeter of the rectangle is =",perimeter)
elif choice ==3:
    a =int(input("Enter the first side of the triangle : "))
    b =int(input("Enter the second side of the triangle : "))
    c =int(input("Enter the third side of the triangle : "))
    base =int(input("Enter the base of the triangle : "))
    height =int(input("Enter the height of the triangle : "))
    area =0.5*base*height
    perimeter = a+b+c
    print("The area of the triangle is =",area,"\n and the perimeter of the triangle is =",perimeter)
elif choice ==4:
    radius =int(input("Enter the radius of the circle : "))
    area =math.pi*radius**2
    perimeter = 2*math.pi*radius
    print("The area of the circle is =",area,"\n and the perimeter of the circle is =",perimeter)
elif choice ==5:
    side =int(input("Enter the side of the equilateral triangle : "))
    area =(3**0.5/4)*side**2
    perimeter = 3*side
    print("The area of the equilateral triangle is =",area,"\n and the perimeter of the equilateral triangle is =",perimeter)
elif choice ==6:
    base =int(input("Enter the base of the parallelogram : "))
    height =int(input("Enter the height of the parallelogram : "))
    area =base*height
    perimeter = 2*(base+height)
    print("The area of the parallelogram is =",area,"\n and the perimeter of the parallelogram is =",perimeter)
elif choice ==7:
    base1 =int(input("Enter the first base of the trapezium : "))
    base2 =int(input("Enter the second base of the trapezium : "))
    height =int(input("Enter the height of the trapezium : "))
    area =0.5*(base1+base2)*height
    perimeter = int(input("Enter the perimeter of the trapezium : "))
    print("The area of the trapezium is =",area,"\n and the perimeter of the trapezium is =",perimeter)
elif choice ==8:
    diagonal1 =int(input("Enter the first diagonal of the rhombus : "))
    diagonal2 =int(input("Enter the second diagonal of the rhombus : "))
    area =0.5*diagonal1*diagonal2
    side = (diagonal1**2 + diagonal2**2)**0.5 / 2
    perimeter = 4 * side
    print("The area of the rhombus is =",area,"\n and the perimeter of the rhombus is =",perimeter)
else:
    print("Invalid choice. Please select a valid shape.")

    
    
print("Thank you for using the area and perimeter calculator!")