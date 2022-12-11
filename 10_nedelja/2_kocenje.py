import pygame
import pygamebg

prozor = pygamebg.open_window(1200, 600, "Ubrzano kretanje")

slika_automobil = pygame.image.load("../sve_slike/auto.png")

pozicija = 0
brzina = 40

def frejm():
    prozor.fill(pygame.Color("white")) 

    global pozicija
    global brzina

    # u svakom frejmu brzina se SMANJI (jer KOCIMO)
    # ukoliko je brzina vec nula, ne mozemo dalje da kocimo!
    if brzina > 0:
        brzina -= 1    
         
    pozicija += brzina  # u svakom frejmu se pomeramo desno sve manjom brzinom,  do zaustavljanja

    prozor.blit(slika_automobil, (pozicija, 200))  # crtamo auto na trenutnoj poziciji

pygamebg.frame_loop(30, frejm)