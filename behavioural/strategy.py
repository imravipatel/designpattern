import types # Import the types module

class Strategy:
	"""The Strategy pattern class"""

	def __init__(self, function=None):
		self.name = "Default Strategy"

		# If a reference to a function provided, replace the execute() method with the given function
		if function:
			self.execute = types.MethodType(function, self)

	def execute(self):
		"""The default method that prints the name of the strategy being used!"""
		print("{} is used".format(self.name))

# Replacement method 1
def strategy_name1(self):
	print("{} is being used to execute method 1".format(self.name))

# Replacement method 2
def strategy_name2(self):
	print("{} is being used to execute method 2".format(self.name))

# Let's create our default strategy
s0 = Strategy()
# Let's execute our default strategy
s0.execute()

# Let's create the first variation of our default strategy by providing a new behaviour
s1 = Strategy(strategy_name1)
# Let's set its name
s1.name = "Strategy 1"
# Let's execute the strategy
s1.execute()

s2 = Strategy(strategy_name2)
s2.name = "Strategy 2"
s2.execute()