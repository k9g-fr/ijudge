"""century"""
def main(year):
    """main bruh"""
    for _ in range(year):
        text = input().strip()
        if text.startswith("B.E."):
            year = int(text[5:])
            if year < 543:
                print("ERROR")
            else:
                toAD = year-543
                cent = (toAD+99) // 100
                print(cent)
        elif text.startswith("A.D."):
            year = int(text[5:])
            cent = (year+99)//100
            print(cent)
        else:
            print("ERROR")
main(int(input()))
