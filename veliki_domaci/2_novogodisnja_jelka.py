import pygame as pg
import pygamebg

prozor = pygamebg.open_window(900, 900, "Jelka")

# bojimo pozadinu u belo
prozor.fill(pg.Color("white"))

# boje koje cemo koristiti
ZELENA = (0, 100, 36)
BRAON = (97, 26, 9)

# krošnja
pg.draw.polygon(prozor, ZELENA, [(150, 750), (450, 450), (750, 750)])
pg.draw.polygon(prozor, ZELENA, [(225, 600), (450, 300), (675, 600)])
pg.draw.polygon(prozor, ZELENA, [(300, 450), (450, 150), (600, 450)])
# stablo
pg.draw.rect(prozor, BRAON, (390, 750, 120, 150))

pygamebg.wait_loop()