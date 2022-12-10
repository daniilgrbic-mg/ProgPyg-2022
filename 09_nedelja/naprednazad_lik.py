import pygame
import pygamebg

prozor = pygamebg.open_window(800, 400, "Napred nazad")

# .. oznacava 'roditeljski folder/direktorijum', u nasem slucaju glavni 
# direktorijum u kojem su materijali sa svih nedelja. Zeljene slike se
# nalaze u direktorijumu 'lik' unutar 'sve_slike':
slike = [
    pygame.image.load("../sve_slike/lik/setanje1.png"),
    pygame.image.load("../sve_slike/lik/setanje2.png"),
    pygame.image.load("../sve_slike/lik/setanje3.png"),
    pygame.image.load("../sve_slike/lik/setanje4.png"),
    pygame.image.load("../sve_slike/lik/setanje5.png")
]

x_pozicija = 0
brzina = 15
brojac_frejmova = 0

def frejm():
    global x_pozicija
    global brzina
    global brojac_frejmova

    x_pozicija += brzina

    if x_pozicija > 690 or x_pozicija < 0:
        brzina = -brzina
        for i in range(5):
            slike[i] = pygame.transform.flip(slike[i], True, False)

    brojac_frejmova += 1

    prozor.fill(pygame.Color("beige"))
    prozor.blit(slike[brojac_frejmova%5], (x_pozicija, 0))

   

pygamebg.frame_loop(10, frejm)