import mysql.connector
con=mysql.connector.connect(host="localhost", user="root", password="", database="student")

class database:
    def __init__(self):
        c=con.cursor()
        c.execute("create table IF NOT EXISTS student_details(student_id int primary key NOT NULL,student_name varchar(30),department varchar(30),m1 int,m2 int,m3 int,m4 int,m5 int,total int,average int, grade varchar(3))")
        c.close()
    
    def display_database(self):
        c=con.cursor()
        c.execute("select * from student_details")
        a=c.fetchall()
        for i in a:
            print(i)

db=database()

class student:
    def __init__(self):
        self.std_id=""
        self.std_name=""
        self.dept=""
        self.m1=int()
        self.m2=int()
        self.m3=int()
        self.m4=int()
        self.m5=int()
        self.total=self.get_total(self.m1,self.m2,self.m3,self.m4,self.m5)
        self.avg=self.get_avg(self.total)
        self.grade=self.get_grade(self.avg)


    def get_student(self):
        self.std_id=input("Enter student id:")
        sql = "SELECT * FROM student_details WHERE student_id = %s"
        id = (self.std_id, )
        db.display_database()

    def add_student(self):
        self.std_id=input("Student id:")
        self.std_name=input("Student Name:")
        self.dept=input("Student department:")
        self.m1=input("Mark 1:")
        self.m2=input("Mark 2:")
        self.m3=input("Mark 3:")
        self.m4=input("Mark 4:")
        self.m5=input("Mark 5:")
        self.total=self.get_total(self.m1,self.m2,self.m3,self.m4,self.m5)
        self.avg=self.get_avg(self.total)
        self.grade=self.get_grade(self.avg)
        c=con.cursor()

        sql="insert into student_details (student_id,student_name,department,m1,m2,m3,m4,m5,total,average,grade) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(self.std_id,self.std_name,self.dept,self.m1,self.m2,self.m3,self.m4,self.m5,self.total,self.avg,self.grade)

        c.execute(sql,val)
        con.commit()
        print("")
        print("Student details added succesfully")
        print("")
        print("Tables present in the database")
        db.display_database()

    def get_total(self,m1,m2,m3,m4,m5):
        total=int(m1)+int(m2)+int(m3)+int(m4)+int(m5)
        total=int(total)
        return total

    def get_avg(self,total):
        self.avg=self.total/5
        self.avg=int(self.avg)
        return self.avg
    
    def get_grade(self,avg):
        if(self.avg>=90 and self.avg<=100):
            grade='O'
        elif(self.avg>=80 and self.avg<90):
            grade='A+'
        elif(self.avg>=70 and self.avg<80):
            grade='A'
        elif(self.avg>=60 and self.avg<70):
            grade='B+'
        elif(self.avg>=50 and self.avg<60):
            grade='B'
        elif(self.avg>=40 and self.avg<50):
            grade='C+'
        else:
            grade='Grade not applicable'
        return grade

    def delete_student(self):
        
        self.std_id=input("Enter the student id of the student you want the details: ")    
        c=con.cursor()
        sql = "DELETE FROM student_details WHERE student_id = %s"
        id = (self.std_id, )
        c.execute(sql,id)
        print("")
        print("The details of studentid is deleted.")
        print("")
        print("The updated database")
        db.display_database()
    

    def get_all_students(self):
        db.display_database()
        
    def update_student(self):
        print("")
        print("Enter the details of the students to be updated")
        print("")
        self.std_id=input("Student id for which the details need to be changed:")
        self.std_name=input("Student Name:")
        self.dept=input("Student department:")
        self.m1=input("Mark 1:")
        self.m2=input("Mark 2:")
        self.m3=input("Mark 3:")
        self.m4=input("Mark 4:")
        self.m5=input("Mark 5:")
        self.total=self.get_total(self.m1,self.m2,self.m3,self.m4,self.m5)
        self.avg=self.get_avg(self.total)
        self.grade=self.get_grade(self.avg)
        c=con.cursor()

        sql="UPDATE student_details SET student_name=%s,department=%s,m1=%s,m2=%s,m3=%s,m4=%s,m5=%s,total=%s,average=%s,grade=%s  WHERE student_id=%s"
        val=(self.std_name,self.dept,self.m1,self.m2,self.m3,self.m4,self.m5,self.total,self.avg,self.grade,self.std_id)

        c.execute(sql,val)
        con.commit()
        print("")
        print("Student details updated succesfully")
        print("")
        print("Tables present in the database")
        db.display_database()


std=student()

print("1. Display all students \n 2.Show a student \n 3.Add a student \n 4.Update student details \n 5.Delete a student \n 6.Exit \n")
task_number=input("Enter task number:")
task_number=int(task_number)
while(task_number):
    if(task_number==1):
        std.get_all_students()
    elif(task_number==2):
        std.get_student()
    elif(task_number==3):
        std.add_student()
    elif(task_number==4):
        std.update_student()
    elif(task_number==5):
        std.delete_student()
    elif(task_number==6):
        print("End of program. Exit")
        break
    else:
        print("Enter correct task number")
    print("\n 1. Display all students \n 2.Show a student \n 3.Add a student \n 4.Update student details \n 5.Delete a student \n 6.Exit \n")
    task_number=input("Enter task number:")
    task_number=int(task_number)


