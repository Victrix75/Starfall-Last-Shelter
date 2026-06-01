import pygame
class Projetil:
    def __init__(self, projx, projy):
        self.projx = projxx
        self.projy = proxy
        self.vel = 10

    def atualizar(self):
        self.projy -= self.vel
    
    def desenhar(self, tela):
        pygame.draw.rect(tela, (255, 0, 0), (self.x, self.y, 5, 15))