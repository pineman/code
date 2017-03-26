"""
EULER 7
http://projecteuler.net/problem=7
---------------------------------
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

primos = [2]

for n in range(3, 2000000, 2):
# Smart Rodrigo
    roof = n**(1/2)
    for prime in primos:
        if prime > roof:
            primos.append(n)
            break
 
        if n % prime == 0:
            break

    if len(primos) > 10005:
        break
print(primos[10000])
# Explanation
"""
então 'roof' é o número a partir do qual tu sabes q não há nenhum número que 
divida o teu 'n' 

depois, tu sabes q o primeiro número a dividir por inteiro um 
número composto X tem de ser primo

logo, basta tentares dividir o teu X por 
números primos... por isso é que fazes "for prime in primos"

depois se o número "prime" que estiveres a usar já tiver passado o "roof", 
então é porque o X não foi dividido antes e já é primo, prq para cima de "roof" 
não há nenhum primo que o divida
"""




# Dumb Pinheiro
"""
for n in range(1000000000):
    for x in range(2, int((n**(1/2)))+1, 1):
        if n % x == 0:
            break

    else:
        primos.append(n)
        if len(primos) > 10005:
            break
"""
