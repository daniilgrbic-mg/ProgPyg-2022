# Podsetnik

<h2 style="color: red;">Uvek pazite na mala/velika slova!</h2>


## Pocetak programa: ukljucivanje biblioteka

```python
# za kreiranje prozora
import pygamebg

# za sve ostalo
import pygame as pg

# skracenica da mozemo da pisemo Vector2 umesto pg.Vector2
from pygame import Vector2
```


## Kreiranje prozora

```python
# ovo stoji na POCETKU programa, ali NAKON IMPORT-OVA!
prozor = pygamebg.open_window(600, 400, "NASLOV")
```
Dalje tokom iscrtavanje uvek korisite prozor koji ste napravili. Na primer, da obojite pozadinu pisacete:
```python
prozor.fill(BOJA)
```
... a za crtanje neke figure (na primer krug) pisacete:
```python
pg.draw.circle(prozor, BOJA, (X_CENTRA, Y_CENTRA), POLUPRECNIK)
```
#### **Programi u kojima iscrtavamo samo jednu sliku**
```python
import pygamebg
import pygame as pg

prozor = pygamebg.open_window(...)

# VAS KOD

pygamebg.wait_loop()   # bez ove linije nista nece da se prikaze!
```
#### **Programi u kojima se slika menja (animacije)**
```python
import pygamebg
import pygame as pg

prozor = pygamebg.open_window(...)

# INICIJALIZACIJA

def update():
    # KOD OVDE SE POZIVA SVAKI FREJM

pygamebg.frame_loop(FPS, update)   # slika se menja FPS broj puta u sekundi!
```


## Boje u Pygame-u
Boje se zadaju ili nazivom:
```
pg.Color("red")
```
ili RGB komponentama (RGB = Red/Green/Blue = Crvena/Zelena/Plava):
```
pg.Color(165, 3, 252)
```
(ovom kodu odgovara <span style="color:#a503fc;">**ova boja**</span>, svoje boje mozete napraviti pomocu [guglovog alata](https://g.co/kgs/u22x4S))


## Funkcije za iscrtavanje nekih figura

Svugde gde pise `tacka` mozete ili staviti par `(x, y)` ili vektor `Vektor2(x, y)`. Druga opcija je povoljnija ukoliko vam treba neka tacka koja se pomera.

Ukoliko izostavite `opciono_debljina_linije`, figura ce biti "obojena", a ako tu opciju ipak stavite dobicete samo stranice/ram figure.

```python
# duz
pg.draw.line(PROZOR, BOJA, pocetna_tacka, krajnja_tacka, debljina)

# krug
pg.draw.circle(PROZOR, BOJA, centar_tacka, poluprecnik, opciono_debljina_linije)

# pravougaonik - prva opcija
pg.draw.rect(PROZOR, BOJA, (x, y, sirina, visina), opciono_debljina_linije)

# pravougaonik - druga opcija
pg.draw.rect(PROZOR, BOJA, (gornja_leva_tacka, (sirina, visina)), opciono_debljina_linije)

# mnogougao (stavljate LISTU tacaka!)
pg.draw.polugon(PROZOR, BOJA, [tacka_1, tacka_2, tacka_3, ...], opciono_debljina_linije)

```

