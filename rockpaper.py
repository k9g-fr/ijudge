"""Rock"""
def main(rps):
    """Paperscissor"""
    scoreA = 0
    scoreB = 0
    for i in range(0,len(rps),2):
        Rnd = rps[i:i+2]
        if Rnd == "RP":
            scoreB += 1
        elif Rnd == "SP":
            scoreA += 1
        elif Rnd == "PR":
            scoreA += 1
        elif Rnd == "SR":
            scoreB += 1
        elif Rnd == "PS":
            scoreB += 1
        elif Rnd == "RS":
            scoreA += 1
    if scoreA > scoreB:
        print(f"A win {scoreA}-{scoreB}")
    elif scoreA < scoreB:
        print(f"B win {scoreB}-{scoreA}")
    else:
        print(f"DRAW {scoreA}")
main(input())
