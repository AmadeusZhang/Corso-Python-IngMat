"""
Created on Tue Mar 22 18:10:35 2022

@author: zhzj

Si caratterizzi sinteticamente la serie di numeri stampati da numeri (in funzione di n)

"""

n = int(input("Inserire un numero: "))
i = 2

while i <= n :
    k = 0               # k is write-only, can't be read
    j = 2
    
    while i%j != 0 :
        k = k + 1
        j = j + 1
        
    if j != i :
        k = k - 1
        
    else :
        print(i)
        
    i = i + 1
