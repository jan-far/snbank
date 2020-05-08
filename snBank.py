import random
import string
import re

staff = "staff.txt"


def get_username():
    print("Please Provide Your details: ")
    Username = input("Username: ").strip()
    Password = input("Password: ").strip()
    return Username, Password


def authorized():
    Username, Password = get_username()
    with open(staff, 'r') as staff_log:
        details = re.findall('.*\n*(username:)\n*(.*)\n*(password:)\n*(.*)\n*'
                             '(email:)\n*(.*)\n*(full name:)\n*(.*)\n*', staff_log.read())

    for item in details:
        if Username in item[1] and Password in item[3]:
            successful = f"""authenticated! welcome back {Username},...You are authorized \n"""
            print(successful)
            return True

    print("Wrong!")
    authorized()


def acct_search():
    print("Welcome! Plese provide your account number;")
    acct_number = input("Account Number: ")
    with open('customer.txt', 'r') as fl:
        list = re.findall('.*\n*(Account Name:)\n*(.*)\n*(Opening Balance:)\n*(.*)\n*'
                          '(Account Type:)\n*(.*)\n*(Account Email:)\n*(.*)\n*'
                          '(Account Number:)\n*(.*)\n*', fl.read())

    # for i, x in enumerate([1, 2, 3, 2]) if x == 2]
    for item in list:
        # print(item)
        if acct_number in item[9]:
            # print(item)
            x = iter(item)
            f = (zip(*([x] * 2)))
            print("Your account details are: \n")
            for u, v in f:
                print(f'{u}{v}')
    print("\n")
    bank_options()


def bank_options():
    print('''   _____ STAFF LOGIN________
            1 Create new bank account
            2 Check Account Details
            3 LogOut ''')
    try:
        choice = input(">>> ").strip()
        if choice == str(1):
            create_account()
        elif choice == str(2):
            acct_search()
        elif choice == str(3):
            print(".......Bye!.........")
            choices()
            return True
        else:
            print('Sorry! wrong input... Enter the corresponding number to your choice \n')
            bank_options()
    except:
        UnboundLocalError("Ensure you pick the number representation of the options"),
        ValueError("Wrong value type! please enter an integer")


def acct_type():
    print(''' What account type are you opening?
            1 Savings Account
            2 Current Account''')
    try:
        uinput = int(input("Account Type: "))
        if uinput == 1:
            ans = "Savings Account"
            return ans
        elif uinput == 2:
            ans = "Current Account"
            return ans
    except TypeError:
            "Wrong value type! please enter an integer \n"
    except ValueError:
        "Wrong value type! please enter an integer \n"
    except UnboundLocalError:
        "Ensure you pick the number representation of the options \n"
    print("WRONG!... Please pick an account type, from 1 or 2 \n")
    acct_type()


def opt2():
    print("Okay! proceed...")
    anw = int(input("Enter your desired Opening Amount: "))
    try:
        if anw is int:
            print("Saved!!!")
            return anw
    except TypeError:
            "Wrong value type! please enter an integer \n"
    except ValueError:
        "Wrong value type! please enter an integer \n"
    except UnboundLocalError:
        "Ensure you pick the number representation of the options \n"
    print("WRONG INPUT!... Again, please. ")
    opt2()


def opening_bal():
    print("""You're opening with how much?
           1 $0.00
           2 Enter desired amount""")
    try:
        uinput = int(input("Enter Option: "))
        if uinput == 1:
            ans = "0.00"
            return ans
        elif uinput == 2:
            opt2()
        else:
            print("Wrong! enter the available options \n")
            opening_bal()
    except TypeError:
        "Wrong value type! please enter an integer \n"
    except ValueError:
        "Wrong value type! please enter an integer \n"
    except UnboundLocalError:
        "Ensure you pick the number representation of the options \n"
    print("Wrong! input, Try again...\n")
    opening_bal()


def writer(notes):
    f = open('customer.txt', "a")
    f.writelines(notes + "\n")
    # seek  with options
    # 0 - for the beginning of the file
    # 1- for the current position of file
    # 2 - for the end of the file
    # f.seek(1)


def create_account():
    passkey = '02' + ''.join(random.choices(string.digits, k=8))
    AccountName = "Account Name: " + input("Account Name: ")
    OpeningBalance = "Opening Balance: $" + str(opening_bal())
    AccountType = "Account Type: " + acct_type()
    AccountEmail = "Account Email: " + input("Account Email: ")
    AccountNumber = "Account Number: " + passkey
    writer("\n" + AccountName)
    writer(OpeningBalance)
    writer(AccountType)
    writer(AccountEmail)
    writer(AccountNumber)
    print("\n Here are your bank details: \n" +
          AccountName + "\n" + OpeningBalance + "\n" + AccountType + \
          "\n" + AccountEmail + "\n" + f"Your Account Number is: {passkey}\n")
    print('*' * 25)
    bank_options()


def choices():
    print(" ")
    print(''' ___________Welcome_____________
        Please choose what you would like to do...
        1 Staff Login
        2 Close app''')
    try:
        choice = int(input(">>> "))
        print('*' * 25)
        if choice == 1:
            authorized()
            bank_options()
        elif choice == 2:
            print("Thank you for banking with us! ")
            quit()
    except TypeError:
            "Wrong value type! please enter an integer \n"
    except ValueError:
        "Wrong value type! please enter an integer \n"
    except UnboundLocalError:
        "Ensure you pick the number representation of the options \n"
    print("WRONG INPUT!... Again, please. ")
    choices()


choices()
# bank_options()
# authorized()

#
# create_account()
