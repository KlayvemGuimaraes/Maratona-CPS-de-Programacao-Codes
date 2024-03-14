while True:
    a, b, c = map(int, input().split())
     
    if a == 0:
        break

    if c > a // 2:
        a, b, c = map(int, input().split())

    violation = 0

    for _ in range(b):
        input()

    for _ in range(c):
        input()

    if b == 0:
        violation = 2
    elif c == 0:
        violation = 0
    elif c > b:
        violation = a - c * 2
    else:
        violation = a - b * 2

    print(violation)
