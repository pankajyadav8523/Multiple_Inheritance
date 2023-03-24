"""
Learning notion of multiple inheritence
Author : Pankaj Yadav
Date: 24 MArch, 2023

""" 

class Length(object):
	"""
	Class represent the length of geometricle shape Rectangle

	"""
	# Defining Getter / Setters for hidden instance attribute

	@property
	def len(self):
		return self._len

	@len.setter
	def len(self, value):
		assert isinstance(value, int)
		self._len = value

	def __init__(self, l):
		self.len = l
		

class Breadth(object):
	"""
	Class Represents the breadth of geometric shape breadth

	"""
	# Defining Getter/Setter for hidden instance attribute
	
	@property
	def bread(self):
		return self._bread

	@bread.setter
	def bread(self, value):
		self._bread = value

	def __init__(self, b):
		self.bread = b
		

class Rect_area(Length, Breadth):
	"""Class Represent to calculate Area of rectangle"""

	def __init__(self, l, b):
		super().__init__(l)      #this is the main Zist of class inheritence
		super(Length, self).__init__(b)

	def r_area(self):
		"""Returns: Area of rectangle"""
		Area = self.len*self.bread
		return Area



obj = Rect_area(5,6)
print(obj.r_area())

	
	

	