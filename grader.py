"""grader"""
def grader(x, y):
    """machine"""
    Sum = 0
    output1 = "pass : "
    if x%2 or x == 1:
        x = x+1
    for i in range(x,y+1,2):
        output1 += f"{i} "
        Sum += i
    return output1, Sum
test,Sum = grader(int(input()),int(input()))
print(test)
print(f"Sum : {Sum}")
