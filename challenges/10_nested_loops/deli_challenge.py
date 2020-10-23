
print('Question 1')
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

# You want to create a menu soon, but first things first...

# loop to add index for the meats
for i in range(len(meats)):
# replacing each meat with a capital version, reassigning each meat with a capital version
	meats[i] = meats[i].capitalize()
	# print(i)
print(meats)	
	
for i in range(len(cheeses)):
	cheeses[i] = cheeses[i].capitalize()
	# print(c)
print(cheeses)
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()

print()

print('Question 2')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list

sandwiches = []
for meat in meats:
	for cheese in cheeses:
		sandwiches.append(f'{meat} & {cheese}')

print(sandwiches)

print('Question 3')
customer_order = input('What is your order?: ')
# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'
for sandwich in sandwiches:
	if customer_order in sandwiches:
# TODO: Loop over the sandwiches list.
		print(f"Great choice! 1 {customer_order} coming right up!")
	else:
		print(f'Sorry! {customer_order}, is not on the menu')
	break
	
# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'
