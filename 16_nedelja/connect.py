import pygame
import pygamebg

prozor = pygamebg.open_window(700,600,"Kolona")

# pocetno stanje
kolone = [[1,2],[2],[],[1,1,1,2],[],[2],[]]

potez = 1

def crtaj():
    prozor.fill(pygame.Color("blue"))
    for kol in range(7):
        broj_el_u_koloni = len(kolone[kol])
        for i in range(broj_el_u_koloni):
            x = 50 + kol*100
            y = 550 - i*100
            if kolone[kol][i] == 1:
                pygame.draw.circle(prozor, pygame.Color("yellow"), (x, y), 40)
            else:
                pygame.draw.circle(prozor, pygame.Color("red"), (x, y), 40)

def obradi_dogadjaj(dogadjaj):
    global potez
    if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
        pos = dogadjaj.pos
        x, y = pos
        kol = x // 100
        if len(kolone[kol]) < 6:
            kolone[kol].append(potez)
            potez = 3 - potez

pygamebg.frame_loop(30, crtaj, obradi_dogadjaj)
