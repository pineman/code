save = [1, 1, 2]
def fact_m(i):
    if len(save) < i+1:
        for j in range(len(save), i+1): # números que faltam calcular
            save.append(save[-1]*j)
    return save[i]

print(fact_m(10))

def fact_r(i):
    if i == 1:
        return 1
    else:
        return fact_r(i-1)*i

print(fact_r(10))

def fact_i(i):
    p = 1
    for j in range(1, i+1):
       p *= j
    return p

print(fact_i(10))
