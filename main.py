def moveTower(level, origin_s, goal_s, auxiliary_s):
    """Hanoi Towers function"""
    if level >= 1:
        moveTower(level-1, origin_s, auxiliary_s, goal_s)
        moveDisk(origin_s, goal_s)
        moveTower(level-1, auxiliary_s, goal_s, origin_s)


def moveDisk(from_s,to_s):
    """Print function"""
    print("shift disk from", from_s, "to", to_s)


def main():
    """Init function"""
    n = int(input('Enter the number of disks: '))
    if n < 1:
        print('ERROR')
        main()
    moveTower(n, "A", "B", "C")  # A - 1st stick B - 2nd stick C - 3rd stick (auxiliary at the beginning)


main()
