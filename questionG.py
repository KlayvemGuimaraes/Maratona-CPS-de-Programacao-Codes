while True:
    value = int(input())
    n = 1

    if value == -1:
        break

    if value == 0:
        s = 4
    else:
        s = value * (4 * value) + (value * 4) + 1

    print(f'Caso {n}')
    print(s)
    print()

    n += 1