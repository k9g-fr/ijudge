"""amefuri"""
def main(hr, weather, wet=8):
    """main eh eh eh"""
    for log in weather:
        if log in "cnw":
            if 6 <= hr < 18:
                wet = max(0, wet-(0.5*(log =="c"))-(1*(log =="n"))-(1.5*(log =="w")))
            else:
                wet = max(0, wet-(0.25*(log =="c"))-(0.5*(log =="n")) -(0.75*(log =="w")))
        elif log in "rs":
            wet = min(16, wet + (2*(log == "r")) +(3*(log == "s")))
        else:
            return print("Lost")
        hr = (hr + 1)*(hr + 1 != 24)
        if not wet:
            return print("Dry")
    return print(f"Still Wet (Wet Level: {wet:.2f})")
main(int(input()), input().lower())
