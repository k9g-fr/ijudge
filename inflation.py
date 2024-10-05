'''Inflation'''
def main(money, year):
    '''main'''
    for _ in range(year):
        money += money*381//10000
    print(f"{money//100}.{money%100:>02}")
main(int(float(input())*100), int(input()))
