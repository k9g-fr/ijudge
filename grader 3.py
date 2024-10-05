"""grade 3"""
def grade(x):
    """average cal"""
    grd = 0
    for _ in range(x):
        y = float(input())
        if 95 <= y <= 100:
            grd += 4
        elif 90 <= y < 95:
            grd += 3.5
        elif 85 <= y < 90:
            grd += 3
        elif 80 <= y < 85:
            grd += 2.5
        elif 75 <= y < 80:
            grd += 2
        elif 70 <= y < 75:
            grd += 1.5
        elif 65 <= y < 70:
            grd += 1
        elif 60 <= y < 65:
            grd += 0.5
    print(f"{grd/x:.2f}")
grade(int(input()))
