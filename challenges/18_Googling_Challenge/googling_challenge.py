'''
GOOGLING CHALLENGE! 

Today, we'll ask you to write a bunch of small pieces of code.

Unlike previous ones, we have NOT showed you the exact code you'll need to answer the questions.

So, you'll want to search out answers on the web, make sure you understand them, then try them out until they work!

For each question, you should also COPY THE LINK TO THE RESOURCE WHERE YOU FOUND THE SOLUTION in so that you can use it in the future too
'''


# 1A. Sort the below list in alphabetical order
print('QUESTION 1\n')
my_friends = ['Yusuf', 'Aedan', 'Mia', 'Ash', 'Paul', 'Aeshna', 'Aryn', 'Rob']


# created a new variable and used the sorted() function which causes strings to be sorted alphabetically
# Got solution at: https://www.w3schools.com/python/ref_func_sorted.asp 
sorted_list = sorted(my_friends)

# printed the new variable which now sorted
print(sorted_list)

# 1B. Comment your code in 1A to convince yourself you understand how it works


# 2A. Get all the keys from the below dictionary, then print them out:
# Hint: there is a single command that can do this
print('QUESTION 2\n')

my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}

# used the .keys() method that pulls out all the keys in dictionary
# Got this method here: https://www.geeksforgeeks.org/python-dictionary-keys-method/
print(my_account.keys())

# 2B. Comment your code in 2A to convince yourself you understand how it works



# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
print('QUESTION 3\n')
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'


# Used the count command to give us how many times 'wood' appears in the string. Which takes the original string and you define the substring you want searched.
# Found command here: https://www.programiz.com/python-programming/methods/string/count
print(my_string.count('wood'))

# 3B. Comment your code in 3A to convince yourself you understand how it works



# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
print('QUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']


# 4B. Comment your code in 4A to convince yourself you understand how it works

# Used the .count method to count the number of 'banana' occurances in the list
print(my_list.count('banana'))


# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
print('QUESTION 5\n')


# used the set() function to pull out all the unique values in the list. 
# pulled info from: https://www.kite.com/python/answers/how-to-count-the-number-of-occurrences-of-an-element-in-a-list-in-python
print(set(my_list))

# 5B. Comment your code in 5A to convince yourself you understand how it works


# 6A. Import numpy, then use it to generate a random number between 0-1
print('QUESTION 6\n')

# imported the random module from numpy
from numpy import random

# set x to equal the random method and placed '1' in the line parentheses since it was meant to generate a random number between 0-1
# found solution here: https://www.w3schools.com/python/numpy_random.asp
x = random.rand(1)

#printed x which is will run the random method
print(x)

# 6B. Comment your code in 6A to convince yourself you understand how it works


'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to search out new code solutions.
We'll be doing more challenges like this coming up in the future. 

Remember to comment all your code and push your work to your Github repo when you're done!
'''
