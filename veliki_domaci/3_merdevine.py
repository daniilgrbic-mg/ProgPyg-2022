import pygame as pg
import pygamebg

prozor = pygamebg.open_window(900, 900, "Rasveta")

prozor.fill(pg.Color("beige")) # bojimo pozadinu ekrana u bež

# leva strana
pg.draw.line(prozor, pg.Color("brown"), (300, 30), (300, 900 - 30), 10)
# desna strana
pg.draw.line(prozor, pg.Color("brown"), (600, 30), (600, 900 - 30), 10)

""" LOS NACIN!
pg.draw.line(prozor, pg.Color("brown"), (300, 150), (600, 150), 30) # 1. prečaga
pg.draw.line(prozor, pg.Color("brown"), (300, 300), (600, 300), 30) # 2. prečaga
pg.draw.line(prozor, pg.Color("brown"), (300, 450), (600, 450), 30) # 3. prečaga
pg.draw.line(prozor, pg.Color("brown"), (300, 600), (600, 600), 30) # 4. prečaga
pg.draw.line(prozor, pg.Color("brown"), (300, 750), (600, 750), 30) # 5. prečaga
"""

# Veoma bolji nacin!
for y in range(150, 751, 150):
    pg.draw.line(prozor, pg.Color("brown"), (300, y), (600, y), 30)

pygamebg.wait_loop()