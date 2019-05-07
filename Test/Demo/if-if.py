#coding=utf-8
sex = raw_input("请输入你的性别：")
if sex == "女":
    white = raw_input("你白吗：")
    money = input("你有多少资产：")
    beatufl = raw_input("你美吗：")
    if white == "白" and money >= 10000 and beatufl == "美":
        print("你是白富美")
    else:
        print("你是矮矬穷")
else:
    print("你是男性，请不要再出现了")