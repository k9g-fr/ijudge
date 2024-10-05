"""sequence 1"""
def sequence(x):
    """square"""
    for _ in range(1,x+1):
        for i in range(1,x+1):
            print(f"{i} ", end="")
        print()
sequence(int(input()))
