#usr/bin/python3
# -*- coding: utf-8 -*-
import os, time 


#Este modulo destinei para todas as funções "graficas" do jogo
#Para os efeitos animados foi apenas utilizada uma função de "descanso" da biblioteca "time".

def menu(): 
    os.system('clear') 
    var = -1
    while var < 1 or var > 3:
        print("\n              \033[1;106m \033[1;37mANIMALS IN ASCII            \033[0;0m")
        print('\n\033[1;34m--------------- MENU PRINCIPAL ----------------')	
        print('\033[1;31m\n      SELECIONE UMA DAS OPCOES ABAIXO')	
        print('\n--------------- 1 INICIAR JOGO ----------------')
        print('--------------- 2 INSTRUCOES ------------------')
        print('--------------- 3 SAIR ------------------------\033[0;0m')
    
        var = int(input())
        os.system('clear') 
    return var 



def instrucoes():
    print("\n\033[1;34mINTRUÇÕES DO JOGO!")
    print("Memorize os 5 animais que aparecerem na tela")
    print("Acerte os cinco para poder ganhar!")
    print("Caso erre algum, perderá o jogo.")
    print(" (_    ,_,    _) \n       / `'--) (--'` \ \n      /  _,-'\_/'-,_  \ \n     /.-'     '     '-.\ \n ")
    print("1 - PARA VOLTAR AO MENU")
    print("2 - PARA VER TODOS OS ANIMAIS")



def loading():
      print("\033[47m\033[31m              _             _                 _                          "
        "  _     ______ _____ _____\n    /\        (_)           | |               (_)             "
        "      /\     | |   / _____|_____|_____)\n  /  \  ____  _ ____   ____| | ___            _ ____   "
        "           /  \     \ \ | /        _     _   \n / /\ \|  _ \| |    \ / _  | |/___)       "
        "   | |  _ \            / /\ \     \ \| |       | |   | |  \n| |__| | | | | | | | ( ( | | |___ |        "
        "  | | | | |          | |__| |_____) ) \_____ _| |_ _| |_ \n|______|_| |_|_|_|_|_|\_||_|_(___/          "
        " |_|_| |_|          |______(______/ \______|_____|_____)\n\033[0;0m")
      print('\033[1m                Loading . . . . .                                ')
      time.sleep(1.2)
      print('                                    ..                            ')
      time.sleep(0.2)
      print('                                      ..                      ')
      time.sleep(0.2)
      print('                                        ..              ')
      time.sleep(0.2)
      print('                                          ..      ')
      time.sleep(0.2)
      print('                                             ..      ')
      time.sleep(0.2)
      print('                                                ..      ')
      time.sleep(0.2)
      print('                                                  ..      ')
      time.sleep(0.2)
      print('                                                    ..     ')
      time.sleep(0.2)
      print('                                                       ..      ')
      time.sleep(0.5)
      print('                                                           ..     ')
      time.sleep(0.2)
      print("           __ \n      (___()'`; AU AU AU\n      /,    /`\n      \\-- \ \ \n  \033[0;0m")

      time.sleep(2)
      os.system('clear')


def gameOver():
    os.system('clear')
    print("\033[1;91m _______  _______  _______  _______    _______           _______  _______\n(  ____ \(  ___  )(       )(  ____ \  (  __"
      "_  )|\     /|(  ____ \(  ____ ) \n| (    \/| (   ) || () () || (    \/  | (   ) || )   ( || (    \/| (    )| \n | |   "
      "   | (___) || || || || (__      | |   | || |   | || (__    | (____)| \n| | ____ |  ___  || |(_)| ||  __)     | |  "
      " | |( (   ) )|  __)   |     __) \n| | \_  )| (   ) || |   | || (        | |   | | \ \_/ / | (      | (\ (    \n| (_"
      "__) || )   ( || )   ( || (____/\  | (___) |  \   /  | (____/\| ) \ \__ \n(_______)|/     \||/     \|(_______/  (__"
      "_____)   \_/   (_______/|/   \__/ \n  ")

    print(" .-.\n(o o) boo! \n| O \ \n \   \ \n  `~~~' \n")
    print("PERDESTE\n01-Para sair \n02- Jogar novamente\033[0;0m")




def logo():
    for i in range (0,3):
          print("\033[46m\033[30m              _             _                 _                          "
                "  _     ______ _____ _____\n    /\        (_)           | |               (_)             "
                "      /\     | |   / _____|_____|_____)\n  /  \  ____  _ ____   ____| | ___            _ ____   "
                "           /  \     \ \ | /        _     _   \n / /\ \|  _ \| |    \ / _  | |/___)       "
                "   | |  _ \            / /\ \     \ \| |       | |   | |  \n| |__| | | | | | | | ( ( | | |___ |        "
                "  | | | | |          | |__| |_____) ) \_____ _| |_ _| |_ \n|______|_| |_|_|_|_|_|\_||_|_(___/          "
                " |_|_| |_|          |______(______/ \______|_____|_____)\033[0;0m\n")
          time.sleep(0.5)
          os.system("clear")
          time.sleep(0.3)


def venceste():
    print("	\033[1;93mParabéns venceste o jogo!!!\033[0;0m")
    print("")
    print("  o  \ o / _ o       __|   \ /    |__      o _ \ o /  o\n /|\   |    /\  ___\o  \o   |"
      "   o/   o/__  /\    |   /|\ \n / \  / \  | \ /)  |   ( \ /o\ / )   |  (\ / |  / \  / \ \n ")


def contagem():
        print('  \033[1;34m             READY?                                ')
        time.sleep(1)
        print('                    1                         ')
        time.sleep(0.8)
        print('                    2                    ')
        time.sleep(0.8)
        print('                    3              \033[0;0m')
        time.sleep(0.8)
        print('\033[1;95m("\|/        (__)\n     `\------(oo) \n       ||    (__) Mooooo\n       ||w--||     \|/ \n   \|/ \n \033[0;0m ")                        ')
        time.sleep(1)
        print('   \033[1;36m                 GO!!! \033[0;0m	')
        time.sleep(1)
        os.system('clear')