# for i in range(1,6):
# 	print("*"*i)
#输出直角三角形


# for i in range(1,6):
# 	for j in range(1,i+1):
# 		print("*",end="")
# 	print()


#输出等边三角形

# for i in range(1,6): #控制行数
# 	print("")
# 	for j in range(1,6-i):
# 		print(" ",end="")
# 	for k in range(1,i+1):
# 		print("* ",end="")


#99乘法口诀


# for i in range(1,10):
# 	for j in range(1,i+1):
# 		#print("%d*%d=%d" %(j,i,i*j),end=" ")
# 		print("{0}*{1}={2}".format(j,i,i*j),end=" ")
# 	print("")

#冒泡排序

a = [1,7,4,89,34,2]
for i in range(len(a)-1):
	for j in range(len(a)-1-i):
		if a[j] > a[j+1]:
			a[j],a[j+1]=a[j+1],a[j]
print(a)
