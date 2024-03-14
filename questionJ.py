def is_subsequence(list1, list2):
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            j += 1
        i += 1
    
    return j == len(list2)


while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))

    if is_subsequence(list1, list2):
        print("Sim")
    else:
        print("Nao")
