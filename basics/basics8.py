## lambda (anonymous functions)

fun_name = lambda x,y: x+y

print(fun_name(1,2))


## declare a function with variable number of params (rest params)
def fun(first, second, *therest):
    print(therest, type(therest))
    print(list(therest))

fun(1,2,3,4,5,6,7,8,9)


## sets and tuples

a=[2,2,3,3]
s=set(a)
print(s)
t=tuple(a)
print(t)

## sets
set1 = set([1,2,3,4,5,6,6])
set2 = set([4,5,6,7,8,8,9])
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))