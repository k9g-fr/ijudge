"""heron"""
def heron(a, b, c):
    """of Alex"""
    a = float(a)
    b = float(b)
    c = float(c)
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print(f"{area:.3f}")
heron(float(input()),float(input()),float(input()))
