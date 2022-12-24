import pygame as pg
import pygamebg
from pygame import Vector2

prozor = pygamebg.open_window(800, 800, "PRIMER")
prozor.fill(pg.Color("beige"))

FPS = 60  # broj frejmova u sekundi, sto je veci to je simulacija brza i izgleda *bolje*

brojac = 0
pozicija = Vector2(10, 10)     # pocetna pozicija
brzina = Vector2(60, 0)        # pocetna brzina, izrazena u pikselima/sekund
gravitacija = Vector2(0, 9.81) # gravitacija, izrazena u pikselima kroz sekund na kvadrat

# broj sekundi izmedju dva frejma, sto je manje to je kretanje preciznije ali sporije
# u proslim zadatcima kada nismo imali dt, podrazumevali smo vrednost 1
dt = 0.1   

def frejm():
    prozor.fill(pg.Color("beige"))

    global pozicija
    global brzina
    pozicija += brzina * dt      # formula x = x0 + v*t
    brzina += gravitacija * dt   # formula v = v0 + a*t

    pg.draw.circle(prozor, pg.Color("black"), pozicija, 10)


pygamebg.frame_loop(FPS, frejm)