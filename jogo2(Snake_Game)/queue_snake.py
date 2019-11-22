# -*- Coding: UTF-8 -*-
#coding: utf-8
from Node_snake import Celula
import pygame, random

class Queue:
    # Esse é o construtor da Fila, a fila é criada sem elementos e com os dois ponteiros apontando para NONE.
    def __init__(self):
        self.tamanho = 0
        self.first = None
        self.last = None
    
    
    
    # É o metodo push comum da Fila o(1) com algumas alterações
    # como precisei percorrer a fila eu adicionei um ponteiro ant, que guarda a referencia do membro anterior 
    def push(self, x,y):
        node = Celula(x,y)
        if self.last is None: # Verifica se a lista é vazia e logo apos adiciona o elemento no fim.
            self.last = node
        else:

            aux = node
            
            # Criando as ligações
            aux.ant = self.last    
            self.last.prox = aux   
            self.last =  aux       

        if self.first is None: 
            self.first = node
        self.tamanho += 1      


    # metodo normal para remoção de elementos na fila
    def pop(self):
        if self.first is not None:
            elem = self.first.dado
            self.first = self.first.prox
            self.tamanho -= 1
            return elem
        raise IndexError("NÃO EXISTE ELEMENTOS NA FILA")    # Caso tente desenfileirar sem existir elementos na fila

    
    # Esse é um metodo especial para a cobra
    # Ele verifica se a cabeça da cobra se chocou com alguma parte do corpo (condição para fim de jogo)
    def colisao(self):
        pointer = self.first

        while pointer != self.last:
            if pointer.dado == self.last.dado:
                return True
            pointer = pointer.prox

        return False


    # Outro metodo especial para a cobra, ele percorre a cobra de trás para frente(da cabeça para o rabo)
    # E desenha os retangulos na tela do jogo.      
    def showCobra(self,tamanho_bloco,superficie,lista):
        i = 0

        pointer = self.last
        while pointer != self.first:
            print('pointer dados [0]: {}  [1]: {}'.format(pointer.dado[0],pointer.dado[1]))
            pygame.draw.rect(superficie,lista[i], (pointer.dado[0],pointer.dado[1],tamanho_bloco,tamanho_bloco))
            pointer = pointer.ant
            i += 1
        if pointer != None:
            print('pointer dados [0]: {}  [1]: {}'.format(pointer.dado[0],pointer.dado[1]))
            pygame.draw.rect(superficie,lista[i], (pointer.dado[0],pointer.dado[1],tamanho_bloco,tamanho_bloco))

    # metodo que mostra o elemento do inicio da fila.
    def peek(self):
        if self.first is not None:
            elem = self.first.dado
            return elem

    # sobrescrita do metodo len, para retornar o tamanho da fila.
    def __len__(self):
        """Sobescreve a função len e Retorna o tamanho da lista"""
        return self.tamanho

