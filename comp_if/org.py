if i in lines and i+2 in lines and i+3 in lines and i+4 in lines and i+7+push_offset in lines and\
    (lines[i][1], lines[i+2][1], lines[i+3][1], lines[i+4][1], lines[i+7+push_offset][1]) == ('PUSH1', 'CALLDATASIZE', 'LT', push, 'JUMPI'):
        print("default function found:",str(i)," - ",lines[i+4][2])
        self.add_func(lines[i+4][2],name="_fallback()")
        break

#[5, 'PUSH1', 4]
#[7, 'CALLDATASIZE']
#[8, 'LT']
#[9, 'PUSH2', 86]
#[12, 'JUMPI']