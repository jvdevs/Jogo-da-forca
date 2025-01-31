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


palavra = random.choice(palavras)
palavra_oculta = ["_" for _ in palavra]
letras_erradas = []
tentativas_restantes = 6

def game_loop():
    global tentativas_restantes
    rodando = True
    while rodando:
        tela.fill(BRANCO)

        texto_palavra = fonte.render(" ".join(palavra_oculta), True, PRETO)
        tela.blit(texto_palavra, (50, 100))
        
        texto_erradas = fonte.render("Letras erradas: " + " ".join(letras_erradas), True, VERMELHO)
        tela.blit(texto_erradas, (50, 150))


