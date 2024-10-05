"""elevator"""
def main(people, lw,):
    """safe or not"""
    total = 0
    Safeornot = False
    for _ in range(people):
        age = int(input().strip())
        weight = float(input().strip())
        total += weight
        if age >= 12:
            Safeornot = True
    if total > lw or (not Safeornot and people > 0):
        print("Not Safe")
    else:
        print("Safe")
main(int(input().strip()),float(input().strip()))
