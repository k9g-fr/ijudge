"""Parity"""
def main(num, evod):
    """two bit"""
    nub = 0
    for i in num:
        if i == "1":
            nub+=1
    if evod == "Even":
        if not nub % 2:
            print(num + "0")
        else:
            print(num + "1")
    elif evod == "Odd":
        if not nub % 2:
            print(num + "1")
        else:
            print(num + "0")
main(str(input()), str(input()))
