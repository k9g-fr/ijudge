"""Paral"""
def main(text):
    """lelelolol eh ehe eh"""
    x = len(text)
    for i in range(1, x+1):
        print(f"{' '*(x-i)}{text[:i]}")
    for i in range(1, x):
        print(f"{text[i:]}")
main(input())
