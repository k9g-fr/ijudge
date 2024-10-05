"""diginity"""
def main():
    """frfr eh eh"""
    num = input()
    while int(num):
        total = 0
        while len(num) > 1:
            total = 0
            for i in num:
                total += int(i)
            num = str(total)
        print(num)
        num = input()
main()
