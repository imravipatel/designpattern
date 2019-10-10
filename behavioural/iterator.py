def count_to(count):
	"""Our iterator implementation"""

	# Our list
	numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

	# Our built-in iterator
	# Create a tuple such as (1, "eins")
	iterator = zip(range(count), numbers_in_german)

	# Iterate through our iterable list
	# Extract the german numbers
	# Put them in generator called number
	for position, number in iterator:

		# Returns a 'generator' containing number in German
		yield number

# Let's test the generator returned by our iterator:
for num in count_to(3):
	print("{}".format(num))

print("==============")
for num in count_to(4):
	print("{}".format(num))
