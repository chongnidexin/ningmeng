#继承

class RobotOne(): #第一代机器人
	"""docstring for Robotone"""
	def __init__(self, year, name):
		self.year=year
		self.name=name

	def walking_on_ground(self):
		print(self.name+"只能在平地上行走，有障碍物就会摔倒")	
	
	def robot_info(self):
		print("{0}年生产的机器人{1}，是中国研发的".format(self.year,self.name))
class RobotTwo(object):
	"""docstring for RobotTwo"""
	def __init__(self, arg):
		self.year=year
		self.name=name
	def walking_on_ground(self):
		print(self.name+"可以在平地上平稳的行走")
	def walking_avoid_block(self):
		print(self.name+"可以避开障碍物")

	def robot_info(self):
		print("{0}年生产的机器人{1}，是中国研发的".format(slef.year,self.name))
