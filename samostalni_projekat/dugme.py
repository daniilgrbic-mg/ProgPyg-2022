import pygamebg
import pygame
from pygame import Vector2, Color, Rect

prozor = pygamebg.open_window(600, 400, "Dugme")

font = pygame.font.Font(None, 50)

slika_teksta = font.render("Click me!", True, Color("black"))  # ovo napravi sliku/sprite sa tekstom
dugme = slika_teksta.get_rect().move(20, 20)  # get_rect() dohvati Rect slike, a move(20,20) pomeri taj rekt za vektor 20,20

def crtaj():
    prozor.fill(Color("white"))

    pygame.draw.rect(prozor, Color("gray"), dugme) # crtamo pravougaonik za dugme
    prozor.blit(slika_teksta, dugme) # crtamo tekst i nabijamo ga u pravougaonik

def obradi_dogadjaj(dogadjaj):
    if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
        if dugme.collidepoint(dogadjaj.pos):
            print("KLIK!")

pygamebg.frame_loop(60, crtaj, obradi_dogadjaj)