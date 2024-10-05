"""largest num"""
def main(a,b,c):
    """main"""
    A = str(a)
    B = str(b)
    C = str(c)
    if A + B < B + A:
        A,B = B,A
    if A + C < C + A:
        A,C = C,A
    if B + C < C + B:
        B,C = C,B
    print(int(A+B+C))
main(int(input()),int(input()),int(input()))
