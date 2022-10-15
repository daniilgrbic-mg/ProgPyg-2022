# Funkcije (16. okt)

Funkcija je deo koda koji za proizvoljan broj ulaznih podataka
(parametara) racuna i vraca neki rezultat. Na primer, pogledajte
funkciju koja racuna obim pravougaonika:
```python
def obim_pravougaonika(a, b):
    obim = 2*a + 2*b
    return obim
```
Ovde imamo 2 ulazna podatka: stranice pravougaonika `a` i `b`, 
unutar funkcije racunamo obim po poznatoj formuli, i zatim uz pomoc
komande `return` "vracamo" izracunatu vrednost. U kodu funkciju koristimo
(pozivamo) na sledeci nacin:
```python
obim = obim_pravougaonika(3, 5)
print(obim)  # ovo ce ispisati 16!
```
*[pogledajte (i pokrenite) kod](0_obim.py)*

---
Funckija moze ali i ne mora da vraca neku vrednost. Primer takve
funkcije je funkcija `pozdrav` koja kao ulazni podatak ima nisku
koja predstavlja ime neke osobe, a umesto da neku vrednost izracuna
ili vrati funkcija samo ispisuje u konzoli "Pozdrav, <ime>!"
```python
def pozdrav(ime):
    print("Pozdrav, " + ime + "!")

pozdrav("Marko") 
pozdrav("Jana")
```
Ovaj kod ispisuje 
```
Pozdrav, Marko!
Pozdrav, Jana!
```
*[pogledajte (i pokrenite) kod](1_pozdrav.py)*
