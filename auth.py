import random
import validation 
from budget import Budget
from getpass import getpass

database = {} #dictionary for the details of the customer
customer = Budget()

def init():
    print("Welcome to Kiitan's Bank")
    
    haveAccount = int(input("Do you have an account with us? 1. (Yes) 2. (No)\n"))

    if haveAccount == 1:
        login()
        
    elif haveAccount == 2:
        register()
    else:
        print("You have selected an invalid option. ")
        init()

def login():
    print("******* LOGIN ******")
    userAccountNumber = int(input("What is your account number? \n"))
    #print(database[userAccountNumber])
    #password = input("What is your password? \n")
    isValidAccounntNumber = validation.account_number_validation (userAccountNumber)
    #print(isValidAccounntNumber)

    if isValidAccounntNumber:

        password = input("What is your password \n")
        if(password != database[userAccountNumber][-1]):
            print("Wrong password")
            login()
        else:
            bankOperation(database[userAccountNumber])
    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("***** REGISTER *****")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password =input("Create a password for yourself \n")

    accountNumber = generateAccountNumber()

    database[accountNumber]= [first_name, last_name, email, password]
    #print(database)
    #print(database[accountNumber][-1])

    print("==== YOUR ACCOUNT HAS BEEN CREATED ====")
    print(f"Your account number is {accountNumber}")
    print("Make sure to keep it safe! ")
    print("==== ==== ==== ==== ==== ==== ==== ====")

    login()

    

def bankOperation(user):
    print("******* Welcome to Kiitan's bank. *******")
    print(f"Welcome {user[0]} {user[1]}")
    selectedOption = int(input("What would you like to do? 1. (deposit) 2. (withdrawal) 3. (logout) 4. (exit)\n"))

    if selectedOption == 1:
        depositOperation()
    elif selectedOption == 2:
        withdrawalOperation()
    elif selectedOption == 3:
        login()
    elif selectedOption == 4:
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)

def withdrawalOperation():
    print("******** Withdrawal ********")
    amount = int(input("How much would you like to withdraw? \n"))
    customer.withdraw(amount)
    print("****** End of Withrawal Operation *****")
    
def depositOperation ():
    print("****** Deposit ******")
    amount = int(input("How much would you like to deposit? \n"))
    customer.deposit(amount)
    print("****** Deopsit Successful *****")

def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)


##### ACTUAL BANKING APP SYSTEM #####
init()