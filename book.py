"""Books"""
def main(n, k, x, y):
    """main"""
    page, book, day, um = k, 0, 0, False
    for _ in range(10**8):
        if book >= n:
            break
        while page > 0:
            today = k *((x + day)/(y + day))
            if today % 1:
                today += 1 -(today % 1)
            page -= today
            day += 1
        book += 1
        page = k
        if today == k:
            um = True
            break
    if um:
        day += n - book
    print(day)
main(int(input()),int(input()),int(input()),int(input()))
