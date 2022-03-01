import abc

class Animal(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def make_sound(self):
		print('adfdas')
		pass

class Dog(Animal):
	def make_sound(self):
		print('bark')

class Cat(Animal):
	def make_sound(self):
		print('meow')

d = Dog()
d.make_sound()
c = Cat()
c.make_sound()