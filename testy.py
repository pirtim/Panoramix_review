import itertools as it

def s1(exp):
    size = exp[1]
    offset = exp[2]
    shl = exp[3]
    exp = exp[4]

    return size, offset, shl, exp


def s2(exp):
    _, size, offset, shl, exp = exp

    return size, offset, shl, exp

strategies = [s1, s2]
data = [
    # '0123',
    '01234',
    # '012345',
]

for i, (s, d) in enumerate(it.product(strategies, data)):

    print(i)
    print(d)
    print(s(d))
