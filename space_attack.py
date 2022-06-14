import pygame
from pygame.locals import *
from sys import exit  # função para fechar janela

pygame.init()  # Iniciando o pygame

largura = 640
altura = 480


fonte = pygame.font.SysFont('arial', 18, True, False)
# Defenindo largura e altura da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')  # Definindo nome do jogo

relogio = pygame.time.Clock()  # Frame


# loop do jogo
while True:

    relogio.tick(10)  # Frame
    tela.fill((255, 255, 255))  # tela preta

    
    for event in pygame.event.get():  # Detectando se algum evento ocorreu

        # Evento de fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
