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


class Inimigo(Sprites):
    def __init__(self, x_origem, y_origem):
        super().__init__()
        self.x_origem = x_origem
        self.y_origem = y_origem
        self.x = x_origem
        self.y = y_origem
        self.vel = 4
       
        # Estados: "grade", "atancando", "retornando"
        self.estado = "grade"
        self.vel_x = 0
        self.vel_y = 0
        self.carregar_sprites()


    def iniciar_ataque(self, pos_jogador):
        if self.estado == "grade":
            self.estado = "atacando"
            # Calcula vetor em direção ao jogador
            dx = pos_jogador[0] - self.x
            dy = pos_jogador[1] - self.y
            distancia = (dx**2 + dy**2) ** 0.5
            if distancia > 0:
                self.vel_x = (dx / distancia) * self.vel
                self.vel_y = (dy / distancia) * self.vel


    def atualizar(self, offset_x):
        if self.estado == "grade":
            # Acompanha o movimento lateral da formação
            self.x = self.x_origem + offset_x
            self.y = self.y_origem
        elif self.estado == "atacando":
            self.x += self.vel_x
            self.y += self.vel_y
            # Se passar da parte inferior da tela, reaparece no topo
            if self.y > 1080:  
                self.y = -50
                self.estado = "retornando"
        elif self.estado == "retornando":
            # Volta para a posição original na grade
            dx = (self.x_origem + offset_x) - self.x
            dy = self.y_origem - self.y
            distancia = (dx**2 + dy**2) ** 0.5
           
            if distancia < 5:
                self.estado = "grade"
            else:
                self.x += (dx / distancia) * self.vel
                self.y += (dy / distancia) * self.vel


        self.atualizar_animacao()


    def desenhar(self, tela):
        sprite = self.sprite_atual()
        if sprite:
            tela.blit(sprite, (self.x, self.y))
        else:
            pygame.draw.rect(tela, (255, 0, 0), (self.x, self.y, 60, 60))




class FrotaInimigos:
    def __init__(self, linhas=2, colunas=6, pode_atacar= False):
        self.inimigos = []
        self.offset_x = 0
        # self.dir_frota = 1
        # self.largura_frota = 600
        self.tempo_ultimo_ataque = pygame.time.get_ticks()
        self.pode_atacar = pode_atacar
        self.largura_grade = (colunas-1) * 80
        self.x_centro_base = 400
       
        # Criar grade de inimigos
        for l in range(linhas):
            for c in range(colunas):
                x = (self.x_centro_base - self.largura_grade //2) + (c * 80)
                #x = 200 + c * 80
                y = 80 + l * 70
                self.inimigos.append(Inimigo(x, y))


    def atualizar(self, pos_jogador):
        # Oscilação da frota para esquerda e direita
        x_jogador = pos_jogador[0]
        diferenca_x = x_jogador - (self.x_centro_base + self.offset_x)
        self.offset_x += diferenca_x * 0.007
       
        # Sorteia um inimigo para atacar a cada 2 segundos
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


    def desenhar(self, tela):
        for inimigo in self.inimigos:
            inimigo.desenhar(tela)
