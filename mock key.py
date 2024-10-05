"""broken"""
def main(text):
    """keyboard"""
    swap = text.translate(str.maketrans("ioIO", 'oiOI'))
    print(swap)
main(input())
