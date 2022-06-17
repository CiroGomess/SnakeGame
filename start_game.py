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

img_fundo = pygame.image.load('./imgs/bg.jpg').convert()
  

pygame.mixer.music.set_volume(0.5)
musica_fundo = pygame.mixer.music.load('./music/HoliznaCC0 - Light At The End Of The Tunnel.mp3')
pygame.mixer.music.play(-1)

# loop do jogo
while True:
    relogio.tick(10)  # Frame
    tela.fill((255, 255, 255))  # tela preta

    font_2 = pygame.font.SysFont("arial", 20, True, False)

    tela.blit(img_fundo, (0, 0))


    messagem_3 = "A -  Snaker Game"

    
    text_formatado_03 = font_2.render(messagem_3, True, (0, 139, 139))
    ret_texto_3 = text_formatado_03.get_rect()
    ret_texto_3.center = (largura // 2, altura // 2 - 15)

 
    tela.blit(text_formatado_03, ret_texto_3)

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
