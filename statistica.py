voti = []
print("inserisci i voti")
print("termina con exit")
riga = input()
while riga.isdigit() :
    voti.append(int(riga))
    riga = input()
voti.remove(min(voti))
voti.remove(max(voti))
print("la media depurata dei voti è", sum(voti)/len(voti))
for voto in voti :  
    print(voto)
