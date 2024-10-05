"""shorten"""
def main():
    """main"""
    state = "start"
    prev = None
    while True:
        x = int(input())
        if state == "start" and x == -1:
            break
        if state == "wait" and x == -1:
            print("-", prev, sep="", end="")
            break
        if state == "start" and prev is None:
            print(x, end='')
        elif state == 'start' and x-prev == 1:
            state = 'wait'
        elif state == 'start' and x-prev != 1:
            print(',', x, end='')
        elif state == 'wait' and x-prev != 1:
            print("-" + str(prev) + ',', x,end="")
            state = 'start'
        prev = x
main()
