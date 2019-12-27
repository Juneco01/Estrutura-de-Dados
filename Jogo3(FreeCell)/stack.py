# -*- Coding: UTF-8 -*-
#coding: utf-8
from Node import Pilha


class Stack:
    
    def __init__(self):
        self.top = None
        self.tamanho = 0
    
    
    def push(self, elem):
        
        node = Pilha(elem)
        node.prox = self.top
        self.top = node
        self.tamanho += 1

    def pop(self):
        
        if self.tamanho > 0:
            node = self.top
            self.top = self.top.prox
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


    def blit_carta(self,tela,dicionario, pos):
        if self.tamanho >= 1:
            tela.blit(dicionario[self.top.dado], pos)
            



pilha = Stack()
