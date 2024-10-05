"""triangle"""
def pytha(a, b, c):
    """pythagorus"""
    if a > b and a > c:
        C = a
        B = b
        A = c
    elif b > a and b > c:
        C = b
        B = c
        A = a
    else:
        C = c
        B = b
        A = a
    if abs(C**2 - ((A**2)+(B**2))) <= 0.01:
        print("Yes")
    else:
        print("No")
pytha(float(input()),float(input()),float(input()))
