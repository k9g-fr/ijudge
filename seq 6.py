"""sequence 6"""
def sequence(x):
    """stair"""
    for col in range(1,x+1):
        for row in range(1,x+1):
            if row <= col:
                print(f"{row} ",end = "")
            else:
                print("", end ="")
        print()
sequence(int(input()))
