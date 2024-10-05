"""sequence"""
def seq(x):
    """numba 9"""
    for i in range(x,0,-1):
        num = 1
        for j in range(1,x+1*(x-i+1)):
            if j < i:
                print("  ",end =" ")
            else:
                if j > x:
                    num -= 1
                    print(f"{num:02}", end=" ")
                else:
                    print(f"{num:02}", end=" ")
                    if j == x:
                        continue
                    num += 1
        print()
seq(int(input()))
