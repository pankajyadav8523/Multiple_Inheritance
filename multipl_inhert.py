"""
Learning notion of multiple inheritance
Author : Pankaj Yadav
Date: 24 MArch, 2023

""" 

class Length(object):
	"""
	Class represent the length of geometricle shape Rectangle

	"""
	# Defining Getter / Setters for hidden instance attribute

	@property
	def lent(self):
		return self._len

	@lent.setter
	def lent(self, value):
		assert isinstance(value, int)
		self._len = value

	def __init__(self, l):
		self.lent = l

		

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
		
		super().__init__(l)      # this is the main Zist of class inheritence
		super(Length, self).__init__(b)

	def r_area(self):
		"""Returns: Area of rectangle"""
		Area = self.lent*self.bread
		return Area



obj = Rect_area(7,8)
l = Length(8)
# print(l.lent)
# print(obj.r_area())

# class Class2:
#     def m(self):
#         print("In Class5")


class Class5(object):
		def m(self):
			print("In Class2")
			# super().m()

class Class2(Class5):
    def m(self):
        print("In Class1")
        super().m()
 

class Class3(Class5):
    def m(self):
        print("In Class3")
        super().m()
 
class Class4(Class3, Class2):
	def m(self):
		print("In Class4")
		super().m()
		# super(Class2, self).m()
obj = Class4()
obj.m() 
print(Class4.mro())         #This will print list
print(Class4.__mro__)        #This will print tuple





	
	

	