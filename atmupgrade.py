import random
from datetime import datetime
now = datetime.now()

database = {}

def init():

    
    print('Welcome')
    print(now)
     

    haveAccount = int(input('Do you have an account with us: 1 (yes) 2 (no) \n'))

    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print('You have selected an invalid option')
        init()


def login():

    print('Login to your account')


    accountNumberFromUser = int(input('Enter Account Number \n'))
    password = input('Enter Password \n')

    for accountNumber,UserDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(UserDetails[3] == password):
                    bankOperation(UserDetails)
                    

    print('Invalid account or password') 
    login()           
    


def register():
    print('Register*')

    email =  input('Enter email address \n')
    firstname = input('Enter Firstname \n')
    lastname = input('Enter Lastname \n')
    password = input('Create a password \n')
    confirmPassword = input('Enter password again \n')

    accountNumber = generateAccountNumber()

    database[accountNumber] = [ firstname, lastname, email, password ]
    
    print('Your account has been created.')
    print('Your account number is: %d' % accountNumber)
    print('Keep your account number SAFE')

    login()

def bankOperation(user):
    print('Welcome %s %s' % ( user[0], user[1] ) )
    
    print('These are the avaliable options:')
    print('1.Deposit') 
    print('2. Withdrawal')
    print('3. Complaint')
    print('4. Logout')
    print('5. Exit')


    selectedOption = int(input('Please select an option: \n'))

    if selectedOption == 1:
       x = int(input('how much do you want to deposit: \n '))
       print('current balance:' ,x)

    elif selectedOption == 2:
        x = int(input('how much would you like to withdraw: \n'))
        print('Take your cash.')

    elif selectedOption == 3:
        x = input('what issue will you like to report: \n')
        print('Thank you for contacting us')

    elif selectedOption == 4:
        login()

    elif selectedOption == 5:
        exit()

    else:
        print('Invalid option selected') 
        bankOperation(user) 

def generateAccountNumber():
    
    return random.randrange(0000000000,9999999999)



init()