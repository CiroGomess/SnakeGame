from ast import While
from asyncio import events
import pygame
from pygame.locals import *
from sys import exit  # função para fechar janela

from random import randint

pygame.init()  # Iniciando o pygame

# Musica do jogo

pygame.mixer.music.set_volume(0.5)
musica_fundo = pygame.mixer.music.load('./music/Linn Friberg - Learning From Mistakes.mp3')
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

red = randint(0, 255)
green = randint(0, 255)
blue = randint(0, 255)

pontos = 0

lista_cobra = []
comprimento_inicial = 5
morreu = False


fonte = pygame.font.SysFont('arial', 18, True, False)
# Defenindo largura e altura da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')  # Definindo nome do jogo
relogio = pygame.time.Clock()  # Frame


def aumentando_cobra(lista_cobra):
    for XeY in lista_cobra:
        # XeY = []
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))


def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cabeca, lista_cobra, x_fruta, y_fruta, morreu

    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    lista_cobra = []
    lista_cabeca = []
    x_fruta = randint(40, 600)
    y_fruta = randint(50, 430)
    morreu = False


# loop do jogo
while True:

    relogio.tick(30)  # Frame
    tela.fill((255, 255, 255))  # tela preta

    potuacao = f'Pontos: {pontos}'

    textoFormatado = fonte.render(potuacao, True, (0, 0, 0))

    for event in pygame.event.get():  # Detectando se algum evento ocorreu

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

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    fruta = pygame.draw.rect(
        tela, (red, green, blue), (x_fruta, y_fruta, 20, 20))

    # Colisao - mudando posição do ret_verde
    if cobra.colliderect(fruta):
        x_fruta = randint(40, 600)
        y_fruta = randint(50, 430)

        pontos = pontos + 1
        comprimento_inicial = comprimento_inicial + 1
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        som_colisao.play()

    # Criando corpo da cobra
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    # verificando se a cobra bateu no proprio corpo
    if lista_cobra.count(lista_cabeca) > 1:

        font_2 = pygame.font.SysFont("arial", 20, True, False)
        messagem = "Game over! Pressione a  trcla R para jogar novamente."
        text_formatado = font_2.render(messagem, True, (0, 0, 0))
        ret_texto = text_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            ret_texto.center = (largura // 2, altura // 2)
            tela.blit(text_formatado, ret_texto)
            pygame.display.update()

    # Verificando se a cobra sai da tela
    if x_cobra > largura:
        x = 0
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
