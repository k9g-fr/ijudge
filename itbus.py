"""it business"""
def main(bank, inme):
    """main bruh eh"""
    error = 0
    while True:
        action = input()
        if action == 'end':
            break
        money = float(action[2:])
        if action[0] == "D": #ฝาก
            if inme >= money:
                inme -= money
                bank += money
                error = 0
            else:
                error += 1
        elif action[0] == "W": #ถอน
            if bank >= money:
                bank -= money
                inme += money
                error = 0
            else:
                error += 1
        if error >= 3:
            break
    print(f"{bank:.2f}")
    print(f"{inme:.2f}")
main(float(input()),float(input()))
