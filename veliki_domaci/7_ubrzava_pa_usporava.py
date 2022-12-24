import pygame
import pygamebg

prozor = pygamebg.open_window(1200, 600, "Ubrzano kretanje")

slika_automobil = pygame.image.load("../sve_slike/auto.png")

pozicija = 0
brzina = 0

def frejm():
    prozor.fill(pygame.Color("white"))

    global pozicija
    global brzina

    if pozicija <= 450:
        brzina += 1 
    elif brzina > 0:
        brzina -= 1
    pozicija += brzina

    prozor.blit(slika_automobil, (pozicija, 200))

pygamebg.frame_loop(30, frejm)