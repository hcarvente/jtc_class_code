#loops inside loops
days = ['monday', 'tuesday', 'wednesday', 'thurs', 'friday', 'saturday', 'sunday']

# outer loop
for day in days:
	print(day)
	# for each day, print each letter individually
	#inner loop
	for letter in day:
		print(letter)

# not nested, but prints first letter each day
for day in days:
	print(day)
	print(day[0])


for day in days:
	print(day)
	# for each day, print each letter individually
	#inner loop
	print(day[0])
	for letter in day:
		print(letter.upper())


# nested loops with range()
for outer_var in range(3):
	for inner_var in range(4):
		print(f'outer: {outer_var}, inner: {inner_var}')

#multiple loo[s, no nesting]
for outer_var in range(3):
	print(f'outer: {outer_var}')
for inner_var in range(4):
	print(f'inner: {inner_var}')

#printing the looping variable after the loop is done
print(inner_var)
print(inner_var)
print(inner_var)
print(inner_var)

#logic inside loops
days = ['monday', 'tuesday', 'wednesday', 'thurs', 'friday', 'saturday', 'sunday']

# XTREME NESTING
# loop through days, print wether its weekend or not
#if it is a weekday, print 'contain o' if the letter o is in the name of the day

for day in days:
	# if day variable starts with s
	if day.startswith('s'):
		print(f'{day} is a weekend')
	else:
		print(f'{day} is a weekday')
		if 'o' in day:
			print('contains o')
		else:
			print('no o')	
#break 

for day in days:
	print(day)
	if day.startswith('w'):
		break

print('done with loop')





