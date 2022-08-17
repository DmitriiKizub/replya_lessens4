def my_functions(**kwargs):
    print(type(kwargs))
    for k,v in kwargs.items():
        print(k)
        print(v)

my_functions(name='leo', age = 18)
my_functions(name='leo', age = 18, is_man= True)


def megafunctions(first, second='2', *args,**kwargs):
    print(first)
    print(second)
    print(args)
    print(kwargs)

megafunctions(1,20,3,4,5,name='1', age= '2')
