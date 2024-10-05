"""For"""
def main(x):
    """baller"""
    pos = 1
    for i in x:
        if i=="A":
            if pos == 1:
                pos = 2
            elif pos == 2:
                pos = 1
        elif i=="B":
            if pos == 2:
                pos = 3
            elif pos == 3:
                pos = 2
        elif i=="C":
            if pos == 1:
                pos = 3
            elif pos == 3:
                pos = 1
    print(pos)
main(input())
