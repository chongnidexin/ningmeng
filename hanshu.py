def add_number(m,n,k=1):
	sum = 0
	for i in range(m, n, k):
		sum = sum + i
	print("%d到%d的和是:%d"%(m,n-1,sum))
add_number(1,11)

# 定义函数三部曲

# 1.先用代码实现功能，还可以选取一组数据来证明自己的 代码是否正确
# 2.变成函数，加def
# 3.想办法提高代码的复用性
