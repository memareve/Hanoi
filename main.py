def moveTower(height, fromm, too, withh):
    """Hanoi Towers feature"""
    if height >= 1:
        moveTower(height-1, fromm, withh, too)
        moveDisk(fromm, too)
        moveTower(height-1, withh, too, fromm)


def moveDisk(fp,tp):
    print("moving disk from", fp, "to", tp)


n = int(input('Enter the number of rings: '))
moveTower(n, "A", "B", "C")  # A - 1st kernel B - 2nd kernel C - 3nd kernel

