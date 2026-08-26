import pygame

class Telas:

    def __init__(self, tela):
        # 1. Configurações fundamentais
        self.tela = tela
        self.cor_texto = (240, 240, 240)
        self.cor_botao = (40, 40, 60)
        self.fonte = pygame.font.Font(None, 40)

        # 2. Dimensões da tela
        largura_tela = self.tela.get_width()
        altura_tela = self.tela.get_height()

        # 3. Configuração dos botões do Menu Principal
        largura_botao = 250
        altura_botao = 60
        x = (largura_tela - largura_botao) // 2

        self.bot_jogar = pygame.Rect(
            x, altura_tela // 2 - 100, largura_botao, altura_botao
        )
        self.bot_creditos = pygame.Rect(
            x, altura_tela // 2, largura_botao, altura_botao
        )
        self.bot_sair = pygame.Rect(
            x, altura_tela // 2 + 100, largura_botao, altura_botao
        )

        # 4. Configuração do Botão Voltar (Canto superior direito)
        largura_voltar = 120
        altura_voltar = 50
        margem = 20
        x_voltar = largura_tela - largura_voltar - margem
        y_voltar = margem

        self.bot_voltar = pygame.Rect(
            x_voltar, y_voltar, largura_voltar, altura_voltar
        )

        # 5. Renderização dos Textos
        self.txt_jogar = self.fonte.render("Jogar", True, self.cor_texto)
        self.txt_creditos = self.fonte.render("Créditos", True, self.cor_texto)
        self.txt_sair = self.fonte.render("Sair", True, self.cor_texto)
        self.txt_voltar = self.fonte.render("Voltar", True, self.cor_texto)

    def menu(self):
        """Desenha os botões da tela de Menu Principal."""
        botoes = [
            (self.bot_jogar, self.txt_jogar),
            (self.bot_creditos, self.txt_creditos),
            (self.bot_sair, self.txt_sair),
        ]

        for botao, texto in botoes:
            pygame.draw.rect(
                self.tela, self.cor_botao, botao, border_radius=10
            )
            self.tela.blit(texto, texto.get_rect(center=botao.center))

    def desenhar_voltar(self):
        """Método auxiliar para desenhar o botão Voltar no canto da tela."""
        pygame.draw.rect(
            self.tela, self.cor_botao, self.bot_voltar, border_radius=10
        )
        self.tela.blit(
            self.txt_voltar,
            self.txt_voltar.get_rect(center=self.bot_voltar.center),
        )

    def creditos(self):
        """Desenha a tela de créditos."""
        texto = self.fonte.render(
            "Feito por: Rafael Victor, Pedro Lázaro, Vinícius Morais",
            True,
            self.cor_texto,
        )
        self.tela.blit(
            texto,
            texto.get_rect(
                center=(
                    self.tela.get_width() // 2,
                    self.tela.get_height() // 2,
                )
            ),
        )

        # Desenha o botão voltar no canto superior direito
        self.desenhar_voltar()


