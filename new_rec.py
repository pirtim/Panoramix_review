def get_opcode(exp):
    return exp[0]

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
    res = []

    while len(exp) > 0:
        if get_opcode(exp[0]) == 'MASK_SHL':
            app, exp = rec_func(exp)
            app[3] = 0
        else:
            app, exp = exp[0], exp[1:]
        res.append(app)

    return ['DATA']+res

def opcode_MASK_SHL(exp):
    size, offset, shl, exp = exp
    return ['MASK_SHL', size, offset, 0, exp]

def fold_data(exp):
    '''new_rec'''
    return {
        'OR' : opcode_OR,
        'MASK_SHL' : opcode_MASK_SHL,
    }.get(
        get_opcode(exp),
        lambda exp: exp
    )(exp[1:])
