# python program to caluculate the percentage and the grade of a student
while True : 
   name = input("Enter the name of the student : ")
   class_name = input("Enter the class of the student : ")
   print("Enter the marks obtained in 5 subjects : ")
   subject1 = float(input("Enter marks for english : "))
   subject2 = float(input("Enter marks for maths : "))
   subject3 = float(input("Enter marks for science : "))
   subject4 = float(input("Enter marks for social studies : "))
   subject5 = float(input("Enter marks for computer science : "))

   total_marks =(subject1 + subject2 + subject3 + subject4 + subject5)
   percentage = (total_marks / 500) * 100
 
   if percentage >= 95:
    grade ="A+"
   elif percentage >= 90:
    grade ="A"
   elif percentage >= 80:
    grade ="B"
   elif percentage >= 70:
    grade ="C"
   elif percentage >= 60:
    grade ="D"
   else:
    grade ="F"

   print("\n--- Student Details ---")
   print("Name :", name)
   print("Class :", class_name)
   print("Total Marks :", total_marks)
   print(f"Percentage : {percentage:.2f}%")
   print("Grade :", grade)

   cont = input("Do you want to enter details for another student? (yes/no): ")
   if cont.lower() != 'yes':
        print("Exiting the program. Goodbye!")
        print("Thank you for using the Student Grade Calculator.")
        break