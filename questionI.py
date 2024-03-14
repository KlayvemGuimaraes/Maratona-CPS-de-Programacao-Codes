while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break
    
    stock = []
    for _ in range(m):
        stock.append(list(map(int, input().split())))

    p = int(input())
    orders = [list(map(int, input().split())) for _ in range(p)]

    sales = 0
    for order in orders:
        i, j = order
        if 0 < i <= m and 0 < j <= n:
            if stock[i - 1][j - 1] > 0:
                stock[i - 1][j - 1] -= 1
                sales += 1

    print(sales)
