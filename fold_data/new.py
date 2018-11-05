def get_opcode(exp):
    return exp[0]

def opcode_OR(exp):
    res = []

    # for idx, x in enumerate(exp):
    #     pass
    for idx, _ in enumerate(exp):
        # assumption:
        # get_opcode(exp[-1]) != 'MASK_SHL'

        if get_opcode(exp[idx]) == 'MASK_SHL':
            def _conditions_list(idx, exp):
                yield idx < len(exp)-1
                yield get_opcode(exp[idx])   == 'MASK_SHL'
                yield get_opcode(exp[idx+1]) == 'MASK_SHL'
                yield exp[idx][2] == exp[idx+1][1] + exp[idx+1][2]
                yield exp[idx][3] == exp[idx+1][3]
                yield exp[idx][4] == exp[idx+1][4]

            while all(_conditions_list(idx, exp)):
                exp[idx] = ['MASK_SHL', exp[idx][1] + exp[idx+1][1], exp[idx+1][2], exp[idx][3], exp[idx][4]]
                exp.pop(idx+1)

            exp[idx][3] = 0

        res.append(exp[idx])

    return ['DATA']+res

def opcode_MASK_SHL(exp):
    size, offset, shl, exp = exp
    return ['MASK_SHL', size, offset, 0, exp]
    # return ['MASK_SHL', exp[1], exp[2], 0, exp[4]]

def fold_data(exp):
    '''new'''
    return {
        'OR' : opcode_OR,
        'MASK_SHL' : opcode_MASK_SHL,
    }.get(
        get_opcode(exp),
        lambda exp: exp
    )(exp[1:])
