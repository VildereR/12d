mala=float(input("Ievadi malas garumu: "))
if mala<5 and mala>0:
    laukums1=mala*mala
    mala+=5
    laukums2=mala*mala
    procenti=laukums2*100/laukums1
    rez=procenti-100
    print(f"Mainās par {round(rez)}%")
else:
    print("Tādi malu garumi neder")

from math import pi as pi
radiuss=float(input("Ievadi riņķa rādiusa garumu: "))
hip=float(input("Ievadi trijstūra hipotenūzas garumu: "))
rl=pi*radiuss*radiuss
h=hip/2
tl=h*hip/2
starp=rl-tl
print(f"Riņķa līnijas laukums ir par {round(starp,1)} lielāks")
