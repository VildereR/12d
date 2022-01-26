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
