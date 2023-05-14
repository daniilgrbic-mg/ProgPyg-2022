import pygamebg
import pygame
from pygame import Vector2, Color, Rect

prozor = pygamebg.open_window(600, 400, "Skelet")

def crtaj():
    prozor.fill(Color("white"))

def obradi_dogadjaj(dogadjaj):
    pass

pygamebg.frame_loop(30, crtaj, obradi_dogadjaj)