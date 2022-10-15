import pygamebg
import pygame as pg

prozor = pygamebg.open_window(400, 400, "Prazan")

# stablo jelke, dimenzija 40x40; gornja leva tacka pomerena za 20px od sredine (x=200-20), a 40px iznad dna (y=400-40)
pg.draw.rect(prozor, pg.Color("brown"), (200-20, 400-40, 40, 40))
pg.draw.polygon(
    prozor,
    pg.Color("green"),
    [
        (200, 0),           # vrh jelke u sredini ekrana (x=200) pri vrhu (y=0)
        (200-100, 400-40),  # donje levo teme za 100px levlje od sredine (x=200-100), 40px iznad dna (y=400-40)
        (200+100, 400-40)   # donje desno teme za 100px desno od sredine (x=200+100), 40px iznad dna (y=400-40)
    ]
)

pygamebg.wait_loop()
