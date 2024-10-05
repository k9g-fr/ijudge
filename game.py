"""game"""
def main(a,b):
    """main"""
    scoreA = a%3
    scoreB = b%3
    if scoreA == scoreB:
        print(scoreA)
    else:
        print("Error")
main(int(input()),int(input()))
