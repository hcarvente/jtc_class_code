print("Challenge 3.1: Debug code snippets")

print()

print("Code Snippet 1:")

a = 1
b = 0
c = (a > b)

print("The value of c is True since a is greater than b.")

print()

print("Code Snippet 2:")

d = (True or (5 > 7) or not (8 < 20))

print("The value of d is True because it combines two false statements and one true statement using or.")

print()


print("Code Snippet 3:")

m = "GOAT"
n = "goat"

o = (m == n)

print ("The value of o is False since Python is case-sensitive.")

print()

print("Code Snippet 4:")

u = 5
v = 2

if u * v == 10:
    print("The product of u and v is 10")
else:
    print("The product of u and v is not 10")

print()

print("Code Snippet 5:")
x = 15
y = 25
z = 30

if z < x:
    print("z is less than x")

elif z > x and z < y:
    print("z is between x and y")

else: 
    print("z is greater than y")


print()
print()
print()

print("Challenge 3.2: Playing with the stock market")

print()

print("Challenge 3.2.1: Creating variables")
# Create variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
facebook = 250
google = 1400
microsoft = 200
# TODO: Create a variable here for the stock price of Apple = 100
# TODO: Create a variable here for the stock price of Facebook = 250
# TODO: Create a variable here for the stock price of Google = 1400
# TODO: Create a variable here for the stock price of Microsoft = 200
print()


print("Challenge 3.2.2: Taking user input")
username = input('What is your name? ')
saving = input('What is your current saving amount? ')
saving = float(saving)

# TODO: Write code to ask the client his name and save it to a variable.
# TODO: Write code to ask the client his saving and save it to another variable.
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft. ")
print()

print("Challenge 3.2.3: Perform user-specific calculations")

price = 0
stock_count = 0
if stock == "amzn":
	price = amazon 
	stock_count = saving / amazon
elif stock == "aapl":
	price = apple
	stock_count = saving / apple
elif stock == "fb":
	price = facebook
	stock_count = saving / facebook
elif stock == "goog":
	price = google
	stock_count = saving / google
else:
	price = microsoft
	stock_count = saving / microsoft

# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''
print()

print("Challenge 3.2.4: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print(f"{username} has ${saving} in savings and he can buy {stock_count} shares of {stock} at the current price of ${price}.")




