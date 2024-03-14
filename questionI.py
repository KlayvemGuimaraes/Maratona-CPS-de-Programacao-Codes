while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0: break
    
    estoque = []
    for _ in range(m):
        estoque.append([int(x) for x in input().split()])

    p = int(input())
    pedidos = []
    for _ in range(p):
        pedidos.append(list(map(int, input().split())))

    vendas = 0
    for pedido in pedidos:
        i, j = pedido
        if estoque[i - 1][j - 1] > 0:
            estoque[i - 1][j - 1] -= 1
            vendas += 1

    print(vendas)