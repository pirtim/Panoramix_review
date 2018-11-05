def get_opcode(exp):
    return exp[0]

def reduce_full(func, iterable):
    res = []
    while len(iterable) > 0:
        new_head, new_tail = func(iterable[0], iterable[1:])
        res.append(new_head)
        iterable = new_tail
    return res

def reduce_full_rec(func, iterable):
    def helper_reduce_full(res, rest):
        if len(rest) == 0:
            return res
        else:
            head, rest = func(rest[0], rest[1:])
            res.append(head)
            return helper_reduce_full(res, rest)
    return helper_reduce_full([], iterable)

def rec_func(exp_left):
    i = exp_left[0]
    j = exp_left[1] if len(exp_left) > 1 else None
    if\
        j != None and\
        all(get_opcode(x) == 'MASK_SHL' for x in (i,j)) and\
        i[2] == j[1] + j[2] and\
        i[3] == j[3] and\
        i[4] == j[4]:

        left = ['MASK_SHL', i[1] + j[1], j[2], i[3], i[4]]
        return rec_func([left] + exp_left[2:])
    else:
        return i, exp_left[1:]

def opcode_OR(exp):
    def meth_sub(head, tail):
        new_head, new_tail = rec_func([head] + tail)
        new_head[3] = 0
        return new_head, new_tail

    def meth(head, tail):
        return (head, tail) if get_opcode(head) != 'MASK_SHL' else meth_sub(head, tail)

    return ['DATA'] + reduce_full(meth, exp)

def opcode_MASK_SHL(exp):
    size, offset, shl, exp = exp
    return ['MASK_SHL', size, offset, 0, exp]

def fold_data(exp):
    '''new_rec_magic'''
    return {
        'OR' : opcode_OR,
        'MASK_SHL' : opcode_MASK_SHL,
    }.get(
        get_opcode(exp),
        lambda: exp
    )(exp[1:])
