"""Bubble"""
def main():
    """main"""
    text = input() + "||||"
    i = 0
    pos = 0
    while text[i] != "|":
        if text[i] == "^":
            if text[i+1] != " ":
                i += 1
                pos += 1
            else:
                print("IMPOSSIBLE")
                print(text.find("|") - i)
                return
        elif text[i] == "o":
            if text[i+1] != " ":
                i += 1
                pos += 1
            else:
                if text[i-1] == "O" and text[i+1:i+4] not in "   ":
                    i -= 1
                else:
                    print("IMPOSSIBLE")
                    print(text.find("|") - i)
                    return
        elif text[i] == "O" and text[i+1:i+4] not in "   ":
            for j in range(3, 0, -1):
                if text[i+j] not in " ":
                    i += j
                    pos += 1
                    break
        else :
            print("IMPOSSIBLE")
            print(text.find("|") - i)
            return
    print("POSSIBLE")
    print(pos)
main()
