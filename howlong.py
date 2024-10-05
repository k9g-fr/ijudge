"""how long"""
def main(num):
    """count"""
    Count = 0
    if int(num) < 0:
        Count = -1
        for _ in num:
            Count += 1
        print(Count)
    else:
        for _ in num:
            Count += 1
        print(Count)
main(str(input()))
