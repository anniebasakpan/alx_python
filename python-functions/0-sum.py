def add(a, b):
    add = __import__('0-sum').add
    return (a + b)
print(add(1, 2))
print(add(98, 0))
print(add(100, -2))