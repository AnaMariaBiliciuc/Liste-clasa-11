x=[1,2,3,4,5]
y=x
s1=x[0]+x[1]+x[2]
print("Suma primelor 3 componente a variabilei x este:", s1)
print("Suma tuturor componentelor variabilei y este:", sum(y))
p=1
for i in x :
    p=p*i
print("Produsul componentelor variabilei x este:",p)
print("Valoarea absoluta a componentei a3 a variabilei x:", x[2]) 
s2= x[0]+y[0]
print("Suma primelor componente a variabilelor x,y: ", s2)