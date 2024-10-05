"""run length"""
def main(text):
    """encoding"""
    encoded = ""
    current = text[0]
    count = 1
    for char in text[1:]:
        if char == current:
            count += 1
        else:
            encoded += f"{count}{current}"
            current = char
            count = 1
    encoded += f"{count}{current}"
    print(encoded)
main(input())
