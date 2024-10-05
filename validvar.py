"""valid"""
def main(num):
    """var"""
    reserved=("and","or","not","if","elif","else","for","while","break","as","def","lambda","pass",
    "return","True","False","try","with","assert","class","continue","del","except","finally","from"
    ,"global","import","in","is","None","nonlocal","raise","yield","async","await")
    for _ in range(num):
        name = input()
        if not name.isidentifier() or name in reserved:
            print("Invalid")
        else:
            print("Valid")
main(int(input()))
