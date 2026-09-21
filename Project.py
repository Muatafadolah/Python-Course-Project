##Python-Based Student Academic Management System.

##Subjects for the students.
Number_of_Students = 0
Students = []
Subjects = ("Python","Math","English")

##Function to calcualte Average any time.
def Calculate_Average(Student):
        Total_Marks = 0
        for subject in Subjects:
            Total_Marks += Student["Grades"][subject]
        Student["Average"] = Total_Marks / len(Subjects)

##Function to determine Student status any time.
def Determine_Status(Student):
        if Student["Average"] >= 60:
            Student["Status"] = "Passed"
        else:
            Student["Status"] = "Failed"

##Function to Add new Student.
def Add_Student():
    global Number_of_Students
    
##Define a dectionry has all data needed.
    Student = {
    "ID": "",
    "Name": "",
    "Grades" :{
        "Python": 0,
        "Math": 0,
        "English": 0
},
    "Average": 0,
    "Status": ""
}
##Add Student ID and check if ID is unique.
    while True:
        ID = input("Enter Student ID: ")
        if any(student["ID"] == ID for student in Students):
            print("Student ID already exists. Please enter a unique ID.")
            continue
        break

    Student["ID"] = ID
    
    ##Add Student's name.
    Student["Name"] = input("Enter Student Name: ")
    
    ##Add valled Subjects Marks.
    for subject in Subjects:
        while True:
                grade = float(input(f"Enter {subject} Grade: "))
                if 0 <= grade <= 100:
                    Student["Grades"][subject] = grade
                    break
                else:
                    print("Grade must be between 0 and 100. Please try again.")
    
    Calculate_Average(Student)
    Determine_Status(Student)
    Students.append(Student)
    Number_of_Students = len(Students)

