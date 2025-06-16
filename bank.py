#Banking Management System

bank_accounts={}

def create_account():
    name=input("Enter Account Holder Name:")
    account_number=input("Enter New Account Number:")
    if account_number in bank_accounts:
        print("Already Exists!")
    else:
        bank_accounts[account_number]={'name': name,'balance':0}
        print("Account Created Successfuly!")

def deposit():
    acc_num=input("Enter your Account Number:")
    if acc_num in bank_accounts:
        print(f"Account Holder: {bank_accounts[acc_num]['name']}")
        amount=float(input("Enter amount to deposit:"))
        bank_accounts[acc_num]['balance']+=amount
        print(f"Amount was Deposited Successfully.")
        print(f"New Balance: {bank_accounts[acc_num]['balance']}")
    else:
        print("Account Not Found!")

def withdraw():
    acc_num=input("Enter the Account Number:")
    if acc_num in bank_accounts:
        print(f"Account Holder: {bank_accounts[acc_num]['name']}")
        amount=float(input("Enter Amount to Withdraw:"))
        if amount<=bank_accounts[acc_num]['balance']:
            bank_accounts[acc_num]['balance']-=amount
            print("Amount Withdraw Successfull!")
            print(f"New Balance:{bank_accounts[acc_num]['balance']}")
        else:
            print("Insufficient Balance!")
    else:
        print("Account Not Found!")

def balance():
    acc_num=input("Enter your Account Number:")
    if acc_num in bank_accounts:
        print(f"Account Holder: {bank_accounts[acc_num]['name']}")
        print(f"Current Balance: {bank_accounts[acc_num]['balance']}")
    else:
        print("Account Not Found!")

def main():
    while True:
        print("***********Bank Management System************")
        print("1.Create Account")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.View Balance")
        print("5.Exit")

        choice=input("Enter a Choice:")

        if choice=="1":
            create_account()
        elif choice=="2":
            deposit()
        elif choice=="3":
            withdraw()
        elif choice=="4":
            balance()
        elif choice=="5":
            print("Thank for Using System")
            break
        else:
            print("Invalid Choice! Please try Again!")


if __name__ == '__main__':
    main()

