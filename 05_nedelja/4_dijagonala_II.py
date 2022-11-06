import pygamebg
import pygame

prozor = pygamebg.open_window(500, 500, "Prazan")

prozor.fill(pygame.Color("red"))

x = 0
y = 400
for i in range(5):
    pygame.draw.rect(prozor, pygame.Color("white"), (x, y, 100, 100))
    x += 100
    y -= 100


pygamebg.wait_loop()
