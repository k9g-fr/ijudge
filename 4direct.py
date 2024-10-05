"""one direct"""
def main(x):
    """two direct"""
    row1 = ""
    row2 = ""
    row3 = ""
    row4 = ""
    row5 = ""
    for i in x:
        if i == "U":
            row1 += "  *   "
            row2 += " ***  "
            row3 += "* * * "
            row4 += "  *   "
            row5 += "  *   "
        elif i == "D":
            row1 += "  *   "
            row2 += "  *   "
            row3 += "* * * "
            row4 += " ***  "
            row5 += "  *   "
        elif i == "L":
            row1 += "  *   "
            row2 += " *    "
            row3 += "***** "
            row4 += " *    "
            row5 += "  *   "
        elif i == "R":
            row1 += "  *   "
            row2 += "   *  "
            row3 += "***** "
            row4 += "   *  "
            row5 += "  *   "
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)
main(input())
