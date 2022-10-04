import pygamebg
import pygame as pg

prozor = pygamebg.open_window(200, 400, "Prazan")

pg.draw.circle(prozor, pg.Color("white"), (100,100), 50)  # glava
pg.draw.line(prozor, pg.Color("white"), (100,100), (100,300), 5)  # telo
pg.draw.line(prozor, pg.Color("white"), (50,200), (150,200), 5)  # ruke
pg.draw.line(prozor, pg.Color("white"), (100,300), (50,350), 5)  # leva noga
pg.draw.line(prozor, pg.Color("white"), (100,300), (150,350), 5)  # desna noga

pygamebg.wait_loop()
