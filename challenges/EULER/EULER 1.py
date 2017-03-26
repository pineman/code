"""
EULER 1
http://projecteuler.net/problem=1
------------------------------------
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

#1 Primeiro - Almiro

soma3 = 0
n = 0
while n <= 1000:
    if n % 3 == 0 or n % 5 == 0:
        soma3 += n
    n += 1
print(soma3)


#2 Segundo - Almiro

soma4 = 0
for n in range(0, 1000, 1):
    if n % 3 == 0 or n % 5 == 0:
        soma4 += n
    n += 1
    
print(soma4)


#3 Lista - Pinheiro

n= 0
list = [ ]
for n in range(0, 1000, 1):
    if n % 3 == 0 or n % 5 == 0:
        list.append(n)
    
n += 1

soma = sum(list)
print(soma)


#4 Função + Lista - Pinheiro

lista = [ ]

def num(x):
    for n in range(0, x, 1):
        if n % 3 == 0 or n % 5 == 0:
            lista.append(n)
            
num(1000)
print(sum(lista))


#5 Almiro

def numa(x):
  soma2 = 0
  for n in range(0,x,1):
   if(n%3==0 or n%5==0):
      soma2+=n
  return soma2

print(numa(1000))



#6 Tito

numbers = [x for x in range(1,1000) if x % 5 == 0 or x % 3 == 0]
print (sum(numbers))
