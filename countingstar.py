"""counting"""
def main(stars):
    """stars"""
    cons = 0
    comet = 0
    shootstar = 0
    i = 0
    while i < len(stars)-1:
        if stars[i:i+2] == "**":
            cons += 1
            i += 2
        elif stars[i:i+2] == "*/":
            shootstar += 1
            i += 2
        elif stars[i:i+2] in ("~*","*~"):
            comet += 1
            i += 2
        else:
            i += 1
    if not cons and not comet and not shootstar:
        print("Tonight is a quiet night.")
    else:
        print("constellation:", cons)
        print("comet:", comet)
        print("shooting star:", shootstar)
main(input())
