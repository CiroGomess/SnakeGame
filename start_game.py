import pygame
from pygame.locals import *
from sys import exit  # função para fechar janela

from snaker_game import skaner_gamer


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
    
    font_2 = pygame.font.SysFont("arial", 20, True, False)
    
    messagem = "A -  Snaker Game"
    messagem_2 = "B -  Snaker Game"
    messagem_3 = "C -  Snaker Game"
   

    text_formatado = font_2.render(messagem, True, (0, 0, 0))
    text_formatado = font_2.render(messagem_2, True, (0, 0, 0))
    text_formatado = font_2.render(messagem_3, True, (0, 0, 0))
    
    ret_texto = text_formatado.get_rect()
    ret_texto_2 = text_formatado.get_rect()
    ret_texto_3 = text_formatado.get_rect()


    ret_texto.center = (largura // 2, altura // 2)
    ret_texto_2.center = (largura // 2, altura // 2 + 25)
    ret_texto_3.center = (largura // 2, altura // 2 - 25)
  
    tela.blit(text_formatado, ret_texto)
    tela.blit(text_formatado, ret_texto_2)
    tela.blit(text_formatado, ret_texto_3)

    controle_jogo = 0
  

    for event in pygame.event.get():  # Detectando se algum evento ocorreu

        # Evento de fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
           
            if event.key == K_a:
                controle_jogo = 1
                if controle_jogo == 1:
                    skaner_gamer(controle_jogo)
               


    pygame.display.update()