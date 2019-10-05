def int_qufan():
    s = str(input('请输入一个整数：'))
    ss = s[::-1]
    result = int(ss)
    print(result)
    print(type(result))

int_qufan()