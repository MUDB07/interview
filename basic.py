# 问题一：字符串排序

s = "hello world"

# 请编写代码，将 s 以 [a-z] 顺序输出

# 答案如下：

s = "hello world"
l = list(s.replace(' ',''))  # 去除空格后转列表
l.sort()  # 默认按照ascii码值排序
s = ''.join(l)  # 还原成字符串
print("排序结果为：",s)  # 打印结果





# 问题二：数值比较

n = [9,15,23,89,33,26,2,76]

# 请编写代码，找出数组中的最大数与最小数

# 答案如下：

n = [9,15,23,89,33,26,2,76]
# 方法一
l = sorted(n)  # 升序排序
max_num = l[-1]  # 取列表中最后一个值
min_num = l[0]  # 取列表中第一个只值
print("最大数：%d，最小数：%d" % (max_num,min_num))

# 方法二
print("最大数：%d，最小数：%d" % (max(n),min(n)))





# 问题三：替换

a = "i,am,a,student,in,chengdu"

# 请编写代码，将 “student” 和 “chengdu” 变为可基于参数输入配置的输出
# 通过参数输入打印出完整的句子

# 答案如下：

a = "i,am,a,student,in,chengdu"

status = input("请输入身份：")
city = input("请输入城市：")

# 将字符串中的,替换为' '，再将'student'，' city'分别替换为输入的值
result = a.replace(',',' ').replace('student',status).replace('chengdu',city)

print("结果：",result)
