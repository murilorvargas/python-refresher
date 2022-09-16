def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total
print(multiply(1, 3, 5))

def add(x, y):
    return x + y
numsList = [3, 5]
print(add(*numsList))
numsDictionaries = {"x": 15, "y": 15}
print(add(**numsDictionaries))

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."
print(apply(1, 3, 6, 7, operator="*"))
