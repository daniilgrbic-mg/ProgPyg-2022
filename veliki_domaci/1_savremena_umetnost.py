import pygame
import pygamebg

prozor = pygamebg.open_window(1000, 1000, "UMETNOST.")

prozor.fill(pygame.Color("black"))
pygame.draw.rect(prozor, pygame.Color("red"), (0, 0, 500, 500))
pygame.draw.rect(prozor, pygame.Color("blue"), (500, 500, 500, 500))
pygame.draw.circle(prozor, pygame.Color("white"), (500, 500), 250)
pygame.draw.polygon(prozor, pygame.Color("green"), [(500, 0), (500,500), (1000,500)])
pygame.draw.line(prozor, pygame.Color("black"), (0, 1000), (1000, 0), 50)

pygamebg.wait_loop()