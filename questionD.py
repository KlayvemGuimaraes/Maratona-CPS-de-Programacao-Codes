def verificar(palavra1, palavra2):
    tamanho_menor = min(len(palavra1), len(palavra2))
    for i in range(tamanho_menor):
        if palavra1[i] != palavra2[i]:
            return i
    return tamanho_menor

def main():
    while True:
        condicao1 = input()
        if condicao1 == "0":
            break

        palavra1 = input()
        condicao2 = input()
        palavra2 = input()

        numeros = verificar(palavra1, palavra2)
        print(numeros)

if __name__ == "__main__":
    main()
