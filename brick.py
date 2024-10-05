"""brick"""
def bridge(a, b, goal):
    """bridge"""
    bneed = goal//5
    buse = min(bneed, b)
    ause = goal - buse*5
    if ause > a:
        print(-1)
    else:
        print(ause)
bridge(int(input()),int(input()),int(input()))
