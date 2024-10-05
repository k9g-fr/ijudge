"""Solar syssysteem"""
def find_hot(left, right):
    """who's hot"""
    hot = ""
    left, right = str(left), str(right)
    loop = -len(left)
    if loop == -2:
        loop = -3
    for i in range(-2, loop, -1):
        if left[i] == " ":
            break
        hot += left[i]
    hot = hot[::-1]
    if right.count(" ")== 1:
        hot += " "+right[1:]
    else:
        hot += " "+right[1:right.find(" ", 1)]
    return hot


def find_cool(left, right):
    """who's cool"""
    left, right = str(left), str(right)
    cold = ""
    cold2 = ""
    if left.count(" ") < right.count(" "):
        for i in range(-2, -len(right), -1):
            if right[i] == " ":
                break
            cold += right[i]
        cold = cold[::-1]
    elif left.count(" ") > right.count(" "):
        cold += left[1:left.find(" ", 1)]
    else:
        cold += left[1:left.find(" ", 1)] + " "
        for i in range(-2, -len(right), -1):
            if right[i] == " ":
                break
            cold2 += right[i]
        cold2 = cold2[::-1]
        cold += cold2
    return cold


def hot_and_cold_murasaki():
    """Man not hot"""
    text = input()
    hot = ""
    cold = ""
    space = text.count(" ")
    text = " " + text + " "
    left = text[:text.find(" Sun ")+1]
    right = text[text.find(" Sun ")+4:]
    if space == 1:
        hot += text.replace("Sun", "").replace(" ", "")
        cold += text.replace("Sun", "").replace(" ", "")
    elif text.startswith(" Sun "):
        hot += text[5:text.find(" ", 5)]
        for i in range(-2, -len(text), -1):
            if text[i] == " ":
                break
            cold += text[i]
        cold = cold[::-1]
    elif text.endswith(" nuS "):
        for i in range(-6, -len(text), -1):
            if text[i] == " ":
                break
            hot += text[i]
        hot = hot[::-1]
        cold += text[1:text.find(" ", 1)]
    else:
        hot += find_hot(left, right)
        cold += find_cool(left, right)
    print(f"Hot: {hot}")
    print(f"Cool: {cold}")
if __name__ == "__main__":
    hot_and_cold_murasaki()
