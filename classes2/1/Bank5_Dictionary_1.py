# Non-OOP Bank
# Version 5
# Any number of accounts - with a list of dictionaries

accountsList = []

def newAccount(aName, aBalance, aPassword):
    global accountsList
    newAccountDict = {'name':aName, 'balance':aBalance, 'password':aPassword}
    accountsList.append(newAccountDict)
   
def show(accountNumber):
    global accountsList
    print('Account', accountNumber)
    thisAccountDict = accountsList[accountNumber]
    print('       Name', thisAccountDict['name'])
    print('       Balance:', thisAccountDict['balance'])
    print('       Password:', thisAccountDict['password'])
    print("ATM Number")
    print()

def getBalance(accountNumber, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None
    return thisAccountDict['balance']

def deposit(accountNumber, amountToDeposit, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None
        
    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None
    
    thisAccountDict['balance'] = thisAccountDict['balance'] + amountToDeposit
    return thisAccountDict['balance']
    
def withdraw(accountNumber, amountToWithdraw, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None

    if password != thisAccountDict['password']:
        print('Incorrect password for this account')
        return None

    if amountToWithdraw > thisAccountDict['balance']:
        print('You cannot withdraw more than you have in your account')
        return None

    thisAccountDict['balance'] = thisAccountDict['balance'] - amountToWithdraw
    return thisAccountDict['balance']
