import pygamebg
import pygame

prozor = pygamebg.open_window(600, 400, "Dogadjaj")

def update():
    pass

# handle event
def obradi_dogadjaj(dogadjaj):
    if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
        if dogadjaj.button == pygame.BUTTON_LEFT:
            pygame.draw.circle(
                prozor,
                pygame.Color("white"),
                dogadjaj.pos,
                50
            )
        if dogadjaj.button == pygame.BUTTON_RIGHT:
            pygame.draw.circle(
                prozor,
                pygame.Color("red"),
                dogadjaj.pos,
                50
            )

pygamebg.frame_loop(30, update, obradi_dogadjaj)
