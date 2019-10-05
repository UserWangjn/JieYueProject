def add(n, i):
    return n + i

def test():
    for i in range(4):
        yield i

g = test()

for n in [1, 10,5]:
    g = (add(i, n) for i in g)
print(list(g))