from Student_functions import *
print("Loading student data...")
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
            Search_position = Search_student()
            if Search_position is not None:
                Print_student(Students[Search_position])
            
        elif Choice == 4:
            Update_student()
            Save_data()
            
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
            print("Saving student data...")
            Save_data()
            print("Data saved successfully.")
            break
        
        else:
            print("Enter a number between 0 and 8.")
    except ValueError:     
        print("Invalid numeric input.")