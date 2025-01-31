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

        texto_tentativas = fonte.render(f"Tentativas restantes: {tentativas_restantes}", True, PRETO)
        tela.blit(texto_tentativas, (50, 200))
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                letra = evento.unicode.upper()
                if letra.isalpha() and len(letra) == 1:
                    if letra in palavra:
                        for i, l in enumerate(palavra):
                            if l == letra:
                                palavra_oculta[i] = letra
                    else:
                        if letra not in letras_erradas:
                            letras_erradas.append(letra)
                            tentativas_restantes -= 1
                    
        if "_" not in palavra_oculta:
            mensagem = "Você venceu!"
            rodando = False
        elif tentativas_restantes == 0:
            mensagem = f"Você perdeu! A palavra era {palavra}"
            rodando = False
        
        pygame.display.flip()
    
    tela.fill(BRANCO)
    texto_final = fonte.render(mensagem, True, PRETO)
    tela.blit(texto_final, (LARGURA//2 - 100, ALTURA//2))
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    
game_loop()



