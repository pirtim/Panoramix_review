def try_add(self, other):

    # so proud of this

    self = deepcopy(self)
    other = deepcopy(other)

    assert get_opcode(other) == 'MUL'
    assert get_opcode(self) == 'MUL'

    if not len(self) == 3:
        return None
    if not len(other) == 3:
        return None

    if self[2] == other[2]:
        return ['MUL', self[1]+other[1], self[2]]

    # ['MUL', 1, ['MASK_SHL', 251, 5, 0, 'SOMETHING']] + ['MUL', 1, ['MASK_SHL', 5, 0, 0, 'SOMETHING']
    #        => ['MUL', 1, ['MASK_SHL', 256, 0, 0, 'SOMETHING']]

    if self[1] == other[1]:
        self_mask = self[2]
        other_mask = other[2]

        if get_opcode(self_mask) == 'MASK_SHL' and get_opcode(other_mask) == 'MASK_SHL' and\
            self_mask[1]+self_mask[2]==256 and self_mask[2] == other_mask[1] and other_mask[2] == 0 and\
            self_mask[3] == other_mask[3] and self_mask[4] == other_mask[4]:
                return mul_op(self[1], mask_op(self_mask[4], size=256, offset=0, shl=self_mask[3]))

    # ['MUL', 1, ['MASK_SHL', 256-y, y, 0, ['ADD', 2**y-1, ['MUL', 1, x] ] ] + ['MUL', -1, x]
    #      => ['ADD', 2**y-y, ['MUL', -1, ['MASK_SHL', y, 0, 0, x]]

    if get_opcode(self[2]) == 'MASK_SHL' and get_opcode(other[2]) != 'MASK_SHL' and self[1] == minus_op(other[1]):
        x = other[2]
        for y in [3,4,5,6,7,8,16,32,64,128]:
            m = ['MASK_SHL', 256-y, y, 0, ['ADD', 2**y-1, ['MUL', 1, x] ] ]# - x #== 2**y-1 - Mask(y,0,0, x)
            if self[2] == m:
                return add_op(2**y-1, mul_op(other[1], mask_op(x, size=y, offset=0, shl=0)))
