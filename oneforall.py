"""one for all"""
def main(num):
    """ahh hero :skull:"""
    count = 0
    allhero = ""
    for _ in range(num):
        hero = input()
        count += 1
        if count == num:
            allhero += hero + "_" + str(num)
        elif count%2:
            allhero += hero + "*"*count
        elif not count%2:
            allhero += hero + "-"*count
    print(allhero)
main(int(input()))
