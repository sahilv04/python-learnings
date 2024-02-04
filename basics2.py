age=29
name="Sahil"

if(age < 20):
    print("Junior")
elif 40 > age > 20 and name.startswith("S"):
    print ("Mid level")
else:
    print("Something else")

################################################

## "is" operator checks if 2 objects refer to same instance
arr1=[1,2,3]
arr2=arr1           ## arr1 and arr2 refer to same instance
arr3=[1,2,3]

print("Print arr1 and arr2", arr1 == arr2, arr1 is arr2)
print("Print arr1 and arr3", arr1 == arr3, arr1 is arr3)



################################################

## "not" operator
print(not(age))
print(not(age == 29))