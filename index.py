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

x_fruta = randint(40, 600)
y_fruta = randint(50, 430)

pontos = 0

lista_cobra = []

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

    relogio.tick(60)  # Frame
    tela.fill((255, 255, 255))  # tela preta

    potuacao = f'Pontos: {pontos}'

    textoFormatado = fonte.render(potuacao, True, (0, 0, 0))

    for event in pygame.event.get():  # Detectando se algum evento ocorreu

        # Evento de fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Movimentação por telcas
    if pygame.key.get_pressed()[K_a]:
        x_cobra = x_cobra - 20
    if pygame.key.get_pressed()[K_LEFT]:
        x_cobra = x_cobra - 20
    if pygame.key.get_pressed()[K_d]:
        x_cobra = x_cobra + 20
    if pygame.key.get_pressed()[K_RIGHT]:
        x_cobra = x_cobra + 20
    if pygame.key.get_pressed()[K_w]:
        y_cobra = y_cobra - 20
    if pygame.key.get_pressed()[K_UP]:
        y_cobra = y_cobra - 20
    if pygame.key.get_pressed()[K_s]:
        y_cobra = y_cobra + 20
    if pygame.key.get_pressed()[K_DOWN]:
        y_cobra = y_cobra + 20

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    fruta = pygame.draw.rect(
        tela, (255, 0, 0), (x_fruta, y_fruta, 20, 20))

    # Colisao - mudando posição do ret_verde
    if cobra.colliderect(fruta):
        x_fruta = randint(40, 600)
        y_fruta = randint(50, 430)

        pontos = pontos + 1

    # Criando corpo da cobra
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)
    aumentando_cobra(lista_cobra)


    tela.blit(textoFormatado, (20, 20))
    pygame.display.update()
