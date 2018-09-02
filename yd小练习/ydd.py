# 练习：
#    1.收费标准：3公里内13元，超过3公里后基本单价为2.3元/公里，空驶费：超过15公里，
# 每公里加收基本单价的50%（3.45元/公里）
# 需求：输入公里数，打印出费用金额（以元为单位四舍五入）
# 2.输一个学生的三科成绩：
#        打印出最高分是多少
#         最低分是多少；平均分是多少
# 3.给出一个年份，判断是否是闰年并打印结果
# 4.BMI指数（Body Mass Index）
#  以称身体质量指数：
#     BMI=体重（公斤）/身高（米）的平方
# BMI<18.5        过轻
# 18.5<=BMI<=24   正常
# BMI>24          过重

# #1
# a=input('输入公里数：')
# a=float(a)
# if 0 < a <= 3:
# 	print('价格为13元')
# elif 3 < a <=15:
# 	s=13+12*2.3
# 	print(round(s))
# elif a > 15:
# 	s=13+12*2.3+(a-15)*3.45
# 	print(round(s))
# else:
# 	print('您输入的公里数有误!!')

# #2
# a=input('请输入数学成绩:')
# b=input('请输入语文成绩:')
# c=input('请输入英语成绩:')
# a=float(a)
# b=float(b)
# c=float(c)
# if a>b>c or a>c>b:
# 	print('最高成绩为:',a)
# 	if b>c:
# 		print('最低成绩为:',c)
# 	else:
# 		print('最低成绩为:',b)
# elif b>a>c or b>c>a:
# 	print('最高成绩为:',b)
# 	if a>c:
# 		print('最低成绩为:',c)
# 	else:
# 		print('最低成绩为:',a)
# elif c>a>b or c>b>a:
# 	print('最高尘极为:',c)
# 	if a>b:
# 		print('最低成绩为:',b)
# 	else:
# 		print('最低成绩为:',a)
# print('平均成绩为:',float((a+b+c)/3))

# #3
# s=int(input('请输入年份:'))
# if s % 4==0:
# 	if s % 100==0:
# 		if s % 400==0:
# 			print(s,'年是闰年')
# 		else:
# 			print(s,'不是闰年')
# 	else:
# 		print(s,'年是闰年')
# else:
# 	print(s,'不是闰年')

# #4
# s=float(input('请输入体重:'))
# l=float(input('请输入身高:'))

# BMI=s/l**2
# if BMI < 18.5:
# 	print(BMI,'BMI过低')
# elif 18.5<=BMI<=24:
# 	print(BMI,'BMI适中')
# else:
# 	print(BMI,'BMI过高')