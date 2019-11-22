#usr/bin/python3
# -*- coding: utf-8 -*-
import os, time, random 
from funcJogo import *
from funcPrint import *

#Este é o modulo principal do jogo



#Todas as listas
lista_Nomes = LinkedList()
lista_desenho = LinkedList()
listaEscolhidos = LinkedList()
listaAuxiliar = []







n = -1



while n != '1':
    
    setBichos(lista_desenho)
    setNames(lista_Nomes)

    
    var = menu()
    
    if  var == 1:
        loading()
        contagem()
        defineLista(listaAuxiliar,lista_desenho)
        inGameImagem(listaAuxiliar)
        listaEscolhe(listaEscolhidos,lista_Nomes)
        compara = comparaListas(listaAuxiliar, listaEscolhidos)
    

        if compara == 1:
            os.system("clear")
            print("	\033[1;93mParabéns venceste o jogo!!!\033[0;0m")
            print("")
            print("  o  \ o / _ o       __|   \ /    |__      o _ \ o /  o\n /|\   |    /\  ___\o  \o   |"
                "   o/   o/__  /\    |   /|\ \n / \  / \  | \ /)  |   ( \ /o\ / )   |  (\ / |  / \  / \ \n ")
            print("\n 01-Para sair \n 02- Jogar novamente")
            n = input()
        else:
            gameOver()
            n = input()

    elif var == 2:
        loading()
        instrucoes()
        ver = input()
        if ver == '2':
            verificaAnimais(lista_desenho,lista_Nomes)
            time.sleep(0.5)
    else:
        exit()
    clearLista(lista_desenho)
    clearLista(lista_Nomes)
    clearLista(listaEscolhidos)

