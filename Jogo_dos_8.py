import random
from collections import deque
from copy import deepcopy
from operator import attrgetter
import math

class Estado():
    def __init__(self, matriz, f, g, h, pai):
        self.__matriz = matriz
        self.__f = f
        self.__g = g
        self.__h = h
        self.__pai = pai
    
    def __repr__(self):
       return repr((self.f))

    @property
    def f(self):
        return self.__f
    
    @f.setter
    def f(self, f):
        self.__f = f
    
    @property
    def g(self):
        return self.__g

    @g.setter
    def g(self, g):
        self.__g = g
    
    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        self.__h = h

    @property
    def matriz(self):
        return self.__matriz

    @property
    def pai(self):
        return self.__pai

    @pai.setter
    def pai(self, pai):
        self.__pai = pai


def imprime_tabuleiro(tab):
    linhas = len(tab)
    colunas = len(tab[0])
    for i in range(linhas):
        for j in range(colunas):
            if j == colunas - 1:
                print("%d" %tab[i][j])
            else:
                print("%d" %tab[i][j], end = " ")
    print()

# Cria o tabuleiro 3x3
tab = []
for i in range(3):
    tab.append( [0] * 3 )

print('Para gerar o estado inicial de forma aleatória digite 1')
print('Se pretende inserir os valores manualmente digite 2')
a = int(input('Digite a opção escolhida (1 / 2): '))

#Inicializa tabuleiro aleatoriamente ou manualmente 
if a == 1:
    #tab = [[0, 1, 2], [3, 4, 5], [6,7,8]]
    #tab = np.array(b) 
    vet = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(vet)
    #print(vet)
    print('\n\tESTADO INICIAL:')
    n = 0
    for i in range(3):
        for j in range(3):
            tab[i][j] = vet[n]
            n = n + 1
    imprime_tabuleiro(tab)
    #print(tab)
elif a == 2:
    for i in range(3):
        for j in range(3):
            x = int(input('tab[{}][{}] = '.format(i, j)))
            tab[i][j] = x
    print('\n\tESTADO INICIAL:')
    imprime_tabuleiro(tab)

#Passa matriz para um vetor
puzzle = []
linhas = len(tab)
colunas = len(tab[0])
for i in range(linhas):
    for j in range(colunas):
        puzzle.append(tab[i][j])

print(puzzle)

#py program to check if a given instance of 8 puzzle is solvable or not 
  
# A utility function to count inversions in given array 'arr[]' 
def getInvCount(arr):
    inv_count = 0
    for i in range(8):
        for j in range(i+1, 9):
             # Value 0 is used for empty space 
            #print ('foi')
            if arr[j] and arr[i] and arr[i] > arr[j]:
                inv_count = inv_count + 1 
    print(inv_count)
    return inv_count
 
  
# This function returns true if given 8 puzzle is solvable. 
def isSolvable(puzzle):
    #Count inversions in given 8 puzzle 
    invCount = getInvCount(puzzle)
  
    # return true if inversion count is even. 
    return (invCount%2 == 0)
    
def paraCima(tab):
    for j in range(3):
        for i in range(3):
            if tab[2][j] == 0:
                return None
            elif tab[i][j] != 0:
                if tab[i-1][j] == 0: #Se o número acima é 0, há o deslocamento.
                    tab[i-1][j] = tab[i][j]
                    tab[i][j] = 0
                    return tab

def paraBaixo(tab):
    for j in range(3):
        for i in range(2, -1, -1):
            if tab[0][j] == 0:
                return None
            elif tab[i][j] != 0 and i+1 < 3:
                if tab[i+1][j] == 0: # Se o número abaixo é 0, há o deslocamento.
                    tab[i+1][j] = tab[i][j]
                    tab[i][j] = 0
                    return tab
        
def paraEsquerda(tab):
    for i in range(3):
        for j in range(1, 3):
            if tab[i][2] == 0:
                return None
            elif tab[i][j] != 0:
                if tab[i][j-1] == 0: # Se o número anterior é 0, há o deslocamento.
                    tab[i][j-1] = tab[i][j]
                    tab[i][j] = 0
                    return tab

def paraDireita(tab):
    for i in range(3):
        for j in range(2, -1, -1):
            if tab[i][0] == 0:
                return None
            elif tab[i][j] != 0 and j + 1 < 3:
                    if tab[i][j+1] == 0: # Se o número posterior é 0, há o deslocamento.
                        tab[i][j+1] = tab[i][j]
                        tab[i][j] = 0
                        return tab

obj = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def imprime_caminho(fechados, estado1, x, passos):
    if estado1 == x:
        imprime_tabuleiro(estado1.matriz)
        return passos
    else:
        p = imprime_caminho(fechados, estado1, x.pai, passos+1)
        imprime_tabuleiro(x.matriz)
    return p
###############################################################################################
                                        # Busca Cega #
###############################################################################################
#Função para verificar se já existe um estado igual em abertos ou fechados.
def verificaIgual(abertos, fechados, est):
    for i in range(len(abertos)):
        if est == abertos[i].matriz:
            return 1
    for i in range(len(fechados)):
        if est == fechados[i].matriz:
            return 1   
    return 0   

#Busca em largura.
def bfs(tab):
    abertos = deque([]) 
    fechados = deque([]) 
    estado1 = Estado(tab, 0, 0, 0, None)
    abertos.append(estado1)
    while abertos != None:
        x = abertos.popleft()
        if x.matriz == obj:
            fechados.append(x)
            print('\n\t# Busca em Largura #')
            print('CAMINHO:')
            passos = imprime_caminho(fechados, estado1, x, 0)
            print('Quantidade de passos até encontrar o Objetivo: ',  passos)
            print('Quantidade de estados abertos: ', len(abertos))
            print('Quantidade de estados fechados: ', len(fechados))
            return 'SUCESSO!'
        else:
            fechados.append(x)
            aux = deepcopy(x.matriz) 
            pc = paraCima(aux)
            aux = deepcopy(x.matriz) 
            pb = paraBaixo(aux)
            aux = deepcopy(x.matriz) 
            pe = paraEsquerda(aux)
            aux = deepcopy(x.matriz) 
            pd = paraDireita(aux)
    
            if pc != None:  
                if verificaIgual(abertos, fechados, pc) == 0:
                    estado2 = Estado(pc, 0, 0, 0, x)
                    abertos.append(estado2)
            if pb != None: 
                if verificaIgual(abertos, fechados, pb) == 0: 
                    estado3 = Estado(pb, 0, 0, 0, x)
                    abertos.append(estado3)
            if pe != None: 
                if verificaIgual(abertos, fechados, pe) == 0:
                    estado4 = Estado(pe, 0, 0, 0, x)
                    abertos.append(estado4)
            if pd != None:
                if verificaIgual(abertos, fechados, pd) == 0:
                    estado5 = Estado(pd, 0, 0, 0, x)
                    abertos.append(estado5)
    return 'FALHA :('
###############################################################################################
                                    # Busca Heurística #
###############################################################################################
# Somatório de peças fora do lugar.
def h1(tab):
    fora = 0
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] != obj[i][j]:
                fora = fora + 1
    return fora

def verificaIgual_h(abertos, fechados, est, f, g, h, pai):
    for i in range(len(abertos)):
        if est == abertos[i].matriz:
            if f < abertos[i].f:
                abertos[i].g = g
                abertos[i].h = h
                abertos[i].f = f
                abertos[i].pai = pai
            return 1
    for i in range(len(fechados)):
        if est == fechados[i].matriz:
            return 1   
    return 0   

def A_Estrela_h1(tab):
    abertos = [] 
    pai = None
    g = 0
    fechados = [] 
    estado1 = Estado(tab, h1(tab) + g, g, h1(tab), pai)
    abertos.append(estado1)
    #print(abertos)
    while abertos != None:
        x = abertos.pop(0)
        if x.matriz == obj:
            fechados.append(x)
            print('\n\t# Peças fora do lugar (h1) #')
            print('CAMINHO:')
            passos = imprime_caminho(fechados, estado1, x, 0)
            print('Quantidade de passos até encontrar o Objetivo: ', passos)
            print('Quantidade de estados abertos: ', len(abertos))
            print('Quantidade de estados fechados: ', len(fechados))
            return('SUCESSO!')
        else:
            g = g + 1
            fechados.append(x)
            aux = deepcopy(x.matriz) 
            pc = paraCima(aux)
            aux = deepcopy(x.matriz) 
            pb = paraBaixo(aux)
            aux = deepcopy(x.matriz) 
            pe = paraEsquerda(aux)
            aux = deepcopy(x.matriz) 
            pd = paraDireita(aux)
            if pc != None:  
                if verificaIgual_h(abertos, fechados, pc, h1(pc) + g, g, h1(pc), x) == 0:
                    estado2 = Estado(pc, h1(pc) + g, g, h1(pc), x)
                    abertos.append(estado2)
            if pb != None: 
                if verificaIgual_h(abertos, fechados, pb, h1(pb) + g, g, h1(pb), x) == 0: 
                    estado3 = Estado(pb, h1(pb) + g, g, h1(pb), x)
                    abertos.append(estado3)
            if pe != None: 
                if verificaIgual_h(abertos, fechados, pe, h1(pe) + g, g, h1(pe), x) == 0:
                    estado4 = Estado(pe, h1(pe) + g, g, h1(pe), x)
                    abertos.append(estado4)
            if pd != None:
                if verificaIgual_h(abertos, fechados, pd, h1(pd) + g, g, h1(pd), x) == 0:
                    estado5 = Estado(pd, h1(pd) + g, g, h1(pd), x)
                    abertos.append(estado5)
            abertos.sort(key = attrgetter('f', 'h'))
    return('FALHA :(')
###############################################################################################
# Distância Manhattan.
def h2(tab):
    total = 0
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == 0:
                total += abs(2-i) + abs(2-j)
            if tab[i][j] == 1:
                total += abs(0-i) + abs(0-j)
            if tab[i][j] == 2:
                total += abs(0-i) + abs(1-j)
            if tab[i][j] == 3:
                total += abs(0-i) + abs(2-j)
            if tab[i][j] == 4:
                total += abs(1-i) + abs(0-j)
            if tab[i][j] == 5:
                total += abs(1-i) + abs(1-j)
            if tab[i][j] == 6:
                total += abs(1-i) + abs(2-j)
            if tab[i][j] == 7:
                total += abs(2-i) + abs(0-j)
            if tab[i][j] == 8:
                total += abs(2-i) + abs(1-j)
    return total

def verificaIgual_gulosa(fechados, est):        
    for i in range(len(fechados)):
        if est == fechados[i].matriz:
            return 1   
    return 0  

# Gulosa utilizando distância manhattan como heurística
def Gulosa_h2(tab):
    abertos = [] 
    pai = None
    fechados = [] 
    estado1 = Estado(tab, h2(tab), 0, h2(tab), pai)
    abertos.append(estado1)
    while abertos != None:
        x = abertos.pop(0)
        if x.matriz == obj:
            fechados.append(x)
            print('\n\t# Distância Manhattan (h2) #')
            print('CAMINHO:')
            passos = imprime_caminho(fechados, estado1, x, 0)
            print('Quantidade de passos até encontrar o Objetivo: ', passos)
            print('Quantidade de estados abertos: ', len(abertos))
            print('Quantidade de estados fechados: ', len(fechados))
            return('SUCESSO!')
        else:
            fechados.append(x)
            aux = deepcopy(x.matriz) 
            pc = paraCima(aux)
            aux = deepcopy(x.matriz) 
            pb = paraBaixo(aux)
            aux = deepcopy(x.matriz) 
            pe = paraEsquerda(aux)
            aux = deepcopy(x.matriz) 
            pd = paraDireita(aux)
            compara = []
            if pc != None: 
                if verificaIgual_gulosa(fechados, pc) == 0:
                    estado2 = Estado(pc, h2(pc), 0, h2(pc), x)
                    compara.append(estado2)
            if pb != None: 
                if verificaIgual_gulosa(fechados, pb) == 0: 
                    estado3 = Estado(pb, h2(pb), 0, h2(pb), x)
                    compara.append(estado3)
            if pe != None: 
                if verificaIgual_gulosa(fechados, pe) == 0:
                    estado4 = Estado(pe, h2(pe), 0, h2(pe), x)
                    compara.append(estado4)
            if pd != None:
                if verificaIgual_gulosa(fechados, pd) == 0:
                    estado5 = Estado(pd, h2(pd), 0, h2(pd), x)
                    compara.append(estado5)
            compara.sort(key = attrgetter('f'))
            abertos.append(compara.pop(0))
    return('FALHA :(')
###############################################################################################
# Distância euclidiana.
def h3(tab):
    total = 0
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == 0:
                total += math.sqrt(pow(abs(2-i), 2) + pow(abs(2-j), 2))
            if tab[i][j] == 1:
                total += math.sqrt(pow(abs(0-i), 2) + pow(abs(0-j), 2))
            if tab[i][j] == 2:
                total += math.sqrt(pow(abs(0-i), 2) + pow(abs(1-j), 2))
            if tab[i][j] == 3:
                total += math.sqrt(pow(abs(0-i), 2) + pow(abs(2-j), 2))
            if tab[i][j] == 4:
                total += math.sqrt(pow(abs(1-i), 2) + pow(abs(0-j), 2))
            if tab[i][j] == 5:
                total += math.sqrt(pow(abs(1-i), 2) + pow(abs(1-j), 2))
            if tab[i][j] == 6:
                total += math.sqrt(pow(abs(1-i), 2) + pow(abs(2-j), 2))
            if tab[i][j] == 7:
                total += math.sqrt(pow(abs(2-i), 2) + pow(abs(0-j), 2))
            if tab[i][j] == 8:
                total += math.sqrt(pow(abs(2-i), 2) + pow(abs(1-j), 2))
    return round(total, 3)

# A* utilizando distância euclidiana como heurística
def A_Estrela_h3(tab):
    abertos = [] 
    pai = None
    g = 0
    fechados = [] 
    estado1 = Estado(tab, h3(tab) + g, g, h3(tab), pai)
    abertos.append(estado1)
    while abertos != None:
        x = abertos.pop(0)
        if x.matriz == obj:
            fechados.append(x)
            print('\n\t# Distância Euclidiana (h3) #')
            print('CAMINHO:')
            passos = imprime_caminho(fechados, estado1, x, 0)
            print('Quantidade de passos até encontrar o Objetivo: ', passos)
            print('Quantidade de estados abertos: ', len(abertos))
            print('Quantidade de estados fechados: ', len(fechados))
            return('SUCESSO!')
        else:
            g = g + 1
            fechados.append(x)
            aux = deepcopy(x.matriz) 
            pc = paraCima(aux)
            aux = deepcopy(x.matriz) 
            pb = paraBaixo(aux)
            aux = deepcopy(x.matriz) 
            pe = paraEsquerda(aux)
            aux = deepcopy(x.matriz) 
            pd = paraDireita(aux)
            if pc != None:  
                if verificaIgual_h(abertos, fechados, pc, h3(pc) + g, g, h3(pc), x) == 0:
                    estado2 = Estado(pc, h3(pc) + g, g, h3(pc), x)
                    abertos.append(estado2)
            if pb != None: 
                if verificaIgual_h(abertos, fechados, pb, h3(pb) + g, g, h3(pb), x) == 0: 
                    estado3 = Estado(pb, h3(pb) + g, g, h3(pb), x)
                    abertos.append(estado3)
            if pe != None: 
                if verificaIgual_h(abertos, fechados, pe, h3(pe) + g, g, h3(pe), x) == 0:
                    estado4 = Estado(pe, h3(pe) + g, g, h3(pe), x)
                    abertos.append(estado4)
            if pd != None:
                if verificaIgual_h(abertos, fechados, pd, h3(pd) + g, g, h3(pd), x) == 0:
                    estado5 = Estado(pd, h3(pd) + g, g, h3(pd), x)
                    abertos.append(estado5)
            abertos.sort(key = attrgetter('f', 'h'))
    return('FALHA :(')
###############################################################################################
# Verifica se é solucionável.    
if isSolvable(puzzle):
    print('Solucionavel')
    print(A_Estrela_h1(tab))
    print(Gulosa_h2(tab))
    print(A_Estrela_h3(tab))
    print(bfs(tab))
else:
    print('Não solucionavel')
