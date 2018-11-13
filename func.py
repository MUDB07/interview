# 使用 while 循环打印 1 3 5 7 9

# 答案如下：

def print_odd(num): # 传递形参代表打印奇数的个数
	n = 1  # 设置开始数字
	s = 1  # 设置一个计数的变量
	while True:
		if s > num:  # 当打印次数达到五次就退出循环停止输出
			break
		print(n)  # 打印
		n += 2  # 数字每次加2
		s += 1  # 计数每次加1

print_odd(5)  # 打印五个数





# 编写一个函数，查找数字 6 是否在列表 l 里，如果在，输出“found”，如果不在，输出“not found”

l = [1,5,7,8,9]

# 答案如下：

l = [1,5,7,8,9]

def find_num(num):  # 定义一个函数，有一个形参num
	if num in l:  #判断num是否在l中
		print('found')
	else:
		print('not found')

find_num(6)  # 传递实参 6





# 将字符串 s 拆分成两个字符串 s1、s2，其中 s1 只包含字母，转换为小写，以 [a-z] 排序，s2 只包含数值，升序排序

s = "aAsnr3id2d4b6gs7DZsf9e1AF"

# 答案如下

s = "aAsnr3id2d4b6gs7DZsf9e1AF"

l1 = []
l2 = []

# 得到两个列表，一个全为小写字母，一个全为数字
def get_list():
	for i in s.lower(): # 将字符串中大写全部转为小写后遍历 
		try:			# 使用异常判断，如果可以转为数字则为数字，如果不能转为数字则为字母
			num = int(i)
			l2.append(num)  # 将数字放入l2
		except ValueError as e:
			l1.append(i)  # 将字母放入l1

#　获取排序后的两个字符串s1,s2
def get_result():
	s1 = ''.join(sorted(l1))  # 将字母列表按照ascii码值升序排序后合并成字符串s1
	s2 = ''.join(map(lambda n:str(n),sorted(l2))) # 将数字列表中的元素升序排序后转换为字符串，再合并为s2
	return (s1,s2)  # 返回一个元组

def main():
	get_list()
	result = get_result()  # 获取get_result()返回值(s1,s2)
	s1 = result[0]
	s2 = result[1]
	print("s1:",s1)
	print("s2:",s2)

main()
