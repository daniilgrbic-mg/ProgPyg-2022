####################################################################################
print('PRVI PRIMER: loklano i globalno a')

a = 4

def f():
    a = 5   # ovo a je lokalno, a ne 2. liniji je gobalno (dakle nisu isti)
    print(a)  

f()
print(a)



####################################################################################
print('DRUGI PRIMER: globalno b u funkciji')

b = 4

def g():
    global b   # koristimo globalno b, dakle isto ce biti i u funkciji i izvan nje
    b = 5
    print(b)  

g()
print(b)

