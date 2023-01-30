# Obrada dogadjaja

Svaki pritisak tastera, klik, pomeraj misa, i slicno predstavlja jedan dogadjaj.

U nasim Pygame programima mozemo te dogadjaje "hvatati" i zatim na njih nekako reagovati.

Na primer, ukoliko zelim karakter u igri koju pravimo skoci kad pritisnemo SPACE taster, bilo bi potrebno da program napravimo tako da hvata i obradjuje bas taj dogadjaj.

---

Za hvatanje dogadjaja potrebno je da napravimo jednu funkciju, nazvacemo je u nase svrhe `obradi_dogadjaj()`:

```python
import pygamebg
import pygame

prozor = pygamebg.open_window(600, 400, "Program")

def update():
    pass

def obradi_dogadjaj(dogadjaj):
    pass

pygamebg.frame_loop(30, update, obradi_dogadjaj)
```

Ova funkcija ima jedan ulazni pdatak, a to je pristigli dogadjaj.

Na nama je da vidimo kakav je to dogadjaj, i da li cemo na njega reagovati (i kako) ili ne.

Postoji vise **tipova** dogadjaja, i tip je prva stvar koju moramo da proverimo. Za nas su bitni sledeci tipovi: 
- `pygame.KEDOWN` - neki taster je stisnut
- `pygame.KEYUP` - neki taster je pusten
- `pygame.MOUSEBUTTONDOWN` - stisnuto je dugme na misu
- `pygame.MOUSEBUTTONUP` - pusteno je udgme na misu
- `pygame.MOUSEMOTION` - pomeren je mis

Proveru vrsimo na sledeci nacin:
```python
def obradi_dogadjaj(dogadjaj):

    if dogadjaj.type == pygame.KEDOWN:
        # stisnut je taster!
        ...

    if dogadjaj.type == pygame.KEYUP:
        # pusten je taster!
        ...

    # dalje provere ako nam trebaju...
```

Nakon sto znamo koji je tip dogadjaja u pitanju, porebno je da saznamo i ostale bitne detalje. Na primer, ukoliko je kliknut taster, koji je taster u pitanju?

## Obrada klika tastera

Da bismo ustanovili koji je taster stisnut (ili pusten), moramo da proverimo vrednost `dogadjaj.key`.

Ta vrednost je jedan broj, a da ne bismo pamtili koji broj odgovara kom tasteru, Pygame za svaki taster ima pridruzene konstante oblika `pygame.K_<taster>`:
- `pygame.K_LEFT` , `pygame.K_RIGHT` , `pygame.K_UP`, `pygame.K_DOWN` - tasteri strelica
- `pygame.K_SPACE` - taster za razmak
- `pygame.K_a` , `pygame.K_b` ,.. - slova abecede `a`, `b`,..
- `pygame.K_1` , `pygame.K_2` - cifre

(pun spisak konstanti mozete naci [ovde](https://www.pygame.org/docs/ref/key.html))

Dakle, da napravimo program koji povecava brojac kad korisnik stisne SPACE, potrebno je da napisemo sledece:
```python
brojac = 0

def obradi_dogadjaj(dogadjaj):
    global brojac
    if dogadjaj.type == pygame.KEDOWN:
        if dogadjaj.key == pygame.K_SPACE:
            brojac += 1
```

## Obrada klika misem

Kad kliknemo misem ne postoji taster, ali postoji pitanje koje je dugme klinuto, kao i gde se na ekranu mis nalazi.

Da bismo saznali koje je dugme u pitanju, potrebno je da proverimo vrednost `dogadjaj.button`. Moze imati sledece brojcane vrednosti:  
1. ili `pygame.BUTTON_LEFT` - levo dugme
2. srednje dugme (nema svaki mis)
3. ili `pygame.BUTTON_RIGHT` - desno dugme
4. scroll nagore
5. scroll nadole

Pozicija klika je jedan par `(x, y)` koji mozemo da dohvatimo iz `dogadjaj.pos`.
