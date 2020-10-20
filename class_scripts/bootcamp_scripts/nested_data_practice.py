# lists inside lists

shopping_list = [['mangos', 'apples', 'oranges'], ['carrots,', 'broccoli','lettuce'], ['corn flakes', 'oatmeal']]
# print(shopping_list)

#access an inner list
# print(shopping_list[1])

# ONE MORE LEVEL DOWN
# access an ITEM inside an inner list
# print(shopping_list[1][0])

shopping_list[1].append('avocados')
# shopping_list[1].append('peach')
# shopping_list[1].append('kiwi')

print(shopping_list)

# nested loops with nested list 
for food_group in shopping_list:
	print(food_group)

for food_group in shopping_list:
	for food in food_group:
		print(food)

# dictionaries inside lists
users = [{'username': 'ash', 'password': 'ilovepython'},
		{'username': 'paul', 'password': 'ilovegit'},
		{'username': 'aryn', 'password': 'ilovepython', 'last_login': '9/28'}]

# print(users)

# print a dictionary inside the list
print(users[2])

# print out an item in a dictionary, in a list
print(users[2]['last_login'])

# loop through a list of dictionaries, and get the same info from each one
for user in users:
	print(user['password'])

# lists inside dictionaries
cart = {'fruits': ['mangos', 'apples'],
		'veggies': ['spinach','peas'],
		'grains':['rice'],
		'total_price': 15.78}


print(cart)

# access a specific list inside a dictionary
print(cart['veggies'])

#add items to a list inside a dictionary
cart['veggies'].append('peach')
cart['veggies'].append('carrots')
cart['veggies'].remove('peach')

print(cart['veggies'])

print(cart)

# braket indexing on a list inside a dictionary
print(cart['fruits'][0])

# loop through a list INSIDE a dictionary
for food in cart['fruits']:
	print(food.upper())

#dictionaries inside dictionaries

restaurant = {'El Basurero': {'address': '32-17 Steinway Street',
							 'menu_url': 'menu.com'},
			  'Joes Pizza': {'address': '7 Carmine Street',
			  				'phone_number':'718-882-9012'}}

print(restaurant)

# specific restaurants -- search by the key
print(restaurants['Joes Pizza'])
​
​
# specific items inside the nested dictionaries
print(restaurants['Joes Pizza']['phone_number'])
​
​
restaurants['Joes Pizza']['phone_number'] = '718-902-6354'
print(restaurants['Joes Pizza']['phone_number'])


