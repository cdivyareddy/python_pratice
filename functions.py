'''def example():
    print('hi')
    example()
print(example())


def test(n=0):
    if n==4:
        return n*10
    return test(n+1)
print(test())


def test(n=0):
    if n==6:
        return n*10
    return n*10+test(n+1)
print(test(3))'''

def test(n=0):
    if n==5:
        return n
    return n+test(n+1)
print(test())
