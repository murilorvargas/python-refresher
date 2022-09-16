add = lambda x, y: x + y 
print(add(5, 5))

print((lambda x, y: x + y)(5, 7))

def double(x):
    return x * 2

sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
doubled =[doubled(x) for x in sequence]
doubled = map(doubled, sequence)

doubled =[(lambda x: x * 2)(x) for x in sequence]
doubled = list(map(lambda x: x * 2, sequence))
