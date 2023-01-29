import pygamebg
import pygame

prozor = pygamebg.open_window(600, 400, "Dogadjaj")

x = 300

# obnovi prozor / crtaj sliku
# poziva se 30 puta u sekundi
def update():
    global x
    
    tasteri = pygame.key.get_pressed()
    if tasteri[pygame.K_LEFT]:
        x -= 5
    if tasteri[pygame.K_RIGHT]:
        x += 5

    prozor.fill(pygame.Color("black"))
    pygame.draw.circle(
        prozor,
        pygame.Color("white"),
        (x, 200),
        50
    )

# handle event
# poziva se samo kad se desi neki dogadjaj
def obradi_dogadjaj(dogadjaj):
    global x

    # reagujemo na KEYDOWN dogadjaje, ostalo ignorisemo
    if dogadjaj.type == pygame.KEYDOWN:
        if dogadjaj.key == pygame.K_LEFT:
            x -= 10
        if dogadjaj.key == pygame.K_RIGHT:
            x += 10

pygamebg.frame_loop(30, update, obradi_dogadjaj)