"""run length"""
def main(text):
    """decoding eh eh eh"""
    decoded = ""
    count = 0
    for i in text:
        if i.isdigit():
            count = count * 10 + int(i)
        else:
            decoded += i * count
            count = 0
    print(decoded)
main(input())
