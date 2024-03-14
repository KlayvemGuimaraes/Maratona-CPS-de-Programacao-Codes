def verificar(p1, p2):

  tam_menor = min(len(p1), len(p2))
  for i in range(tam_menor):
    if p1[i] != p2[i]:
      return i
  return tam_menor


while True:
    c1 = input()
    if(c1 == "0"): break

    p1 = input()
    c2 = input()
    p2 = input()

    numeros = verificar(p1, p2)
    print(numeros)
