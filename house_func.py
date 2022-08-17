def hous(height, wall_sybmol= '|'):
    print('    /\\  ')
    print('   /  \\   ')
    print('  /    \\')
    for i in range(height):
        print('|        |')
        print(f'{wall_sybmol}   {wall_sybmol}    {wall_sybmol}')
    print('-'*10)


hous(2, '#')


hous(wall_sybmol='*',height=5)