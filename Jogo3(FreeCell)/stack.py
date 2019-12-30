# -*- Coding: UTF-8 -*-
#coding: utf-8
from Node import Pilha


class Stack:
    
    #Construtor da classe
    #Um ponteiro para o elemento do topo, e um para o primeiro, o ponteiro auxiliar serve para ajuda nas ligações
    def __init__(self):
        self.top = None
        self.first = None
        self.aux = None
        self.tamanho = 0
    
    #Como havia dito, o metodo de inserção, continua o(1), com mudanças apenas em algumas ligações
    #Foi necessario a criação de dois nós com o mesmo elemento, pois sem isso, os ponteiros teriam o
    #mesmo endereço, impossibilitando que algumas ligações pudessem ser feitas em o(1).
    def push(self, elem):
        node = Pilha(elem) 
        node2 = Pilha(elem)
        node.prox = self.top #Elemento do topo recebe como prox o novo
        self.top = node  #novo elemento vira o topo da pilha
        
        #Ligações da lista encadeada
        if self.tamanho >= 1:
            self.aux.prox = node2    
            anterior = self.aux
            self.aux = node2
            self.aux.ant = anterior
            self.aux.prox = None            
        else:
            self.aux = node2
            self.first = self.aux 
        
        self.tamanho += 1      #Tamanho aumenta sempre que é chamada
      

    #remove o elemento do topo da lista
    def pop(self):        
        if self.tamanho > 0:
            node = self.top        #Variavel aux recebe o elemento do topo
            self.top = self.top.prox  #Topo passa a ser o segundo elemento da pilha
            
            #O mesmo acontece com a "lista encadeada", porém, sem resgatar o elemento.
            if self.tamanho > 1:
                self.aux = self.aux.ant
                self.aux.prox = None
            else:
                self.aux = None
                self.first = None
            
            self.tamanho -= 1      #Tamanho decrementa em 1
            
            return node.dado   #Retorna o elemento retirado
        
        raise IndexError("A pilha está vazia")  #Caso a pilha esteja vazia, a mensagem aparecerá no terminal
    #obs: Possiveis underflows já são tratados dentro do codigo do jogo

    #metodo que mostra o elemento do topo da lista sem retirar.
    def peek(self):
        if self.tamanho > 0:
            return self.top.dado
        raise IndexError("A pilha está vazia")

    #Sobreescreve a função len que retorna o tamanho da pilha
    def __len__(self):
        return self.tamanho

    #metodo que desenha apenas uma carta, a do topo da pilha (usada nas fundações/celulas vazias)
    def blit_carta(self,tela,dicionario, pos):
        if self.tamanho >= 1:
            tela.blit(dicionario[self.top.dado], pos)
            
    #Percorre toda a pilha (É usada para desenhar os decks principais durante o jogo)
    def percorre_deck(self,tela,dicionario,pos_x):
        pointer = self.first
        y = 180
        while pointer:
            tela.blit(dicionario[pointer.dado],[pos_x, y])
            y += 32
            pointer = pointer.prox

        













