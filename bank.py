import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sankar",
    database="bank_db"
)
cursor = conn.cursor()

conn.commit()

# Function to create a new account
def create_account():
    name = input("Enter Account Holder Name: ")
    acc_num = input("Enter New Account Number: ")

    cursor.execute("SELECT * FROM accounts WHERE account_number = %s", (acc_num,))
    if cursor.fetchone():
        print("⚠️ Account already exists!")
    else:
        cursor.execute("INSERT INTO accounts (account_number, name, balance) VALUES (%s, %s, %s)", (acc_num, name, 0))
        conn.commit()
        print("✅ Account Created Successfully!")

# Function to deposit money
def deposit():
    acc_num = input("Enter Account Number: ")
    cursor.execute("SELECT name, balance FROM accounts WHERE account_number = %s", (acc_num,))
    result = cursor.fetchone()

    if result:
        print(f"Account Holder: {result[0]}")
        amount = float(input("Enter amount to deposit: "))
        new_balance = result[1] + amount
        cursor.execute("UPDATE accounts SET balance = %s WHERE account_number = %s", (new_balance, acc_num))
        conn.commit()
        print("💰 Amount Deposited Successfully.")
        print(f"New Balance: ₹{new_balance}")
    else:
        print("❌ Account Not Found!")

# Function to withdraw money
def withdraw():
    acc_num = input("Enter Account Number: ")
    cursor.execute("SELECT name, balance FROM accounts WHERE account_number = %s", (acc_num,))
    result = cursor.fetchone()

    if result:
        print(f"Account Holder: {result[0]}")
        amount = float(input("Enter amount to withdraw: "))
        if amount <= result[1]:
            new_balance = result[1] - amount
            cursor.execute("UPDATE accounts SET balance = %s WHERE account_number = %s", (new_balance, acc_num))
            conn.commit()
            print("🏧 Amount Withdrawn Successfully.")
            print(f"New Balance: ₹{new_balance}")
        else:
            print("⚠️ Insufficient Balance!")
    else:
        print("❌ Account Not Found!")

# Function to view balance
def balance():
    acc_num = input("Enter Account Number: ")
    cursor.execute("SELECT name, balance FROM accounts WHERE account_number = %s", (acc_num,))
    result = cursor.fetchone()

    if result:
        print(f"Account Holder: {result[0]}")
        print(f"Current Balance: ₹{result[1]}")
    else:
        print("❌ Account Not Found!")

# Function to show all accounts
def show_all_accounts():
    cursor.execute("SELECT account_number, name, balance FROM accounts")
    rows = cursor.fetchall()
    if rows:
        print("\n📋 All Account Details:")
        print("-" * 40)
        for acc in rows:
            print(f"Account Number: {acc[0]}")
            print(f"Name          : {acc[1]}")
            print(f"Balance       : ₹{acc[2]}")
            print("-" * 40)
    else:
        print("No accounts found.")

# Main menu loop
def main():
    while True:
        print("\n*********** Bank Management System ************")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Balance")
        print("5. View All Account Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            balance()
        elif choice == "5":
            show_all_accounts()
        elif choice == "6":
            print("✅ Thank you for using the Bank Management System!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
    cursor.close()
    conn.close()



# #Banking Management System

# bank_accounts={}

# def create_account():
#     name=input("Enter Account Holder Name:")
#     account_number=input("Enter New Account Number:")
#     if account_number in bank_accounts:
#         print("Already Exists!")
#     else:
#         bank_accounts[account_number]={'name': name,'balance':0}
#         print("Account Created Successfuly!")

# def deposit():
#     acc_num=input("Enter your Account Number:")
#     if acc_num in bank_accounts:
#         print(f"Account Holder: {bank_accounts[acc_num]['name']}")
#         amount=float(input("Enter amount to deposit:"))
#         bank_accounts[acc_num]['balance']+=amount
#         print(f"Amount was Deposited Successfully.")
#         print(f"New Balance: {bank_accounts[acc_num]['balance']}")
#     else:
#         print("Account Not Found!")

# def withdraw():
#     acc_num=input("Enter the Account Number:")
#     if acc_num in bank_accounts:
#         print(f"Account Holder: {bank_accounts[acc_num]['name']}")
#         amount=float(input("Enter Amount to Withdraw:"))
#         if amount<=bank_accounts[acc_num]['balance']:
#             bank_accounts[acc_num]['balance']-=amount
#             print("Amount Withdraw Successfull!")
#             print(f"New Balance:{bank_accounts[acc_num]['balance']}")
#         else:
#             print("Insufficient Balance!")
#     else:
#         print("Account Not Found!")

# def balance():
#     acc_num=input("Enter your Account Number:")
#     if acc_num in bank_accounts:
#         print(f"Account Holder: {bank_accounts[acc_num]['name']}")
#         print(f"Current Balance: {bank_accounts[acc_num]['balance']}")
#     else:
#         print("Account Not Found!")

# def main():
#     while True:
#         print("***********Bank Management System************")
#         print("1.Create Account")
#         print("2.Deposit Money")
#         print("3.Withdraw Money")
#         print("4.View Balance")
#         print("5.Exit")

#         choice=input("Enter a Choice:")

#         if choice=="1":
#             create_account()
#         elif choice=="2":
#             deposit()
#         elif choice=="3":
#             withdraw()
#         elif choice=="4":
#             balance()
#         elif choice=="5":
#             print("Thank for Using System")
#             break
#         else:
#             print("Invalid Choice! Please try Again!")


# if __name__ == '__main__':
#     main()

