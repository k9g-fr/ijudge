"""Ball"""
def main(height):
    """bouncy"""
    count = -1
    while height >= 0.01:
        height *= 0.60
        count += 1
    print(count)
main(float(input()))
