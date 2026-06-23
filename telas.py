import pygame


class Telas:

    def __init__(self, tela):

        self.tela = tela

        self.cor_texto = (240, 240, 240)
        self.cor_botao = (40, 40, 60)

        self.fonte = pygame.font.Font(None, 40)

        # Tamanho da tela
        largura_tela = self.tela.get_width()
        altura_tela = self.tela.get_height()

        # Tamanho dos botões
        largura_botao = 250
        altura_botao = 60

        # Centraliza horizontalmente
        x = (largura_tela - largura_botao) // 2

        # Criação dos botões
        self.bot_jogar = pygame.Rect(
            x,
            altura_tela // 2 - 100,
            largura_botao,
            altura_botao
        )

        self.bot_creditos = pygame.Rect(
            x,
            altura_tela // 2,
            largura_botao,
            altura_botao
        )

        self.bot_sair = pygame.Rect(
            x,
            altura_tela // 2 + 100,
            largura_botao,
            altura_botao
        )

        # Textos
        self.txt_jogar = self.fonte.render(
            "Jogar", True, self.cor_texto
        )

        self.txt_creditos = self.fonte.render(
            "Créditos", True, self.cor_texto
        )

        self.txt_sair = self.fonte.render(
            "Sair", True, self.cor_texto
        )

    def menu(self):

        botoes = [
            (self.bot_jogar, self.txt_jogar),
            (self.bot_creditos, self.txt_creditos),
            (self.bot_sair, self.txt_sair)
        ]

        for botao, texto in botoes:

            pygame.draw.rect(
                self.tela,
                self.cor_botao,
                botao,
                border_radius=10
            )

            self.tela.blit(
                texto,
                texto.get_rect(center=botao.center)
            )

    def creditos(self):

        texto = self.fonte.render(
            "Feito por: Rafael Victor, Pedro Lázaro, Vinícius Morais",
            True,
            self.cor_texto
        )

        self.tela.blit(
            texto,
            texto.get_rect(
                center=(
                    self.tela.get_width() // 2,
                    self.tela.get_height() // 2
                )
            )
        )