"""longer"""
import math as m
def main(r, a, b):
    """circle rec"""
    rec = (2*a)+(2*b)
    cir = 2*m.pi*r
    dif = abs(rec-cir)
    if cir > rec:
        print('Circle is longer')
    elif cir < rec:
        print('Rectangle is longer')
    else:
        print('Equal')
    print(f"{dif:.5f}")
main(float(input()),float(input()),float(input()))
