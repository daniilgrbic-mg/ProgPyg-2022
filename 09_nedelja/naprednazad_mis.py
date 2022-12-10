import pygame
import pygamebg

prozor = pygamebg.open_window(800, 400, "Napred nazad")

# . oznacava trenutni folder, slike mis1.png i mis2.png 
# se nalaze na istom mestu kao i program!!!
mis1 = pygame.image.load("./mis1.png")
mis2 = pygame.image.load("./mis2.png")

x_pozicija = 0
brzina_misa = 5
krila_nagore = True
brojac_frejmova = 0

def frejm():
    global x_pozicija
    global brzina_misa
    global krila_nagore
    global brojac_frejmova

    # if x_pozicija < 544:
    #     x_pozicija += 5

    x_pozicija += brzina_misa

    if x_pozicija > 544 or x_pozicija < 0:
        brzina_misa = -brzina_misa

    brojac_frejmova += 1

    prozor.fill(pygame.Color("beige"))

    if krila_nagore == True:
        prozor.blit(mis1, (x_pozicija, 0))
    else:
        prozor.blit(mis2, (x_pozicija, 0))

    if brojac_frejmova % 5 == 0:
        krila_nagore = not krila_nagore
   

pygamebg.frame_loop(30, frejm)