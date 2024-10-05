"""sequence"""
def seq(x):
    """numba 12"""
    for i in range(-x+1,x):
        for j in range(-x+1,x):
            ans = x-abs(abs(i)-abs(j))
            print(f"{ans:02}" ,end =" ")
        print()
seq(int(input()))
