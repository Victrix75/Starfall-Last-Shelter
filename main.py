import pygame

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("StarFall-Last-Shelter")

cor_fundo = (30, 30, 30)
cor_texto = (240, 240, 240)    
cor_botao = (40, 40, 60)
relogio = pygame.time.Clock()
fps = 60

bot_jogar = pygame.Rect(300, 200, 200, 50)
bot_creditos = pygame.Rect(300, 280, 200, 50)
bot_sair = pygame.Rect(300, 360, 200, 50)
fonte = pygame.font.Font(None, 40)

txt_jogar = fonte.render("Jogar", True, cor_texto)
txt_creditos = fonte.render("Creditos", True, cor_texto)
txt_sair = fonte.render("Sair", True, cor_texto)
estado_atual = "menu"

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(cor_fundo)

    pygame.draw.rect(tela, cor_botao, bot_jogar)
    pygame.draw.rect(tela, cor_botao, bot_creditos)
    pygame.draw.rect(tela, cor_botao, bot_sair)

    tela.blit(txt_jogar, (bot_jogar.x + 60, bot_jogar.y + 10))
    tela.blit(txt_creditos, (bot_creditos.x + 45, bot_creditos.y + 10))
    tela.blit(txt_sair, (bot_sair.x + 70, bot_sair.y + 10))

    pygame.display.flip()
    relogio.tick(fps)

pygame.quit()