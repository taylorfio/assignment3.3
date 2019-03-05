"""
Write a program to create a new customer at the bank and performs the following tasks:

Part A: Within the Customer class (think logically about how to prompt the user)
- Creates a new customer asking for the attributes as needed.
- Continually ask for the customer what action they want to do until the indicate they want to quit.
Examples:
Print Balance, Deposit, Withdrawal

Part B: create a textfile of customers where each line is a new customer
Write a program that asks the user to interact, but they need to 'login' correctly.
"""
import time
import datetime
import os


class Customer:
    def __init__(self, bank_money, username):
        self.bank_money = bank_money
        self.username = username

    def __str__(self):
        return "your account balance is " + str(self.bank_money)

    def deposit(self, bank_money, username):
        print("your account balance is " + str(bank_money))
        deposit_input = int(input("how much do you want to deposit?"))
        while deposit_input < 0:
            print("not possible")
            deposit_input = int(input("how much do you want to deposit?"))
        print("processing...")
        time.sleep(2)
        bank_money = bank_money + deposit_input
        try:
            money = open(username + ".txt", "w")
            money.write(str(bank_money))
            money.close()
        except IOError:
            print("error 404 / files not found")
        print("your account balance is now " + str(bank_money))
        try:
            transaction_file = open("bank accounts.txt", "a")
            ts = datetime.datetime.now()
            transaction_file.write("\n" + username + " deposit of " + str(deposit_input) + " at " + str(ts))
            transaction_file.close()
        except IOError:
            print("error 404 / files not found")

    def withdrawal(self, bank_money, username):
        print("your account balance is " + str(bank_money))
        withdrawal_input = int(input("how much do you want to withdrawal?"))
        while withdrawal_input < 0 and withdrawal_input < bank_money:
            print("not possible")
            withdrawal_input = int(input("how much do you want to withdrawal?"))
        print("processing...")
        time.sleep(2)
        bank_money = bank_money - withdrawal_input
        try:
            money = open(username + ".txt", "w")
            money.write(str(bank_money))
            money.close()
        except IOError:
            print("error 404 / files not found")
        print("your account balance is now " + str(bank_money))
        try:
            transaction_file = open("bank accounts.txt", "a")
            ts = datetime.datetime.now()
            transaction_file.write("\n" + username + " withdrawal of " + str(withdrawal_input) + " at " + str(ts))
            transaction_file.close()
        except IOError:
            print("error 404 / files not found")


def sign_in():
    temp_list = []
    username = input("enter username  ")
    temp_list.append(username)
    password = input("enter password  ")
    temp_list.append(password)
    return temp_list


global username_input
restart = False
log_in_success = False
while restart == False:
    while log_in_success == False:
        new_user_input = input("r u new to our bank [y/n]")
        while new_user_input != "y" and new_user_input != "n":
            new_user_input = input("r u new to our bank [y/n]")
        if new_user_input == "y":
            print("welcome to the internet bank!")
            name_list = sign_in()
            username_input = name_list[0]
            password_input = name_list[1]
            try:
                file = open("passwordsave.txt", "r+")
                if (username_input + ", " + password_input) in file:
                    print("error already exists")
                elif (username_input + ", " + password_input) not in file:
                    file.write("\n" + username_input + ", " + password_input)
                    file.close()
                    new_file = open("newfile.txt", "x")
                    newfile = username_input + ".txt"
                    os.rename("newfile.txt", str(newfile))
                    print("new account saved")
                    money_input = int(input("how much money do you want to put in account"))
                    while money_input < 0:
                        print("error need number")
                        money_input = int(input("how much money do you want to put in account"))
                    file = open(username_input + ".txt", 'w')
                    file.write(str(money_input))
                    log_in_success = True
            except IOError:
                print("error 404 / files not found")

        if new_user_input == "n":
            name_list = sign_in()
            username_input = name_list[0]
            password_input = name_list[1]
            try:
                file = open("passwordsave.txt", "r+")
                if (username_input + ", " + password_input) in file:
                    print("success")
                    log_in_success = True
                elif (username_input + ", " + password_input) not in file:
                    print("account does not exist")
                file.close()
            except IOError:
                print("error 404 / files not found")

    if log_in_success == True:
        money_file = open(username_input + ".txt", "r+")
        bank_balance = int(money_file.read().strip())
        cur_user = Customer(bank_balance, username_input)

        user_choice = input("deposit_1 withdrawal_2 balance_3 logout_4")
        while user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4":
            print("error")
            user_choice = input("deposit_1 withdrawal_2 balance_3 logout_4")

        if user_choice == "1":
            cur_user.deposit(bank_balance, username_input)
        if user_choice == "2":
            cur_user.withdrawal(bank_balance, username_input)
        if user_choice == "3":
            print("processing...")
            time.sleep(2)
            print(Customer(bank_balance, username_input))
        if user_choice == "4":
            print("goodbye")
            restart = True
