import pygame
from personagens import Nave, Sprites
pygame.init()

info = pygame.display.Info()
tela_cheia = (info.current_w, info.current_h)


tela = pygame.display.set_mode((tela_cheia))

pygame.display.set_caption("StarFall-Last-Shelter")

cor_fundo = (30, 30, 30)
cor_texto = (240, 240, 240)
cor_botao = (40, 40, 60)

relogio = pygame.time.Clock()
fps = 60

bot_jogar = pygame.Rect(300, 200, 200, 50)
bot_creditos = pygame.Rect(300, 280, 200, 50)
bot_sair = pygame.Rect(300, 360, 200, 50)

fonte = pygame.font.Font(None, 40)

txt_jogar = fonte.render("Jogar", True, cor_texto)
txt_creditos = fonte.render("Creditos", True, cor_texto)
txt_sair = fonte.render("Sair", True, cor_texto)

estado_atual = "menu"

nave = Nave()

rodando = True

while rodando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if estado_atual == "menu":
                
                if bot_sair.collidepoint(evento.pos):
                    rodando = False

                if bot_jogar.collidepoint(evento.pos):
                    estado_atual = "jogo"

    tela.fill(cor_fundo)

    if estado_atual == "menu":

        pygame.draw.rect(tela, cor_botao, bot_jogar)
        pygame.draw.rect(tela, cor_botao, bot_creditos)
        pygame.draw.rect(tela, cor_botao, bot_sair)

        tela.blit(txt_jogar, (bot_jogar.x + 60, bot_jogar.y + 10))
        tela.blit(txt_creditos, (bot_creditos.x + 45, bot_creditos.y + 10))
        tela.blit(txt_sair, (bot_sair.x + 70, bot_sair.y + 10))

    elif estado_atual == "jogo":

        nave.mover()
        nave.desenhar(tela)

    pygame.display.flip()
    relogio.tick(fps)

pygame.quit()