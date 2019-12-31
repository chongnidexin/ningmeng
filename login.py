# password = {"admin":"123456","user1":"1234"}
# count = 3
# while True:
# 	username = input("请输入你的用户名")
#
# 	if username in password.keys():
# 		while count > 0:
# 			pwd = input("请输入你的密码")
# 			if pwd == password[username]:
# 				print("登陆成功")
# 				break
# 			else:
# 				print("密码错误请重新输入")
# 				count -= 1
# 				print("你还有{}次输入机会".format(count))
# 		break
#
# 	elif username not in password.keys() or username == " ":
# 		print("请输入正确的用户名")
# #
# password = {"admin":"123456","user1":"1234"}
# username = input("请输入你的用户名")
# while True:
# 	for a in password:
# 		if username in password:
# 			for b in range(1,3):
# 				pwd = input("请输入你的密码")
# 				if pwd == password[username]:
# 					print("登陆成功")
#
# 		elif username not in password or username==" ":
# 			print("请输入正确的用户名")