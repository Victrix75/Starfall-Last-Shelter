import pygame
from cenario import Cenario
from personagens import Nave
from telas import Telas

pygame.init()

# 1. Configuração da Tela Cheia
info = pygame.display.Info()
tela_cheia = (info.current_w, info.current_h)
tela = pygame.display.set_mode(tela_cheia)
pygame.display.set_caption("StarFall-Last-Shelter")

# 2. Configurações Globais
cor_fundo = (30, 30, 30)
relogio = pygame.time.Clock()
fps = 60
estado_atual = "menu"

# 3. Instância dos Objetos
nave = Nave()
telas = Telas(tela)
cenario = Cenario(tela)

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # --- CAPTURA DE CLIQUES DO MOUSE ---
        if evento.type == pygame.MOUSEBUTTONDOWN:

            # Menu Principal
            if estado_atual == "menu":
                if telas.bot_sair.collidepoint(evento.pos):
                    rodando = False

                elif telas.bot_jogar.collidepoint(evento.pos):
                    # Limpa projéteis acumulados antes de iniciar a partida
                    if hasattr(nave, "projeteis"):
                        nave.projeteis.clear()
                    estado_atual = "jogo"

                elif telas.bot_creditos.collidepoint(evento.pos):
                    estado_atual = "creditos"

            # Tela de Jogo ou Créditos (Botão Voltar)
            elif estado_atual in ("jogo", "creditos"):
                if (
                    hasattr(telas, "bot_voltar")
                    and telas.bot_voltar.collidepoint(evento.pos)
                ):
                    estado_atual = "menu"

    # --- DESENHO E RENDERIZAÇÃO ---
    tela.fill(cor_fundo)

    if estado_atual == "menu":
        telas.menu()

    elif estado_atual == "jogo":
        # 1º Desenha o cenário ao fundo
        cenario.desenhar()

        # 2º Move e desenha a nave (sem passar parâmetro para evitar TypeError)
        nave.mover(tela)
        nave.desenhar(tela)

        # 3º Desenha o botão de voltar por cima do jogo
        if hasattr(telas, "desenhar_voltar"):
            telas.desenhar_voltar()

    elif estado_atual == "creditos":
        telas.creditos()

    pygame.display.flip()
    relogio.tick(fps)

pygame.quit()