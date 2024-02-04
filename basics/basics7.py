## Generator functions return iterable set of values by using yield keyword

def fun(N):
    a=0
    b=1
    yield a
    yield b
    for n in range(3, N+1):
        yield a + b
        a,b = b, a+b



for n in fun(10):
    print(n)