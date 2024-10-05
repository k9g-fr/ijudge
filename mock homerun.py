"""baseball"""
def main(n, distance):
    """homerun!"""
    Count = 0
    for _ in range(n):
        field = float(input())
        if distance > field:
            Count += 1
    print(Count)
main(int(input()),float(input()))
