import pygame
import random

pygame.init()


LARGURA, ALTURA = 600, 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Forca")


BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)


fonte = pygame.font.Font(None, 36)

palavras = ["PYTHON", "JANELA", "CACHORRO", "PROGRAMACAO", "GUITARRA"]
