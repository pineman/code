#!/bin/bash
echo -n 'procedural solution: '
python -m timeit -n 10000 -c "$(cat one.py)" | grep loops
echo -n 'one liner solution: '
python -m timeit -n 10000 -c "$(cat one_oneliner.py)" | grep loops
echo 'Uma potencial explicação para o oneliner ser mais rápido, embora passe mais vezes pelo input por causa dos .split()s, é que o oneliner passa mais tempo em C e portanto é 'menos python'. A versão grande tem mais código python, if: dentro de for (e append talvez).'
