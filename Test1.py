import math


def choose(n, r):
    return math.factorial(n)/math.factorial(r)/math.factorial(n-r)


def function(x):
    z = 0
    y = 0
    while z <= x:
        y = y + choose(x+z, z)*1/(2**z)
        z += 1
    return y


a = 0
b = 2

print(choose(b, a)*1/(2**a))

print(function(16))


x = 0


while x < 100:
    print(x)
    print(function(x))
    x += 1
