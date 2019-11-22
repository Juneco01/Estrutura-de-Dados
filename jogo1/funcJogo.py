#usr/bin/python3
# -*- coding: utf-8 -*-
import os, time
from funcPrint import *
import random


#Este modulo foi criado para criar todas as funções importantes do programa
#Além de criar a classe para a lista Encadeada e todas suas caracteristicas e metodos

#Classe que é utilizada para a criação dos nós.
#recebe um atributo dado, e também atribui uma referencia para um proximo nó
class celula:
    def __init__(self,dado):
        self.dado = dado
        self.prox = None



class LinkedList:
    #Contrutor da lista, tem o atributo cabeça e o atributo tamanho
    def __init__(self):
        self.imi = None
        self.tamanho = 0
    
    #Metodo que adiciona um elemento no fim da lista (E depois incrementa em 1 o tamanho dela)
    #Utilizo a variavel ponteiro para percorrer a lista.
    def adicionar(self, elemento):
        if self.imi:
            ponteiro = self.imi
            while(ponteiro.prox):
                ponteiro = ponteiro.prox
            ponteiro.prox = celula(elemento)
        else:
            self.imi = celula(elemento)
        
        self.tamanho = self.tamanho + 1
    
    #Metodo que sobreescreve a função len do python, o metodo retorna o tamanho atualizado da lista
    def __len__(self):
        """Sobescreve a função len e Retorna o tamanho da lista"""
        return self.tamanho


     #Metodo para dado um indice, retornar o valor que está dentro daquele nó na lista.   
    def getItem(self, indice):
        ponteiro = self.imi
        for i in range(0,indice):
            if ponteiro:
                ponteiro = ponteiro.prox
            else:
                raise IndexError("Indice fora de alcance")
    
        if ponteiro:
            return ponteiro.dado
        raise IndexError("Indice fora de alcance")

    #funcao pra remover um elemento da lista
    def remove(self,elemento):
        ponteiro = self.imi
        if self.imi.dado == elemento:
            self.imi = self.imi.prox
            self.tamanho = self.tamanho - 1
            return True
        else:
            while ponteiro and ponteiro.prox.dado != elemento:
                ponteiro = ponteiro.prox
            if ponteiro:
                ponteiro.prox = ponteiro.prox.prox
                self.tamanho = self.tamanho - 1
                return True
        return False
    

#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################


#DESENHOS DOS ANIMAIS 
lobo =("                     .\n                    / V\ \n                  / `  / \n        "
      "         <<   | \n                 /    | \n               /      | \n             /        | \n     "
      "      /    \  \ / \n          (      ) | | \n  ________|   _/_  | | \n<__________\______)\__) \n")
aranha = (" ||  ||  \n \\\ ()// \n//(__)\\ \n||    ||\n")
escorpiao = ("  _    _\n  /_]  [_\ \n //      \\ \n \\      // \n  \`-..-'/ \n   `\  /` \n   "
      "  ||    _ \n     ||   ( ) \n     \\___/ \n ")
rato = ("()(),~~,.\n .. ___; )\n=`=     (_.\n")

esquilo = (" __  (\_ \n(_ \ ( '> \n  ) \/_)=\n  (_(_ )\n_")

tartaruga = (" \n   _____    \n /      \  |  o | \n|        |/ ___\| \n|_________/     \n|_|_| |_|_|\n")

coelho = ("               ((`\ \n            ___ \\ '--._ \n         .'`   `'    o  ) \n    "
      "    /    \   '. __.' \n       _|    /_  \ \_\_ \n      {_\______\-'\__\_\ \n")

macaco = ("          __ \n     w  c(..)o   ( \n      \__(-)    __) \n          /\   ( \n     "
      "    /(_)___) \n         w /| \n          | \ \n         m  m \n")

sapo = ("       _e-e_ \n     _(-._.-)_ \n  .-(  `---'  )-. \n __\ \\\___/// /__ \n'-._.'/M\ /M\`._,-\n ")

tubarao = ("      . \n\_____)\_____ \n/--v____ __`<  \n         )/       \n        '\n")

peixe = ("   ,\n  /|\n /_|  , \n/o  \/| \n\<__/\| \n \ |  ` \n  \| \n")

cachorro = ("           __ \n      (___()'`;\n      /,    /`\n      \\-- \ \ \n ")
gato = (" |\__/,|   (`\ \n |_ _  |.--.) ) \n ( T   )     / \n(((^_(((/(((_/ \n")

urso = (" __         __\n/  \.-""-. /  \ \n\    -   -    / \n |   o   o   | \n \  .-'''-.  / \n  '-\__Y__/-' \n     `---`\n")

coruja = (" /\_/\ \n((@v@))\n():::()\n VV-VV\n")

cavalo = ("           ,--,\n     _ ___/ /\|\n ,;'( )__, )  ~\n//  //   '--; \n'   \     | ^\n     ^    ^\n")

morcego = ("       (_    ,_,    _) \n       / `'--) (--'` \ \n      /  _,-'\_/'-,_  \ \n     /.-'           '-.\ \n  \n")

vaca = ("\|/          (__)\n     `\------(oo) \n       ||    (__) \n       ||w--||     \|/ \n   \|/ \n ")

camelo = ("   // \n _oo\ \n(__/ \  _  _ \n   \  \/ \/ \ \n   (         )\ \n    \_______/  \ \n     [[] [[] \n     [[] [[] \n")

abelha = ("          __         .' '. \n        _/__)        .   .       .\n       (8|)_}}- .      .        . \n        `\__)    '. . ' ' .  . ' \n")



#Função que exibe o desenho com o nome de cada animal.
def verificaAnimais(lista,lista2):
    ponteiro2 = lista2.imi
    ponteiro = lista.imi
    while ponteiro:
        os.system('clear')
        print("\n\033[1;31m Confira a lista dos animais \033[0;0m")
        print("\n\n" + ponteiro.dado)
        print("\n\033[1;31m   " + ponteiro2.dado + "\033[0;0m")
        time.sleep(1)
        ponteiro = ponteiro.prox 
        ponteiro2 = ponteiro2.prox

#Função que exibe os 5 animais que o jogador terá que memorizar
def inGameImagem(lista):
    a = 10
    os.system("clear")
    print("\033[1;31m MEMORIZE ESSES 5 ANIMAIS \033[0;0m")
    for item in lista:
        print(item)
    time.sleep(a)
    os.system("clear")

#Função que verifica os animais escolhidos pelo usuario, e adiciona eles na lista encadeada dos animais escolhidos
def listaEscolhe(listaEscolhidos,animaisnom):
    for i in range(0,5):
        os.system("clear")
        exibeLista(animaisnom)
        print("\n\n\033[1;31m Digite o nome de cada um dos 5 animais que você memorizou \033[0;0m")
        animal = input()
        if animal == 'lobo':
            listaEscolhidos.adicionar(lobo)
        elif animal == 'aranha' :
            listaEscolhidos.adicionar(aranha)
        elif animal == 'escorpiao' :
            listaEscolhidos.adicionar(escorpiao)
        elif animal == 'rato' :
            listaEscolhidos.adicionar(rato)
        elif animal == 'esquilo' :
            listaEscolhidos.adicionar(esquilo)
        elif animal == 'tartaruga' :
            listaEscolhidos.adicionar(tartaruga)
        elif animal == 'coelho' :
            listaEscolhidos.adicionar(coelho)
        elif animal == 'macaco' :
            listaEscolhidos.adicionar(macaco)
        elif animal == 'sapo' :
            listaEscolhidos.adicionar(sapo)
        elif animal == 'tubarao' :
            listaEscolhidos.adicionar(tubarao)
        elif animal == 'peixe' :
            listaEscolhidos.adicionar(peixe)
        elif animal == 'cachorro' :
            listaEscolhidos.adicionar(cachorro)
        elif animal == 'urso' :
            listaEscolhidos.adicionar(urso)
        elif animal == 'coruja' :
            listaEscolhidos.adicionar(coruja)
        elif animal == 'cavalo' :
            listaEscolhidos.adicionar(cavalo)
        elif animal == 'morcego' :
            listaEscolhidos.adicionar(morcego)
        elif animal == 'vaca' :
            listaEscolhidos.adicionar(vaca)
        elif animal == 'camelo' :
            listaEscolhidos.adicionar(camelo)
        elif animal == 'abelha' :
            listaEscolhidos.adicionar(abelha)


#Essa função é importante pois ela verifica a possibilidade do usuario digitar animais repetidos
#o uso de set eliminará qualquer elemento repetido, fazendo assim o tamanho da lista diminuir e consequentemente

def verificaIguais(listaEncadeada):
    aux = []
    ponteiro = listaEncadeada.imi
    while ponteiro:
        aux.append(ponteiro.dado)
        ponteiro = ponteiro.prox
    if len(set(aux)) != 5:
        return 0
    return 1


#Função que exibe a lista com o nome de todos os animais.
def exibeLista(listaAnimais):
    ponteiro = listaAnimais.imi
    i = 0
    while ponteiro:
        if i == 4:
            i = -1
            print(ponteiro.dado)
        else:
            print(ponteiro.dado, end ="\t\t\t")
        ponteiro = ponteiro.prox
        i += 1


#Essa função define aleatoriamente os 5 elementos que serão exibidos durante o jogo
def defineLista(lista, listaEnc):
    while len(lista) > 0 : 
        lista.pop()
    for i in range(0,5):
        auxiliar = listaEnc.getItem(random.randint(0,len(listaEnc)-1))
        lista.append(auxiliar)
        listaEnc.remove(auxiliar)

#Esta é a funcao que compara os elementos Sorteados e os elementos escolhidos pelo usuario
def comparaListas(lista,encLista):
    ponteiro = encLista.imi
    if len(encLista) == 5 and verificaIguais(encLista) == 1:
        while ponteiro:           
            if ponteiro.dado in lista:
                pass
            else:
                return 0
            ponteiro = ponteiro.prox
        return 1
    else:
        return 0


#Função insere todos os bichos (desenhos), dentro de uma lista encadeada (a lista padrão dos desenhos)
def setBichos(animaisEnc):
    animaisEnc.adicionar(lobo)
    animaisEnc.adicionar(aranha)
    animaisEnc.adicionar(escorpiao)
    animaisEnc.adicionar(rato)
    animaisEnc.adicionar(esquilo)
    animaisEnc.adicionar(tartaruga)
    animaisEnc.adicionar(coelho)
    animaisEnc.adicionar(macaco)
    animaisEnc.adicionar(sapo)
    animaisEnc.adicionar(tubarao)
    animaisEnc.adicionar(peixe)
    animaisEnc.adicionar(cachorro)
    animaisEnc.adicionar(urso)
    animaisEnc.adicionar(coruja)
    animaisEnc.adicionar(cavalo)
    animaisEnc.adicionar(morcego)
    animaisEnc.adicionar(vaca)
    animaisEnc.adicionar(camelo)
    animaisEnc.adicionar(abelha)

#função que insere o nome de todos os  animais em uma lista encadeada (a lista padrão dos nomes dos animais)
#É utilizada na função  verificaAnimais()
def setNames(animaisNome):
    animaisNome.adicionar("lobo")
    animaisNome.adicionar("aranha")
    animaisNome.adicionar("escorpiao")
    animaisNome.adicionar("rato")
    animaisNome.adicionar("esquilo")
    animaisNome.adicionar("tartaruga")
    animaisNome.adicionar("coelho")
    animaisNome.adicionar("macaco")
    animaisNome.adicionar("sapo")
    animaisNome.adicionar("tubarao")
    animaisNome.adicionar("peixe")
    animaisNome.adicionar("cachorro")
    animaisNome.adicionar("urso")
    animaisNome.adicionar("coruja")
    animaisNome.adicionar("cavalo")
    animaisNome.adicionar("morcego")
    animaisNome.adicionar("vaca")
    animaisNome.adicionar("camelo")
    animaisNome.adicionar("abelha")



#Essa função elimina todos os membros de uma lista
#é usada no final do laço principal do jogo
#Evita que sejam adicionados elementos repetidos nas listas dos animais
def clearLista(listaEncadeada):
    while (len(listaEncadeada) > 0):
        auxiliar = listaEncadeada.getItem(random.randint(0,len(listaEncadeada)-1))
        listaEncadeada.remove(auxiliar)


# Pôde se observar o uso de varios laços de repetições, porém boa parte deles apenas farão iterações pequenas
# Como exibir 5 desenhos, sortear alguns elementos, verificar se as 2 listas com 5 elemetos cada são iguais, etc.

#Caso o numero de iterações fosse macro, poderiam ser feita algumas melhorias, como utilizar o mesmo laço
#que faz o sorteio dos elementos(desenhos) para exibi-los logo em seguida, ou utilizando a função clear/setItens apenas quando
#o numero de elementos nas listas forem menor do que 5.