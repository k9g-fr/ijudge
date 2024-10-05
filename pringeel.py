"""pringle"""
def main(top_cover, piece, bottom_cover, finger):
    """main eh eh eh"""
    chip = piece[:min(len(top_cover),finger)].count(")")
    piece = " " * min(len(top_cover),finger) + piece[min(len(top_cover),finger):]
    print(chip)
    if piece.count(")") > 0:
        print("There are still some left.")
    else:
        print("None.")
    print(top_cover)
    print(piece)
    print(bottom_cover)
main(str(input()),str(input()),str(input()),int(input()))
