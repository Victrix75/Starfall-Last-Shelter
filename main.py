import pygame
from personagens import Nave
from telas import Telas

pygame.init()

info = pygame.display.Info()
tela_cheia = (info.current_w, info.current_h)

tela = pygame.display.set_mode(tela_cheia)

pygame.display.set_caption("StarFall-Last-Shelter")

cor_fundo = (30, 30, 30)

relogio = pygame.time.Clock()
fps = 60

estado_atual = "menu"

nave = Nave()

telas = Telas(tela)

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

        nave.mover()
        nave.desenhar(tela)

    elif estado_atual == "creditos":
        telas.creditos()

    pygame.display.flip()
    relogio.tick(fps)

pygame.quit()