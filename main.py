import pygame
from cenario import Cenario
from personagens import Nave, FrotaInimigos
from telas import Telas

pygame.init()
pygame.font.init()

info = pygame.display.Info()
tela_cheia = (info.current_w, info.current_h)
tela = pygame.display.set_mode(tela_cheia)
pygame.display.set_caption("StarFall-Last-Shelter")

cor_fundo = (30, 30, 30)
relogio = pygame.time.Clock()
fps = 60
estado_atual = "menu"

# Configuração de Fonte da HUD
fonte_hud = pygame.font.SysFont("arial", 28, bold=True)

frota = FrotaInimigos(linhas=2, colunas=6, pode_atacar=True, espacamento_x=70, espacamento_y=100)
nave = Nave()
telas = Telas(tela)
cenario = Cenario(tela)

pontuacao = 0

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if estado_atual == "menu":
                if telas.bot_sair.collidepoint(evento.pos):
                    rodando = False

                elif telas.bot_jogar.collidepoint(evento.pos):
                    # Reinicia variáveis do jogo ao dar Play
                    frota = FrotaInimigos(linhas=2, colunas=6, pode_atacar=True, espacamento_x=70, espacamento_y=100)
                    nave = Nave()
                    pontuacao = 0
                    estado_atual = "jogo"

                elif telas.bot_creditos.collidepoint(evento.pos):
                    estado_atual = "creditos"

            elif estado_atual in ("jogo", "creditos"):
                if (
                    hasattr(telas, "bot_voltar")
                    and telas.bot_voltar.collidepoint(evento.pos)
                ):
                    estado_atual = "menu"

    tela.fill(cor_fundo)

    if estado_atual == "menu":
        telas.menu()

    elif estado_atual == "jogo":
        cenario.desenhar()

        nave.mover(tela)
        nave.desenhar(tela)

        frota.atualizar((nave.x, nave.y))
        
        # Computa colisões e adiciona os pontos
        pontos = frota.checar_colisoes(nave.projeteis, nave)
        pontuacao += pontos

        if not frota.inimigos:
            frota = FrotaInimigos(linhas=2, colunas=6, pode_atacar=True, espacamento_x=70, espacamento_y=100)

        frota.desenhar(tela)

        # Exibição de HUD (Pontos e Vidas)
        texto_pontos = fonte_hud.render(f"Pontos: {pontuacao}", True, (255, 255, 255))
        texto_vidas = fonte_hud.render(f"Vidas: {nave.vida}", True, (255, 50, 50))
        tela.blit(texto_pontos, (20, 20))
        tela.blit(texto_vidas, (20, 55))

        # Checa condição de Game Over
        if nave.vida <= 0:
            estado_atual = "menu"

        if hasattr(telas, "desenhar_voltar"):
            telas.desenhar_voltar()

    elif estado_atual == "creditos":
        telas.creditos()

    pygame.display.flip()
    relogio.tick(fps)

pygame.quit()