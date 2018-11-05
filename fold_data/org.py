def get_opcode(exp):
    return exp[0]

def fold_data(exp):
    '''org'''

    if get_opcode(exp) == 'OR':

        res = []
        idx = 1
        while idx < len(exp):

            if get_opcode(exp[idx]) != 'MASK_SHL':
                res.append(exp[idx])
            else:
                while idx<len(exp)-1 and (get_opcode(exp[idx+1]), get_opcode(exp[idx])) == ('MASK_SHL', 'MASK_SHL') and \
                    exp[idx][2] == exp[idx+1][1] + exp[idx+1][2] and\
                    exp[idx][4] == exp[idx+1][4] and exp[idx][3]==exp[idx+1][3]:
                        exp[idx] = ['MASK_SHL', exp[idx][1]+exp[idx+1][1], exp[idx+1][2], exp[idx][3], exp[idx][4]]
                        exp.pop(idx+1)

                exp[idx][3] = 0
                res.append(exp[idx])

            idx = idx+1

        return ['DATA']+res

    if get_opcode(exp) == 'MASK_SHL':

        size = exp[1]
        offset = exp[2]
        shl = exp[3]
        exp = exp[4]

        return ['MASK_SHL', size, offset, 0, exp]


    return exp