import math
# Math é a biblioteca para cálculos matemáticos, math.sqrt é para raiz quadrada e o math.ceil é para arredondar para cima
# Se eu utilizar a forma: from math import sqrt - eu só preciso manter sqrt no código e não preciso referenciar a biblioteca math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
