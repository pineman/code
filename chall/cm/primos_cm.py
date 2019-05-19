def ex_primos(ini, qtd):
    primos = []
    while qtd > 0:
        for x in range(2, ini):
            if ini % x == 0:
                break
        else:
            # primo
            primos.append(ini)
            qtd -= 1
        ini += 1
    return primos

print ex_primos(7869, 12)
