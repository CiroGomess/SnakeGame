from ast import While
from asyncio import events
from email.mime import image
import pygame

from pygame.locals import *
from sys import exit  # função para fechar janela
from random import randint


def skaner_gamer(num):

    pygame.init()  # Iniciando o pygame

    # Musica do jogo
    pygame.mixer.music.set_volume(0.5)
    musica_fundo = pygame.mixer.music.load(
        './music/Linn Friberg - Learning From Mistakes.mp3')
    pygame.mixer.music.play(-1)
    som_colisao = pygame.mixer.Sound('./music/smw_yoshi_spit.wav')

    largura = 640
    altura = 480

    # centrlizado objeto na tela
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)

    velocidade = 10
    x_controle = velocidade
    y_controle = 0

    x_fruta = randint(40, 600)
    y_fruta = randint(50, 430)

    x_bomba = randint(40, 600)
    y_bomba = randint(50, 430)

    pontos = 0

    lista_cobra = []
    comprimento_inicial = 5
    morreu = False

   
    img_py_fruta = pygame.image.load('./imgs/img_py.png') # Fruta_python
    bomba = pygame.image.load('./imgs/bomba.png')  # Bomba
    bg_img = pygame.image.load('./imgs/bg_snaker.png')   # Background

    img_py_fruta = pygame.transform.scale(img_py_fruta, (20, 20))
    bomba = pygame.transform.scale(bomba, (20, 20))

    fonte = pygame.font.SysFont('arial', 18, True, False)

    # Defenindo largura e altura da tela
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Snake Game')  # Definindo nome do jogo
    relogio = pygame.time.Clock()  # Frame

    pygame.display.set_caption('Sprites')

    if num == 1:

        def aumentando_cobra(lista_cobra):
            for XeY in lista_cobra:
                pygame.draw.rect(tela, (0, 255, 255), (XeY[0], XeY[1], 20, 20))

        def dificuldade_jogo():
            if pontos < 5:
                relogio.tick(18)
            elif pontos < 10:
                relogio.tick(23)
            elif pontos < 15:
                relogio.tick(30)
            elif pontos < 20:
                relogio.tick(35)
            elif pontos >= 20:
                relogio.tick(40)

        
        # loop do jogo
        while True:

            # Aumenando dificuldade do jogo de acordo com a pontuação
            dificuldade_jogo()

            # add background
            tela.blit(bg_img,(0,0))

            potuacao = f'Pontos: {pontos}'
            textoFormatado = fonte.render(potuacao, True, (255, 255, 255))

            for event in pygame.event.get():

                # Evento de fechar o jogo
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_a:
                        if x_controle == velocidade:
                            pass
                        else:
                            x_controle = -velocidade
                            y_controle = 0

                    if event.key == K_d:
                        if x_controle == -velocidade:
                            pass
                        else:
                            x_controle = +velocidade
                            y_controle = 0

                    if event.key == K_w:
                        if y_controle == velocidade:
                            pass
                        else:
                            x_controle = 0
                            y_controle = -velocidade

                    if event.key == K_s:
                        if y_controle == velocidade:
                            pass
                        else:
                            x_controle = 0
                            y_controle = velocidade

            x_cobra = x_cobra + x_controle
            y_cobra = y_cobra + y_controle

            cobra = pygame.draw.rect(
                tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))

            fruta = tela.blit(img_py_fruta, (x_fruta, y_fruta))
            get_bomba = tela.blit(bomba, (x_bomba, y_bomba))

            # Colisao - mudando posição da fruta_python
            if cobra.colliderect(fruta):
                # Nascimento do local da fruta
                x_fruta = randint(40, 600)
                y_fruta = randint(50, 430)

                x_bomba = randint(40, 600)
                y_bomba = randint(50, 430)

                pontos = pontos + 1
                comprimento_inicial = comprimento_inicial + 1
                som_colisao.play()

            # Colisao com a bomba
            if cobra.colliderect(get_bomba):
                # Nascimento do local da fruta
                font_2 = pygame.font.SysFont("arial", 20, True, False)
                messagem = "Você colidiu com a bomba! reiniciar o jogo R"
                text_formatado = font_2.render(messagem, True, (255, 255, 255))
                ret_texto = text_formatado.get_rect()

                morreu = True
                while morreu:
                    tela.blit(bg_img,(0,0))
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            exit()
                        if event.type == KEYDOWN:
                            if event.key == K_r:
                                pontos = 0
                                comprimento_inicial = 5
                                x_cobra = int(largura / 2)
                                y_cobra = int(altura / 2)
                                lista_cobra = []
                                lista_cabeca = []
                                x_fruta = randint(40, 600)
                                y_fruta = randint(50, 430)
                                morreu = False

                    ret_texto.center = (largura // 2, altura // 2)
                    tela.blit(text_formatado, ret_texto)
                    pygame.display.update()

            # Criando corpo da cobra
            lista_cabeca = []
            lista_cabeca.append(x_cobra)
            lista_cabeca.append(y_cobra)
            lista_cobra.append(lista_cabeca)

            # verificando se a cobra bateu no proprio corpo
            if lista_cobra.count(lista_cabeca) > 1:

                font_2 = pygame.font.SysFont("arial", 20, True, False)
                messagem = "Game over! Pressione a tecla R para jogar novamente."
                text_formatado = font_2.render(messagem, True, (255, 255, 255))
                ret_texto = text_formatado.get_rect()

                morreu = True
                while morreu:
                    tela.blit(bg_img,(0,0))
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            exit()
                        if event.type == KEYDOWN:
                            if event.key == K_r:
                                pontos = 0
                                comprimento_inicial = 5
                                x_cobra = int(largura / 2)
                                y_cobra = int(altura / 2)
                                lista_cobra = []
                                lista_cabeca = []
                                x_fruta = randint(40, 600)
                                y_fruta = randint(50, 430)
                                morreu = False

                    ret_texto.center = (largura // 2, altura // 2)
                    tela.blit(text_formatado, ret_texto)
                    pygame.display.update()

            # Verificando se a cobra sai da tela
            if x_cobra > largura:
                x_cobra = 0
            if x_cobra < 0:
                x_cobra = largura
            if y_cobra < 0:
                y_cobra = altura
            if y_cobra > altura:
                y_cobra = 0

            if len(lista_cobra) > comprimento_inicial:
                del lista_cobra[0]
            aumentando_cobra(lista_cobra)

            tela.blit(textoFormatado, (20, 20))
            pygame.display.update()
