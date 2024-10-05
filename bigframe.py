"""big frame"""
def main():
    """main eh eh"""
    text = [input().rstrip() for _ in range(5)]
    max_long = max(len(line) for line in text)
    frame = "*" * (max_long+4)
    print(frame)
    for line in text:
        print(f"* {line:<{max_long}} *")
    print(frame)
main()
