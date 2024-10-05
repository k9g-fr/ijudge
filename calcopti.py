"""caclac"""
def calc_count(num):
    """counting"""
    count = 0
    digits = 1
    while True:
        start = 10**(digits - 1)
        end = min(num, 10**digits - 1)
        if start > num:
            break
        count += (end - start + 1) * (digits + 1)
        digits += 1
    return count
def main():
    """main"""
    num = int(input())
    if num == 1:
        print(1)
    else:
        print(calc_count(num))
main()
