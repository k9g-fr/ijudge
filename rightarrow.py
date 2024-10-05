"""Right Arrow"""
def main(k, n):
    """right arrow eiei"""
    for i in range(n // 2 + 1):
        print(" " * abs(i) + "*" * k)
    for i in range(n // 2):
        print(" " * abs(n // 2 - i - 1) +  "*" * k)
main(int(input()),int(input()))
