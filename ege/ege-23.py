"""
1. Прибавь 1
2. Прибавь 3
3. Получи число Фибоначчи по номеру
сколько 6 -> 21
"""
fib = [0]*23
fib[1]=fib[2]=1
for i in range(3,23):
    fib[i] += fib[i-1] + fib[i-2]
M = [0]*30
M[6]=1
for x in range(6,22):
    M[x+1] += M[x]
    M[x+3] += M[x]
    if fib[x]<=21: M[fib[x]] += M[x]
print(M[21])
