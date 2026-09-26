## Python file to define the functions that program need.

## Subjects for the students.
Students = []
Subjects = ("Python","Math","English")

## Function to calcualte Average any time.
def Calculate_Average(Student):
    
    average = sum(Student["Grades"].values()) / len(Student["Grades"])
    Student["Average"] = average

## Function to determine Student status any time.
def Calculate_Status(Student):
    
        if Student["Average"] >= 60:
            Student["Status"] = "Passed"
        else:
            Student["Status"] = "Failed"

## Function that determine Classification of the student.
def Calculate_Classification(Student):
    
    if Student["Average"] >= 90:
        Student["Classification"] = "Excellent"
    elif Student["Average"] >= 80:
        Student["Classification"] = "Very Good"
    elif Student["Average"] >= 70:
        Student["Classification"] = "Good"
    elif Student["Average"] >= 60:
        Student["Classification"] = "Pass"
    else:
        Student["Classification"] = "Fail"

## Function to Add new Student.
def Add_Student():
    
    print("You are in add new student session, Enter all new student data.")

## Define a dectionry has all data needed.
    Student = {
    "ID": "",
    "Name": "",
    "Grades" :{
        "Python": 0,
        "Math": 0,
        "English": 0
},
    "Average": 0,
    "Status": "",
    "Classification": ""
}
## Add Student ID and check if ID is unique.
    while True:
        ID = input("Enter Student ID: ").strip().replace(" ","")
        if ID == "":
            print("Student ID cannot be empty.")
            continue
        if any(student["ID"] == ID for student in Students):
            print("Student ID already exists. Please enter a unique ID.")
            continue
        break

    Student["ID"] = ID
    
    ## Add Student's name.
    while True:
        Student["Name"] = input("Enter Student Name: ").strip()
        if Student["Name"] == "":
            print("The name cannot be empty.")
        else:
            break
        
    
    ## Add valled Subjects Marks.
    for subject in Subjects:
        while True:
            try:
                grade = float(input(f"Enter {subject} Grade: "))
                if 0 <= grade <=100:
                    Student["Grades"][subject] = grade
                    break
                else:
                    print("Grade must be between 0 and 100. Please try again.")
            except ValueError:
                print("Invaled grade.")
    
    Calculate_Average(Student)
    Calculate_Status(Student)
    Calculate_Classification(Student)
    
    Students.append(Student)
    
def ID_search():
    
    while True:
        
        Search_ID = input("Enter student ID: ").strip().replace(" ","")
        for position ,student in enumerate(Students):
            if student["ID"] == Search_ID:
                print("Student Found.")
                Search_position = position
                return Search_position
        else:
            print("Student not found.")
            
## Function that search for a student by ID or Name.
def Search_student():
    
    while True:
        
        print("Now you are in search session.\n")
        print("What method you need to search?")
        print("1.Student ID.")
        print("2.Student name.")
        print("3.Back.")
        try:
            
            Search_method = int(input("Enter a number (1 or 2 or 3): "))
            if Search_method == 1:
                
                Search_position = ID_search()
                return Search_position
                
            elif Search_method == 2:
                Search_name = input("Enter student name: ").strip()
                for position , student in enumerate(Students):
                    if student["Name"].lower() == Search_name.lower():
                        print("Student found.")
                        Search_position = position
                        return Search_position
                else:
                    print("Student not found.")
                    Search_position = None
            elif Search_method == 3:
                return None
            else:
                print("Enter a number between 1 or 2 or 3.")
        except ValueError:
            print("Invalid numeric input.")
    return Search_position
        
                
## Functoin that update student marks.
def Update_student():

    print("You are in update student grades session")
    print("You must search for the student by ID or Name:\n")

    Search_position = Search_student()
    
    if Search_position is None:
        return

    Student = Students[Search_position]

    while True:
        
        print("Choose what grade you need to update:")
        print("1.Python")
        print("2.Math")
        print("3.English")
        print("4.Back")

        try:
            Update_method = int(input("Enter a number 1 or 2 or 3 or 4: "))

            if 1 <= Update_method <= 3:
                Subject = Subjects[Update_method - 1]
                while True:
                    try:
                        grade = float(input(f"Enter new {Subject} grade: "))
                        if 0 <= grade <= 100:
                            Student["Grades"][Subject] = grade
                            
                            Calculate_Average(Student)
                            Calculate_Status(Student)
                            Calculate_Classification(Student)

                            print(f"{Subject} grade updated successfully.")
                            break
                        else:
                            print("Grade must be between 0 and 100. Please try again.")
                            
                    except ValueError:
                        print("Please enter a valid number.")
                        
            elif Update_method == 4:
                break

            else:
                print("Enter a number between 1 or 2 or 3 or 4.")

        except ValueError:
            print("Invalid numeric input.")
            
                
## Funcion that display student acadimic report.         
def Display_student_report():
    
    print("To display student report you must search for the student.\n")
    Search_position = Search_student()
    if Search_position is None:
        return
    else:
        Student = Students[Search_position]
        print("\n=================================")
        print(" STUDENT REPORT ")
        print("=================================\n")
        print(f"Student ID:{Student["ID"]}")
        print(f"Name:{Student["Name"]}")
        for subject in Subjects: 
            print(f"{subject}: {Student["Grades"][subject]}")
        print(f"Average: {Student["Average"]}")
        print(f"Status:{Student["Status"]}")
        print(f"Classification:{Student["Classification"]}")

def Delete_student():
    print("You are in delete student session, you must search for the student first.\n")
    Search_position = ID_search()
    if Search_position is None:
        return
    else:
        Student = Students[Search_position]
        print(f"Student:{Student["Name"]}")
        
        while True:
            Confirm_key = input("Are you sure you want to delete this student? (yes/no):").strip().lower()
            if Confirm_key == "yes":
                Students.pop(Search_position)
                print("Student deleted successfully.")
                return
            elif Confirm_key == "no":
                return
            else:
                print("Wrong answer.")
            
        
## Function that display class statistics.
def Display_statistics():
    
    Subject_average = {}
    Highest_grade = {}
    Count_p = 0
    Count_f = 0

    # Check if there are no students.
    if len(Students) == 0:
        print("There are no students in the class.")
        return

    for Subject in Subjects:
        Total = 0
        Highest_grade[Subject] = Students[0]["Grades"][Subject]

        for Student in Students:
            Total += Student["Grades"][Subject]

            Highest_grade[Subject] = max(Highest_grade[Subject],Student["Grades"][Subject])

        Subject_average[Subject] = Total / len(Students)

    Total_averages = 0

    Max_average = Students[0]["Average"]
    Min_average = Students[0]["Average"]

    Highest_position = 0
    Lowest_position = 0

    for position, Student in enumerate(Students):
        
        if Student["Status"] == "Passed":
            Count_p += 1
        else:
            Count_f += 1

        if Student["Average"] > Max_average:
            Max_average = Student["Average"]
            Highest_position = position

        if Student["Average"] < Min_average:
            Min_average = Student["Average"]
            Lowest_position = position

        Total_averages += Student["Average"]

    Class_average = Total_averages / len(Students)

    ##Output.
    print("\n===== CLASS STATISTICS =====\n")
    print(f"Number of Students: {len(Students)}")
    print(f"Class Average: {Class_average:.2f}")
    print(f"Highest Average: {Students[Highest_position]['Name']} - {Max_average:.2f}")
    print(f"Lowest Average: {Students[Lowest_position]['Name']} - {Min_average:.2f}")
    print(f"Passed Students: {Count_p}")
    print(f"Failed Students: {Count_f}")

    print("\n===== SUBJECT STATISTICS =====")
    
    for Subject in Subjects:
        print(f"\n{Subject}:")
        print(f"Highest Grade: {Highest_grade[Subject]:.2f}")
        print(f"Average Grade: {Subject_average[Subject]:.2f}")
    
def Sort_by_name(Student):
    return Student["Name"].lower()

def Sort_by_average(Student):
    return Student["Average"]

def Sort_students():
    
    print("Now you are in sorting part.")
    print("What type of sort you need?")
    
    while True:
        
        print("1.Sort by name.")
        print("2.Sort by average.")
        print("3.Back.")
        
        try:
            Sort_method = int(input("Enter a number (1 or 2 or 3): "))
            if Sort_method == 1:
                Sorted_students = sorted(Students,key = Sort_by_name)
                return Sorted_students,Sort_method
            elif Sort_method == 2:
                Sorted_students = sorted(Students,key = Sort_by_average,reverse = True)
                return Sorted_students,Sort_method
            elif Sort_method == 3:
                return None,None
            else:
                print("Enter a number between 1 and 3.")
        except ValueError:
            print("Invalid numeric input.")

## Function that print students data by sorting by name or average.
def View_students():
    
    if len(Students) == 0:
        print("There are no students in the class. Please add students to continue.")
        return
    print("To view students data you must choose sort method.")
    Sorted_students,Sort_method = Sort_students()
    if Sort_method is None:
        return
    
    if Sort_method == 1:
        print("\n===== STUDENTS SORTED BY NAME =====")
    elif Sort_method == 2:
        print("\n===== STUDENTS SORTED BY AVERAGE =====")

    for Student in Sorted_students:
        print(f"ID: {Student["ID"]}")
        print(f"Name: {Student["Name"]}")
        print(f"Average: {Student["Average"]:.2f}")
        print(f"Status: {Student["Status"]}")
        print(f"Classification: {Student["Classification"]}")
        print("=================================\n")

## Function that saves the data on file "Students.txt".
def Save_data():
    
    try:
        with open("Students.txt","w") as File:
            for Student in Students:
                Line = Student["ID"] + "," + Student["Name"]
                for Subject in Subjects:
                    Line += "," + str(Student["Grades"][Subject])
                File.write(Line + "\n")
    except FileNotFoundError:
        print("File does not exist. ")
        
## Function that load the data saved from "Students.txt".
def Load_data():
    
    try:
        with open("Students.txt","r") as File:
            for Line in File:
                Data = Line.strip().split(",")
                
                Student = {
                    "ID": Data[0],
                    "Name": Data[1],
                    "Grades": {
                        "Python": float(Data[2]),
                        "Math": float(Data[3]),
                        "English": float(Data[4])
                    },
                    "Average": 0,
                    "Status": "",
                    "Classification": ""
                }
                
                Calculate_Average(Student)
                Calculate_Status(Student)
                Calculate_Classification(Student)
                Students.append(Student)
    except FileNotFoundError:
        print("No data found.")
        