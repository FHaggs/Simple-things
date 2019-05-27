import pygame
import time
import random

pygame.init()

LARGURA = 800
ALTURA = 600
# RGB
preto = (0, 0, 0)
branco = (225, 225, 225)
# imagem do carro
carImg = pygame.image.load('car.png')

Game_Display = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Fam game")
tempo = pygame.time.Clock()
carLargura = 73


def coisas(coisX, coisaY, coisaLargura, coisaAltura, cor):
    pygame.draw.rect(Game_Display, cor, [coisX, coisaY, carLargura, coisaAltura])


def car(x, y):
    Game_Display.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, preto)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((LARGURA / 2), (ALTURA / 2))
    Game_Display.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    gameloop()


def crash():
    message_display('Vc bateu')


def gameloop():
    x = (LARGURA * 0.45)
    y = (ALTURA * 0.8)

    novoX = 0


    coisaStartX = random.randrange(0, LARGURA)
    coisaStartY = -600
    CoisaVelo = 7
    coisaAltura = 100
    coisaLargura = 100

    gamesair = False

    while not gamesair:
        # TRATAMENTO DE EVENTOS
        for evento in pygame.event.get():  # pegar eventos
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    novoX = -5
                elif evento.key == pygame.K_RIGHT:
                    novoX = 5
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    novoX = 0

        x += novoX
        Game_Display.fill(branco)

        coisas(coisaStartX, coisaStartY, coisaLargura, coisaAltura, preto)
        coisaStartY += CoisaVelo

        car(x, y)

        if x > LARGURA - carLargura or x < 0:
            crash()

        if coisaStartY > ALTURA:
            coisaStartY = 0 - coisaAltura
            coisaStartX = random.randrange(0, LARGURA)


        if y < coisaStartY + coisaAltura:
            print("y passoouuuu")

            if x > coisaStartX and x < coisaStartX + coisaLargura or x + carLargura > coisaStartX and carLargura < coisaStartX + coisaLargura:
                print("x passoouu")
                crash()

        pygame.display.update()
        tempo.tick(60)


gameloop()
# Saindo do main loop
pygame.quit()
quit()
