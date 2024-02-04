nums=[2,3,5,7]

## for loop
for num in nums:            ## iterates through array
    print(num)

print("----------")

for num in range(10):       ## range gives an iterator from 0 to 9 in this case
    print(num)


print("----------")

for num in range(3, 10):    ## iterates from 3 to 9
    print(num)

print("----------")

for num in range(4, 10, 2):         ## will start from 4, jump numbers by 2 and will print numbers till 9
    print(num)

########################################
## "else" block for loops executes if loop condition fails
## if break is executed, then else is skipped