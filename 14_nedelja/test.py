import pygame
import pygamebg

prozor = pygamebg.open_window(600, 600, "IKS OKS")

sl_tabla = pygame.image.load("tabla.png")
sl_iks   = pygame.image.load("iks.png")
sl_oks   = pygame.image.load("oks.png")

PRAZNO = 0
IKS = 1
OKS = 2

tabla = [
    [PRAZNO, PRAZNO, PRAZNO],
    [PRAZNO, PRAZNO, PRAZNO],
    [PRAZNO, PRAZNO, PRAZNO]
]

potez = IKS

def crtaj():
    prozor.blit(sl_tabla, (0, 0))
    for red in range(3):
        for kol in range(3):
            x = kol*200
            y = red*200
            if tabla[red][kol] == IKS:
                prozor.blit(sl_iks, (x, y))
            if tabla[red][kol] == OKS:
                prozor.blit(sl_oks, (x, y))

def obradi_dogadjaj(dogadjaj):
    global potez
    if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
        x, y = dogadjaj.pos
        red = y // 200
        kol = x // 200
        tabla[red][kol] = potez

        # 1. nacin
        #potez = 3 - potez

        # 2. nacin
        if potez == IKS:
            potez = OKS
        else:
            potez = IKS

pygamebg.frame_loop(30, crtaj, obradi_dogadjaj)
