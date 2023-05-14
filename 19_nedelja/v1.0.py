import pygamebg
import pygame
from pygame import Vector2, Color, Rect

prozor = pygamebg.open_window(600, 400, "Pong")

def crtaj():
    prozor.fill(Color("white"))
    pygame.draw.circle(prozor, Color("black"), (300, 200), 10)
    pygame.draw.rect(prozor, Color("black"), (20, 200-30, 10, 50))
    pygame.draw.rect(prozor, Color("black"), (600-20-10, 200-30, 10, 50))

def obradi_dogadjaj(dogadjaj):
    pass

pygamebg.frame_loop(30, crtaj, obradi_dogadjaj)