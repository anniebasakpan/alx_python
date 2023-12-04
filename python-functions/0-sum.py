def add(a, b):
    add = __import__('0-sum').add
    return (a + b)
print(add(1, 2))