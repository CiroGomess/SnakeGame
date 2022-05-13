from asyncio import events
import pygame
from pygame.locals import *
from sys import exit  # função para fechar janela

from random import randint

pygame.init()  # Iniciando o pygame

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

pontos = 0

lista_cobra = []
comprimento_inicial = 5


fonte = pygame.font.SysFont('arial', 18, True, False)
# Defenindo largura e altura da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')  # Definindo nome do jogo
relogio = pygame.time.Clock()  # Frame


def aumentando_cobra(lista_cobra):
    for XeY in lista_cobra:
        # XeY = []
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))


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
        tela, (255, 0, 0), (x_fruta, y_fruta, 20, 20))

    # Colisao - mudando posição do ret_verde
    if cobra.colliderect(fruta):
        x_fruta = randint(40, 600)
        y_fruta = randint(50, 430)

        pontos = pontos + 1
        comprimento_inicial = comprimento_inicial + 1

    # Criando corpo da cobra
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    aumentando_cobra(lista_cobra)

    tela.blit(textoFormatado, (20, 20))
    pygame.display.update()
