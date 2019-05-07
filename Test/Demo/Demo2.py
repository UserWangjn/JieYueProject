#encoding=utf-8

num = int(input("您共乘坐了多少次地铁："))
i=1	#次数

while i <= num:
	res = i * 6  # 总金额
	if 50<=res<80:
		u = 6*0.8	#单次金额
		t = 1
		res = 6*(i-1)+u*t
		t += 1
	if 80<=res<400:
		res = res+6*0.5
	i+=1

print("您共花费：%r元"%res)