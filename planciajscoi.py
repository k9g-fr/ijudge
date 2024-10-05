"""Planasdnasd"""
def main(s0rt,num1,num2,num3):
    """Sort num"""
    if s0rt == "Ascend": #น้อยไปมาก
        if num1 > num2:
            num1, num2 = num2, num1
        if num1 > num3:
            num1, num3 = num3, num1
        if num2 > num3:
            num2, num3 = num3, num2
    if s0rt == "Descend": #มากไปน้อย
        if num1 < num2:
            num1, num2 = num2, num1
        if num1 < num3:
            num1, num3 = num3, num1
        if num2 < num3:
            num2, num3 = num3, num2
    print(f"{num1:.2f}, {num2:.2f}, {num3:.2f}")
main(str(input()),float(input()),float(input()),float(input()))
