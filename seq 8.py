"""Sequence"""
def seq(x):
    """numa 8"""
    for i in range(x):
        print(" " * (3 * (x-i-1)), end="")
        for j in range(i+1):
            if i >= j:
                print(f"{j+1:02}", end=" ")
            else:
                print("", end="")
        print()
seq(int(input()))
