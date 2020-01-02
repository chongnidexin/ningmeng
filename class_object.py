#python类的语法    关键字class   def函数名(参数)：函数的关键字
#class类名：#类名的规范是 数字字母下划线组成，不能以数字开头，首字母大写  驼峰命名

class BoyFriend:
	#类属性
	height = 175
	weight = 120
	money = 100
	#初始化函数，在有多次赋值调用的时候可使用
	def __init__(self,*args):

	def cooking(self):
		print("要会做饭")


	def earn(self): #会挣钱
		print("月薪2毛8")



#实例方法需传递self
	def tool(self):

#类方法  需传递cls
  	@clsssmethod
  	def tools_1(cls):


#静态方法  不用传递参数
	@staticmethon
	def tools_2():



#1：实例方法self,类方法cls，静态方法（普通方法） 实例和类名都可以直接调用
#2：不同点：静态方法和类方法不可以调用类里面的属性值，如果需要参数请自己传递
