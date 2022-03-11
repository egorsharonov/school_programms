"""
Укажите наибольшее из таких чисел x,
при вводе которых алгоритм печатает сначала 3, а потом 120.
  x = int(input())
  L = 0; M = 1
  while x > 0:
    L = L + 1
    M = M*(x % 8)
    x = x // 8
  print(L, M)
"""
for y in range(1000,1,-1): # ~ 8*8*8
    x = y
    L = 0; M = 1
    while x > 0:
        L = L + 1
        M = M*(x % 8)
        x = x // 8
    if L==3 and M==120:
        print(y)
        break
