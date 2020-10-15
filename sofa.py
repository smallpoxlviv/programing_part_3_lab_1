class Sofa:
	def __init__(self, width, length, colour, brand):
		self.width = int(width)
		self.length = int(length)
		self.colour = colour
		self.brand = brand

	def __str__(self):
		return "width = {}, length = {}, colour = '{}', brand = '{}'".format(self.width, self.length, self.colour, self.brand)