import pygamebg
import pygame as pg

window = pygamebg.open_window(600, 600, "Приказ слике")

sprites = []
for i in range(1, 8):
    img = pg.image.load("./slike/macka_puca/shooting_"+str(i)+".png")
    img = pg.transform.scale(img, (600,400))
    sprites.append(img)

frame = 0

def update_frame():
    global frame
    window.fill(pg.Color("white"))
    window.blit(sprites[frame], (0, 0))

    frame += 1
    if frame == 7:
        frame = 0

pygamebg.frame_loop(3, update_frame)