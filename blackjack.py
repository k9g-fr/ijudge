"""blackjack"""
def main(num):
    """score calc"""
    score = 0
    ace = 0
    for _ in range(num):
        card = input()
        if card == "A":
            score += 11
            ace += 1
        elif card in ('J','Q','K'):
            score += 10
        else:
            score += int(card)
    while score > 21 and ace > 0:
        score -= 10
        ace -= 1
    print(score)
main(int(input()))
