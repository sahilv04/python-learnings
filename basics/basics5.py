class FirstClass:
    some_var=1                              ## Variables in class and outside functions are static
    static_age=28
    def __init__(self, age):
        print("From inside constructor, initial static age ", self.static_age)
        self.static_age = age
        print("From inside constructor, new static age ", self.static_age)

    def fun(self, age):                     ## First parameter of function inside class is self (this) through which we can access static members
        self.some_var=2                     ## This will update value of static variable
        print("This is inside fun, my age is %d."%age)

    def get_static_age(self):
        return self.static_age


first_obj = FirstClass(30)

print(first_obj.some_var)
first_obj.fun(29)
print(first_obj.some_var)

print(first_obj.get_static_age())
