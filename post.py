"""post"""
def main(env, pac):
    """office"""
    total = 0
    for _ in range(env):
        w_env = float(input())
        if 0 < w_env <= 10:
            total += 16+13
        elif 10 < w_env <= 20:
            total += 18+13
        elif 20 < w_env <= 100:
            total += 23+13
        elif 100 < w_env <= 250:
            total += 28+13
        elif 250 < w_env <= 500:
            total += 33+13
        elif 500 < w_env <= 1000:
            total += 48+13
        elif 1000 < w_env <= 2000:
            total += 68+13
    for _ in range(pac):
        w_pac = float(input())
        if 0 < w_pac <= 500:
            total += 45+15
        elif 500 < w_pac <= 1000:
            total += 55+15
        elif 1000 < w_pac <= 2000:
            total += 70+15
    print(total)
main(int(input()),int(input()))
