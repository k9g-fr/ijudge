"""Lotto"""
def main():
    """main"""
    no1 = input()
    end2 = input()
    front1 = input()
    front2 = input()
    end31 = input()
    end32 = input()
    lotto = input()
    money = 0
    near1up, near1down = int(no1) + 1, int(no1) - 1
    near1up -= 1000000 if near1up > 999999 else 0
    near1down += 1000000 if near1down < 0 else 0
    near1up, near1down = f"{near1up:>06}", f"{near1down:>06}"
    if lotto == no1:
        money += 6000000
    if lotto == near1up:
        money += 100000
    if lotto == near1down:
        money += 100000
    if lotto[-2:] == end2:
        money += 2000
    if lotto[:3] == front1:
        money += 4000
    if lotto[:3] == front2:
        money += 4000
    if lotto[-3:] == end31:
        money += 4000
    if lotto[-3:] == end32:
        money += 4000
    print(money)
main()