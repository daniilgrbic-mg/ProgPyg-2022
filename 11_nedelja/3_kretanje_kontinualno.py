import pygame 
import pygamebg
from pygame import Vector2

prozor = pygamebg.open_window(600, 400, "Dogadjaji")

pozicija = Vector2(300, 200)


def update():
    prozor.fill(pygame.Color("white"))

    # ovde umesto dogadjaja dohvatamo trenutno stanje svih tastera
    # na primer, keys[pygame.K_RIGHT] je True ako je stisnuta desna strelica, a False inace
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        pozicija.x += 5
    if keys[pygame.K_LEFT]:
        pozicija.x -= 5
    if keys[pygame.K_DOWN]:
        pozicija.y += 5
    if keys[pygame.K_UP]:
        pozicija.y -= 5

    pygame.draw.circle(prozor, pygame.Color("black"),pozicija,30)


def handle_event(dogadjaj):
    pass


pygamebg.frame_loop(30, update, handle_event)
