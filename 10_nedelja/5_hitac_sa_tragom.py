import pygame
import pygamebg
from pygame import Vector2

prozor = pygamebg.open_window(1000, 900, "ubrzanje")

FPS = 10

poz = Vector2(0, 450)
v = Vector2(50, -50)
g = Vector2(0, 10)
dt = 0.1

proslo_frejmova = 0
proslo_vremena = 0   # ovo nije stvarno vreme, nego zavisi od dt i FPS

def frejm():
    global poz
    global v
    global proslo_frejmova
    global proslo_vremena

    v += g * dt
    poz += v * dt

    proslo_frejmova += 1
    proslo_vremena += dt

    # ukoliko nismo pali na dno ispisujemo broj frejma i proteklo vreme!
    if poz.y <= 900:
        print(f"{proslo_frejmova}. frejm, t = {proslo_vremena:.2f} s, pozicija = {poz}")

    pygame.draw.line(prozor, pygame.Color("red"), (786, 0), (786, 900), 5)
    pygame.draw.circle(prozor, pygame.Color("white"), poz, 10)

pygamebg.frame_loop(FPS, frejm)