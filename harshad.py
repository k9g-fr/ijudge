"""harshad"""
def main():
    """harshallal eh eh"""
    for _ in range(10):
        harshal = input()
        harshad = abs(int(harshal))
        divide = sum(int(i) for i in str(harshad))
        if not divide:
            print("No")
        elif not harshad%divide:
            print("Yes")
        else:
            print("No")
main()
