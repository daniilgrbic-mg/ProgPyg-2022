import pygamebg
import pygame
from pygame import Vector2, Color, Rect

# ov je lep dodatak jer mozete lako posle d amenjate velicinu prozora igre
SIRINA = 700
VISINA = 500

prozor = pygamebg.open_window(SIRINA, VISINA, "Pong")

lopta = Vector2(SIRINA//2, VISINA//2)
brzina = Vector2(7, 2)

igrac1 = Rect(20, VISINA//2-30, 10, 50)
igrac2 = Rect(SIRINA-20-10, VISINA//2-30, 10, 50)
BRZINA = 5

def crtaj():
    global lopta
    global brzina
    global igrac1
    global igrac2

    # u svakom frejmu pomeramo rekete

    tasteri = pygame.key.get_pressed()

    if tasteri[pygame.K_w] and igrac1.y > 0:
        igrac1.y -= BRZINA
    if tasteri[pygame.K_s] and igrac1.y < VISINA - igrac1.h:
        igrac1.y += BRZINA

    if tasteri[pygame.K_UP] and igrac2.y > 0:
        igrac2.y -= BRZINA
    if tasteri[pygame.K_DOWN] and igrac2.y < VISINA - igrac2.h:
        igrac2.y += BRZINA

    # u svakom frejmu pomeramo lopticu i gledamo da s eodbije od zidova

    lopta += brzina
    if lopta.x < 0 or lopta.x > SIRINA: 
        brzina.x *= -1
    if lopta.y < 0 or lopta.y > VISINA: 
        brzina.y *= -1



    # u svakom frejmu crtamo novonastalu sliku

    prozor.fill(Color("white"))
    pygame.draw.circle(prozor, Color("black"), lopta, 10)
    pygame.draw.rect(prozor, Color("black"), igrac1)
    pygame.draw.rect(prozor, Color("black"), igrac2)

def obradi_dogadjaj(dogadjaj):
    pass

pygamebg.frame_loop(60, crtaj, obradi_dogadjaj)