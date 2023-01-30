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

    # kada stisnemo bilo koji taster, boja se PROMENI
    if dogadjaj.type == pygame.KEYDOWN:
        if dogadjaj.key == pygame.K_SPACE:
            if boja == "red": 
                # ako je bila crvena, postane zelena
                boja = "green"
            else: 
                # ako je bila zelena, postane crvena
                boja = "red"

pygamebg.frame_loop(30, update, handle_event)
