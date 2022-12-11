import pygame
import pygamebg

prozor = pygamebg.open_window(1200, 600, "Ubrzano kretanje")

# .. oznacava 'roditeljski direktorijum' - u nasem slucaju
# glavni direktorijum sa svim materijalima. U njemu se
# nalazi i folder 'sve_slike', a u njemu slika auto.png
slika_automobil = pygame.image.load("../sve_slike/auto.png")

pozicija = 0
brzina = 0
ubrzanje = 1

# ovo se poziva svaki frejm!
def frejm():
    prozor.fill(pygame.Color("white"))  # cistimo prozor

    # menjamo promenljive 'brzina' i 'pozicija' pa moramo da kazemo da su GLOBALNE
    global pozicija
    global brzina

    brzina += ubrzanje  # u svakom frejmu brzina se poveca (jer se krecemo ubrzano)
    pozicija += brzina  # u svakom frejmu se pomeramo desno sve vecom brzinom

    prozor.blit(slika_automobil, (pozicija, 200))  # crtamo auto na trenutnoj poziciji

pygamebg.frame_loop(30, frejm)