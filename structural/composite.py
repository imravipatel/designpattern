class Component(object):
	"""Abstract class"""

	def __init__(self, *args, **kwargs):
		pass

	def component_function(self):
		pass

class Child(Component): # Inherits from abstract class, Component
	"""Concrete class"""

	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)

		# This is where we store the name of your child item!
		self.name = args[0]

	def component_function(self):
		# Print the name of your child item here!
		print("{}".format(self.name))

class Composite(Component): # Inherits from the abstract class, Component
	"""Concrete class and maintains the three recursive structure"""

	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)

		# This is where we store the name of the composite object
		self.name = args[0]

		# This is where we keep our child items
		self.children = []

	def append_child(self, child):
		"""Method to add new child item"""
		self.children.append(child)

	def remove_child(self, child):
		"""Method to remove child item"""
		self.children.remove(child)

	def component_function(self):
		# Print the name of the composite object
		print("{}".format(self.name))

		# Iterate through the child objects and invoke their component function printing their names
		for i in self.children:
			i.component_function()

# Build a composite submenu1
sub1 = Composite("Submenu1")

# Create a new child sub_submenu 11
sub11 = Child("Sub submenu 11")

# Create a new child sub_submenu 12
sub12 = Child("Sub submenu 12")

# Add the sub_submenu 11 to submenu1
sub1.append_child(sub11)
# Add the sub_submenu 12 to submenu1
sub1.append_child(sub12)

# Build a top level composite menu
top = Composite("Top menu")

# Build a submenu 2 that is not a composite
sub2 = Child("Submenu2")

# Add the composite submenu 1 to top level composite menu
top.append_child(sub1)

# Add plain submenu 2 to top level composite menu
top.append_child(sub2)

# Let's test if our composite pattern works!
top.component_function()