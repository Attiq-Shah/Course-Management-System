#   Course Management System, Project for Object Oriented Programming
#   Defining Course Class whose objects will be used as a course
class Course:
    def __init__(self, CourseCode, Title, Credit, Grade):
        self.coursecode = CourseCode
        self.title = Title
        self.credit = Credit
        self.grade = Grade

#   Display Function will display attributes of Course Class Object
    def Display(self):
        print("Course Code:",self.coursecode,", Course Title:",self.title,", Course Credit:",self.credit,", Course Grade:",self.grade)

#   Defining Base class Person, it can also be called as Parent class.
class Person:
    def __init__(self, Name, Age, Sex):
        self.name = Name
        self.age = Age
        self.sex = Sex

    def Display(self):
        print("Name : ",self.name,"Age : ",self.age,"Sex : ",self.sex)

#   Subclass or child class of Person is Student.
#   Concept of Inheritance is used here.
class Student( Person ):
    Student_List = []       #   List which will contain all the objects of Student class
    def __init__(self, Name, Age, Sex, RegNo, Depart, Semester, Regcourse = []):
        super().__init__(Name, Age, Sex)        #   Super Function is used to call all the attributes of constructor of Parent class.
        self.regno = RegNo
        self.depart = Depart
        self.sem = Semester
        self.regcourse = Regcourse

    def Display(self):
        super().Display()
        print("Reg.No :",self.regno,"Department: ",self.depart,"Semester :",self.sem)

    def Add_Student(self):                      # This method will add a Student Object to a Student_List defined above.
        Name = input("Enter Name Of a Student: ")
        age = int(input("Enter Age Of a Student: "))
        sex = input("Enter Gender Of a Student: ")
        regno = int(input("Enter Registration Number: "))
        dep = input("Enter Department: ")
        sem = int(input("Enter Semester Of a Student: "))
        Course_List = []
        regcourse = int(input("How many Courses You Want to register to this Student: "))
        for i in range(1, regcourse + 1):       #   Since more than one course can be registered by student, so for that we use for loop. 
            print(".....Course",i,".....")
            C = Course(int(input("Enter Course Code: ")), input("Course Title: "), int(input("Course Credit: ")), float(input("Course Grade: ")))
            Course_List.append(C)

        Obj = Student(Name, age, sex, regno, dep, sem, Regcourse = Course_List)
        Student.Student_List.append(Obj)

    def Register_Courses(self):     #   This method will register course to a specific student.
        try:
            Count = 0
            User = int(input("Enter Registration Number Of a Student: "))
            for object in Student.Student_List:
                if User == object.regno:
                    Count += 1
                    regcourse = int(input("How many Courses You Want to register to this Student: "))
                    for i in range(regcourse):
                        C = Course(int(input("Enter Course Code: ")), input("Course Title: "), int(input("Course Credit: ")), float(input("Course Grade: ")))
                        object.regcourse.append(C)
            if Count == 0:
                print("Sorry No Student Found!")
            else:
                print("Course Registered Successfully!")
        except ValueError:
            print("Registration Number Of a Student Should Be in Integers")

    def Set_Grade(self):        #   This method will set grade for a student by giving registration number.
        Count = 0
        name = input("Enter Name Of a Student: ")
        for student in Student.Student_List:
            if name == student.name:
                Count += 1
                try:
                    User = int(input("Enter Course Code: "))           #    For specific course, course code will be asked.
                    for course in student.regcourse:
                        if User == course.coursecode:
                            Count += 1
                            Grade = float(input("Enter New Grade: "))
                            course.grade = Grade
                    if Count == 1:
                        print("Sorry No Course Is Available with this code",User)
                    else:
                        print("Grades Updated")
                except ValueError:
                    print("Course Code is in Integer Format!")
        if Count == 0:
                    print("Sorry No Student Is Available with this Name",name)

    def Search_Student(self):       #   Searches for a student in Student_List
        try:
            Count = 0
            User = int(input("Enter Registration Number Of a Student: "))
            for object in Student.Student_List:
                if User == object.regno:
                    Count += 1
                    object.Display()
                    print("Courses Registered is/are:")
                    for course in object.regcourse:
                        course.Display()
            if Count == 0:
                print("Sorry No Student With this Registration Number Found")
        except ValueError:
            print("Please Enter Registration Number in Integer Format!")

    def Remove_Course(self):        #   Remove course from a Student
        Count = 0
        User = int(input("Enter Registration Number Of a Student: "))
        for object in Student.Student_List:                             #   Searches Input reg no in Student_List.
            if User == object.regno:
                Count += 1
                Enter = int(input("Enter Course Code Of a Course You Want to Remove: "))
                for course in object.regcourse:
                    if Enter == course.coursecode:
                        Count += 1
                        object.regcourse.remove(course)
                if Count == 1:
                    print("Sorry No Course Found")
        if Count == 0:
            print("Sorry No Student Found!")
        else:
            print("Course Removed Successfully!")

#   Another subclass of Parent class is Instructor. Here Single Inheritance is used in our project.
class Instructor( Person ):
    Instructor_List = []        #   List which will contain object of Instructor Class.
    def __init__(self, Name, Age, Sex, Experience, Salary, AssigCourses = []):
        super().__init__(Name, Age, Sex)
        self.experience = Experience
        self.salary = Salary
        self.assigncourse = AssigCourses

    def Display(self):
        super().Display()
        print("Experience: ",self.experience,"Salary: ",self.salary)

    def Add_Instructor(self):           #   This Method will add Instructor Object to Instructor_List
        Name = input("Enter Instructor Name: ")
        Age = int(input("Enter Instructor Age: "))
        Sex = input("Enter Gender: ")
        Experience = input("Enter Experience: ")
        Salary = int(input("Enter Salary: "))
        assigncourse = int(input("How Many Courses You want to assign to this Instructor: "))
        Course_List = []
        for i in range(1, assigncourse + 1):    #   Since more than one course can be assigned to Instructor, So we use for Loop.
            C = Course(int(input("Enter Course Code: ")), input("Course Title: "), int(input("Course Credit: ")), float(input("Course Grade: ")))
            Course_List.append(C)
            
        Obj = Instructor(Name, Age, Sex, Experience, Salary, AssigCourses= Course_List)     #Creating Object of Instructor Class
        Instructor.Instructor_List.append(Obj)
        print("Instructor Added Successfully")

    def Assign_Course(self):        #    This Method will assign a course or courses to instructor for teaching.
        Count = 0
        User = input("Enter Name Of Instructor to Assign Him/Her Course: ")
        for object in Instructor.Instructor_List:
            if User == object.name:
                Count += 1
                assigncourse = int(input("How Many Courses You want to assign to this Instructor: "))
                for i in range(1, assigncourse + 1):
                    print(".....Course",i,".....")
                    C = Course(int(input("Enter Course Code: ")), input("Course Title: "), int(input("Course Credit: ")), float(input("Course Grade: "))) 
                    object.assigncourse.append(C)
                print("Course Assigned")

        if Count == 0:
            print("Sorry No Instructor with this Name Found")

    def Search_Instructor(self):        #   Searches for instructor in Instructor_List
        Count = 0
        User = input("Enter Name Of a Instructor: ")
        for object in Instructor.Instructor_List:
            if User == object.name:
                Count += 1
                object.Display()
                print("Courses Assigned is/are:")
                for course in object.assigncourse:
                    course.Display()
        if Count == 0:
            print("Sorry No Instructor With this Name Found")


    def Remove_Course(self):        #   Removes Course for instructor in instructor_List
        Count = 0
        User = input("Enter Name of Instructor From which You want to Remove a Course: ")
        for object in Instructor.Instructor_List:
            if object.name == User:
                Count += 1
                Code = int(input("Enter Course Code: "))
                for course in object.assigncourse:
                    if Code == course.coursecode:
                        Count += 1
                        object.assigncourse.remove(course)
                if Count == 1:
                    print("Sorry No Course Found!")
                else:
                    print("Course Removed from Instructor",User)

        if Count == 0:
            print("Sorry No Instructor Found with name",User)


#   Making Raw Objects Of Student and Instructor Classes
S1 = Student("Attiq",18,"Male","21","CS",2)
I1 = Instructor("Zia", 45, "Male", "Phd", 100000)
#   Setting Menu of Our Project

while True:
    try:
        print("\n.....COURSE MANAGEMENT SYSTEM.....")
        User = int(input("For Student Press 1\nFor Instructor Press 2\nFor Terminating Program Press 3: "))
        if User == 3:
            print("Program Terminated...")
            break

        elif User == 1:
            while True:
                print("\n.....STUDENT PORTAL.....")
                User = input("Enter A for Adding Student\nB for Setting Grade\nC for Searching Student\nD for Removing Course\nE for Registering a Course\nX for Exit: ")
                if User == "X" or User == "x":
                    print("Student Module Terminated!")
                    break
                elif User == "A" or User == "a":
                    S1.Add_Student()
                    # S1.Register_Courses()
                    print("")
                
                elif User == "B" or User == "b":
                    S1.Set_Grade()
                    print("")

                elif User == "C" or User == "c":
                    S1.Search_Student()
                    print("")

                elif User == "D" or User == "d":
                    S1.Remove_Course()
                    print("")

                elif User == "E" or User == "e":
                    S1.Register_Courses()
                    print("")

                else:
                    print("Invalid Input\nPlease Try Again...")

        elif User == 2:
            while True:
                print("\n.....INSTRUCTOR PORTAL.....")
                User = input("Enter A for Adding Instructor\nB for Assigning Course\nC for Searching Instructor\nD for Removing Course\nX for Exit: ")
                if User == "X" or User == "x":
                    print("Instructor Module Terminated!")
                    break

                elif User == "A" or User == "a":
                    I1.Add_Instructor()
                    print("")

                elif User == "B" or User == "b":
                    I1.Assign_Course()
                    print("")

                elif User == "C" or User == "c":
                    I1.Search_Instructor()
                    print("")

                elif User == "D" or User == "d":
                    I1.Remove_Course()
                    print("")
        else:
            print("Sorry Invalid Input\nPlease Try Again")
    except ValueError:
        print("Please Enter Integers Like 1,2,3,.....")