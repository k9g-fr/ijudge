"""Rule"""
def main(snack):
    """of tree"""
    b_val = None
    b_price = None
    b_size = None
    for _ in range(snack):
        price = float(input())
        size = float(input())
        val = size / price
        if b_val is None or val > b_val or (val == b_val and price < b_price):
            b_val = val
            b_price = price
            b_size = size
    print(f"{b_price:.2f} {b_size:.2f}")
main(int(input()))
