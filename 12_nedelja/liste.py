dani = ['ponedeljak', 'utorak', 'sreda', 'cetvrtak']

print(f'{dani = }')
print(f'{dani[1] = }')

# append(element) dodaje element na kraj liste
dani.append('subota')
print(f'{dani = }')

# ovako menjamo vrednost elementa sa rednim brojem
dani[4] = 'petak'
print(f'{dani = }')

# remove(element) uklanja element
dani.remove('utorak')
print(f'{dani = }')
dani = ['ponedeljak', 'utorak', 'sreda', 'cetvrtak', 'petak'] # vracam na staro

# pop(broj) uklanja element na rednom broju
dani.pop(2)
print(f'{dani = }')
dani = ['ponedeljak', 'utorak', 'sreda', 'cetvrtak', 'petak'] # vracam na staro

if 'subota' in dani:
    print("subota je u listi")
else:
    print("subota nije u listi")

if 'sreda' in dani:
    print("sreda je u listi")
else:
    print("sreda nije u listi")

# ispituje redne brojeve i dane u nedelji sa brojacem
# brojac = 1
# for element in dani:
#     print(f'{brojac}. dan u nedelji je {element}')
#     brojac += 1

# ispituje redne brojeve i dane u nedelji sa enumerate (brojac ide od 0)
for i, element in enumerate(dani):
    print(f'{i+1}. dan u nedelji je {element}')
