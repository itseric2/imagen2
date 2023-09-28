# Tabla de frecuencia
from math import sqrt
def redondeo(numero, cerca=0.5):
    diferencia_superior = numero - int(numero)
    if diferencia_superior >= cerca:
        return int(numero) + 1
    else:
        return numero

ei = input("Ingrese una lista de números separado por comas:  ")
s = ei.split(",")
ns = []
n = 0
for net in s:
    nm = float(net.strip())
    ns.append(nm)
    n += 1
xmax = max(ns)
xmin = min(ns)
rango = xmax - xmin
m = sqrt(n)
c = rango/m
decimales_deseados = 2
mr = round(m,decimales_deseados)
cr = round(c,decimales_deseados)
mrr = redondeo(mr)
crr = redondeo(cr)
contador = 0


print()
print("Xmax = Valor más grande\nXmin = Valor más pequeño\nRango = Xmax-Xmin\nN = Total de datos\nCantidad de intervalos(M) =  √N\nAmplitud de intervalos(C) Rango/M\nmedia(x̅) = suma(xifi)/n\nmoda(Mo) = li+[(fi-fi-1)/(fi-fi-1)+(fi-fi+1)]\nmediana(Me) = li+[(((n/2)+Fi-1)/fi)*C\n\n")
print("Xmax = ",xmax,"\nXmin = ",xmin,"\nRango = ",rango,"\nN = ",n,"\nM = ",mr,"=",mrr,"\nC = ",cr,"=",crr)


print()
print("Tabla de Frecuencia")


li = xmin
ls = xmin + crr
fi = [0] * int(mrr + 1)  
Fi = [0] * int(mrr + 1)
lli = []
sxifi = 0
print(" Li  -  Ls     Xi    fi    Fi    xifi")
cdci = 0
while contador <= mrr:
    contador += 1
    cdci += 1
    if cdci > mrr :
        break
    xi = (li + ls) / 2
    xir = round(xi,decimales_deseados)
    xifi = li + ls
    xifir = round(xifi,decimales_deseados)
    lli.append(li)
    sxifi += xifi
    for num in ns:
        if li <= num < ls:
            fi[contador - 1] += 1
    Fi[contador - 1] = sum(fi)
    fi_r = round(fi[contador - 1],decimales_deseados)
    Fi_r = round(Fi[contador - 1],decimales_deseados)
    print(li, "-", ls, "   ", xir, "   ", fi_r, "   ", Fi_r, "   ", xifir)
    li = ls
    ls += crr

media = sxifi/n
media_r = round(media,decimales_deseados)
print("\nMedia (x̅) = ",media_r)


Li_mas_cercano = 0
distancia_minima = float("inf")
for lim_inf in lli:
    if lim_inf <= media and media - lim_inf < distancia_minima:
        Li_mas_cercano = lim_inf
        distancia_minima = media - lim_inf
indice_Li = lli.index(Li_mas_cercano)
fi_modal = fi[indice_Li]
Mo = Li_mas_cercano + ((fi_modal - fi[indice_Li - 1]) / (fi_modal - fi[indice_Li - 1] + fi[indice_Li + 1])) * c
Mo_r = round(Mo,decimales_deseados)
print("Li =",Li_mas_cercano)
print("Moda (Mo) =", Mo_r)


indice_intervalo_anterior = indice_Li - 1
if indice_intervalo_anterior >= 0:
    Fi_anterior = Fi[indice_intervalo_anterior]
else:
    Fi_anterior = 0
print("fi =",fi_modal)
print("Fi-1 =", Fi_anterior)
Me = Li_mas_cercano + ((n/2 - Fi_anterior)/fi_modal) * c
Me_r = round(Me,decimales_deseados)
print("Mediana (Me) =",Me_r)