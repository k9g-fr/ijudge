"""fully charged pair YEAHHH"""
def main(text):
    """main eh eh"""
    counter = ""
    unpair = ""
    for i in text:
        if counter.count(i) < 1:
            counter += i
    for j in counter:
        if text.count(j) %2:
            unpair += j
    if not unpair:
        print("fully paired")
    else:
        print(unpair)
main(input())
