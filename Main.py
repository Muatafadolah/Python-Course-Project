from Student_functions import *
Load_data()

while True:
    print("=====Student Academic Management System=====\n")
    print("1.Add Student")
    print("2.View All Students")
    print("3.Search Student")
    print("4.Update Student Grades")
    print("5.Delete Student")
    print("6.Student Report")
    print("7.Class Statistics")
    print("8.Save Data")
    print("0.Exit")
    try:
        Choice = int(input("Enter your choice: "))
        
        if Choice == 1:
            Add_Student()
            Save_data()
            
        elif Choice == 2:
            View_students()
            
        elif Choice == 3:
            Search_student()
            
        elif Choice == 4:
            Update_student()
            
        elif Choice == 5:
            Delete_student()
            Save_data()
            
        elif Choice == 6:
            Display_student_report()
            
        elif Choice == 7:
            Display_statistics()
            
        elif Choice == 8:
            Save_data()
            
        elif Choice == 0:
            Save_data()
            break
        
        else:
            print("Enter a number between 0 and 8.")
    except ValueError:     
        print("Invalid numeric input.")