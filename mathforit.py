"""Math for IT"""
import math


def main():
    """circle"""
    R = float(input())
    print("Area:", f"{math.pi*R**2:.3f}")
    print("Circumference:", f"{2*math.pi*R:.3f}")
main()
