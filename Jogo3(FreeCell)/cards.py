import pygame
pygame.init()    
pygame.display.set_mode((1000,600))
card_dicionario = {}
    
#Aqui estão todas as imagens utilizadas no jogo, as instancias são armazenadas em um dicionario
#As chaves também são armazenadas em uma lista.

img = pygame.image.load("playing_cards/ace_clubs.png").convert()
card_dicionario["ace_clubs"] = img
img = pygame.image.load("playing_cards/2_clubs.png").convert()
card_dicionario["2_clubs"] = img
img = pygame.image.load("playing_cards/3_clubs.png").convert()
card_dicionario["3_clubs"] = img
img = pygame.image.load("playing_cards/4_clubs.png").convert()
card_dicionario["4_clubs"] = img
img = pygame.image.load("playing_cards/5_clubs.png").convert()
card_dicionario["5_clubs"] = img
img = pygame.image.load("playing_cards/6_clubs.png").convert()
card_dicionario["6_clubs"] = img
img = pygame.image.load("playing_cards/7_clubs.png").convert()
card_dicionario["7_clubs"] = img
img = pygame.image.load("playing_cards/8_clubs.png").convert()
card_dicionario["8_clubs"] = img
img = pygame.image.load("playing_cards/9_clubs.png").convert()
card_dicionario["9_clubs"] = img
img = pygame.image.load("playing_cards/10_clubs.png").convert()
card_dicionario["10_clubs"] = img
img = pygame.image.load("playing_cards/jack_clubs.png").convert()
card_dicionario["jack_clubs"] = img
img = pygame.image.load("playing_cards/queen_clubs.png").convert()
card_dicionario["queen_clubs"] = img
img = pygame.image.load("playing_cards/king_clubs.png").convert()
card_dicionario["king_clubs"] = img
img = pygame.image.load("playing_cards/ace_spades.png").convert()
card_dicionario["ace_spades"] = img
img = pygame.image.load("playing_cards/2_spades.png").convert()
card_dicionario["2_spades"] = img
img = pygame.image.load("playing_cards/3_spades.png").convert()
card_dicionario["3_spades"] = img
img = pygame.image.load("playing_cards/4_spades.png").convert()
card_dicionario["4_spades"] = img
img = pygame.image.load("playing_cards/5_spades.png").convert()
card_dicionario["5_spades"] = img
img = pygame.image.load("playing_cards/6_spades.png").convert()
card_dicionario["6_spades"] = img
img = pygame.image.load("playing_cards/7_spades.png").convert()
card_dicionario["7_spades"] = img
img = pygame.image.load("playing_cards/8_spades.png").convert()
card_dicionario["8_spades"] = img
img = pygame.image.load("playing_cards/9_spades.png").convert()
card_dicionario["9_spades"] = img
img = pygame.image.load("playing_cards/10_spades.png").convert()
card_dicionario["10_spades"] = img
img = pygame.image.load("playing_cards/jack_spades.png").convert()
card_dicionario["jack_spades"] = img
img = pygame.image.load("playing_cards/queen_spades.png").convert()
card_dicionario["queen_spades"] = img
img = pygame.image.load("playing_cards/king_spades.png").convert()
card_dicionario["king_spades"] = img
img = pygame.image.load("playing_cards/ace_hearts.png").convert()
card_dicionario["ace_hearts"] = img
img = pygame.image.load("playing_cards/2_hearts.png").convert()
card_dicionario["2_hearts"] = img
img = pygame.image.load("playing_cards/3_hearts.png").convert()
card_dicionario["3_hearts"] = img
img = pygame.image.load("playing_cards/4_hearts.png").convert()
card_dicionario["4_hearts"] = img
img = pygame.image.load("playing_cards/5_hearts.png").convert()
card_dicionario["5_hearts"] = img
img = pygame.image.load("playing_cards/6_hearts.png").convert()
card_dicionario["6_hearts"] = img
img = pygame.image.load("playing_cards/7_hearts.png").convert()
card_dicionario["7_hearts"] = img
img = pygame.image.load("playing_cards/8_hearts.png").convert()
card_dicionario["8_hearts"] = img
img = pygame.image.load("playing_cards/9_hearts.png").convert()
card_dicionario["9_hearts"] = img
img = pygame.image.load("playing_cards/10_hearts.png").convert()
card_dicionario["10_hearts"] = img
img = pygame.image.load("playing_cards/jack_hearts.png").convert()
card_dicionario["jack_hearts"] = img
img = pygame.image.load("playing_cards/queen_hearts.png").convert()
card_dicionario["queen_hearts"] = img
img = pygame.image.load("playing_cards/king_hearts.png").convert()
card_dicionario["king_hearts"] = img
img = pygame.image.load("playing_cards/ace_diamonds.png").convert()
card_dicionario["ace_diamonds"] = img
img = pygame.image.load("playing_cards/2_diamonds.png").convert()
card_dicionario["2_diamonds"] = img
img = pygame.image.load("playing_cards/3_diamonds.png").convert()
card_dicionario["3_diamonds"] = img
img = pygame.image.load("playing_cards/4_diamonds.png").convert()
card_dicionario["4_diamonds"] = img
img = pygame.image.load("playing_cards/5_diamonds.png").convert()
card_dicionario["5_diamonds"] = img
img = pygame.image.load("playing_cards/6_diamonds.png").convert()
card_dicionario["6_diamonds"] = img
img = pygame.image.load("playing_cards/7_diamonds.png").convert()
card_dicionario["7_diamonds"] = img
img = pygame.image.load("playing_cards/8_diamonds.png").convert()
card_dicionario["8_diamonds"] = img
img = pygame.image.load("playing_cards/9_diamonds.png").convert()
card_dicionario["9_diamonds"] = img
img = pygame.image.load("playing_cards/10_diamonds.png").convert()
card_dicionario["10_diamonds"] = img
img = pygame.image.load("playing_cards/jack_diamonds.png").convert()
card_dicionario["jack_diamonds"] = img
img = pygame.image.load("playing_cards/queen_diamonds.png").convert()
card_dicionario["queen_diamonds"] = img
img = pygame.image.load("playing_cards/king_diamonds.png").convert()
card_dicionario["king_diamonds"] = img


lista_cartas = ["ace_clubs","2_clubs","3_clubs","4_clubs","5_clubs","6_clubs",
        "7_clubs","8_clubs","9_clubs","10_clubs","jack_clubs","queen_clubs",
        "king_clubs","ace_spades","2_spades","3_spades","4_spades",
        "5_spades","6_spades","7_spades","8_spades","9_spades","10_spades",
        "jack_spades","queen_spades","king_spades","ace_hearts","2_hearts",
        "3_hearts","4_hearts","5_hearts","6_hearts","7_hearts","8_hearts",
        "9_hearts","10_hearts","jack_hearts","queen_hearts","king_hearts",
        "ace_diamonds","2_diamonds","3_diamonds","4_diamonds","5_diamonds",
        "6_diamonds","7_diamonds","8_diamonds","9_diamonds","10_diamonds",
        "jack_diamonds","queen_diamonds","king_diamonds"]