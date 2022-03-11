"""
Определите наименьшее натуральное число A, такое что выражение
(X & 56 ≠ 0) → ((X & 48 = 0) → (X & A ≠ 0))
"""
f = lambda A: all([((x&56!=0) <= ((x&48==0) <= (x&A!=0))) for x in range(1,100)]) #8
for a in range(1,1000):
    if f(a):
        print(a)
        break
    
"""
Для какого наибольшего натурального числа А формула
  (¬ДЕЛ(x,А) ∧ ДЕЛ(x,6)) → ¬ДЕЛ(x,3)
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?
"""
f1 = lambda A: all([ ((x%A!=0 and x%6==0)<=(x%3!=0)) for x in range(1,100) ]) #6
for a in range(1000,1,-1):
    if f1(a):
        print(a)
        break

"""((x ∈ {1,3,5,7,9,12}) → (x ∈ {3,6,9,12})) ∨ (x ∈ A)
истинно (т. е. принимает значение 1) при любом значении переменной х.
Определите наименьшее возможное значение суммы элементов множества A."""
M1 = {1,3,5,7,9,12}
M2 = {3,6,9,12}
from itertools import combinations
f2 = lambda A: all([((x in M1) <= (x in M2 or x in A)) for x in range(20)])
M = M1|M2
A = set()
for i in range(len(M)+1):
    A |= {x for x in combinations(M,i)}
print(min([sum(x) for x in A if f2(x)]))
#проще решить руками