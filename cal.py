"""calculator"""
def cal(num):
    """calculate"""
    if num == 1:
        return "1"
    result = ""
    for i in range(1,num+1):
        result += f"{i}+"
    return result
output = cal(int(input()))
print(len(output))
