import pygame
import time
import random
from queue_snake import Queue





# Modulo que inicia o pygame retorna uma tupla (6,0) caso tenha iniciado corretamente
# A tupla (6,0) significando 6 processos iniciados corretamentes e 0 com erros.
pygame.init()



# Carregando as imagens utilizadas no jogo
grama = pygame.image.load('grama.jpg')

relampago = pygame.image.load('relampagoTrans.png')

gramaObj = pygame.image.load('gramaObj.jpg')



# Cores são declaradas por meio de tuplas com valores (R,G,B)
WHITE = (255,255,255)
WHITE2 = (220,220,220)
BLACK = (0,0,0)
RED = (102,0,0)
RED2 = (200,0,0)
redOver = (225,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (102,120,0)
ORANGE = (255,165,0)
LIGHT_BLUE = (0,191,255)
GRAY = (112,128,144)
AQUAMARINE = (127,255,212)
GREEN_YELLOW = (173,255,47)
SIENNA = (160,82,45)
MAGENTA = (255,0,255)
PINK = (255,20,147)
INDIGO = (138,43,226)


# É uma lista auxiliar que será utilizada para sortear uma dessas cores. 
listaCores = [RED2,ORANGE,LIGHT_BLUE,GRAY,GREEN_YELLOW,SIENNA,INDIGO,PINK,WHITE2]


# Constantes pra altura e largura do jogo
LARGURA = 800
ALTURA = 600


# Inicializo a fila que vou usar para a cobra
fila = Queue()



# Aqui crio uma superficie para o jogo, com as medidas de Largura e Altura
# E logo abaixo o titulo do jogo
superficie = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("SNAKE GAME")



# Função que atualiza tudo que foi desenhado na superficie (nesse caso a superficie)
pygame.display.update()



# Variavel constante para o tamanho de cada bloco da cobra
tamanho_bloco = 20


# Relogio para definir a quantos frames por segundo o jogo irá funcionar.  
# A variavel FPS é usada como velocidade nesse jogo
clock = pygame.time.Clock()
FPS = 12


# Essas são as fontes utilizadas nos textos dos jogos. Todas estão na mesma pasta desse arquvio. 
fonte_pequena = pygame.font.Font("MarioLuigi2.ttf",25)
fonte_media = pygame.font.Font("MarioLuigi2.ttf",50)
fonte_grande = pygame.font.Font("MarioLuigi2.ttf",80)

angry_font = pygame.font.Font("angrybirds-regular.ttf",25)
angryG_font = pygame.font.Font("angrybirds-regular.ttf",40)
gta_font = pygame.font.Font("pricedow.ttf", 55)
gtaB_font = pygame.font.Font("pricedow.ttf",200)



# Função que retorna uma tupla(R,G,B) com a cor aleatoria
def corAleatoria():
    random.shuffle(listaCores)
    return listaCores[0]



# Caso aperte P, o usuario poderá pausar o jogo
def pause():
    resume = False    
    
    
    pygame.display.update()

    while not resume:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if botao("Resume", 278, 450, 250, 50, RED, GREEN, acao="resume" ):
            resume = True
        mensagem("Pausado",WHITE, deslocamento_y = -50, tamanho = "gta")
        pygame.display.update()

        clock.tick(15)



# Função que desenha o placar durante o jogo.
def score(pontuacao):
    texto =angry_font.render("Score: " + str(pontuacao), True, WHITE)
    superficie.blit(texto, [0,0])




# Aqui é criada a função que define a velocidade da cobra, a cada 3 de FPS a velocidade aumenta em 1x
def velocidade(FPS):
    velocidade = FPS
    var = 1
    while velocidade > 15:
        velocidade -= 3
        var += 1        

    texto = angry_font.render("Velocidade: " + str(var) + 'x', True, WHITE)
    superficie.blit(texto, [150,0])
    


# Utilizo as fontes declaradas no inicio para definir algumas formas de texto
# Retorno o texto com a fonte escolhida o tamanho e a cor, além da posição que se encontra o texto
def formata_texto(texto,cor,tamanho):
    if tamanho == "pequeno":
        textosuperficie = fonte_pequena.render(texto, True, cor)
    if tamanho == "medio":
        textosuperficie = fonte_media.render(texto, True, cor)
    if tamanho == "grande":
        textosuperficie = fonte_grande.render(texto, True, cor)
    if tamanho == "angry":
        textosuperficie = angryG_font.render(texto, True, cor)
    if tamanho == "angrym":
        textosuperficie = angry_font.render(texto, True, cor)
    if tamanho == "gta":
        textosuperficie = gta_font.render(texto, True, cor)
    if tamanho == "gtab":
        textosuperficie = gtaB_font.render(texto, True, cor)
    return textosuperficie, textosuperficie.get_rect()



# Função que cria o desenho de um botão na tela
# É utilizada a função anterior para o texto dentro do botão
def botao_texto(msg,cor,botao_x,botao_y,botao_largura,botao_altura,tamanho = "pequeno"):
    superficieTexto, textoRect = formata_texto(msg,cor,tamanho)
    textoRect.center = ((botao_x+(botao_largura/2)), (botao_y+(botao_altura/2)))
    superficie.blit(superficieTexto, textoRect)



# Função que desenha uma mensagem centralizada na tela, com ela você pode definir a altura da mensagem a partir
# do parametro deslocamento.
def mensagem(msg,cor, deslocamento_y = 0,tamanho = 'pequeno'):
    
    superficieTexto, textoRect = formata_texto(msg,cor,tamanho)
    textoRect.center = (LARGURA/2), (ALTURA/2) + deslocamento_y
    superficie.blit(superficieTexto, textoRect)



# Funçao que cria os efeitos e a funcionalidade de um botão, é obtido o click e a posição do mouse
# com isso é possivel fazer algumas animações, além da função também receber uma ação, a que o botão é designado
def botao(texto,x,y,largura,altura,cor_inativa,cor_ativa,acao = None):
    
    cursor = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()
    
    # Verifica se o mouse esta ou nao sobre o botao
    if x + largura > cursor[0] > x and y + altura > cursor[1]> y:
        pygame.draw.rect(superficie, cor_ativa,(x,y,largura,altura))
        
        if click[0] == 1 and acao != None: # Verifica a ação e executa o que lhe é pedido.
            if acao == "quit":
                pygame.quit()
                quit()
            if acao == "objetivos":
                instrucoes()
            if acao == "play":
                gameLoop()
            if acao == "Main":
                game_menu()
            if acao == "novamente":
                direction = "direita"
                gameLoop()
            if acao == 'resume':
                return True
            if acao == 'menu':
                game_menu()
    else:
        pygame.draw.rect(superficie, cor_inativa,(x,y,largura,altura))
    botao_texto(texto,WHITE,x,y, largura, altura)  #É aqui o desenho do botão, com o uso a função anterior.


# Essa é a função de menu, utilizo botões e mensagens no texto
# o numero grande de variaveis é devido as animações que criei para o menu
def game_menu():
    
    menu = True

    var1 = 0
    var2 = 0
    l_1 = 700
    l_2 = 70
    
    control_a = -80
    while menu:

        superficie.blit(grama,(0,0))
        
        COR1 = RED
        COR2 = BLUE
        COR3 = YELLOW
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mensagem("S                        ", GREEN, deslocamento_y= -250, tamanho = "medio")
        mensagem("  N                    ", RED, deslocamento_y= -250, tamanho = "medio")
        mensagem("    A                ", BLUE, deslocamento_y= -250, tamanho = "medio")
        mensagem("      K            ", YELLOW, deslocamento_y= -250, tamanho = "medio")
        mensagem("        E        ", WHITE, deslocamento_y= -250, tamanho = "medio")
        mensagem("                       G              ", PINK, deslocamento_y= -250, tamanho = "medio")
        mensagem("                         A          ", INDIGO, deslocamento_y= -250, tamanho = "medio")
        mensagem("                           M      ", SIENNA, deslocamento_y= -250, tamanho = "medio")
        mensagem("                             E  ", LIGHT_BLUE, deslocamento_y= -250, tamanho = "medio")
        
        botao("PLAY", 280, 150, 250, 50, RED, GREEN, acao="play" )
        botao("INSTRUCOES",280,250,250,50,BLUE, GREEN,acao= "objetivos")
        botao("SAIR",280,350,250,50,YELLOW, GREEN,acao="quit")
            
        mensagem("© uespi.com, 2019 Developed by @juneco_r/Gabriel Marinho", WHITE, deslocamento_y= 281 , tamanho = "angrym")
        
        
        
        
        cursor = pygame.mouse.get_pos()

        click = pygame.mouse.get_pressed()

        if 280 + 250 > cursor[0] > 280 and 150 + 50 > cursor[1]> 150:
            superficie.blit(relampago,(l_1 + 40, 155))
            superficie.blit(relampago,(l_2 - 40, 155))
            superficie.blit(relampago,(l_1 + 80, 155))
            superficie.blit(relampago,(l_2 - 80, 155))

        if 280 + 250 > cursor[0] > 280 and 250 + 50 > cursor[1]> 250:
            superficie.blit(relampago,(l_1 + 40, 255))
            superficie.blit(relampago,(l_2 - 40, 255))
            superficie.blit(relampago,(l_1 + 80, 255))
            superficie.blit(relampago,(l_2 - 80, 255))
        if 280 + 250 > cursor[0] > 280 and 350 + 50 > cursor[1]> 350:
            superficie.blit(relampago,(l_1 + 40, 355))
            superficie.blit(relampago,(l_2 - 40, 355))
            superficie.blit(relampago,(l_1 + 80, 355))
            superficie.blit(relampago,(l_2 - 80, 355))

        superficie.blit(relampago,(l_1, 155))
        superficie.blit(relampago,(l_2, 155))
        superficie.blit(relampago,(l_1, 255))
        superficie.blit(relampago,(l_2, 255))
        superficie.blit(relampago,(l_1, 355))
        superficie.blit(relampago,(l_2, 355))

        l_1 -= 10
        l_2 += 10
        if l_1 <= 540:
            l_1 = 700

        if l_2 >= 230:
            l_2 = 70


        
        if control_a < 800:
            control_a += 10
        else:
            control_a = -80

        pygame.draw.rect(superficie, RED, [control_a, 480, 20, 20])
        pygame.draw.rect(superficie, GREEN, [control_a+20, 480, 20, 20])
        pygame.draw.rect(superficie, BLUE, [control_a+40, 480, 20, 20])
        pygame.draw.rect(superficie, MAGENTA, [control_a+60, 480, 20, 20])
        pygame.draw.rect(superficie, SIENNA, [control_a+80, 480, 20, 20])


        
        pygame.display.update()
        clock.tick(10)



# As instruções são desenhadas na tela
def instrucoes():
    instrucoes = True
    while instrucoes:
        superficie.blit(gramaObj,(0,0))

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
        mensagem("INSTRUÇÕES", WHITE, deslocamento_y= -260, tamanho='gta')

        mensagem("- Faça o maximo de pontos que você conseguir", BLACK, deslocamento_y= -200, tamanho='angrym')
        mensagem("- A dificuldade do jogo aumenta com base nas suas decisões", BLACK, deslocamento_y= -155, tamanho='angrym')
        mensagem("- Se mantenha dentro dos limites da tela do jogo", BLUE, deslocamento_y= -110, tamanho='angrym')
        mensagem("- A cada pedaço comido, a velocidade do jogo aumenta", BLUE, deslocamento_y= -65, tamanho='angrym')
        mensagem("- Comer um pedaço igual a cabeça o fará perder pontos e a cabeça", BLUE, deslocamento_y= -15, tamanho='angrym')
        superficie.blit(relampago,(632,310))
        mensagem("- Escolha entre perder a cabeça, ou comer o Raio      ", RED, deslocamento_y= 30, tamanho='angrym')
        mensagem("- O Raio vale mais pontos, mas aumenta sua velocidade em 1x", RED, deslocamento_y= 75, tamanho='angrym')
        mensagem("- A velocidade nunca diminui", RED, deslocamento_y= 120, tamanho='angrym')

        
    
        botao("Voltar", 280, 500, 250,50, RED, GREEN, acao= "menu"  )
        
        pygame.display.update()
        clock.tick(10)


# LAÇO PRINCIPAL DO JOGO
def gameLoop():
    
    global direction, fila, FPS
    
    # Variaveis onde controlo a situação do jogo
    # Fim de jogo e Game Over
    gameExit = False
    gameOver = False

    # Variavel que controla o texto que será exibido no gameOver
    over = "Fim da linha"
    
    # Variaveis que controlam as cordenadas dos pedaços da cobra.
    direcao_x = LARGURA/2
    direcao_y = ALTURA/2

    # Variaveis que modificam as cordenadas
    direcao_x_mudanca = tamanho_bloco
    direcao_y_mudanca = 0 

    # Variaveis que controlam a posição da comida no mapa
    # As cordenadas são aleatorias
    randMacaX = (round(random.randrange(0,LARGURA))//20) * 20
    randMacaY = (round(random.randrange(0,ALTURA))//20) * 20

    # Variaveis que controlam a posição do raio no jogo
    # as coordenadas sao obtidas aleatoriamente
    bonusX = (round(random.randrange(0,LARGURA))//40) * 40
    bonusY = (round(random.randrange(0,ALTURA))//40) *  40


    # Variavel que armazena a pontuação no jogo
    pontuacao = 0

    # Variavel que controla o tamanho da cobra (é melhor explicada na frente)
    snakeTamanho = 1


    # Variaveis que são utilizadas para as cores da comida
    cor = corAleatoria()
    cor2 = corAleatoria()
    
    # Lista auxiliar que controla as cores de cada pedaço da cobra
    lista = [cor]

    
    # Laço Principal
    while not gameExit:

        
        # Mensagem de game Over na tela
        if gameOver == True:
            fila = Queue() # A fila é novamente declarada para voltar a ser vazia.
            mensagem("Game Over",redOver, deslocamento_y = -100, tamanho = "gtab")
            mensagem(over,WHITE, deslocamento_y = 40, tamanho = "gta")
            
            pygame.display.update()
        
        
        # Laço que controla a situação de gameOver
        # Desenha os botões na tela e espera uma ação do Usuario
        while gameOver == True:
            

            FPS = 12
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
  
            botao("Jogar Novamente", 100, 400, 250, 50, RED, GREEN, acao="novamente" )
            botao("Menu",450,400,250,50,BLUE, GREEN,acao= "Main")

            pygame.display.update()

        # Aqui controlo os eventos do jogo
        for event in pygame.event.get():

            # Caso o usuario queira sair, ele sai do laço principal e finaliza o programa
            if event.type == pygame.QUIT:
                gameExit = True
            # Verifica se o evento obtido no get() foi de uma tecla que foi pressionada.   
            if event.type == pygame.KEYDOWN:

                # Em cada verificação de tecla a cordenada que corresponde a direção equivalente  recebe o tamanho do bloco
                # As duas são usadas posteriormente pra efetuar o movimento da cobra
                
                # Verifica se a tecla pressionada foi a seta esquerda
                if event.key == pygame.K_LEFT:
                    direcao_x_mudanca = - tamanho_bloco  
                    direcao_y_mudanca  = 0
                
                # Verifica se foi a seta direita    
                elif event.key == pygame.K_RIGHT:
                    direcao_x_mudanca = tamanho_bloco
                    direcao_y_mudanca  = 0
                    
                # Verifica se foi a seta pra cima
                elif event.key == pygame.K_UP:
                    direcao_y_mudanca = - tamanho_bloco
                    direcao_x_mudanca  = 0
                    
                # Verifica se foi a seta pra baixo
                elif event.key == pygame.K_DOWN:
                    direcao_y_mudanca = tamanho_bloco
                    direcao_x_mudanca  = 0
                
                # Verifica se o usuario pressionou a tecla p, que chama a função que pausa o jogo   
                elif event.key == pygame.K_p:
                    pause()


        # Aqui é onde ocorre a atualização das coordenas da cabeça, 
        # a cada repetição do laço as cordenadas x e y mudam
        # As variaveis incrementam sempre na direçao que o usuario selecionou 
        direcao_x += direcao_x_mudanca
        direcao_y += direcao_y_mudanca
        

        # Essa parte verifica a colisão da cobra com a parede, caso as cordenadas ultrapassem
        # a largura ou a altura maxima do jogo, a variavel de controle GameOVer é acionada.
        if direcao_x >= LARGURA or direcao_x < 0 or direcao_y >= ALTURA or direcao_y <0:
            over = "Preste atenção por onde anda"
            gameOver = True
            

        # Aqui é onde desenho a imagem de fundo durante o jogo
        superficie.blit(grama,(0,0))
        
        # Aqui é o retangulo da comida, que recebe como parametros as cordenadas aleatorias e a cor aleatoria
        pygame.draw.rect(superficie, cor2, [randMacaX, randMacaY, tamanho_bloco, tamanho_bloco])

        
        
        # USO DA FILA PARA O CRESCIMENTO E MOVIMENTO DA COBRA

        fila.push(direcao_x,direcao_y)  # Adiciono as novas cordenadas no fim da fila (cabeça)
        
        if len(fila) > snakeTamanho:    # Verifico se o tamanho da fila é maior que o da cobra
            
            fila.pop()                  # caso seja, removo o primeiro elemento (cordenadas mais antigas ou seja, o rabo)
        
        # caso a variavel snakeTamanho seja maior, então ele não removerá o rabo
        # o rabo continuará com as mesmas cordenadas, mas a  nova cabeça
        # continuará tendo sido adicionada, ou seja, o tamanho da cobra/fila aumentará
        
        
        
        
        # Esse metodo imprime a cobra no jogo, é explicada no arquivo da classe Queue
        fila.showCobra(tamanho_bloco,superficie,lista)
        
        # FUnção que desenha o score na tela
        score(pontuacao)

        # FUncao que desenha a velocidade na tela
        velocidade(FPS)
        
        # Metodo que verifica se a cabeça da cobra colidiu com alguma outra parte dela
        # logo apos chama o gameOver
        if fila.colisao():
            over = "Cuidado com a cabeça"
            gameOver = True


        # É aqui que verifico a colisão entre  a cabeça da cobra e o pedaço de comida
        # Verifico usando os intervalos entre as cordenadas, de uma extremidade a outra (tamanho do bloco é 20)
        # Caso fizesse +20, passar do lado de uma das extremidades também contaria como colisão
        if direcao_x >= randMacaX and direcao_x <= randMacaX + 19:
            if direcao_y >= randMacaY and direcao_y <= randMacaY + 19:
                
                # Caso entre aqui, ele sorteara novas cordenadas para a nova comida
                # e também para o proximo raio (que pode ou não ser desenhado na tela)
                randMacaX = round(random.randrange(0,LARGURA - 20)//20) * 20
                randMacaY = round(random.randrange(0,ALTURA - 20)//20) * 20
                bonusX = (round(random.randrange(0,LARGURA-40))//40) * 40
                bonusY = (round(random.randrange(0,ALTURA-40))//40) *  40
                
                # caso a cabeça da cobra seja da mesma cor que o pedaço de comida
                if lista[0] == cor2:
                    
                    # caso o usuario tenha comido um pedaço igual a cabeça no começo
                    if len(fila) == 1:  
                        over = "Voce fez uma pessima escolha"
                        gameOver = True 
                   
                   # Diminui o tamanho da fila (cobra) e retira a cor da cabeça, além de diminuir a pontuação     
                    else:
                        
                        pontuacao -= 100 if pontuacao >= 100 else pontuacao 
                        fila.pop()      
                        del[lista[0]]   
                        snakeTamanho -= 1  
                
                
                # Caso ele tenha comido um pedaço de cor diferente da cabeça
                # O tamanho da cobra aumenta e a nova cor é adicionada na lista e vira a cor do novo rabo
                else: 
                    
                    pontuacao += 13 
                    snakeTamanho +=1    
                    lista.append(cor2)  
                    FPS += 0.3         
                cor2 = corAleatoria()   
                

        # Aqui também verifico se a cor da cabeça é igual a da comida]
        # caso seja a parte de dentro desenha o raio na tela e verifica se houve alguma colisão com ele        
        if (cor2 == lista[0]) and gameOver == False:
            
            # Desenha o raio na tela
            superficie.blit(relampago, (bonusX, bonusY))
            
            # Verifica uma colisão com o raio.
            if direcao_x >= bonusX and direcao_x <= bonusX + 40:
                if direcao_y >= bonusY and direcao_y <= bonusY + 40:
                    
                    # Incrementa o fps (mais que o normal)
                    FPS += 3
                    
                    pontuacao += 25 
                    
                    # Obtem novas cordenadas para o proximo raio
                    bonusX = (round(random.randrange(0,LARGURA))//40) * 40
                    bonusY = (round(random.randrange(0,ALTURA))//40) *  40
                    
                    # obtem novas cordenadas para a proxima maça
                    randMacaX = round(random.randrange(0,LARGURA - 20)//20) * 20
                    randMacaY = round(random.randrange(0,ALTURA - 20)//20) * 20
                    
                    # obtem nova cor para a proxima maça
                    cor2 = corAleatoria()
            
                
                
        # Atualiza a tela com todos os eventos que aconteceram durante uma repetição
        pygame.display.update()
        
        # Define o clock do jogo com o FPS (velocidade)
        clock.tick(FPS)
    
    # Caso saia do laço o jogo é finalizado
    pygame.quit()
    quit()
game_menu()
