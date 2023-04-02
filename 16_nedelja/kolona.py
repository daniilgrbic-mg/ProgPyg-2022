import pygame
import pygamebg

prozor = pygamebg.open_window(200,800,"Kolona")

kolona = ["yellow"]

def update_frejm():
    prozor.fill(pygame.Color("blue"))
    for i in range(len(kolona)):
        pygame.draw.circle(
            prozor, 
            pygame.Color(kolona[i]), 
            (100, 750-i*100),
            40
        )

def handle_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(event.button)
        if event.button == 1:
            if len(kolona) < 8:
                kolona.append("yellow")
        if event.button == 3:
            if len(kolona) > 0:
                kolona.pop()


pygamebg.frame_loop(30, update_frejm, handle_event)
