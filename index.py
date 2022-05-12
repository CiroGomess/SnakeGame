from asyncio import events
import pygame
from pygame.locals import *
from sys import exit  # função para fechar janela

from random import randint

pygame.init()  # Iniciando o pygame

largura = 640
altura = 480

# centrlizado objeto na tela
x = int(largura / 2)
y = int(altura / 2)

x_verde = randint(40, 600)
y_verde = randint(50, 430)

pontos = 0

fonte = pygame.font.SysFont('arial', 18, True, False)

# Defenindo largura e altura da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Mini-Game')  # Definindo nome do jogo
relogio = pygame.time.Clock()  # Frame


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
        x = x - 20
    if pygame.key.get_pressed()[K_LEFT]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_RIGHT]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_UP]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20
    if pygame.key.get_pressed()[K_DOWN]:
        y = y + 20
   
   

    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    ret_verde = pygame.draw.rect(
        tela, (000, 255, 0), (x_verde, y_verde, 40, 50))

    # Colisao - mudando posição do ret_verde
    if ret_vermelho.colliderect(ret_verde):
        x_verde = randint(40, 600)
        y_verde = randint(50, 430)

        pontos = pontos + 1
    

    tela.blit(textoFormatado, (20, 20))
    pygame.display.update()
