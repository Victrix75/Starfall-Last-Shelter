import pygame
from personagens import Nave
from telas import Telas
from cenario import Cenario

pygame.init()

tela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("StarFall-Last-Shelter")

cor_fundo = (30, 30, 30)

relogio = pygame.time.Clock()
fps = 60

estado_atual = "menu"

nave = Nave()
telas = Telas(tela)
nave.projeteis.clear()
cenario = Cenario(tela)  # <-- 2. CRIAMOS A INSTÂNCIA DO CENÁRIO

rodando = True

while rodando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if estado_atual == "menu":

                if telas.bot_sair.collidepoint(evento.pos):
                    rodando = False

                if telas.bot_jogar.collidepoint(evento.pos):
                    estado_atual = "jogo"

                if telas.bot_creditos.collidepoint(evento.pos):
                    estado_atual = "creditos"

    tela.fill(cor_fundo)

    if estado_atual == "menu":
        telas.menu()

    elif estado_atual == "jogo":
        # <-- 3. DESENHAMOS O CENÁRIO PRIMEIRO (FICA AO FUNDO)
        cenario.desenhar()

        # <-- 4. DEPOIS MOVEMOS E DESENHAMOS A NAVE (FICA POR CIMA)
        nave.mover(tela)
        nave.desenhar(tela)

    elif estado_atual == "creditos":
        telas.creditos()

    pygame.display.flip()
    relogio.tick(fps)

pygame.quit()