import pygame
import pygamebg

prozor = pygamebg.open_window(150,800,"Kolona")

kolona = []
potez = 0

def crtaj():
    prozor.fill(pygame.Color("blue"))
    for i in range(len(kolona)):
        x = 75
        y = 750 - i*100
        if kolona[i] == 0:
            pygame.draw.circle(prozor, pygame.Color("yellow"), (x, y), 40)
        else:
            pygame.draw.circle(prozor, pygame.Color("red"), (x, y), 40)

def obradi_dogadjaj(dogadjaj):
    global krugovi
    global potez
    if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
        if dogadjaj.button == pygame.BUTTON_LEFT:
            kolona.append(potez)
        if dogadjaj.button == pygame.BUTTON_RIGHT and len(kolona) > 0:
            kolona.pop()
        potez = 1 - potez
        print(kolona)

pygamebg.frame_loop(30, crtaj, obradi_dogadjaj)
