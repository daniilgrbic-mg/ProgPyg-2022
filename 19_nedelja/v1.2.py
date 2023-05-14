import pygamebg
import pygame
from pygame import Vector2, Color, Rect

# ov je lep dodatak jer mozete lako posle d amenjate velicinu prozora igre
SIRINA = 700
VISINA = 500

prozor = pygamebg.open_window(SIRINA, VISINA, "Pong")

lopta = Vector2(SIRINA//2, VISINA//2)

igrac1 = Rect(20, VISINA//2-30, 10, 50)
igrac2 = Rect(SIRINA-20-10, VISINA//2-30, 10, 50)

def crtaj():
    prozor.fill(Color("white"))
    pygame.draw.circle(prozor, Color("black"), lopta, 10)
    pygame.draw.rect(prozor, Color("black"), igrac1)
    pygame.draw.rect(prozor, Color("black"), igrac2)

def obradi_dogadjaj(dogadjaj):
    pass

pygamebg.frame_loop(30, crtaj, obradi_dogadjaj)