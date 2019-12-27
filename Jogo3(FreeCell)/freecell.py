import pygame
import random
from stack import Stack
from cards import card_dicionario, lista_cartas

pygame.init()

espadas = pygame.image.load("espadas.png")
copas = pygame.image.load("copas.png")
ouros = pygame.image.load("ouros.png")
paus = pygame.image.load("paus.png")

tela = pygame.display.set_mode((1000,700))

tela.fill((36,150,84))
576




#class celulas_vazias():
    


random.shuffle(lista_cartas)


deck_1, lista_aux_1 = Stack(), []
deck_2, lista_aux_2 = Stack(), []
deck_3, lista_aux_3 = Stack(), []
deck_4, lista_aux_4 = Stack(), []
deck_5, lista_aux_5 = Stack(), []
deck_6, lista_aux_6 = Stack(), []
deck_7, lista_aux_7 = Stack(), []
deck_8, lista_aux_8 = Stack(), []

celula_vazia_1 = Stack()
celula_vazia_2 = Stack()
celula_vazia_3 = Stack()
celula_vazia_4 = Stack()


fundacao_copas = Stack()
fundacao_espada = Stack()
fundacao_ouros = Stack()
fundacao_paus = Stack()



def empilha_decks(lista,lista_cont):
    global lista_aux_1, lista_aux_2, lista_aux_3,lista_aux_4
    global lista_aux_5, lista_aux_6, lista_aux_7, lista_aux_8
    global deck_1, deck_2, deck_3, deck_4, deck_5, deck_6, deck_7, deck_8    
    for i in range (0,lista_cont[0]):
        deck_1.push(lista[i])
        lista_aux_1.append(lista[i])
    for i in range (6,lista_cont[1]):
        deck_2.push(lista[i])
        lista_aux_2.append(lista[i])
    for i in range (12,lista_cont[2]):
        deck_3.push(lista[i])
        lista_aux_3.append(lista[i])
    for i in range (18,lista_cont[3]):
        deck_4.push(lista[i])
        lista_aux_4.append(lista[i])
    for i in range (24,lista_cont[4]):
        deck_5.push(lista[i])
        lista_aux_5.append(lista[i])
    for i in range (31,lista_cont[5]):
        deck_6.push(lista[i])
        lista_aux_6.append(lista[i])
    for i in range (38,lista_cont[6]):
        deck_7.push(lista[i])
        lista_aux_7.append(lista[i])
    for i in range (45,lista_cont[7]):
        deck_8.push(lista[i])
        lista_aux_8.append(lista[i])







print(lista_cartas)

lista_contador = [6,12,18,24,31,38,45,52]
lista_coordenadas = [[100,394],[200,394],[300,394],[400,394],[500,424],[600,424],[700,424],
                    [800,424], [40,65],[135,65],[230,65],[325,65],[595,65],[690,65],[785,65],[880,65]]

    



def decks(dicionario_cartas):
    y = 180
    global lista_aux_1, lista_aux_2, lista_aux_3,lista_aux_4
    global lista_aux_5, lista_aux_6, lista_aux_7, lista_aux_8
    for i in lista_aux_1:
        tela.blit(dicionario_cartas[i], (100,y))
        y += 32
    y = 180
    for i in lista_aux_2:
        tela.blit(dicionario_cartas[i], (200,y))
        y += 32

    y = 180
    for i in lista_aux_3:
        tela.blit(dicionario_cartas[i], (300,y))
        y += 32 
    y = 180 
    for i in lista_aux_4:
        tela.blit(dicionario_cartas[i], (400,y))
        y += 32
    y = 180
    for i in lista_aux_5:
        tela.blit(dicionario_cartas[i], (500,y))
        y += 32
    y = 180
    for i in lista_aux_6:
        tela.blit(dicionario_cartas[i], (600,y))
        y += 32
    y = 180
    for i in lista_aux_7:
        tela.blit(dicionario_cartas[i], (700,y))
        y += 32
    y = 180
    for i in lista_aux_8:
        tela.blit(dicionario_cartas[i], (800,y))
        y += 32
    
    

def verify(valor, cordenadas):
    global lista_coordenadas
    valor -= 1
    for i in range(0,8):
        if i == valor:
            continue
        if cordenadas[0] >= lista_coordenadas[i][0] and cordenadas[0] <= lista_coordenadas[i][0] + 71:
            if cordenadas[1] >= lista_coordenadas[i][1] and cordenadas[1] <= lista_coordenadas[i][1] + 45:
                return [True, i]
    for i in range(8,16):
        if i == valor:
            continue
        if cordenadas[0] >= lista_coordenadas[i][0] and cordenadas[0] <= lista_coordenadas[i][0] + 71:
            if cordenadas[1] >= lista_coordenadas[i][1] and cordenadas[1] <= lista_coordenadas[i][1] + 95:
                return [True, i]

    
    return [False]


def coloca_no_deck(pos_deck,card):
    global lista_aux_1, lista_aux_2, lista_aux_3,lista_aux_4
    global lista_aux_5, lista_aux_6, lista_aux_7, lista_aux_8
    global deck_1, deck_2, deck_3, deck_4, deck_5, deck_6, deck_7, deck_8  
    global lista_coordenadas
    
    pos_deck += 1
    carta_nova = card.split("_")
    if pos_deck == 1:
        if len(deck_1) > 0:
            carta_topo = deck_1.peek().split("_")
            verificacao_cartas = verifica_cartas(carta_nova, carta_topo)
        else:
            verificacao_cartas = True
        if len(deck_1)  < 13 and verificacao_cartas :
            lista_aux_1.append(card)
            deck_1.push(card)
            lista_coordenadas[0][1] += 32
            return True

    elif pos_deck == 2:
        if len(deck_2) > 0:
            carta_topo = deck_2.peek().split("_")
            verificacao_cartas = verifica_cartas(carta_nova, carta_topo)
        else:
            verificacao_cartas = True
        if len(deck_2)  < 13 and verificacao_cartas :
            lista_aux_2.append(card)
            deck_2.push(card)
            lista_coordenadas[1][1] += 32
            return True

    elif pos_deck == 3:
        if len(deck_3) > 0:
            carta_topo = deck_3.peek().split("_")
            verificacao_cartas = verifica_cartas(carta_nova, carta_topo)
        else:
            verificacao_cartas = True
        if len(deck_3)  < 13 and verificacao_cartas :
            lista_aux_3.append(card)
            deck_3.push(card)
            lista_coordenadas[2][1] += 32
            return True

    elif pos_deck == 4:
        if len(deck_4) > 0:
            carta_topo = deck_4.peek().split("_")
            verificacao_cartas = verifica_cartas(carta_nova, carta_topo)
        else:
            verificacao_cartas = True
        if len(deck_4)  < 13 and verificacao_cartas :
            lista_aux_4.append(card)
            deck_4.push(card)
            lista_coordenadas[3][1] += 32
            return True  
    
    elif pos_deck == 5:
        if len(deck_5) > 0:
            carta_topo = deck_5.peek().split("_")
            verificacao_cartas = verifica_cartas(carta_nova, carta_topo)
        else:
            verificacao_cartas = True
        if len(deck_5)  < 13 and verificacao_cartas :
            lista_aux_5.append(card)
            deck_5.push(card)
            lista_coordenadas[4][1] += 32
            return True  
    
    elif pos_deck == 6:
        if len(deck_6) > 0:
            carta_topo = deck_6.peek().split("_")
            verificacao_cartas = verifica_cartas(carta_nova, carta_topo)
        else:
            verificacao_cartas = True
        if len(deck_6)  < 13 and verificacao_cartas :
            lista_aux_6.append(card)
            deck_6.push(card)
            lista_coordenadas[5][1] += 32
            return True 
    
    elif pos_deck == 7:
        if len(deck_7) > 0:
            carta_topo = deck_7.peek().split("_")
            verificacao_cartas = verifica_cartas(carta_nova, carta_topo)
        else:
            verificacao_cartas = True
        if len(deck_7)  < 13 and verificacao_cartas :
            lista_aux_7.append(card)
            deck_7.push(card)
            lista_coordenadas[6][1] += 32
            return True 
                   
    elif pos_deck == 8: 
        if len(deck_8) > 0:
            carta_topo = deck_8.peek().split("_")
            verificacao_cartas = verifica_cartas(carta_nova, carta_topo)
        else:
            verificacao_cartas = True        
        if len(deck_8)  < 13 and verificacao_cartas :           
            lista_aux_8.append(card)
            deck_8.push(card)
            lista_coordenadas[7][1] += 32
            return True
    
    elif pos_deck == 9:
        if len(celula_vazia_1) == 0:
            celula_vazia_1.push(card)
            return True
    elif pos_deck == 10:
        if len(celula_vazia_2) == 0:
            celula_vazia_2.push(card)
            return True
    elif pos_deck == 11:
        if len(celula_vazia_3) == 0:
            celula_vazia_3.push(card)
            return True

    elif pos_deck == 12:
        if len(celula_vazia_4) == 0:
            celula_vazia_4.push(card)
            return True

    elif pos_deck == 13:
        if len(fundacao_copas) == 0:
            if (card == "ace_hearts"):
                fundacao_copas.push(card)
                return True
        elif fundacao_copas.peek()  != "king":
            if verifica_carta_fundacao(carta_nova,fundacao_copas.peek().split("_")):
                fundacao_copas.push(card)
                return True  

    elif pos_deck == 14:
        if len(fundacao_espada) == 0:
            if (card == "ace_spades"):
                fundacao_espada.push(card)
                return True      
        elif fundacao_espada.peek()  != "king":
            if verifica_carta_fundacao(carta_nova,fundacao_espada.peek().split("_")):
                fundacao_espada.push(card)
                return True  

    elif pos_deck == 15:
        
        if len(fundacao_ouros) == 0:
            if (card == "ace_diamonds"):
                fundacao_ouros.push(card)
                return True

        elif fundacao_ouros.peek()  != "king":
            if verifica_carta_fundacao(carta_nova,fundacao_ouros.peek().split("_")):
                fundacao_ouros.push(card)
                return True  

    else:
        if len(fundacao_paus) == 0:
            if (card == "ace_clubs"):
                fundacao_paus.push(card)
                return True        
        elif fundacao_paus.peek()  != "king":
            if verifica_carta_fundacao(carta_nova,fundacao_paus.peek().split("_")):
                fundacao_paus.push(card)
                return True  

    return False



def verifica_cartas(new_card,card_topo):
    if "hearts" in new_card or "diamonds" in new_card:
        if "spades" in card_topo or "clubs" in card_topo:
            if "king" == card_topo[0] and new_card[0] == "queen":
                return True
            elif "queen" == card_topo[0] and new_card[0] == "jack":
                return True
            elif "jack" == card_topo[0] and new_card[0] == "10":
                return True
            elif "10" == card_topo[0] and new_card[0] == "9":
                return True
            elif "9"  == card_topo[0] and new_card[0] == "8":
                return True
            elif "8"  == card_topo[0] and new_card[0] == "7":
                return True
            elif "7"  == card_topo[0] and new_card[0] == "6":
                return True
            elif "6"  == card_topo[0] and new_card[0] == "5":
                return True
            elif "5"  == card_topo[0] and new_card[0] == "4":
                return True
            elif "4"  == card_topo[0] and new_card[0] == "3":
                return True
            elif "3"  == card_topo[0] and new_card[0] == "2":
                return True
            elif "2"  == card_topo[0] and new_card[0] == "ace":
                return True
    elif "hearts" in card_topo or "diamonds" in card_topo:
        if "king" == card_topo[0] and new_card[0] == "queen":
            return True
        elif "queen" == card_topo[0] and new_card[0] == "jack":
            return True
        elif "jack" == card_topo[0] and new_card[0] == "10":
            return True
        elif "10" == card_topo[0] and new_card[0] == "9":
            return True
        elif "9"  == card_topo[0] and new_card[0] == "8":
            return True
        elif "8"  == card_topo[0] and new_card[0] == "7":
            return True
        elif "7"  == card_topo[0] and new_card[0] == "6":
            return True
        elif "6"  == card_topo[0] and new_card[0] == "5":
            return True
        elif "5"  == card_topo[0] and new_card[0] == "4":
            return True
        elif "4"  == card_topo[0] and new_card[0] == "3":
            return True
        elif "3"  == card_topo[0] and new_card[0] == "2":
            return True
        elif "2"  == card_topo[0] and new_card[0] == "ace":
            return True

    return False





def verifica_carta_fundacao(new_card,card_topo):
    if "hearts" in new_card and "hearts" in card_topo:
        if ordem_fundacao(card_topo[0], new_card[0]):
            return True
    if "spades" in new_card and "spades" in card_topo:
        if ordem_fundacao(card_topo[0], new_card[0]):
            return True
    if "clubs" in new_card and "clubs" in card_topo:
        if ordem_fundacao(card_topo[0], new_card[0]):
            return True
    if "diamonds" in new_card and "diamonds" in card_topo:
        if ordem_fundacao(card_topo[0], new_card[0]):
            return True
    return False
    
def ordem_fundacao(carta_do_topo, carta_nova):
        if "ace" == carta_do_topo and carta_nova == "2":
            return True
        if "2" == carta_do_topo and carta_nova == "3":
            return True
        if "3" == carta_do_topo and carta_nova == "4":
            return True
        if "4" == carta_do_topo and carta_nova == "5":
            return True
        if "5" == carta_do_topo and carta_nova == "6":
            return True
        if "6" == carta_do_topo and carta_nova == "7":
            return True
        if "7" == carta_do_topo and carta_nova == "8":
            return True
        if "8" == carta_do_topo and carta_nova == "9":
            return True
        if "9" == carta_do_topo and carta_nova == "10":
            return True
        if "10" == carta_do_topo and carta_nova == "jack":
            return True
        if "jack" == carta_do_topo and carta_nova == "queen":
            return True
        if "queen" == carta_do_topo and carta_nova == "king":
            return True      
      
      
      

clock = pygame.time.Clock()

running = True

cartax = int(1000/2)
cartay = int(600/2)
held = False
controle = False
qualquer = False

empilha_decks(lista_cartas,lista_contador)

deck_escolhido = 0
while running:
    cordenadas = pygame.mouse.get_pos()  
    tela.fill((36,150,84))
    pygame.draw.rect(tela, (12,94,51), (0,50,1000,120))
    pygame.draw.rect(tela, (51,51,51), (0,0,1000,50))
    pygame.draw.rect(tela, (255,255,255), (0,50,1000,2))
    pygame.draw.rect(tela, (51,51,51), (0,170,1000,3))
    
    #Desenha as celulas vazias
    pygame.draw.rect(tela,(0,0,0),[40,65,71,96],5)
    pygame.draw.rect(tela,(0,0,0),[135,65,71,96],5)
    pygame.draw.rect(tela,(0,0,0),[230,65,71,96],5)
    pygame.draw.rect(tela,(0,0,0),[325,65,71,96],5)

    
    #Desenha as fundações
    pygame.draw.rect(tela,(0,0,0),[595,65,71,96],5)
    pygame.draw.rect(tela,(0,0,0),[690,65,71,96],5)
    pygame.draw.rect(tela,(0,0,0),[785,65,71,96],5)
    pygame.draw.rect(tela,(0,0,0),[880,65,71,96],5)
    
    
    tela.blit(copas, (618,103))
    tela.blit(espadas, (715,103))
    tela.blit(ouros, (809,100))
    tela.blit(paus, (902,100))


    
    
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            cordAl = cartax,cartay
            
            held = True
            controle = True
            
            

        if event.type == pygame.MOUSEBUTTONUP:
            if qualquer:
                
                if deck_escolhido == 1:
                    resultado = verify(deck_escolhido, cordenadas)
                    if len(resultado) == 2:
                    
                        deck_cheio = coloca_no_deck(resultado[1],card)

                        if deck_cheio == False:
                            lista_aux_1.append(card)  
                            deck_1.push(card)
                        else:
                            lista_coordenadas[0][1] -= 32
                    else:
                        lista_aux_1.append(card)  
                        deck_1.push(card)
                
                elif deck_escolhido == 2:
                    resultado = verify(deck_escolhido, cordenadas)
                    if len(resultado) == 2:
                    
                        deck_cheio = coloca_no_deck(resultado[1],card)
                        

                        if deck_cheio == False:
                            lista_aux_2.append(card)  
                            deck_2.push(card)
                        else:
                            lista_coordenadas[1][1] -= 32
                    else:
                        lista_aux_2.append(card)  
                        deck_2.push(card)
                
                elif deck_escolhido == 3:
                    resultado = verify(deck_escolhido, cordenadas)
                    if len(resultado) == 2:
                    
                        deck_cheio = coloca_no_deck(resultado[1],card)
                        

                        if deck_cheio == False:
                            lista_aux_3.append(card)  
                            deck_3.push(card)
                        else:
                            lista_coordenadas[2][1] -= 32
                    else:
                        lista_aux_3.append(card)  
                        deck_3.push(card)

                elif deck_escolhido == 4:
                    resultado = verify(deck_escolhido, cordenadas)
                    if len(resultado) == 2:
                    
                        deck_cheio = coloca_no_deck(resultado[1],card)

                        if deck_cheio == False:
                            lista_aux_4.append(card)  
                            deck_4.push(card)
                        else:
                            lista_coordenadas[3][1] -= 32
                    else:
                        lista_aux_4.append(card)  
                        deck_4.push(card)
                
                elif deck_escolhido == 5:
                    resultado = verify(deck_escolhido, cordenadas)
                    if len(resultado) == 2:
                    
                        deck_cheio = coloca_no_deck(resultado[1],card)                        

                        if deck_cheio == False:
                            lista_aux_5.append(card)  
                            deck_5.push(card)
                        else:
                            lista_coordenadas[4][1] -= 32
                    else:
                        lista_aux_5.append(card)  
                        deck_5.push(card)
                
                elif deck_escolhido == 6:                   
                    resultado = verify(deck_escolhido, cordenadas)
                    if len(resultado) == 2:
                    
                        deck_cheio = coloca_no_deck(resultado[1],card)

                        if deck_cheio == False:
                            lista_aux_6.append(card)  
                            deck_6.push(card)
                        else:
                            lista_coordenadas[5][1] -= 32
                    else:
                        lista_aux_6.append(card)  
                        deck_6.push(card)
                
                elif deck_escolhido == 7:                    
                    resultado = verify(deck_escolhido, cordenadas)
                    if len(resultado) == 2:
                    
                        deck_cheio = coloca_no_deck(resultado[1],card)
                        

                        if deck_cheio == False:
                            lista_aux_7.append(card)  
                            deck_7.push(card)
                        else:
                            lista_coordenadas[6][1] -= 32
                    else:
                        lista_aux_7.append(card)  
                        deck_7.push(card)
                
                elif deck_escolhido == 8:
                    
                    resultado = verify(deck_escolhido, cordenadas)
                    if len(resultado) == 2:
                    
                        deck_cheio = coloca_no_deck(resultado[1],card)

                        if deck_cheio == False:
                            lista_aux_8.append(card)  
                            deck_8.push(card)
                        else:
                            lista_coordenadas[7][1] -= 32
                    else:
                        lista_aux_8.append(card)  
                        deck_8.push(card)

                elif deck_escolhido == 9:
                    resultado = verify(deck_escolhido,cordenadas)
                    if len(resultado) == 2:
                        deck_cheio = coloca_no_deck(resultado[1],card)
                        if deck_cheio == False and len(celula_vazia_1) == 0:
                            celula_vazia_1.push(card)
                    else:
                        celula_vazia_1.push(card)  
                
                elif deck_escolhido == 10:
                    resultado = verify(deck_escolhido,cordenadas)
                    if len(resultado) == 2:
                        deck_cheio = coloca_no_deck(resultado[1],card)
                        if deck_cheio == False and len(celula_vazia_2) == 0:
                            celula_vazia_2.push(card)
                    else:
                        celula_vazia_2.push(card)  

                elif deck_escolhido == 11: 
                    resultado = verify(deck_escolhido,cordenadas)
                    if len(resultado) == 2:
                        deck_cheio = coloca_no_deck(resultado[1],card)
                        if deck_cheio == False and len(celula_vazia_3) == 0:
                            celula_vazia_3.push(card)
                    else:
                        celula_vazia_3.push(card)  
                
                else:  
                    resultado = verify(deck_escolhido,cordenadas)
                    if len(resultado) == 2:
                        deck_cheio = coloca_no_deck(resultado[1],card)
                        if deck_cheio == False and len(celula_vazia_4) == 0:
                            celula_vazia_4.push(card)
                    else:
                        celula_vazia_4.push(card)         
                


                
                qualquer = False
            pygame.mouse.set_visible(True)
            held = False


    
    
    print(held)
    
    if held and controle:               
        
        if cordenadas[0] >= lista_coordenadas[0][0] and cordenadas[0] <= lista_coordenadas[0][0] + 71:
            if cordenadas[1] >= lista_coordenadas[0][1] and cordenadas[1] <= lista_coordenadas[0][1] + 45:
                if len(deck_1) > 0:
                    card = lista_aux_1.pop()
                    deck_1.pop()
                    deck_escolhido = 1
                    qualquer = True
                    controle = False
                    
        
        if cordenadas[0] >= lista_coordenadas[1][0] and cordenadas[0] <= lista_coordenadas[1][0] + 71:
            if cordenadas[1] >= lista_coordenadas[1][1] and cordenadas[1] <= lista_coordenadas[1][1] + 45:
                if len(deck_2) > 0:    
                    card = lista_aux_2.pop()
                    deck_2.pop()
                    qualquer = True
                    controle = False
                    deck_escolhido = 2

        if cordenadas[0] >= lista_coordenadas[2][0] and cordenadas[0] <= lista_coordenadas[2][0] + 71:
            if cordenadas[1] >= lista_coordenadas[2][1] and cordenadas[1] <= lista_coordenadas[2][1] + 45:
                if len(deck_3) > 0:
                    card = lista_aux_3.pop()
                    deck_3.pop()
                    qualquer = True
                    controle = False
                    deck_escolhido = 3
        
        if cordenadas[0] >= lista_coordenadas[3][0] and cordenadas[0] <= lista_coordenadas[3][0] + 71:
            if cordenadas[1] >= lista_coordenadas[3][1] and cordenadas[1] <= lista_coordenadas[3][1] + 45:
                if len(deck_4) > 0:
                    card = lista_aux_4.pop()
                    deck_4.pop()
                    qualquer = True
                    controle = False
                    deck_escolhido = 4

        if cordenadas[0] >= lista_coordenadas[4][0] and cordenadas[0] <= lista_coordenadas[4][0] + 71:
            if cordenadas[1] >= lista_coordenadas[4][1] and cordenadas[1] <= lista_coordenadas[4][1] + 45:
                if len(deck_5) > 0:
                    card = lista_aux_5.pop()
                    deck_5.pop()
                    qualquer = True
                    controle = False
                    deck_escolhido = 5

        if cordenadas[0] >= lista_coordenadas[5][0] and cordenadas[0] <= lista_coordenadas[5][0] + 71:
            if cordenadas[1] >= lista_coordenadas[5][1] and cordenadas[1] <= lista_coordenadas[5][1] + 45:
                if len(deck_6) > 0:    
                    card = lista_aux_6.pop()
                    deck_6.pop()
                    qualquer = True
                    controle = False
                    deck_escolhido = 6
        
        if cordenadas[0] >= lista_coordenadas[6][0] and cordenadas[0] <= lista_coordenadas[6][0] + 71:
            if cordenadas[1] >= lista_coordenadas[6][1] and cordenadas[1] <= lista_coordenadas[6][1] + 45:
                if len(deck_7) > 0:    
                    card = lista_aux_7.pop()
                    deck_7.pop()
                    qualquer = True
                    controle = False
                    deck_escolhido = 7

        if cordenadas[0] >= lista_coordenadas[7][0] and cordenadas[0] <= lista_coordenadas[7][0] + 71:
            if cordenadas[1] >= lista_coordenadas[7][1] and cordenadas[1] <= lista_coordenadas[7][1] + 45:
                 if len(deck_8) > 0:    
                    card = lista_aux_8.pop()
                    deck_8.pop()
                    qualquer = True
                    controle = False
                    deck_escolhido = 8
        
        if cordenadas[0] >= lista_coordenadas[8][0] and cordenadas[0] <= lista_coordenadas[8][0] + 71:
            if cordenadas[1] >= lista_coordenadas[8][1] and cordenadas[1] <= lista_coordenadas[8][1] + 95:
                if len(celula_vazia_1) > 0:
                    card = celula_vazia_1.pop()
                    qualquer = True
                    controle = False
                    deck_escolhido = 9
        
        if cordenadas[0] >= lista_coordenadas[9][0] and cordenadas[0] <= lista_coordenadas[9][0] + 71:
            if cordenadas[1] >= lista_coordenadas[9][1] and cordenadas[1] <= lista_coordenadas[9][1] + 95: 
                if len(celula_vazia_2) > 0:
                    card = celula_vazia_2.pop()
                    qualquer = True
                    controle = False
                    deck_escolhido = 10
        
        if cordenadas[0] >= lista_coordenadas[10][0] and cordenadas[0] <= lista_coordenadas[10][0] + 71:
            if cordenadas[1] >= lista_coordenadas[10][1] and cordenadas[1] <= lista_coordenadas[10][1] + 95:
                if len(celula_vazia_3) > 0:
                    card = celula_vazia_3.pop()
                    qualquer = True
                    controle = False
                    deck_escolhido = 11
    
        if cordenadas[0] >= lista_coordenadas[11][0] and cordenadas[0] <= lista_coordenadas[11][0] + 71:
            if cordenadas[1] >= lista_coordenadas[11][1] and cordenadas[1] <= lista_coordenadas[11][1] + 95:
                if len(celula_vazia_4) > 0:
                    card = celula_vazia_4.pop()
                    qualquer = True
                    controle = False
                    deck_escolhido = 12

##inserir aqui
    
    
    
    decks(card_dicionario)
    
    celula_vazia_1.blit_carta(tela,card_dicionario,lista_coordenadas[8])
    celula_vazia_2.blit_carta(tela,card_dicionario,lista_coordenadas[9])
    celula_vazia_3.blit_carta(tela,card_dicionario,lista_coordenadas[10])
    celula_vazia_4.blit_carta(tela,card_dicionario,lista_coordenadas[11])


    fundacao_copas.blit_carta(tela,card_dicionario,lista_coordenadas[12])
    fundacao_espada.blit_carta(tela,card_dicionario,lista_coordenadas[13])
    fundacao_ouros.blit_carta(tela,card_dicionario,lista_coordenadas[14])
    fundacao_paus.blit_carta(tela,card_dicionario,lista_coordenadas[15])

    

    if qualquer == True:
        pygame.mouse.set_visible(False)
        cartax = cordenadas[0] - (card_dicionario[card].get_width()//2)
        cartay = cordenadas[1] - (card_dicionario[card].get_height()//2)
        tela.blit(card_dicionario[card],(cartax,cartay))
    




    cursor = pygame.mouse.get_pos()

    
    clock.tick(60)
    
    pygame.display.update()



pygame.quit()
quit()