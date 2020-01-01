
#异常处理

import os

#初级
#1.处理某个错误  2.处理某种类型错误  3.有错就抓


#既要捕获异常，又要处理异常try...except
try:
	os.rmdir("Alisa")
except Exception as e :
	print("抓捕归案，等待进一步处理")
	print("错误为{}".format(e))

	#拿一个小本本记录起来
	file = open("error.txt","a+")
	file.write(str(e))
	file.close()

#try...except...finally
try:
	os.rmdir("Alisa")
except Exception as e :
	print("抓捕归案，等待进一步处理")
	print("错误为{}".format(e))

	#拿一个小本本记录起来
	file = open("error.txt","a+")
	file.write(str(e))
	file.close()
finally:   #有无异常都会执行
	print("就是这么强大")

#try...except...else
try:
	os.rmdir("Alisa")
except Exception as e :
	print("抓捕归案，等待进一步处理")
	print("错误为{}".format(e))

	#拿一个小本本记录起来
	file = open("error.txt","a+")
	file.write(str(e))
	file.close()
else:   #跟try下面的代码是一起的， 没有异常执行，有异常不执行
	print("就是这么强大")