"""donut"""
def donut(price, buy, free, want):
    """donut"""
    pro = want//(buy+free)
    buy1 = (buy+free)*pro
    price1 = pro*buy*price
    left = want - buy1
    if left >= buy:
        buy1 += buy + free
        price1 += price*buy
    else:
        buy1 += left
        price1 += left*price
    print(price1, buy1)
donut(int(input()),int(input()),int(input()),int(input()))
