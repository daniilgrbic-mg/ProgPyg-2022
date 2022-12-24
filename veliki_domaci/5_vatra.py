import pygamebg
import pygame as pg

window = pygamebg.open_window(800, 800, "Приказ слике")

baklja = pg.image.load("./baklja.png")
vatra = []
for i in range(1, 61):
    img = pg.image.load("./vatra/vatra_"+str(i)+".png")
    img = pg.transform.scale(img, (400,400))
    vatra.append(img)

frame = 0

def update_frame():
    global frame
    
    window.fill(pg.Color("white"))
    window.blit(baklja, (260, 270))
    window.blit(vatra[frame], (200, 40))

    frame += 1
    if frame == 60:
        frame = 0

pygamebg.frame_loop(10, update_frame)