"""Ping"""
def find_ip(x):
    """Find IP address"""
    stop = x.find("with") - 2
    start, var = stop, x[stop]
    while not var.isspace():
        start -= 1
        var = x[start]
    return x[start:stop + 1].replace("[", "").replace("]", "").strip()
def find_time(x):
    """Find reply time"""
    if x.find("time<1") != -1:
        return 0
    if x.find("time=") != -1:
        start = x.find("time=") +5
        stop, var = start, x[start]
        while var != "s":
            stop += 1
            var = x[stop]
        return int(x[start:stop +1].replace("m", "").replace("s", "").strip())
    return None
def get_ping(give, get):
    """Get the ping value"""
    give, get = 4, 0
    line = [input(), input(), input(), input(), input()]
    time = [None, None, None, None]
    ip_address = find_ip(line[0])
    for i in range(1, 5):
        x = find_time(line[i])
        time[i-1] = x
        get += 1 if x is not None else 0
    print(f"Ping statistics for {ip_address}:")
    if not get:
        print("    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),")
    else:
        lowest = time[0] if time[0] is not None else time[1] if time[1] is not None else \
                        time[2] if time[2] is not None else time[3]
        highest = lowest
        ping_avg = 0
        for i in range(4):
            if str(time[i]).isnumeric():
                lowest = time[i] if lowest > time[i] else lowest
                highest = time[i] if highest < time[i] else highest
                ping_avg += time[i]
        print(f"    Packets: Sent = 4, Received = {get}, \
Lost = {give-get} ({int((give-get)/give*100)}% loss),")
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {lowest}ms, Maximum = {highest}ms, \
Average = {int(ping_avg/get)}ms")
get_ping(input(), input())
