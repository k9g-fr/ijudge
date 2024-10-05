"""MAC"""
def main(ip):
    """maggy bruh"""
    if len(ip) != 17 and len(ip) != 14:
        return "ERROR"
    parts = ip.split('-') if '-' in ip else ip.split(':') if ':' in ip else ip.split('.')
    if len(parts) == 6 and all(len(part) == 2 for part in parts):
        if '-' in ip:
            return "VALID 1" if all(c in '0123456789ABCDEFabcdef' for c in ip.replace('-', '')) \
                else "ERROR"
        if ':' in ip:
            return "VALID 2" if all(c in '0123456789ABCDEFabcdef' for c in ip.replace(':', '')) \
                else "ERROR"
    elif len(parts) == 3 and all(len(part) == 4 for part in parts):
        return "VALID 3" if all(c in '0123456789ABCDEFabcdef' for c in ip.replace('.', '')) \
            else "ERROR"
    return "ERROR"
mac_address = input().strip()
RESULT = main(mac_address)
print(RESULT)
