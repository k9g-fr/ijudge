"""stampy"""
def main(n, a, b, c, d):
    """mainn"""
    stamp = 0
    bill = 0
    for _ in range(n):
        price = int(input())
        if stamp >= c:
            discount = price // d
            if price % d > 0:
                discount += 1
            tmp = stamp // c
            can = min(discount, tmp)
            if can > 0:
                price -= can * d
                price = max(price, 0)
                stamp -= can * c
        if price >= a:
            stamp += (price//a)*b
        bill += price
    print(bill)
    print(stamp)
main(int(input()),int(input()),int(input()),int(input()),int(input()))
