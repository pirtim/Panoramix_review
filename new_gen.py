from random import choice
# from collections import defaultdict

def get_opcode(exp):
    return choice(['OR', 'MASK_SHL'])


def complx(exp):
    i = 0
    while i < len(exp)-1:
        yield exp[i], exp[i+1]
        i += 1
    yield exp[i], 'END'

def opcode_OR(exp):
    res = []

    # for idx, x in enumerate(exp):
    #     pass
    for idx, x in enumerate(exp):
        # assumption:
        # get_opcode(exp[-1]) != 'MASK_SHL'

        if get_opcode(exp[idx]) == 'MASK_SHL':
            for i, j in complx(exp):
                if j == 'END':
                    break
                if all([
                    *[get_opcode(x)=='MASK_SHL' for x in (i,j)],
                    i[2] == j[1] + j[2],
                    i[3] == j[3],
                    i[4] == j[4],
                ]):
                    exp[idx] = ['MASK_SHL', i[1] + j[1], j[2], i[3], i[4]]
                    exp.pop(idx+1)

            # while all([
            #     idx < len(exp)-1, # kiedy jest na -1 to poprostu dodaje
            #     get_opcode(exp[idx])   == 'MASK_SHL',
            #     get_opcode(exp[idx+1]) == 'MASK_SHL',
            #     exp[idx][2] == exp[idx+1][1] + exp[idx+1][2],
            #     exp[idx][3] == exp[idx+1][3],
            #     exp[idx][4] == exp[idx+1][4],
            # ]):
            #     exp[idx] = ['MASK_SHL', exp[idx][1] + exp[idx+1][1], exp[idx+1][2], exp[idx][3], exp[idx][4]]
            #     exp.pop(idx+1)

            exp[idx][3] = 0

        res.append(exp[idx])

    return ['DATA']+res

def opcode_MASK_SHL(exp):
    size, offset, shl, exp = exp
    return ['MASK_SHL', size, offset, 0, exp]
    # return ['MASK_SHL', exp[1], exp[2], 0, exp[4]]

@staticmethod
def fold_data(exp):
    return {
        'OR' : opcode_OR,
        'MASK_SHL' : opcode_MASK_SHL,
    }.get(
        get_opcode(exp),
        lambda exp: exp
    )(exp[1:])
