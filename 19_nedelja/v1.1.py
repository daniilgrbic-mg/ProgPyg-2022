import pygamebg
import pygame
from pygame import Vector2, Color, Rect

prozor = pygamebg.open_window(600, 400, "Pong")

# uvek je lepa ideja da dinamicke stvari odvojite u zasebne promenljive 
# (lopta je dinamicka jer se krece i pratmo njenu poziciju, a reketima upravljaju igraci)
lopta = Vector2(300, 200)
igrac1 = Rect(20, 200-30, 10, 50)
igrac2 = Rect(600-20-10, 200-30, 10, 50)

def crtaj():
    prozor.fill(Color("white"))
    pygame.draw.circle(prozor, Color("black"), lopta, 10)
    pygame.draw.rect(prozor, Color("black"), igrac1)
    pygame.draw.rect(prozor, Color("black"), igrac2)

def obradi_dogadjaj(dogadjaj):
    pass

pygamebg.frame_loop(30, crtaj, obradi_dogadjaj)