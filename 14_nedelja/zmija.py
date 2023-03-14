import pygame
import pygamebg
import random

KOCKICA = 40
REDOVI = 15
KOLONE = 15

prozor = pygamebg.open_window(KOLONE*KOCKICA, REDOVI*KOCKICA, "ZMIJA")

jabuka = (REDOVI//2, KOLONE//2)

zmija = [
    (REDOVI//2, KOLONE//3),
    (REDOVI//2, KOLONE//3-1),
    (REDOVI//2, KOLONE//3-2)
]
pravac = "DESNO"

frejm = 0

def pomeri_se():
    global zmija
    global jabuka
    glava_red, glava_kol = zmija[0]
    if pravac == "DESNO":
        glava_kol += 1
    if pravac == "LEVO":
        glava_kol -= 1
    if pravac == "DOLE":
        glava_red += 1
    if pravac == "GORE":
        glava_red -= 1
    nova_glava = (glava_red, glava_kol)

    if glava_kol<0 or glava_red<0 or glava_red>=REDOVI or glava_kol>=KOLONE or nova_glava in zmija:
        print("GAME OVER")
        print("Score:", len(zmija)*100)
        exit()        

    if nova_glava == jabuka:
        jabuka = (random.randint(0, REDOVI-1),random.randint(0, KOLONE-1))
        while jabuka in zmija:
            jabuka = (random.randint(0, REDOVI-1),random.randint(0, KOLONE-1))
    else:
        zmija.pop()
    
    zmija = [nova_glava] + zmija

def crtaj():
    prozor.fill(pygame.Color("black"))
    for delic in zmija:
        red, kol = delic
        pygame.draw.rect(
            prozor,
            pygame.Color("white"),
            (kol*KOCKICA, red*KOCKICA, KOCKICA-1, KOCKICA-1)
        )
    red, kol = jabuka
    pygame.draw.circle(
        prozor,
        pygame.Color("red"),
        (kol*KOCKICA+KOCKICA//2, red*KOCKICA+KOCKICA//2),
        KOCKICA//2
    )

    global frejm
    frejm += 1
    if frejm % 5 == 0:
        pomeri_se()

def obradi_dogadjaj(dogadjaj):
    global pravac
    if dogadjaj.type == pygame.KEYDOWN:
        if dogadjaj.key == pygame.K_RIGHT:
            pravac = "DESNO"
        if dogadjaj.key == pygame.K_LEFT:
            pravac = "LEVO"
        if dogadjaj.key == pygame.K_DOWN:
            pravac = "DOLE"
        if dogadjaj.key == pygame.K_UP:
            pravac = "GORE"

pygamebg.frame_loop(30, crtaj, obradi_dogadjaj)
