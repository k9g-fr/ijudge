"""distance"""
import math

def main():
    """main main"""
    q1 = float(input())
    q2 = float(input())
    p1 = float(input())
    p2 = float(input())
    ED = math.sqrt((q1-p1)**2 + (q2-p2)**2)
    print(ED)
main()
