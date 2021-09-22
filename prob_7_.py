v=[220,340,260,780,100,500,40]
zi=['Luni','Marti','Miercuri','Joi','Vineri','Sambata','Duminica']
s= sum(v)
m=0
print("Venitul saptamanal al interpinderii este:",s)
for i in v:
    m=s/len(v)
print("Media venitului zilnic este:",m)
m1=v.index(max(v))
print("Ziua cu venitul cel mai mare",zi[m1])
m2=v.index(min(v))
print("Ziua cu venitul cel mai mic:",zi[m2])