import mysql.connector
from datetime import datetime

conn=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sankar",
    database="attendance_db"
)

cursor=conn.cursor()

def register_user():
    user_id=int(input("Enter New User ID:"))
    username=input("Enter New Username:")
    password=input("Enter New Password:")

    sql="INSERT INTO users (user_id,username,password) VALUES (%s,%s,%s)"
    values=(user_id,username,password)
    cursor.execute(sql,values)
    conn.commit()
    print("User ID Created Successfully!")

def login_user():
    username=input("Enter Username:")
    password=input("Enter Pasword:")

    sql="SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(sql(username,password))
    user=cursor.fetchone()

    if user:
        print("Login successful!")
        attendance_menu()
    else:
        print("Invalid credentials.")
