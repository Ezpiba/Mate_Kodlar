


def indirim_hesapla():
    tutar= float(input("Fiyatsız tutarı yazın\n"))
    i_y= float(input("İndirim yüzdesini yazın\n"))
    
    a = 100 - i_y
    b = (tutar * a)/100
    return (b)

print(indirim_hesapla())