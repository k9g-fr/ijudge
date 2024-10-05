"""second"""
def main(k, s, m, h):
    """converter"""
    par_min, second = divmod(k, s)
    par_hr, minute = divmod(par_min, m)
    if par_hr >= h:
        par_hr %= h
    print(f"{int(par_hr)}:{int(minute)}:{int(second)}")
main(int(input()),int(input()),int(input()),int(input()))
