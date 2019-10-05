def add(s, x):
    return s + x

def gen():
    for i in range(4):
        yield i
base = gen()
for n in [1, 10]:
    base = (add(i, n) for i in base)

print (list(base))
