import pygamebg
import pygame as pg

prozor = pygamebg.open_window(300, 300, "Приказ слике")

slika = pg.image.load("./slike/auto.png")
slika2 = pg.image.load("./slike/macka.png")

slika2 = pg.transform.scale(slika2, (300, 300))
# slika2 = pg.transform.flip(slika2, True, True)
slika2 = pg.transform.rotate(slika2, 30)

def update_frame():
    prozor.fill(pg.Color("white"))
    prozor.blit(slika, (0, 0))
    prozor.blit(slika2, (0, 0))

pygamebg.frame_loop(30, update_frame)