from operator import contains
from random import choice

import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sankar",
    database="admission_db"
)

cursor=conn.cursor()

def add_admission():
    name=input("Enter Student Name:")
    age=int(input("Enter Age:"))
    gender=input("Enter Gender(Male/Female):")
    course=input("Enter Course Name:")
    contact=input("Enter Contact Number:")

    sql="INSERT INTO admissions(name,age,gender,course,contact) VALUES (%s,%s,%s,%s,%s)"
    values=(name,age,gender,course,contact)
    cursor.execute(sql,values)
    conn.commit()
    print("Admission Added Successfully!")

def view_admissions():
    cursor.execute("SELECT * FROM admissions")
    rows=cursor.fetchall()

    print("\n---All Admissions---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}, Course: {row[4]}, Contact: {row[5]}")

def search_admission():
    admission_id=int(input("Enter Admisson ID to Search:"))
    cursor.execute("SELECT * FROM admissions WHERE id=%s",(admission_id,))
    row=cursor.fetchone()

    if row:
        print(f"Id:{row[0]},Name:{row[1]},Age:{row[2]},Gender:{row[3]},Course:{row[4]},Contact:{row[5]}")
    else:
        print("No Record Found with That ID")

def update_admission():
    admission_id=int(input("Enter Admission ID to Update:"))
    name=input("Enter New Name:")
    age=int(input("Enter New Age:"))
    gender=input("Enter New Gender:")
    course=input("Enter New Course:")
    contact=input("Enter New Contact:")

    sql="UPDATE admissions SET name=%s,age=%s,gender=%s,course=%s,contact=%s WHERE id=%s"
    values=(name,age,gender,course,contact,admission_id)
    cursor.execute(sql,values)
    conn.commit()
    print("Admission Updated Successfully!")

def delete_admission():
    admission_id=int(input("Enter Admission Id to Delete:"))
    cursor.execute("DELETE FROM admissions WHERE id=%s",(admission_id))
    conn.commit()
    print("Admission Deleted Successfully!")

def menu():
    while True:
        print("\n=======Admission Management System=======")
        print("1.Add Admission")
        print("2.view All Admissions")
        print("3.Search Admission by ID")
        print("4.Update Admission")
        print("5.Delete Admission")
        print("Exit")

        choice=input("Enter your Choice:")

        if choice=="1":
            add_admission()
        elif choice=="2":
            view_admissions()
        elif choice=="3":
            search_admission()
        elif choice=="4":
            update_admission()
        elif choice=="5":
            delete_admission()
        elif choice=="6":
            print("Thank you for Using System")
            break
        else:
            print("Invalid Choice.Try Again!!")

menu()

cursor.close()
conn.close()



