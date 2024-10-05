"""US num baba"""
def main(num):
    """main fr eh eh"""
    if 5 <= num <= 95:
        if not num%10:
            print("Horizontal Major Interstate")
            print(f"I-{num}")
        elif not num%5:
            print("Vertical Major Interstate")
            print(f"I-{num}")
        else:
            print("Others")
    elif 100 <= num <= 999:
        new=num%100
        if 5<= new<= 95:
            if not num//100%2 and (not new%5 or not new%10):
                print("Even Minor Interstate")
                print(f"I-{new}")
            elif num//100%2 and (not new%5 or not new%10):
                print("Odd Minor Interstate")
                print(f"I-{new}")
            else:
                print("Others")
        else:
            print("Others")
    else:
        print("Others")
main(int(input()))
