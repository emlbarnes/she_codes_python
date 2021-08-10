def double(x):
    return x * 2


def halve(x):
    return x / 2


def add(x, y):
    return x + y

print(halve(5))

print(halve(double(5)))

print(add (5,6))
print (double (add(5,6)))
print (halve (add(6,8)))