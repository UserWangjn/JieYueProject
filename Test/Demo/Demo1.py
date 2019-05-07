import random
j = 5
id = []
id = ''.join(str(i) for i in random.sample(range(0,9),j))    # sample(seq, n) 从序列seq中选择n个随机且独立的元素；
print(id)