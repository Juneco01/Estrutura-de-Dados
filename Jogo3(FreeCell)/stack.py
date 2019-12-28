# -*- Coding: UTF-8 -*-
#coding: utf-8
from Node import Pilha


class Stack:
    
    def __init__(self):
        self.top = None
        self.first = None
        self.aux = None
        self.tamanho = 0
    
    
    def push(self, elem):
        node = Pilha(elem)
        node2 = Pilha(elem)
        node.prox = self.top
        self.top = node
        if self.tamanho >= 1:
            self.aux.prox = node2
            anterior = self.aux
            self.aux = node2
            self.aux.ant = anterior
            self.aux.prox = None            
        else:
            self.aux = node2
            self.first = self.aux 
        self.tamanho += 1
        

    def pop(self):        
        if self.tamanho > 0:
            node = self.top
            self.top = self.top.prox
            if self.tamanho > 1:
                self.aux = self.aux.ant
                self.aux.prox = None
            else:
                self.aux = None
                self.first = None
            
            self.tamanho -= 1
            return node.dado
        raise IndexError("A pilha está vazia")

    def peek(self):
        if self.tamanho > 0:
            return self.top.dado
        raise IndexError("A pilha está vazia")

    def __len__(self):
        """Sobescreve a função len e Retorna o tamanho da lista"""
        return self.tamanho

    def percorre(self):
        pointer = self.first
        while pointer:
            print(pointer.dado)
            pointer = pointer.prox


    def blit_carta(self,tela,dicionario, pos):
        if self.tamanho >= 1:
            tela.blit(dicionario[self.top.dado], pos)
            
    def percorre_deck(self,tela,dicionario,pos_x):
        pointer = self.first
        y = 180
        while pointer:
            tela.blit(dicionario[pointer.dado],[pos_x, y])
            y += 32
            pointer = pointer.prox

        













