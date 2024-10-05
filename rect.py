"""rectangle"""
H = int(input())
W = int(input())
H = abs(H)
W = abs(W)

def rspace():
    """RSPACE"""
    print(H*W)

def circum():
    """Circum"""
    print((H*2)+(W*2))

rspace()
circum()
