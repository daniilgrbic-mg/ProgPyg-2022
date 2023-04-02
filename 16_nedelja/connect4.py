import pygame
import pygamebg

prozor = pygamebg.open_window(700,600,"Kolona")

red, kol = 6, 7
kolone = [[], [], [], [], [], [], []]

na_redu = "yellow"  # koji je igrac na redu (zut ili crven)

def update_frejm():
    prozor.fill(pygame.Color("blue"))
    for i in range(red):
        for j in range(kol):
            pygame.draw.circle(
                prozor,
                pygame.Color("white"),
                (50+j*100, 50+i*100),
                40
            )

    for i_kolona in range(len(kolone)):
        for j in range(len(kolone[i_kolona])):
            pygame.draw.circle(
                prozor, 
                pygame.Color(kolone[i_kolona][j]), 
                (50+i_kolona*100, 550-j*100),
                40
            )


def obradi_dogadjaj(dogadjaj):
    global na_redu
    if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
        x, y = dogadjaj.pos
        kolona = x//100
        print(f'{x=} {y=} {kolona=}')
        if len(kolone[kolona]) < 6:
            kolone[kolona].append(na_redu)
            na_redu = "yellow" if na_redu=="red" else "red"

pygamebg.frame_loop(30, update_frejm, obradi_dogadjaj)
