# creating account 

def create_account():
	username = input('Create a username: ')
	password = input('Create a password: ')
	account = {'user': username, 'pass': password, 'balance': 0.0}
	return(account)

'''
PART 2: deposit()
This function should make a deposit to add money to the account
The function should take 2 arguments
-account (a dicionary representing a bank account, aka the output of create_account())
-amount (a float representing the amount to deposit)

The function does not need to return anything, but should increase the balance value by the appropriate amount

Test your function by making a few deposits to your account, then printing out your account
'''

def deposit(account, amount):
	account['balance'] += amount


'''
PART 3: withdraw()
This function should make a withdrawal to take money out of the account
The function should take 2 arguments:
-account (a dicionary representing a bank account, aka the output of create_account())
-amount (a float representing the amount to withdraw)

FIRST, the function should check whether there is enough money in the account to withdraw the requested amount
-If there is enough money, the function should decrease the balance value by the appropriate amount
-If there is not enough money, the function should print a message about the balance and tell the user there is not enough available to make that withdrawal

Test your function by making several withdrawals to your account
-try some you think will work AND some you think will not be allowed (more than the balance)
'''

def withdraw(account,amount):
	if amount <= account['balance']:
		account['balance'] -= amount
	else:
		print('You do not have enough money in your balance')


'''
BONUS QUESTION 4: Password-protect withdrawal and deposits
Make new deposit_secure() and withdraw_secure() functions that prompt the user for their username/password FIRST
Only let the transaction proceed if they enter the right info!
Otherwise, tell the user the info is wrong

Test out your new functions to make sure they accept correct info, and let the user know if the password/username is incorrect
'''
def deposit_secure(account, amount)



def withdraw_secure()





