"""halal"""
def halal(text, text1):
    """halel lul ya"""
    count = 0
    for i, _ in enumerate(text):
        if text[i] != text1[i]:
            count += 1
    print(count)
halal(str(input()),str(input()))
