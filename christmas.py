"""ChristmasTree"""
def main(leaf, stem):
    """main"""
    num = 1
    x = ""
    for i in range(leaf):
        for j in range(1, leaf - i):
            j = j * 1
            x += " "
        for _ in range(i + num):
            _ = _ * 1
            x += "*"
        print(x)
        length = len(x)
        x = ""
        num += 1
    for i in range(stem):
        print(("-" * 3).center(length))
main(int(input()),int(input()))
