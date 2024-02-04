## map function

arr = [10,20,30,40]

def fun(age):
    return "My age is %s"%str(age)

new_arr=list(map(fun, arr))

print(new_arr)

## filter function

def adults(age):
    return age > 18
filtered=list(filter(adults,arr))
print(filtered)