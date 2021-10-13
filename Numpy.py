import numpy as np

#criação de arrays e numpy.random

#álgebra linear para python
#construção de todas as outras bibliotecas de análise de dados 
#principais métodos escritos em C

#arrays -> vetores e matrizes

#kernel = núcleo, integração entre as aplicações e o processamento dos dados

#criar um array de numpy
l = [1,2,3]
np.array(l)

m =[[1,2,3],[4,5,6],[7,8,9]]
np.array(m)

#arranjo de números (start, stop[não incluso], step)
np.arange(1,10,1)

#criar matriz de zeros
np.zeros(3)

np.zeros((5,5)) #matriz bidimensional

#criar matriz de uns 
np.ones(3)

np.ones((5,5))

#matriz identidade
np.eye(4)

#linspace é parecido com o arange, porém os parâmetros são start, stop e quantos números devem ter entre eles
np.linspace(0, 10, 20)

#sub biblioteca random
#gerar 5 números aleatórios
np.random.rand(5) 

#gerar matriz de números aleatórios
np.random.rand(4,3) #sim, não é uma tupla, apenas dois parâmetros

#distribuição gaussiana
np.random.randn(4)

#números aleatórios inteiros
#start, stop não incluso, quantidade de números desejados
np.random.randint(0,100,20) #20 números inteiros aleatórios esntre 0 e 100

#reshape
arr = np.random.rand(5,5)

#passar de 5x5 para 1x25
arr.reshape(25) #==> não foi mudado na memória, necessida reassociação 

arr = arr.reshape(25) #==> reassociação

#função max detecta o maior valor no array
arr.max()
#função min detecta o menor valor no array
arr.min()

#indice do maior numero no array
arr.argmax()
#indice do menor numero no array
arr.min()

#indexação e fatiamento de arrays

arr = np.arange(0,30,3)

#arr[índice para pegar um elemento específico]
#arr[índiceInic : índiceFim(não incluso)] ==> puxar varios elementos de uma vez
#arr[: índiceFim(não incluso)] ==> todos os números anteriores ao índiceFim
#arr[ÍndiceInic :] ==> todos os números anteriores ao índiceFim

#podem ser usados para modificar também:
#arr[2:] == 100 ==> faz com que todos os elementos com índice maior que 2 sejam 100

arr = np.arange(50).reshape(5,10) #cria um arranjo de 50 números e distrinui em uma matriz 5x10

arr[:3][:] #==> pega linhas 0,1,2 e todas as colunas, "fatia". A mesma coisa de escrever arr[:3]

arr[:][:3] #==> pega todas as linhas e colunas 0,1,2

arr2 = arr[:2] #==> ele não copia, apenas aponta

#para evitar podemos usar o método de cópia
arr2 = arr[:2].copy()

#fatiação por partes
arr[1:4, 5:] #linhas 1,2,3 e colunas da 5 para frente

arr > 50 #==> retorna um array de verdadeiros ou falsos

bool = arr > 50

arr[bool] #==> retorna um array de elementos que satisfazem a condicional

#operações com arrays

arr = np.arange(0,16)

#soma índice por índice, portanto devem ser do mesmo tamanho
arr = arr + 2

#subtração
arr = arr - 2

#multiplicação
arr = arr*2

#divisão
arr = arr/2 #==> quando encontra um valor NaN, uma mensagem de alerta é disparada

#exponenciação
arr = arr**3

#raíz
arr = np.sqrt(arr)

#exponencial
arr = np.exp(arr)

#média do array
arr = np.mean(arr)

#desvpad
arr = np.std(arr)

#sen
arr = np.sin(arr)

#cos
arr = np.cos(arr)

#arr.max() == np.max(arr)

#exercícios

