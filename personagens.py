import pygame
import os
from telas import *
import random

TAMANHO = 140

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
        self.largura = 6
        self.altura = 16
        # Retângulo para cálculo de colisão
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def atualizar(self):
        self.y -= self.vel
        self.rect.y = self.y

    def desenhar(self, tela):
        pygame.draw.rect(
            tela,
            (0, 255, 255),
            self.rect
        )


class Nave(Sprites):
    def __init__(self):
        super().__init__()
        self.x = 380
        self.y = 500
        self.vel = 10
        self.projeteis = []
        
        self.tempo_ultimo_tiro = 0
        self.cooldown_tiro = 250  # Intervalo entre tiros em ms

        self.carregar_sprites()

    def mover(self, tela):
        teclas = pygame.key.get_pressed()

        # Movimentação
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.x -= self.vel
            self.direcao = "esquerda"

        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.x += self.vel
            self.direcao = "direita"

        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            self.y -= self.vel
            self.direcao = "cima"

        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            self.y += self.vel
            self.direcao = "baixo"

        # Disparo de tiro
        if teclas[pygame.K_SPACE]:
            agora = pygame.time.get_ticks()
            if agora - self.tempo_ultimo_tiro >= self.cooldown_tiro:
                self.atirar()
                self.tempo_ultimo_tiro = agora

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
        pos_x = self.x + (TAMANHO // 2) - 3
        pos_y = self.y
        novo_projetil = Projetil(pos_x, pos_y)
        self.projeteis.append(novo_projetil)

    def atualizar_projeteis(self):
        for proj in self.projeteis[:]:
            proj.atualizar()
            if proj.y < -15:
                self.projeteis.remove(proj)

    def desenhar(self, tela):
        for proj in self.projeteis:
            proj.desenhar(tela)

        sprite = self.sprite_atual()
        if sprite:
            tela.blit(sprite, (self.x, self.y))
        else:
            pygame.draw.rect(
                tela,
                (0, 255, 0),
                (self.x, self.y, TAMANHO, TAMANHO)
            )


class Inimigo(Sprites):
    def __init__(self, x_origem, y_origem):
        super().__init__()
        self.x_origem = x_origem
        self.y_origem = y_origem
        self.x = x_origem
        self.y = y_origem
        self.vel = 4
        
        # Sistema de Vida e Tamanho da Hitbox
        self.vida = 3
        self.largura = 60
        self.altura = 60
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

        self.estado = "grade"
        self.vel_x = 0
        self.vel_y = 0
        self.carregar_sprites()

    def iniciar_ataque(self, pos_jogador):
        if self.estado == "grade":
            self.estado = "atacando"
            dx = pos_jogador[0] - self.x
            dy = pos_jogador[1] - self.y
            distancia = (dx**2 + dy**2) ** 0.5
            if distancia > 0:
                self.vel_x = (dx / distancia) * self.vel
                self.vel_y = (dy / distancia) * self.vel

    def atualizar(self, offset_x):
        if self.estado == "grade":
            self.x = self.x_origem + offset_x
            self.y = self.y_origem
        elif self.estado == "atacando":
            self.x += self.vel_x
            self.y += self.vel_y
            if self.y > 1080:  
                self.y = -50
                self.estado = "retornando"
        elif self.estado == "retornando":
            dx = (self.x_origem + offset_x) - self.x
            dy = self.y_origem - self.y
            distancia = (dx**2 + dy**2) ** 0.5
            
            if distancia < 5:
                self.estado = "grade"
            else:
                self.x += (dx / distancia) * self.vel
                self.y += (dy / distancia) * self.vel

        # Atualiza o retângulo de colisão junto com o movimento
        self.rect.x = self.x
        self.rect.y = self.y

        self.atualizar_animacao()

    def desenhar(self, tela):
        sprite = self.sprite_atual()
        if sprite:
            tela.blit(sprite, (self.x, self.y))
        else:
            # Alterna a cor dependendo da vida (Retângulo fallback)
            cor = (255, 0, 0)
            if self.vida == 2:
                cor = (200, 100, 0)
            elif self.vida == 1:
                cor = (255, 255, 0)
            pygame.draw.rect(tela, cor, self.rect)


class FrotaInimigos:
    def __init__(self, linhas=2, colunas=6, pode_atacar=False):
        self.inimigos = []
        self.offset_x = 0
        self.tempo_ultimo_ataque = pygame.time.get_ticks()
        self.pode_atacar = pode_atacar
        self.largura_grade = (colunas - 1) * 80
        self.x_centro_base = 400
        
        for l in range(linhas):
            for c in range(colunas):
                x = (self.x_centro_base - self.largura_grade // 2) + (c * 80)
                y = 80 + l * 70
                self.inimigos.append(Inimigo(x, y))

    def atualizar(self, pos_jogador):
        x_jogador = pos_jogador[0]
        diferenca_x = x_jogador - (self.x_centro_base + self.offset_x)
        self.offset_x += diferenca_x * 0.007
        
        if self.pode_atacar:
            agora = pygame.time.get_ticks()
            if agora - self.tempo_ultimo_ataque > 2000 and self.inimigos:
                inimigos_disponiveis = [i for i in self.inimigos if i.estado == "grade"]
                if inimigos_disponiveis:
                    atacante = random.choice(inimigos_disponiveis)
                    atacante.iniciar_ataque(pos_jogador)
                self.tempo_ultimo_ataque = agora

        for inimigo in self.inimigos:
            inimigo.atualizar(self.offset_x)

    def checar_colisoes(self, projeteis):
        """Processa as colisões entre projéteis da nave e a frota de inimigos"""
        for proj in projeteis[:]:
            for inimigo in self.inimigos[:]:
                if inimigo.rect.colliderect(proj.rect):
                    inimigo.vida -= 1  # Subtrai 1 de vida por acerto
                    
                    if proj in projeteis:
                        projeteis.remove(proj)  # Destrói o tiro atingido
                    
                    if inimigo.vida <= 0:
                        self.inimigos.remove(inimigo)  # Destrói o inimigo com 0 de vida
                    
                    break  # Para de testar este projétil já destruído

    def desenhar(self, tela):
        for inimigo in self.inimigos:
            inimigo.desenhar(tela)