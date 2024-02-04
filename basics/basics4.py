## functions are declared using def keyword

def fun(N):
    for num in range(1, N+1):
        if(num%2 == 0):
            print(num)
            if(num == N):
                break
    else:
        print("Out of loop")

fun(31)
