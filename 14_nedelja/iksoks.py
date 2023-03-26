import pygame
import pygamebg

prozor = pygamebg.open_window(600, 600, "IKS OKS")

iks = pygame.image.load("iks.png")
oks = pygame.image.load("oks.png")
tabla = pygame.image.load("tabla.png")

PRAZNO = 0
IKS = 1
OKS = 2

potez = IKS

mat = [
    [PRAZNO, PRAZNO, PRAZNO],
    [PRAZNO, PRAZNO, PRAZNO],
    [PRAZNO, PRAZNO, PRAZNO]
]

def crtaj():
    prozor.blit(tabla,(0,0))
    for br_red, red in enumerate(mat):
        for br_kol, polje in enumerate(red):
            if polje == IKS:
                prozor.blit(iks,(br_kol*200, br_red*200))
            if polje == OKS:
                prozor.blit(oks,(br_kol*200, br_red*200))

            
def obradi_dogadjaj(dogadjaj):
    if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
        print(f'{dogadjaj.pos = }')
        x = dogadjaj.pos[0]
        y = dogadjaj.pos[1]
        br_kol = x // 200
        br_red = y // 200

        global potez
        if mat[br_red][br_kol] == PRAZNO:
            mat[br_red][br_kol] = potez
            potez = 3 - potez

pygamebg.frame_loop(30, crtaj, obradi_dogadjaj)
