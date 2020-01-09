class MathMethod(object):
	"""定义数学方法类"""
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def add(self):
		"""加法函数"""
		return self.a+self.b

	def multi(self):
		"""乘法函数"""
		return self.a*self.b

