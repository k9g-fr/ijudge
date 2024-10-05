"""weight"""
def main():
    """station"""
    avg = float(input())
    w1 = float(input())
    w2 = float(input())
    w3 = float(input())
    w4 = (avg*4)-w1-w2-w3
    unbalanced = avg / 2
    if w1+w2+w3+w4 > 15000:
        print("Overweight")
        return
    if (abs(w1 - avg) > unbalanced or
        abs(w2 - avg) > unbalanced or
        abs(w3 - avg) > unbalanced or
        abs(w4 - avg) > unbalanced) :
        print("Unbalance")
        return
    print(f"Pass {w4:.2f}")
main()
