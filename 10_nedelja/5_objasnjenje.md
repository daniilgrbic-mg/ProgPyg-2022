# 5. Kosi hitac, racunski zadatak

Pogledajmo sledecu situaciju: imamo loptu na poziciji `x0 = 0` i `y0 = 450` , koju ispaljujemo brzinom `vx = 50`, `vy = -50` (`vy` je negativna jer se telo krece nagore unutar Pygame prozora). Visina prozora je `900`. Zelimo da nadjemo na kojoj udaljenosti od pocetka lopta pada na dno prozora.

Da bude jasnije evo slike kako izgleda kretanje, zadatak je da nadjemo `x`-koordinatu crvene linije:

<img src="/10_nedelja/5_slika.png" style="width: 50%">

<hr>

## Kako?

Bice nam potrebne formule ravnomernog i ubrzanog kretanja:
- `pozicija = pocetna_pozicija + brzina * vreme`
- `pozicija = pocetna_pozicija + brzina * vreme + 1/2 * ubrzanje * vreme_na_kvadrat`

Za `x`-koordinatu vazi:
- `x = 0 + 50 * t`, odnosno ako nadjemo `t` znacemo i `x`, a to bas trazimo!

Za `y`-koordinatu vazi:
- `y = 900` krajnja visina
- `y0 = 450` pocetna visina
- `900 = 450 - 50 * t + 1/2 * 10 * t * t` , odnosno <br>
    `900 = 450 - 50 * t + 5 * t * t`

Ovo mozemo resiti koristeci [kvadratnu formulu](https://sr.wikipedia.org/wiki/Kvadratna_formula) (ukratko, to je formula za resavanje jednacina oblika `a + b*x + c*x*x = 0`, gde je `x` nepoznata, a `a`, `b` i `c` brojevi). Nama ovo nije bitno, bitno je samo da se dobije da je resenje otprilike `15.72`, odnosno `t = 15.72` sekundi.

> Mozete da proverite rezultat tako sto ubacite `t` u jednacinu `900 = 450 - 50 * t + 5 * t * t`. Dobija se `900 = 899.592`, imamo malu gresku zbog zaokrizvanaj ali to je zanemarljivo.

Doslo je vreme da odredimo `x` i da zavrsimo zadatak! Ako `t` ubacimo u jednacinu `x = 0 + 50 * t`, dobijamo `x = 786`.

<hr>

## Simuliranje uz pomoc Pajtona

> Kod koji simulira ovakvo kretanje mozete videti [ovde](/10_nedelja/5_hitac_sa_tragom.py)

Ali kako on radi?

Na pocetku koda postavljamo sve pocetne vrednosti:
```python
poz = Vector2(0, 450)
v = Vector2(50, -50)
g = Vector2(0, 10)
dt = 0.1
```

U petlji obnavljamo brzinu i poziciju:
```python
proslo_frejmova += 1
proslo_vremena += dt
```

Da bi shvatili sta se desava, sve dok je `y < 900` (dakle dok lopta nije pala) ispisujemo broj frejma, proteklo vreme i poziciju. (Ne brinite o tome da razumete ovaj kod, poenta je ispis na terminalu)
```python
if poz.y <= 900:
    print(f"{proslo_frejmova}. frejm, t = {proslo_vremena:.2f} s, pozicija = {poz}")
```

Sta ovaj program ispisuje? Pogledajmo poslednje 4 linije:
```
153. frejm, t = 15.30 s, pozicija = [765, 863.1]
154. frejm, t = 15.40 s, pozicija = [770, 873.5]
155. frejm, t = 15.50 s, pozicija = [775, 884]
156. frejm, t = 15.60 s, pozicija = [780, 894.6]
```

Vidimo da je kretanje trajalo `156` frejmova, sto odgovara bas vremenu ` t = 15.6 sekundi`. Kao sto smo pricali na casu, preciznost simulacije kretanja zavisi od vremnskog koraka `dt` (**sto je `dt` manje, to je kretanje preciznije ali zato traje duze**).

Kako mozemo da povecamo preciznost bez da cekamo 100 godina da se program zavrsi? tako sto **povecamo FPS**! 

Na primer, za vrednosti `FPS=10` i `dt=0.01` dobijamo rezultat koji je mnogo blizi pravom odgovoru: vreme kretanja je `15.71 sekundi`, a krajnja `x` pozicija je `785` umesto `780`! (prava vrednost je bliza `786`)   
```
1569. frejm, t = 15.69 s, pozicija = [784.5, 897.165]
1570. frejm, t = 15.70 s, pozicija = [785, 898.235]
1571. frejm, t = 15.71 s, pozicija = [785.5, 899.306]
```

<hr>

## Veza izmedju `FPS` i `dt`

Kao sto vidimo, `dt` utice na brzinu i preciznost:
- sto je `dt` vece, brzina raste, a preciznost pada
- sto je `dt` manje, to je kretanje sporije, a preciznost veca

S druge strane:
- sto je `FPS` veci, brzina je veca, i animacije je vise "glatka"
- sto je `FPS` manji, brzina je manja, i animacija krece da "secka"

Dakle, treba da imamo visok `FPS` i mali `dt`? Da, **ALI** bitno je da se shvati da maksimalna vrednost `FPS` zavisi od brzine racunara, i sto je `FPS` veci to racunar trosi vise energije (sto moze biti problem za prenosive uredjaje, na primer). Zato je najbitniji **balans** :)

![](https://media.tenor.com/Hqyg8s_gh5QAAAAC/perfectly-balanced-thanos.gif)