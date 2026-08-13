import pygame
import os
from telas import *

TAMANHO = 160

ASSETS = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "front",
    "sprites"
)


class Sprites:
    def __init__(self):
        self.direcao = "direita"
        self.frame = 0
        self.sprites = {}

    def carregar_sprites(self):
        nome = self.__class__.__name__.lower()

        for direcao in ("direita", "esquerda", "cima", "baixo"):
            quadros = []
            for f in (0, 1):
                caminho = os.path.join(
                    ASSETS,
                    f"{nome}{direcao}{f}.png"
                )

                if os.path.exists(caminho):
                    img = pygame.image.load(caminho).convert_alpha()
                    img = pygame.transform.scale(img, (TAMANHO, TAMANHO))
                    quadros.append(img)

            self.sprites[direcao] = quadros

    def atualizar_animacao(self):
        self.frame += 1

    def sprite_atual(self):
        quadros = self.sprites.get(self.direcao, [])

        if len(quadros) == 0:
            quadros = self.sprites.get("direita", [])

        if len(quadros) == 0:
            return None

        return quadros[(self.frame // 5) % len(quadros)]


class Projetil:
    def __init__(self, projx, projy):
        self.x = projx
        self.y = projy
        self.vel = 12

    def atualizar(self):
        self.y -= self.vel

    def desenhar(self, tela):
        pygame.draw.rect(
            tela,
            (0, 255, 255),
            (self.x, self.y, 5, 15)
        )


class Nave(Sprites):
    def __init__(self):
        super().__init__()

        self.x = 380
        self.y = 500
        self.vel = 10
        self.projeteis = []
        self.cooldown_tiro = 0

        self.carregar_sprites()

    def mover(self, tela):
        teclas = pygame.key.get_pressed()

        # Movimentação
        if teclas[pygame.K_a]:
            self.x -= self.vel
            self.direcao = "esquerda"

        if teclas[pygame.K_d]:
            self.x += self.vel
            self.direcao = "direita"

        if teclas[pygame.K_w]:
            self.y -= self.vel
            self.direcao = "cima"

        if teclas[pygame.K_s]:
            self.y += self.vel
            self.direcao = "baixo"

        # Disparo de tiro (Espaço)
        if teclas[pygame.K_SPACE] and self.cooldown_tiro == 0:
            self.atirar()
            self.cooldown_tiro = 15

        if self.cooldown_tiro > 0:
            self.cooldown_tiro -= 1

        # Limites da tela
        largura_tela = tela.get_width()
        altura_tela = tela.get_height()

        if self.x < 0:
            self.x = 0

        if self.x > largura_tela - TAMANHO:
            self.x = largura_tela - TAMANHO

        if self.y < 0:
            self.y = 0

        if self.y > altura_tela - TAMANHO:
            self.y = altura_tela - TAMANHO

        self.atualizar_animacao()
        self.atualizar_projeteis()

    def atirar(self):
        # Centraliza o projétil na parte superior da nave
        pos_x = self.x + (TAMANHO // 2) - 2
        pos_y = self.y
        novo_projetil = Projetil(pos_x, pos_y)
        self.projeteis.append(novo_projetil)

    def atualizar_projeteis(self):
        # Atualiza a posição e remove tiros fora da tela
        for proj in self.projeteis[:]:
            proj.atualizar()
            if proj.y < -15:
                self.projeteis.remove(proj)

    def desenhar(self, tela):
        # 1. Desenha os projéteis
        for proj in self.projeteis:
            proj.desenhar(tela)

        # 2. Desenha o sprite da nave
        sprite = self.sprite_atual()
        if sprite:
            tela.blit(sprite, (self.x, self.y))
        else:
            pygame.draw.rect(
                tela,
                (0, 255, 0),
                (self.x, self.y, TAMANHO, TAMANHO)
            )
