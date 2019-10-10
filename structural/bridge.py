class DrawingAPIOne(object):
	"""Implementation-specific abstraction: concrete class one"""
	def draw_circle(self, x, y, radius):
		print("API 1 drawing a circle at ({}, {} with radius {})!".format(x, y, radius))

class DrawingAPITwo(object):
	"""Implementation-specific abstraction: concrete class two"""
	def draw_circle(self, x, y, radius):
		print("API 2 drawing a circle at ({}, {} with radius {})!".format(x, y, radius))

class Circle(object):
	"""Impelmentation independent abstaction: for example, there could be Ractangle class"""

	def __init__(self, x, y, radius, drawing_api):
		"""Initialize the necessary attributes"""
		self._x = x
		self._y = y
		self._radius = radius
		self._drawing_api = drawing_api

	def draw(self):
		"""Implementation specific abstraction taken care of by another class: DrawingAPI"""
		self._drawing_api.draw_circle(self._x, self._y, self._radius)

	def scale(self, percentage):
		"""Implementation independant"""
		self._radius *= percentage

# Build the first Circle object using API one
circle1 = Circle(1,2,3,DrawingAPIOne())

# Draw a circle
circle1.draw()

# Build the second circle object using API two
circle2 = Circle(2,4,6,DrawingAPITwo())

# Draw a circle
circle2.draw()