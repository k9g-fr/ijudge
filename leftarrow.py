"""Left"""
def main(k, n):
    """arrow"""
    for i in range(n):
        print(" " * abs(n // 2 - i) + "*" * k)
main(int(input()),int(input()))
