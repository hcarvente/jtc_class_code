#RUNNING EXISTING FUNCTIONS
# print is a function
# print('hi')

# # name of the function comes first, followed by parentheses
# # what is inside the parenthese is called 'parameters' or 'argument'
# print(int(2.0))

# CREATING A FUNCTION
# DEFININF a function
def say_hello():
	#anything inside as part of the function is indended
	print('hello world!')


# RUN the function (calling a function)
say_hello()

# include a function inside a logical statement

a= 1

if a > 0:
	print('greater than 0')
	say_hello()
else:
	print('less than or equal to 0')


# run a function in a for loop
for num in range(1):
	print(num)
	say_hello()

# parameter / arguments / inputs 

# these let us make our functions more FLEXIBLE 

#add parameters inside the parenthese
def say_hello_personal(person_name):
	print(f'hello, {person_name}!')

# running the function with parameters 
say_hello_personal(person_name = 'Yusuf')
say_hello_personal(person_name ='Ash')
say_hello_personal(person_name ='Aeshna')
say_hello_personal(person_name ='Aedan')

#function to multiple numbers by 2
def times_two(number):
	print(number*2)

times_two(100)
times_two(True)

# function to multiply any numbers
def multiply(number_a, number_b, number_c):
	print(number_a*number_b*number_c)
	
multiply(5, 10, 3)
multiply(500, 10.2368, 12)


#default arguments 
def say_hello_personal(person_name='there'):
	print(f'Hello, {person_name}')

say_hello_personal()
say_hello_personal('Aryn')

def greeting(first_name, last_name, middle_name = ''):
	print(f'Hello, {first_name} {middle_name} {last_name}')


greeting(first_name = 'Paul', last_name = 'Bloom', middle_name = 'A')


# RETURN statements

# return vs print

# print - for display not manipulating data
# print - puts the output on the consile (command line) where you 
# print - does NOT save anything, cant be saved to variabke

# return function - give you actual output from function 
# output returnd by functions can be saved to variable

def multiply(number_a, number_b):
	return(number_a*number_b)


answer = multiply(2,3)
print(answer+4.0)


def capitalize_first_letter(word):
	return(word[0].upper()) + word[1:]

a = capitalize_first_letter('paul')
print(a)

# func() object.fun()
# .upper()
# .join()
# .append()

# functions with the . in front are called 'methods'




