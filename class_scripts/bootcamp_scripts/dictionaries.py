dictionaries 
user_account = {
	'username': 'pbloom',
	'balance': 270.26
}

#adding a new value
user_account['last_transation_date'] = '9/15/2020'

print(user_account)

user_account['user_birthyear'] = 1993

print(user_account)

#reassigning a value key
user_account['balance'] = 500

print(user_account)

#remove a key value pair 
user_account.pop('user_birthyear')

print(user_account)


lists vs dictionaries
groceries = ['apples', 'bananas', 'cherries']
print(groceries[1])

blank_dict = {}

groceries_dict = {
	'fruits': ['apples', 'bananas', 'cherries'],
	'vegetables': ['carrots', 'parsley'],
	'random':23234
}

print(groceries_dict['fruits'])



nums = [ 100, 200, 300, 400, 500, 600]
print(nums[0], nums[2], nums[4])

# user_account = {
# 	'username': 'ask',
# 	'balance': 200
# }

# print(user_account['username'], user_account['balance'])




