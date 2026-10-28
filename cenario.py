import os
import pygame

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE_PATH, "front")


def resolver_caminho_arquivo(nome_arquivo):
    locais = [
        os.path.join(ASSETS, "cenario_e_tela", nome_arquivo),
        os.path.join(ASSETS, "sprites", nome_arquivo),
        os.path.join(BASE_PATH, nome_arquivo),
    ]

    for caminho in locais:
        if os.path.exists(caminho):
            return caminho

    return os.path.join(ASSETS, "cenario_e_tela", nome_arquivo)


class Cenario:
    def __init__(self, tela):
        self.tela = tela
        self.fundo = None
        self.velocidade_scroll = 1.2
        self.offset_y = 0
        self.carregar_fundo()

    def carregar_fundo(self):
        caminho = resolver_caminho_arquivo("cenario0.png")

        if not os.path.exists(caminho):
            return

        img = pygame.image.load(caminho).convert()
        largura_tela = self.tela.get_width()

        proporcao = largura_tela / img.get_width()
        altura_ajustada = max(self.tela.get_height(), int(img.get_height() * proporcao))
        self.fundo = pygame.transform.scale(img, (largura_tela, altura_ajustada))

        self.offset_y = max(0, self.fundo.get_height() - self.tela.get_height())

    def atualizar_animacao(self):
        if not self.fundo:
            return

        altura_fundo = self.fundo.get_height()
        altura_tela = self.tela.get_height()

        if altura_fundo <= altura_tela:
            return

        self.offset_y -= self.velocidade_scroll

        while self.offset_y < 0:
            self.offset_y += altura_fundo

        while self.offset_y >= altura_fundo:
            self.offset_y -= altura_fundo

    def desenhar(self):
        if not self.fundo:
            return

        self.atualizar_animacao()

        altura_tela = self.tela.get_height()
        altura_fundo = self.fundo.get_height()

        if altura_fundo <= altura_tela:
            self.tela.blit(self.fundo, (0, 0))
            return

        y = -self.offset_y
        while y < altura_tela:
            self.tela.blit(self.fundo, (0, y))
            y += altura_fundo