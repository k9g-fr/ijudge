"""diamond"""
def main(num):
    """main"""
    for i in range(num//2+1):
        blank = " "*(num//2-i)
        if not i:
            print(blank + "*")
        elif i == num//2:
            print("*" *num)
        else:
            diamond = "*" + " " *(2*i-1) + "*"
            print(blank + diamond)
    for i in range(num//2-1,-1,-1):
        blank = " "*(num//2-i)
        if not i:
            print(blank + "*")
        else:
            diamond = "*" + " " * (2*i-1) + "*"
            print(blank+diamond)
main(int(input()))
