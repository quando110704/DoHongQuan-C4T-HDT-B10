population = [150300, 247100, 333300, 266800, 420900, 318000]
acreage = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
lo = len(population)
l = len(acreage)
for i in range(lo):
    for u in range(l):
        density = population[i]//acreage[u]
        print(density) 

