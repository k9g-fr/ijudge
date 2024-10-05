"""Saint Seiya"""
def main(sec, punch):
    '''หมัดดาวเหนือ'''
    punched = 0
    for i in range(2, sec+1, 2):
        if punched < punch:
            if not i%6:
                punched += 1
            elif not i%2:
                punched += 165
        else:
            punched += (sec+1-i)*12
            break
    print(punched)
main(int(input()), int(input()))
