"""timing"""
def main():
    """tiinniibg"""
    sec = int(input())
    s = sec%60
    minute = sec//60
    m = minute%60
    hour = minute//60
    h = hour%24
    day = hour//24
    if day > 9999 or sec < 0:
        print("ERR_:__:__:__")
    else:
        print(f"{day:04}:{h:02}:{m:02}:{s:02}")
main()