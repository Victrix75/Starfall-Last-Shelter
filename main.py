import pygame

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("StarFall-Last-Shelter")

cor_fundo = (30, 30, 30)

relogio = pygame.time.Clock()
fps = 60

rodando = True
while rodando:
    for evento in pygame.event.get():
     if evento.type == pygame.QUIT:
        rodando = False

tela.fill(cor_fundo)
pygame.display.flip()
relogio.tick(fps)

pygame.quit()