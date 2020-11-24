print('Question 1')


class CheckingAccount():
	def __init__(self, account_holder, account_number):
		self.account_holder = account_holder
		self.account_number = account_number
		self.withdrawal_limit = 2000
		self.balance = 0

	def deposit(self, amount):
		try:
			self.balance += amount
			return self.balance
		except:
			print('System Error: Deposit amount not valid')

	def withdraw(self, amount):
		try:
			if amount > self.balance:
				print('Insufficient funds')
			elif amount > self.withdrawal_limit:
				print('Withdrawal amount exceeds the max withdrawal limit')
			else:
				self.balance -= amount
				return self.balance
		except:
			print('System Error: Withdrawal amount not valid')


print('')

print('Question 2')

# 2.1 Create a checking account using CheckingAccount class, use your name and add a random number for initialization
# 2.2 Deposit the amount of 1500
# 2.3 Withdraw the amount of 4000
# 2.4 Print the account balance

hernan_carvente = CheckingAccount(account_holder = 'Hernan Carvente', account_number = 201219)

print(hernan_carvente)

hernan_carvente.deposit(1500)
hernan_carvente.withdraw(4000)

print(hernan_carvente.balance)

print('')

print('Question 3')

# Currently, if you pass non int or float values, the methods 'deposit' and 'withdraw' will error out

# 3.1 - In the 'deposit' method, handle exceptions by wrapping code block with try/except.
# If an exception occurs, print 'System Error: Deposit amount not valid'

# 3.2 - Call the deposit method with the argument: 'cats' (string)
hernan_carvente.deposit('cats')

# 3.3 - In the 'withdraw' method, handle exceptions by wrapping code block with try/except.
# If an exception occurs, print 'System Error: Withdrawal amount not valid'

# 3.4 - Call the withdraw method with the argument: {} (dictionary)

hernan_carvente.withdraw({})



