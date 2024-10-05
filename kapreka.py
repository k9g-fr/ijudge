"""kapreka"""
def ascend(num): #น้อยไปมาก
    """ascendi"""
    for _ in range(len(num)):
        for j in range(len(num)-1):
            if num[j]>num[j+1]:
                num = num[:j]+num[j+1]+num[j]+num[j+2:]
    return ''.join(num)

def descend(num): #มากไปน้อย
    """descendi"""
    for _ in range(len(num)):
        for j in range(len(num)-1):
            if num[j]<num[j+1]:
                num = num[:j]+num[j+1]+num[j]+num[j+2:]
    return ''.join(num)
def main(x):
    """main"""
    count = 0
    while x != "6174":
        y = descend(x.zfill(4))
        z = ascend(x.zfill(4))
        x = str(int(y) - int(z)).zfill(4)
        count += 1
    print(count)
main(str(input()))
