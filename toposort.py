# a: 0, b: 1, c: 2, d:3, e:4, f:5, g:6, x:7


# 1. korak: Preberi podatke in 
# jih spravi v obliko s katero lahko delaš

# Za vsako vozlišče kaže na id-je njegovih naslednikov
graf = [
    [1, 2] ,    # a: 0
    [3, 4] ,    # b: 1
    [3, 5] ,    # c: 2
    [4,]   ,    # d: 3
    []     ,    # e: 4
    [6, 4] ,    # f: 5
    []     ,    # g: 6
    [2, ]  ,    # x: 7
]

# 2. korak: Poračunamo kje naj začnemo
# Za vsako vozlišče (za vsak id od [0 do len(graf)-1]) v grafu si bomo poračunali 
# koliko jih kaže nanj

indeg = []

for j in range(len(graf)):
    indeg.append(0)

for vozlice in graf:
    for kaze_na in vozlice:
        indeg[kaze_na] += 1

print(indeg)

# 3. korak 

nule = []

for j in range(len(indeg)):

    if indeg[j] == 0:
        nule.append(j)

print(nule)
posortirano = []

while len(nule) != 0:
    
    trenutni = nule.pop() # Enega vzamemo ven
    posortirano.append(trenutni)
    sosedi = graf[trenutni]

    for sosed in sosedi:
        indeg[sosed] -= 1
        if indeg[sosed] == 0:
            nule.append(sosed)

if len(posortirano) == len(graf):
    print("POSORTIRANO")
    print(posortirano)
else:
    print("TALE RECEPT PA NI PRAV PRAKTIČEN ZA IZVEDBO")

