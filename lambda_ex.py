# Передача функции в функцию
def print_who(name):
    print(name)



def other(name, func):
    # Вызов переданной функции внутри другой функции
    func(name)

other('kate',print_who)


def print_namex5(name):
    print(name*5)

other('Max', print_namex5)

'''
print_who('max')

p = print_who('Max')
print(p)

p = print_who
print(p)
print(type(p))

p('leo')
'''