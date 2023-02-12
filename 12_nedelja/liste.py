dani = ['pon', 'uto', 'sre', 'cet']

print(dani)
print(dani[1])

dani.append('sub')
print(dani)

dani[4] = 'pet'
print(dani)

# dani.remove('uto')
# print(dani)

# dani.pop(2)
# print(dani)

if 'sub' in dani:
    print("subota je u listi")
else:
    print("subota nije u listi")


if 'sre' in dani:
    print("sreda je u listi")
else:
    print("sreda nije u listi")

# brojac = 1
# for element in dani:
#     print(str(brojac) + ". dan u nedelji je", element)
#     brojac += 1

for i, element in enumerate(dani):
    print(i, element)
