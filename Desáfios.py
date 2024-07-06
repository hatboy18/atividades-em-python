import random
import time

from pygame import mixer


#coisa a adicionar: Classe de armadura e Sistema de ataques diferentes que usam mana
ataquesuper = random.randint(0,1)
manaJ = 1
vidaJogador = 10
ataqueJogador = 15
classeArmJog = 4
vidaMonstro = 15
ataqueMonstro = 10
classeArMon = 6

mixer.init()
mixer.music.load('menu.mp3')
mixer.music.play(-1)

def vitoria():
    mixer.stop()
    mixer.init()
    mixer.music.load('vitoria.mp3')
    mixer.music.play(1)
    
def derrota():
    mixer.stop()
    mixer.init()
    mixer.music.load('gameover.mp3')
    mixer.music.play(1)


menu = int (input('''

Bem Vindo
(1) Jogar
(2) Sair
(3) Créditos

'''))
match menu:
    case 1:
        mixer.stop()
        mixer.init()
        mixer.music.load('fundo.mp3')
        mixer.music.play(-1)
        print('Bem vindo ao jogo')
        print()
        print('Você tem 10 de HP, 1d15 de dano e 5d5 de ataque especial porém gasta mana')
        print('O monstro tem 15 de HP e 1d10 de dano')
        print()
        while True:
            jogada = int (input('Digite 1 para atacar o monstro:'))
            match jogada:
                case 1:
                    ataqueJ_Sound = mixer.Sound('danoM.mp3')
                    ataqueJ_Sound.play()
                    ataqueJogador = random.randint(0, 15)
                    if ataqueJogador <= classeArMon:
                        print(f'Você errou o ataque')
                    else:
                        vidaMonstro = vidaMonstro - ataqueJogador
                    print('')
                    time.sleep(0.5)
                    if ataqueJogador > classeArMon:
                        print(f'\33[31m Você tirou {ataqueJogador} de hp do monstro\33[m')
                    print(f'O monstro esta com {vidaMonstro} de vida')
                    time.sleep(0.5)
                    print('')
                    if vidaMonstro <= 0:
                        monstro_Sound = mixer.Sound('monstroD.mp3')
                        monstro_Sound.play()
                        time.sleep(4)
                        vitoria()
                        print("\33[32mVocê derrotou o Monstro Parabéns!!!\33[m")
                        time.sleep(10)
                        apar = 3 #random.randint(0,3)
                        match apar:
                            case 3:
                                print('Outro monstro apareceu!!!')
                                vidaMonstro = 25
                                mixer.init()
                                mixer.music.load('fundo.mp3')
                                mixer.music.play(-1)
                                ataq = int(input('digite 2 para usar ataque especial: '))
                                match ataq:
                                    case 2:
                                        contdemage = 0
                                        for _ in range (0,5):
                                            espec = random.randint(1,5)
                                            contdemage += espec
                                        ataqueJ_Sound.play()
                                        vidaMonstro =  vidaMonstro - contdemage  
                                        print(f'O monstro esta com {vidaMonstro} de vida')
                                        if vidaMonstro <= 0:
                                            monstro_Sound = mixer.Sound('monstroD.mp3')
                                            monstro_Sound.play()
                                            time.sleep(4)
                                            vitoria()
                                            print("\33[32mVocê derrotou o Monstro Parabéns!!!\33[m")
                                            time.sleep(10)
                                            break
                                        else:
                                            print('Turno do monstro')
                                            print('')
                                            ataqueMonstro = random.randint(0,10)
                                            if ataqueMonstro <= classeArmJog:
                                                print('O monstro errou o ataque')
                                            else:
                                                vidaJogador = vidaJogador - ataqueMonstro
                                            ataqueM_Sound = mixer.Sound('danoP.mp3')
                                            ataqueM_Sound.play()
                                            time.sleep(0.8)
                                            if ataqueMonstro > classeArmJog:
                                                print(f"\33[31mo montro te tirou {ataqueMonstro} de hp\33[m")
                                            print(f'você está com {vidaJogador} de vida')
                                            time.sleep(0.5)
                                            print('')
                                            if vidaJogador <= 0: 
                                                playerdeath = mixer.Sound('playerdeath.mp3')
                                                playerdeath.play()
                                                time.sleep(2)
                                                derrota()
                                                print('\33[31mVocê foi derrotado Game Over!!!\33[m') 
                                                time.sleep(7)
                                                break
                            case _:
                                break
                    else:
                        print('Turno do monstro')
                        print('')
                        ataqueMonstro = random.randint(0,10)
                        if ataqueMonstro <= classeArmJog:
                            print('O monstro errou o ataque')
                        else:
                            vidaJogador = vidaJogador - ataqueMonstro
                        ataqueM_Sound = mixer.Sound('danoP.mp3')
                        ataqueM_Sound.play()
                        time.sleep(0.8)
                        if ataqueMonstro > classeArmJog:
                            print(f"\33[31mo montro te tirou {ataqueMonstro} de hp\33[m")
                        print(f'você está com {vidaJogador} de vida')
                        time.sleep(0.5)
                        print('')
                        if vidaJogador <= 0: 
                            playerdeath = mixer.Sound('playerdeath.mp3')
                            playerdeath.play()
                            time.sleep(2)
                            derrota()
                            print('\33[31mVocê foi derrotado Game Over!!!\33[m') 
                            time.sleep(7)
                            break
                case _:
                    print("\33[31mVocê errou o ataque \nagora é a vez do monstro\33[m")
                    print('')
                    print('Turno do monstro')
                    print('')
                    ataqueMonstro = random.randint(0,10)
                    vidaJogador = vidaJogador - ataqueMonstro
                    ataqueM_Sound = mixer.Sound('danoP.mp3')
                    ataqueM_Sound.play()
                    time.sleep(0.8)
                    print(f"\33[31mO montro te tirou {ataqueMonstro} de hp\33[m")
                    print(f'você está com {vidaJogador} de vida')
                    time.sleep(0.5)
                    print('')
                    if vidaJogador <= 0: 
                        playerdeath = mixer.Sound('playerdeath.mp3')
                        playerdeath.play()
                        time.sleep(2)
                        derrota()
                        print('\33[31mVocê foi derrotado Game Over!!!\33[m') 
                        time.sleep(7)
                        break
    case 2:
        print("DESLIGANDO...")

