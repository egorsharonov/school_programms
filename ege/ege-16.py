def F(n):
    print( '*' )
    if n > 0:
      F(n-2)
      F(n-2)
      F(n // 2)
#F(6)



def F1( n ):
    print( '*' )
    if n > 0: G(n - 1)
    
def G( n ):
    print( '*' )
    if n > 1:
        F1(n - 2)
#F1(13)


"""
 F(0) = 1, F(1) = 1
  F(n) = F(n-1)+2*F(n-2), при n > 1
Чему равно значение функции F(6)?
"""
def F2(n):
    if n<=1: return n
    return F2(n-1)+2*F2(n-2)
print(F2(6))
