def szinek(lista, r):
    jelenlegi = tuple(lista)
    hossz = len(jelenlegi)
    if r > hossz:
        return
    resz = list(range(r))
    yield tuple(jelenlegi[x] for x in resz)
    while True:
        for x in reversed(range(r)):
            if resz[x] != x + hossz - r:
                break
        
        else:
            return
        resz[x] += 1
        for y in range(x+1, r):
            resz[y] = resz[y-1] + 1
        yield tuple(jelenlegi[x] for x in resz)

def kombinacio(szinlista):
    combo = 0
    for x in range(2, len(szinlista)+1):
        combo += len(list(szinek(szinlista, x)))
    return combo

szinlista = [] # a színeket ebbe a listába kell írni

print(kombinacio(szinlista))
