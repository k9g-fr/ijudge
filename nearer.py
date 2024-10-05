"""nearer"""
def ice():
    """ice cream"""
    alice = int(input())
    bob = int(input())
    icecream = int(input())
    distance = 0
    if abs(icecream-alice) < abs(icecream-bob):
        distance = abs(icecream-alice)
        print("Alice", distance)
    elif abs(icecream-alice) > abs(icecream-bob):
        distance = abs(icecream-bob)
        print("Bob", distance)
    else:
        distance = abs(icecream-bob)
        print("Sundaes", distance)
ice()
