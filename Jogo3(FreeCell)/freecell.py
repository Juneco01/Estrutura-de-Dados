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


#class celulas_vazias():
    

#Ordenar aleatoriamente a lista de cartas
random.shuffle(lista_cartas)

#Inicializar todos os decks (pilhas)
deck_1 = Stack()
deck_2 = Stack()
deck_3 = Stack()
deck_4 = Stack()
deck_5 = Stack()
deck_6 = Stack()
deck_7 = Stack()
deck_8 = Stack()


#Inicializar as celulas vazias (pilhas)
celula_vazia_1 = Stack()
celula_vazia_2 = Stack()
celula_vazia_3 = Stack()
celula_vazia_4 = Stack()

#Inicializar as fundacoes (pilhas)
fundacao_copas = Stack()
fundacao_espada = Stack()
fundacao_ouros = Stack()
fundacao_paus = Stack()

#Lista para armazenar todas as pilhas criadas
lista_decks = [deck_1,deck_2,deck_3,deck_4,deck_5,deck_6,deck_7,deck_8, 
                celula_vazia_1,celula_vazia_2,celula_vazia_3,celula_vazia_4,
                fundacao_copas, fundacao_espada, fundacao_ouros, fundacao_paus
              ]

lista_contador = [[0,6],[6,12],[12,18],[18,24],[24,31],[31,38],[38,45],[45,52]]
lista_coordenadas = [[100,394],[200,394],[300,394],[400,394],[500,424],[600,424],[700,424],
                    [800,424], [40,65],[135,65],[230,65],[325,65],[595,65],[690,65],[785,65],[880,65]]


def empilha_decks(lista,intervalo):
    global lista_decks
    cont_aux = 0
    for i in lista_decks[:8]:
        for j in range(intervalo[cont_aux][0],intervalo[cont_aux][1]):
            i.push(lista[j])
        cont_aux += 1
 

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


def coloca_no_deck(indice,card):
    global lista_decks, lista_coordenadas
    carta_nova = card.split("_")
    
    if len(lista_decks[indice]) > 0:
        carta_topo =  lista_decks[indice].peek().split("_")
        verificacao_cartas = verifica_cartas(carta_nova,carta_topo)
    else:
        verificacao_cartas = True
    if len(lista_decks[indice]) < 13 and verificacao_cartas:
        lista_decks[indice].push(card)
        if indice <= 7:
            lista_coordenadas[indice][1] += 32
        return True

    return False



def verifica_cartas(new_card,card_topo):
    if "hearts" in new_card or "diamonds" in new_card:
        if "spades" in card_topo or "clubs" in card_topo:
            
            if "king" == card_topo[0] and new_card[0] == "queen":
                return True
            if "queen" == card_topo[0] and new_card[0] == "jack":
                return True
            if "jack" == card_topo[0] and new_card[0] == "10":
                return True
            try:
                if int(card_topo[0]) - 1 == int(new_card[0]):
                    return True
            except:
                return False
    
    elif "hearts" in card_topo or "diamonds" in card_topo:
        
        if "king" == card_topo[0] and new_card[0] == "queen":
            return True
        elif "queen" == card_topo[0] and new_card[0] == "jack":
            return True
        elif "jack" == card_topo[0] and new_card[0] == "10":
            return True
        try:
            if int(card_topo[0]) - 1 == int(new_card[0]):
                return True
        except:
            return False

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
    try:
        if int(carta_do_topo) + 1 == int(carta_nova):
            return True
    except:
        pass
    if "10" == carta_do_topo and carta_nova == "jack":
        return True
    if "jack" == carta_do_topo and carta_nova == "queen":
        return True
    if "queen" == carta_do_topo and carta_nova == "king":
        return True      
    return False
      
      
def modifica_deck(deck_escolhido,cordenadas,card):
    global lista_decks, lista_coordenadas
    indice = deck_escolhido - 1
    resultado = verify(deck_escolhido, cordenadas)
    if len(resultado) == 2:
        deck_cheio = coloca_no_deck(resultado[1], card)

        if deck_cheio == False:
            lista_decks[indice].push(card)
        else:
            if indice <= 7:
                lista_coordenadas[indice][1] -=32
    else:
        lista_decks[indice].push(card)

clock = pygame.time.Clock()


def game_loop():
    global lista_cartas, lista_coordenadas, lista_decks
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                held = True
                controle = True
                
            if event.type == pygame.MOUSEBUTTONUP:
                if qualquer:
                    modifica_deck(deck_escolhido,cordenadas,card)                              
                    qualquer = False 
                pygame.mouse.set_visible(True)
                held = False


        if held and controle:               
            
            for indice in range (len(lista_coordenadas) - 8):
                if cordenadas[0] >= lista_coordenadas[indice][0] and cordenadas[0] <= lista_coordenadas[indice][0] + 71:
                    if cordenadas[1] >= lista_coordenadas[indice][1] and cordenadas[1] <= lista_coordenadas[indice][1] + 45:
                        if len(lista_decks[indice]) > 0:
                            card = lista_decks[indice].pop()
                            deck_escolhido = indice + 1
                            qualquer = True
                            controle = False
            
            for indice in range(8, len(lista_coordenadas)- 4):            
                if cordenadas[0] >= lista_coordenadas[indice][0] and cordenadas[0] <= lista_coordenadas[indice][0] + 71:
                    if cordenadas[1] >= lista_coordenadas[indice][1] and cordenadas[1] <= lista_coordenadas[indice][1] + 95:
                        if len(lista_decks[indice]) > 0:
                            card = lista_decks[indice].pop()
                            deck_escolhido = indice + 1
                            qualquer = True
                            controle = False
        
        
        pos_x = 100
        for deck in lista_decks[:8]: 
            deck.percorre_deck(tela,card_dicionario,pos_x)
            pos_x+= 100


        indice_blit = 8
        for deck in lista_decks[8:]:
            deck.blit_carta(tela,card_dicionario,lista_coordenadas[indice_blit])
            indice_blit += 1
        
        
        if qualquer == True:
            pygame.mouse.set_visible(False)
            cartax = cordenadas[0] - (card_dicionario[card].get_width()//2)
            cartay = cordenadas[1] - (card_dicionario[card].get_height()//2)
            tela.blit(card_dicionario[card],(cartax,cartay))
        

        cursor = pygame.mouse.get_pos()
        

        clock.tick(60)
        
        pygame.display.update()

game_loop()
pygame.quit()
quit()