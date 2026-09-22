##Python file to define the functions we need.

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
def Calculate_Status(Student):
        if Student["Average"] >= 60:
            Student["Status"] = "Passed"
        else:
            Student["Status"] = "Failed"

##Function that determine Classification of the student.
def Calculate_Classification(Student):
    if Student["Average"] >= 90:
        Student["Classification"] = "Exellent"
    elif Student["Average"] >= 80 and Student["Average"] < 90:
        Student["Classification"] = "Very Good"
    elif Student["Average"] >= 70 and Student["Average"] < 80:
        Student["Classification"] = "Good"
    elif Student["Average"] >= 60 and Student["Average"] <70:
        Student["Classification"] = "Pass"
    else:
        Student["Classification"] = "Fail"

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
    "Status": "",
    "Classification": ""
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
            try:
                grade = float(input(f"Enter {subject} Grade: "))
                if 0 <= grade <=100:
                    Student["Grades"][subject] = grade
                    break
                else:
                    print("Grade must be between 0 and 100. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
    
    Calculate_Average(Student)
    Calculate_Status(Student)
    Calculate_Classification(Student)
    Students.append(Student)
    Number_of_Students = len(Students)

##Function that search for a student by ID or Name.
def Search_student():
    print("What method you need to search?")
    print("1.Student ID")
    print("2.Student name")
    Search_method = int(input("Enter a number (1 or 2): "))
    if Search_method == 1:
        Search_ID = input("Enter the ID: ")
        for position ,student in Students:
            if student["ID"] == Search_ID:
                print("Student Found.")
                print(Students[position])
            elif Search_method == 2:
                for position , studnet 

def Update_student():
    
def Display_student_report():

def Display_statistics():
