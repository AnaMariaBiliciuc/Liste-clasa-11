t=[0,1,3,6,8,9,10,10,12,13,16,17,18,16,15,14,12,10,8,6,5,3,2,1]
x=['ora1','ora2','ora3','ora4','ora5','ora6','ora7','ora8','ora9','ora10','ora11','ora12','ora13','ora14','ora15','ora16','ora17','ora18','ora19','ora20','ora21','ora22','ora23','ora24']
s=0
m=0
for i in t:
    s=s+i
    m=s/len(t)
print("Temperatura medie este: ",int(m),"grade")
print("Temperatura maxima inregistrata in aceasta zi:",max(t),"grade")
print("Temperatura minima inregistrata in aceasta zi:",min(t),"grade")
m1=t.index(max(t))
m2=t.index(min(t))
print("Temperatura maxima s-a inregistrat la", x[m1])
print("Temperatura minima s-a inregistrat la ora", x[m2])
