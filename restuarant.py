"""restaurant"""
def main(a,b,c,d):
    """main"""
    pro1 = a - (a*c/100)
    pro2 = (a + d) - ((a + d)*c)/100
    if a == b:
        if a == b and not d:
            print("Yes")
        elif pro1 == pro2:
            print("Yes")
        elif pro1 > pro2:
            print(f"Yes {abs(pro1 - pro2):.3f}")
        elif pro1 < pro2:
            print(f"No {abs(pro2 - pro1):.3f}")
    elif a + d >= b:
        if a == pro2:
            print("Yes")
        elif a > pro2:
            print(f"Yes {abs(a - pro2)  :.3f}")
        else:
            print(f"No {abs(a - pro2):.3f}")
    else:
        print("Yes")
main(float(input()),float(input()),float(input()),float(input()))
