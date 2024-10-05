"""number"""
def main(text):
    """messagei"""
    translated = ""
    x = text.replace("12", "R")
    x = x.replace("13", "B")
    x = x.replace("0", "O")
    x = x.replace("1", "I")
    x = x.replace("3", "E")
    x = x.replace("5", "S")
    x = x.replace("4", "A")
    for i in x:
        if i.isnumeric():
            translated += ""
        else:
            translated += i
    print(translated.upper())
main(str(input()))
