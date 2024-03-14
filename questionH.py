while True:
    values = list(map(int, input().split()))
    v = values[0]

    if v == 0:
        break

    quantities = values[1:]

    count = 0
    for quantity in quantities:
        if v >= quantity:
            count += 1
            v -= quantity
        else:
            break

    print(count)
