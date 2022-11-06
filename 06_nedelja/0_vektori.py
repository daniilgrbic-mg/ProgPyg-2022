from pygame import Vector2

print("\nVektori a (=Vector2(10,20)) i b (=Vector2(5,-5)):")
a = Vector2(10, 20)
print(f"    a = {a}")
b = Vector2(5, -5)
print(f"    b = {b}")

print("\nKomponente i svojstva vektora:")
print(f"    X-komponenta:  a.x = {a.x}")
print(f"    Y-kompoenta:  a.y = {a.y}")
print(f"    Duzina (intenzitet):  a.length() = {a.length()}")

print("\nZbir i razlika vektora:")
print(f"    a + b = {a + b}")
print(f"    a - b = {a - b}")

print("\nOperacije sa vektorima:")
print(f"    Rotacija (okretanje): a.rotate(90) = {a.rotate(90)}")
print(f"    Mnozenje vektora brojem (promena intenziteta):  a * 2 = {a * 2}")
print(f"    Normalizacija (pravac isti, intenzitet nula):  a.normalize() = {a.normalize()}")
print(f"    Ugao izmedju vektora (u primeru b i X-osa):  b.angle_to( Vector2(1,0) ) = {b.angle_to( Vector2(1,0) )}")
