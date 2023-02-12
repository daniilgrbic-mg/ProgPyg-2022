import pygame
import pygamebg

prozor = pygamebg.open_window(800, 800, "Popunjavanje")

mat = [
    [False, True, False, False],
    [False, False, False, False],
    [False, False, False, True],
    [False, False, False, False]
]

def crtaj():
    for br_red, red in enumerate(mat):
        for br_kol, polje in enumerate(red):
            if polje:
                pygame.draw.rect(
                    prozor,
                    pygame.Color("red"),
                    (br_kol*200, br_red*200, 200, 200)
                )
            
def obradi_dogadjaj(dogadjaj):
    if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
        print(f'{dogadjaj.pos = }')
        x = dogadjaj.pos[0]
        y = dogadjaj.pos[1]
        br_kol = x // 200
        br_red = y // 200
        mat[br_red][br_kol] = True

pygamebg.frame_loop(30, crtaj, obradi_dogadjaj)
