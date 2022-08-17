# filter, sorted, map

friends= ['max','kate','man','leo']

result = []
for friend in friends:
    if friend.startswith('m'):
        result.append(friend)

print(result)

def f(x):
    if x.startswith('m'):
        return True
    else:
        return False


result = filter(f, friends)
print(list(result))

# map

friends= ['max','kate','man','leo']

result = []
for friend in friends:
    result.append(friend.upper())
print(result)

def f(x):
    return x.upper()

print(list(map(f,friends)))

def t(x):
    return x.title()

print(list(map(lambda x: x.title(),friends)))

# sorted
def f(x):
    return x[-1]

print(sorted(friends,key=lambda x:x[-1]))


# lambda функция

def f(x):
    if x.startswith('m'):
        return True
    else:
        return False

result = filter(lambda x: True if x.startswith('m') else False,friends)
print(result)