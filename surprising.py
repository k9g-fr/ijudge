"""surprising"""
def surprise(total,highest):
    """vote"""
    sec = min(total-highest, highest)
    lowest = total - highest - sec
    if highest - lowest > 2:
        print("Surprising")
    else:
        print("Not surprising")
surprise(float(input()), float(input()))
