def get_opcode(*x):
    pass
exp, idx = [], 1

# not lazy
while all(map(lambda x:x(),[
    lambda: idx < len(exp)-1,
    lambda: get_opcode(exp[idx])   == 'MASK_SHL',
    lambda: get_opcode(exp[idx+1]) == 'MASK_SHL',
    lambda: exp[idx][2] == exp[idx+1][1] + exp[idx+1][2],
    lambda: exp[idx][3] == exp[idx+1][3],
    lambda: exp[idx][4] == exp[idx+1][4],
])):
    pass

def _conditions_list(idx, exp):
    yield idx < len(exp)-1
    yield get_opcode(exp[idx])   == 'MASK_SHL'
    yield get_opcode(exp[idx+1]) == 'MASK_SHL'
    yield exp[idx][2] == exp[idx+1][1] + exp[idx+1][2]
    yield exp[idx][3] == exp[idx+1][3]
    yield exp[idx][4] == exp[idx+1][4]
while all(_conditions_list(idx, exp)):
    pass

while\
    idx < len(exp)-1 and\
    get_opcode(exp[idx])   == 'MASK_SHL' and\
    get_opcode(exp[idx+1]) == 'MASK_SHL' and\
    exp[idx][2] == exp[idx+1][1] + exp[idx+1][2] and\
    exp[idx][3] == exp[idx+1][3] and\
    exp[idx][4] == exp[idx+1][4]:
    pass