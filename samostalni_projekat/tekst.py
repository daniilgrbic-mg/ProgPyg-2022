import pygamebg
import pygame
from pygame import Vector2, Color, Rect

prozor = pygamebg.open_window(600, 400, "Tekst")

font = pygame.font.Font(None, 50)

def crtaj():
    prozor.fill(Color("white"))
    slika_teksta = font.render("Zdravo svete!", True, Color("black"))
    prozor.blit(slika_teksta, (20, 20))

def obradi_dogadjaj(dogadjaj):
    pass

pygamebg.frame_loop(30, crtaj, obradi_dogadjaj)