'''
Planning challenge 2!

For each piece here, write out the pseudocode as comments FIRST, then write your code!
'''


'''
1. Shipping

You are building a system to handle shipping orders. Each order should be a dictionary that has 3 pieces of information:
-destination (string) (for the purposes of this challenge this can be any place, no need to make a full address)
-date_shipped (string)
-weight (float) (how many pounds the package is)

Assign 3 separate orders to 3 separate variables
'''
print('\nPART 1')

# create three seperate order variables 
# for each variable include the destination, date_shipped, and weight
shipping_order1 = {'destination': 'Queens, NY' , 'date_shipped': 'October 20' , 'weight':float(50)}
shipping_order2 = {'destination': 'Richmond, VA' , 'date_shipped': 'October 22' , 'weight':72.5}
shipping_order3 = {'destination': 'Wichita, KS' , 'date_shipped': 'October 24' , 'weight':10.7}


'''
2. Building the database

Now, let's put the orders all into a database togther (all the orders are storedin 1 variable). 

Your database can either be a dictionary or a list. 

Print out the database to make sure all the info is in there. 

'''
print('\nPART 2')

# create a order database list 
# call in all the shipping orders into the variable 
# print the database

database_l = [shipping_order1, shipping_order2, shipping_order3]

database_d = {'order 1': shipping_order1, 'order 2': shipping_order2, 'order 3':shipping_order3}

print(database_l, database_d)


'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
print('\nPART 3')

#define function 
def add_order_l(database, order):
	database.append(order)

def add_order_d(database, order):
	count = 0
	for k, v in database.items(): # get every key, value pair in the dictionarys
		count += 1
	key = count + 1

	database[key] = order


new_order1 = {'destination': 'Los Angeles, CA' , 'date_shipped': 'May 20' , 'weight':45.5}
add_order_l(database_l, new_order1)
# print(database_l)

add_order_d(database_d, new_order1)
print(database_d)

'''
4. Define a function called complete_order() to mark a specific order in your database complete

This means that it should add a new key/value pair called 'complete' to a specific order, and set the value to True

Test this out and print out your database to make sure it works!

HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database
'''
print('\nPART 4')


