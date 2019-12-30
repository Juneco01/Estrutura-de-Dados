import pygame,csv
import random
from functools import partial
from stack import Stack
from cards import card_dicionario, lista_cartas
from tkinter import *


pygame.init()


#Imagens usadas nas fundações
espadas = pygame.image.load("espadas.png")
copas = pygame.image.load("copas.png")
ouros = pygame.image.load("ouros.png")
paus = pygame.image.load("paus.png")


BLACK = (14,17,17)
GREEN_TABLE = (36,150,84)
WHITE = (255,255,255)
RED = (158,11,15)


LARGURA = 1000
ALTURA = 700

tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Freecell Game")


fonte_media = pygame.font.Font("CloisterBlack.ttf",25)
fonte_pequena = pygame.font.Font("AachenBoldBT.ttf",25)
fonte_grande = pygame.font.Font("CloisterBlack.ttf",140)

LARGURA = 1000
ALTURA = 700

clock = pygame.time.Clock()



def game_menu(tela):
    
    menu = True


    while menu:

        tela.fill(GREEN_TABLE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mensagem("FreeCell", RED,tela, deslocamento_y= -250, tamanho = "grande")

        
        botao("Play", 120, 250, 350, 60, BLACK, RED,tela, acao="play")
        botao("Instruções",120,400,350,60,BLACK, RED,tela,acao= "objetivos")
        botao("Sair",560,400,350,60,BLACK,RED,tela,acao="quit")
        botao("tempos",560,250,350,60,BLACK,RED,tela,acao="tempos")


        tela.blit(card_dicionario["jack_hearts"], [10,530])
        tela.blit(card_dicionario["king_spades"], [110,530])
        tela.blit(card_dicionario["queen_diamonds"], [220,530])
        tela.blit(card_dicionario["jack_clubs"], [330,530])
        tela.blit(card_dicionario["king_hearts"], [440,530])
        tela.blit(card_dicionario["queen_clubs"], [550,530])
        tela.blit(card_dicionario["jack_diamonds"], [660,530])
        tela.blit(card_dicionario["king_clubs"], [770,530])
        tela.blit(card_dicionario["queen_diamonds"], [880,530])

        mensagem("© uespi.com, 2019 Developed by @juneco_r/Gabriel Marinho", BLACK,tela, deslocamento_y= 330 , tamanho = "medio")
        
  
        pygame.display.update()
        clock.tick(10)


#Função que desenha e controla as ações do botao
def botao(texto,x,y,largura,altura,cor_inativa,cor_ativa,tela,acao = None):
    
    cursor = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()
    
    # Verifica se o mouse esta ou nao sobre o botao
    if x + largura > cursor[0] > x and y + altura > cursor[1]> y:
        pygame.draw.rect(tela, cor_ativa,(x,y,largura,altura))
        
        if click[0] == 1 and acao != None: # Verifica a ação e executa o que lhe é pedido.
            if acao == "quit":
                pygame.quit()
                quit()
            if acao == "objetivos":
                pass
            if acao == "play":
                game_loop()
            if acao == "Main":
                game_menu(tela)
            if acao == "tkinter-sim":
                return True
            if acao == "tkinternao":
                return True
            if acao == "tempos":
                tempos_loop()
    else:
        pygame.draw.rect(tela, cor_inativa,(x,y,largura,altura))
    botao_texto(texto,WHITE,x,y, largura, altura,tela,"medio")  

#Desenha uma mensagem no centro da tela, a altura e tamanho da fonte podem ser definidos
def mensagem(msg,cor,tela, deslocamento_y = 0, tamanho = 'pequeno'):
    
    superficieTexto, textoRect = formata_texto(msg,cor,tamanho)
    textoRect.center = (LARGURA/2), (ALTURA/2) + deslocamento_y
    tela.blit(superficieTexto, textoRect)


#recebe as coordenadas do botao para desenhar o texto no centro dele
def botao_texto(msg,cor,botao_x,botao_y,botao_largura,botao_altura,tela,tamanho = "pequeno"):
    superficieTexto, textoRect = formata_texto(msg,cor,tamanho)
    textoRect.center = ((botao_x+(botao_largura/2)), (botao_y+(botao_altura/2)))
    tela.blit(superficieTexto, textoRect)

#Retorna um texto formatado com o tamanho da fonte passado por parametro
def formata_texto(texto,cor,tamanho):
    if tamanho == "pequeno":
        textosuperficie = fonte_pequena.render(texto, True, cor)
    if tamanho == "medio":
        textosuperficie = fonte_media.render(texto, True, cor)
    if tamanho == "grande":
        textosuperficie = fonte_grande.render(texto, True, cor)
    return textosuperficie, textosuperficie.get_rect()


def score(lista_decks):
    pontuacao = len(lista_decks[12]) + len(lista_decks[13]) + len(lista_decks[14]) + len(lista_decks[15])
    texto = fonte_media.render("Score: " + str(pontuacao * 12), True, WHITE)
    tela.blit(texto, [10,10])
    return pontuacao


#Exibe o tempo de jogo durante o laço principal
def timer(passed_time,tempo_minuto):
    if passed_time >= 10 and tempo_minuto < 10:
        tempo_formatado = "0"+str(tempo_minuto)+":"+str(passed_time)
        texto = fonte_media.render("0{}:{}"  .format(tempo_minuto,str(passed_time)), True, WHITE)
    elif passed_time >= 10 and tempo_minuto >=10:
        tempo_formatado = str(tempo_minuto)+":"+str(passed_time)
        texto = fonte_media.render("{}:{}"  .format(tempo_minuto,str(passed_time)), True, WHITE)
    elif passed_time <= 9 and tempo_minuto >= 10:
        tempo_formatado = str(tempo_minuto)+":"+"0"+str(passed_time)
        texto = fonte_media.render("{}:0{}"  .format(tempo_minuto,str(passed_time)), True, WHITE)
    else:
        tempo_formatado = "0"+str(tempo_minuto)+":"+"0"+str(passed_time)
        texto = fonte_media.render("0{}:0{}"  .format(tempo_minuto,str(passed_time)), True, WHITE)
    tela.blit(texto, [470,105])
    return tempo_formatado



# Parte que lida com arquivo de texto e o GUI que recebe o nome do player #
def cancel_onclick():
    janela.destroy()


def arquivo_csv(nome, tempo):
    f = open('tabela_tempo.csv', 'a')
    try: 
        writer = csv.writer(f)
        writer.writerow((nome,tempo))
    finally:
        f.close()


def ir_onclick(tempo,entrada,janela):
    arquivo_csv(entrada.get(),tempo)
    janela.destroy()
    
def pega_do_csv():
    f = open('tabela_tempo.csv', 'r')
    lista = []
    try:
        leitor = csv.reader(f)
        for linha in leitor:
            lista.append(linha)
    finally:
        f.close()
    del[lista[0]]
    return lista
    
##############################################################################


#Loop da tela de fim de jogo (quando o player vence)
#Os elementos de Tkinter são para criar uma janela que recebe o nome do jogador
#Caso ele queira cadastrar o seu tempo
def game_win_loop(tempo):
    janela = Tk()

    janela["bg"] = "#0C5E33"

    janela.geometry("260x140+550+300")
    janela.title("Name Box")
    janela.resizable(False,False)

    lb_rank = Label(janela, text="Entre no Ranking", background ="#0C5E33")
    lb_rank.config(font=("Arial", 15,"bold"))
    lb_rank.place(x=52,y= 10)

    lb_nome = Label(janela, text="Nome: ", background ="#0C5E33")
    lb_nome.config(font=("Arial", 12,"bold"))
    lb_nome.place(x=20,y= 60)

    entrada = Entry(janela, width = 20)
    entrada.place(x=72,y=60)

    botao1 = Button(janela, width = 8, text ="Cancelar", background ="#259654", command = cancel_onclick)
    botao1.place(x=72, y=100)


    botao2 = Button(janela, width = 4, text ="Ir", background ="#259654")
    botao2["command"] = partial(ir_onclick,tempo,entrada,janela)

    botao2.place(x=180, y= 100)
    
    
    
    running = True

    while running:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()   
            

        
        pygame.draw.rect(tela,(12,94,51),(240,212,540,300))
        pygame.draw.rect(tela,WHITE,[240,210,540,300],3)
        pygame.draw.rect(tela,BLACK,[237,207,545,305],2)
        pygame.draw.rect(tela,BLACK,[243,213,534,294],2)

        texto = fonte_grande.render("Parabéns", True, (255,255,255))
        texto2 = fonte_media.render("Você colocou todas as cartas nas fundações!", True, (255,255,255))
        texto3 = fonte_media.render("Deseja Cadastrar seu Tempo?", True, (255,255,255))
        texto4 = fonte_media.render("Tempo", True, (255,255,255))
        
        tela.blit(texto, [250,200])
        tela.blit(texto2, [300,350])
        tela.blit(texto3, [350,390])
        tela.blit(texto4, [468,70]) 
        
        gui_sim = botao("Sim", 530, 460, 120, 40, (12,94,51), GREEN_TABLE, tela, acao="tkinter-sim")
        gui_cancelar = botao("Não", 350, 460, 120, 40, (12,94,51), GREEN_TABLE, tela, acao="tkinter-nao")
        
        pygame.display.update()
        if gui_sim == True:
            janela.mainloop()
            gui_sim = False
            running = False
            tempos_loop()
        
        elif gui_cancelar == False:
            running = False
            game_menu()




#Função que exibe os dados do arquivo tabela_tempo.csv na tela do jogo
def tempos_loop():
    lista_nomes = pega_do_csv()
    running = True

    while running:
        
      
        tela.fill((36,150,84))

        pygame.draw.rect(tela,(12,94,51),(240,212,540,300))
        pygame.draw.rect(tela,WHITE,[240,210,540,300],3)
        pygame.draw.rect(tela,BLACK,[237,207,545,305],2)
        pygame.draw.rect(tela,BLACK,[243,213,534,294],2)

        texto = fonte_grande.render("Tempos", True, (255,255,255))
        tela.blit(texto, [270,40])
        texto2 = fonte_media.render("Nome ----------------------------- Tempo", True, (255,255,255))
        tela.blit(texto2, [280,230])

        altura = 260 
        for i in lista_nomes:
            texto_nome = fonte_media.render(i[0], True, (255,255,255))
            tela.blit(texto_nome, [280,altura])
            texto_tempo = fonte_media.render(i[1], True, (255,255,255))
            tela.blit(texto_tempo, [650,altura])
            altura += 30

    

        botao("Menu Principal", 770, 600, 170, 40, GREEN_TABLE, (12,94,51), tela, acao="Main")
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()   

        pygame.display.update()



#É chamado sempre no começo de cada loop principal
#Empilha todos os decks a partir de uma lista ordenada aleatoriamente
def empilha_decks(lista,intervalo,lista_decks):
    
    cont_aux = 0
    for i in lista_decks[:8]:
        for j in range(intervalo[cont_aux][0],intervalo[cont_aux][1]):
            i.push(lista[j])
        cont_aux += 1
 


#Verifica em qual deck(pela coordenada) o usuario quer inserir a carta
#Retorna o indice do deck escolhido
def verify(valor, cordenadas,lista_coordenadas):
    
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


#A função recebe o indice do deck selecionado e verifica se a carta pode ser inserida ou não.
def coloca_no_deck(indice,card,lista_decks, lista_coordenadas):
   
    
    carta_nova = card.split("_")

    if indice <= 11:
        if len(lista_decks[indice]) > 0:
            carta_topo =  lista_decks[indice].peek().split("_")
            verificacao_cartas = verifica_cartas(carta_nova,carta_topo)
        else:
            verificacao_cartas = True
        if len(lista_decks[indice]) < 13 and verificacao_cartas:
            if indice <= 7:
                lista_coordenadas[indice][1] += 32
                lista_decks[indice].push(card)
                return True
            else:
                if len(lista_decks[indice]) == 0:
                    lista_decks[indice].push(card)
                    return True               
            
        return False
    else:
        return coloca_fundacao(indice,card,carta_nova,lista_decks)




#Funcao que efetua a troca da carta do deck para uma das fundações
def coloca_fundacao(indice,card,carta_nova, lista_decks):
    if indice == 12:
        if len(lista_decks[12]) == 0:
            if (card == "ace_hearts"):
                lista_decks[12].push(card)
                return True
        elif lista_decks[12].peek()  != "king":
            if verifica_carta_fundacao(carta_nova,lista_decks[12].peek().split("_")):
                lista_decks[12].push(card)
                return True  

    if indice == 13:
        if len(lista_decks[13]) == 0:
            if (card == "ace_spades"):
                lista_decks[13].push(card)
                return True      
        elif lista_decks[13].peek()  != "king":
            if verifica_carta_fundacao(carta_nova,lista_decks[13].peek().split("_")):
                lista_decks[13].push(card)
                return True  

    if indice == 14:
        if len(lista_decks[14]) == 0:
            if (card == "ace_diamonds"):
                lista_decks[14].push(card)
                return True

        elif lista_decks[14].peek()  != "king":
            if verifica_carta_fundacao(carta_nova,lista_decks[14].peek().split("_")):
                lista_decks[14].push(card)
                return True  
    
    if indice == 15:
        if len(lista_decks[15]) == 0:
            if (card == "ace_clubs"):
                lista_decks[15].push(card)
                return True        
        elif lista_decks[15].peek()  != "king":
            if verifica_carta_fundacao(carta_nova,lista_decks[15].peek().split("_")):
                lista_decks[15].push(card)
                return True  
    return False

#verifica se a carta do topo do deck, e a carta que o player estiver tentando inserir
#estão em ordem decrescente, caso sim, retorna True.
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



#Verifica a carta em movimento e a carta do topo da fundação
#Caso o naipe seja o mesmo da fundação, verifica os valores.
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
    


#se as duas carta estiverem em ordem crescente (topo < carta em movimento)
#A função retorna true.
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
      

#Essa função é responsavel por controlar a remoção da carta do deck antigo
# e dentro dela, é também chamada a função que coloca no novo deck/fundacao      
def modifica_deck(deck_escolhido,cordenadas,card, lista_decks, lista_coordenadas):
    
    indice = deck_escolhido - 1
    resultado = verify(deck_escolhido, cordenadas,lista_coordenadas)
    if len(resultado) == 2:
        deck_cheio = coloca_no_deck(resultado[1], card,lista_decks, lista_coordenadas)

        if deck_cheio == False:
            lista_decks[indice].push(card)
        else:
            if indice <= 7:
                lista_coordenadas[indice][1] -=32
    else:
        lista_decks[indice].push(card)


clock = pygame.time.Clock()


#Funcao que desenha os elementos do jogo
def desenhos_em_jogo():
        #Preenche o Fundo
        tela.fill((36,150,84)) 
        
        
        #Desenho das bordas
        pygame.draw.rect(tela, (12,94,51), (0,50,1000,120))
        pygame.draw.rect(tela, WHITE, (0,52,1000,3))
        pygame.draw.rect(tela, WHITE, (0,170,1000,3))
        
        #Desenha as celulas vazias
        pygame.draw.rect(tela,BLACK,[40,65,71,96],5)
        pygame.draw.rect(tela,BLACK,[135,65,71,96],5)
        pygame.draw.rect(tela,BLACK,[230,65,71,96],5)
        pygame.draw.rect(tela,BLACK,[325,65,71,96],5)
    
        #Desenha as fundações
        pygame.draw.rect(tela,BLACK,[595,65,71,96],5)
        pygame.draw.rect(tela,BLACK,[690,65,71,96],5)
        pygame.draw.rect(tela,BLACK,[785,65,71,96],5)
        pygame.draw.rect(tela,BLACK,[880,65,71,96],5)

        #espaço dos DECKS
        pygame.draw.rect(tela,BLACK,[100,180,71,96],1)
        pygame.draw.rect(tela,BLACK,[200,180,71,96],1)
        pygame.draw.rect(tela,BLACK,[300,180,71,96],1)
        pygame.draw.rect(tela,BLACK,[400,180,71,96],1)
        pygame.draw.rect(tela,BLACK,[500,180,71,96],1)
        pygame.draw.rect(tela,BLACK,[600,180,71,96],1)
        pygame.draw.rect(tela,BLACK,[700,180,71,96],1)
        pygame.draw.rect(tela,BLACK,[800,180,71,96],1)

        #Desenha os simbolos nas fundações
        tela.blit(copas, (618,103))
        tela.blit(espadas, (715,103))
        tela.blit(ouros, (809,100))
        tela.blit(paus, (902,100))





def game_loop():
    
    global lista_cartas, clock

    #Ordena aleatoriamente a lista com todas as cartas
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
    #Armazena os intervalos em que estão os indices das cartas que serão colocadas em cada deck no inicio.
    lista_contador = [[0,6],[6,12],[12,18],[18,24],[24,31],[31,38],[38,45],[45,52]]
    
    #Lista que controla as cordenadas das cartas do topo de cada deck   
    #Incrementa a posição x, sempre que uma nova carta é colocada no deck, e decrementa quando uma é removida.
    lista_coordenadas = [[100,394],[200,394],[300,394],[400,394],[500,424],[600,424],[700,424],
                        [800,424], [40,65],[135,65],[230,65],[325,65],[595,65],[690,65],[785,65],[880,65]]
   
    
    #Controla o loop do jogo
    running = True


    #Variaveis que controlam as coordenadas da carta em movimento
    cartax = int(1000/2)
    cartay = int(600/2)
    
    #Variaveis para controle de ações com o mouse
    held = False
    controle = False
    qualquer = False

    #Empilha as cartas em cada deck
    empilha_decks(lista_cartas,lista_contador,lista_decks)

    #Variavel que controla qual deck o usuario escolheu
    deck_escolhido = 0

    #Variaveis para controle do tempo
    start_time = pygame.time.get_ticks() 
    tempo_controle_1 = True
    tempo_minutos = 0
    control = 0
    
    #Laço principal do jogo
    while running:

        #Recebe as coordenadas da posição do mouse na tela
        cordenadas = pygame.mouse.get_pos()  
        
        #Desenha os elementos na tela
        desenhos_em_jogo()

        #            Lógica de controle de tempo         #
        
        passed_time = pygame.time.get_ticks() - start_time
        tempo = int(passed_time//1000)
        
        if int(passed_time//1000) % 60 == 0 and control != int(passed_time//1000):
            tempo_minutos += 1
            tempo_controle_1 = False
            control = int(passed_time//1000)
        
        if tempo_controle_1 == False:
            tempo = int(passed_time//1000) - (tempo_minutos * 60)
        
        ###################################################
        
        
        tempo_formatado = timer(tempo,tempo_minutos)
        
        
        
        
        botao("Voltar", 870, 3, 120, 40, GREEN_TABLE, (12,94,51), tela, acao="Main")
        
        #Detecta os eventos do jogo
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                held = True
                controle = True
                
            if event.type == pygame.MOUSEBUTTONUP:
                if qualquer:
                    modifica_deck(deck_escolhido,cordenadas,card,lista_decks, lista_coordenadas)                              
                    qualquer = False 
                pygame.mouse.set_visible(True)
                held = False

        #Verifica se houve o click no mouse
        #Logo depois, verifica se o click foi em alguma carta do topo de algum deck
        #Caso sim, remove a carta do topo da pilha, e transforma ela em uma carta em movimento
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
        
        
        #percorre a pilha (serve apenas para desenhar todas as cartas dos decks na tela)
        pos_x = 100
        for deck in lista_decks[:8]: 
            deck.percorre_deck(tela,card_dicionario,pos_x)
            pos_x+= 100

        #Desenha a carta das celulas vazias, e as do topo das fundações
        indice_blit = 8
        for deck in lista_decks[8:]:
            deck.blit_carta(tela,card_dicionario,lista_coordenadas[indice_blit])
            indice_blit += 1
        
        
        #Verifica se há alguma carta em movimento, caso sim, desenha as coordenadas dela, a partir das do mouse
        if qualquer == True:
            pygame.mouse.set_visible(False)
            cartax = cordenadas[0] - (card_dicionario[card].get_width()//2)
            cartay = cordenadas[1] - (card_dicionario[card].get_height()//2)
            tela.blit(card_dicionario[card],(cartax,cartay))

    
        #Desenha o score na tela
        pontos = score(lista_decks)

        #Verifica se o usuario venceu o jogo.
        if pontos == (13 * 4):
            game_win_loop(tempo_formatado)
            running = False


        clock.tick(60)
        
        pygame.display.update()
    pygame.quit()
    quit()
game_menu(tela)
