import pygame 
import pygamebg

prozor = pygamebg.open_window(600, 400, "Dogadjaji")

boja = "red"

def update():
    prozor.fill(pygame.Color("white"))
    pygame.draw.circle(
        prozor, 
        pygame.Color(boja), 
        (300, 200), 
        100
    )

def handle_event(dogadjaj):
    global boja

    # kada stisnemo SPACE, boja postane zelena
    if dogadjaj.type == pygame.KEYDOWN:
        if dogadjaj.key == pygame.K_SPACE:
            boja = "green"

    # kada pustimo SPACE, boja se vrati u crvenu
    if dogadjaj.type == pygame.KEYUP:
        if dogadjaj.key == pygame.K_SPACE:
            boja = "red"

pygamebg.frame_loop(30, update, handle_event)
