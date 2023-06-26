#funzione che per una funzione, 
# (x = insieme dei punti sulle x, y insieme delle immagini di x)
# se non ti interessano le x, mettici una lista qualsiasi (magari con un indice
# che va da 0 a len(y)) basta che sia della stessa lunghezza di y!


def find_maxima(x,y,n):
    if len(x) != len(y):
        raise BaseException ("Le liste non sono di lunghezza uguale")
    maxima = []
    local = y[0]
    max_xs = []
    for i in range(len(x)-1):
        if y[i] >local and y[i] > y[i+1]:
            maxima.append(y[i])
            max_xs.append(x[i])
            local = y[i]
        else:
            local = y[i]
            #print("bb")
    #print(maxima,max_xs)
    max_rev = {} #qui vogliamo conservare l'ascissa relativa ad ogni massimo
    for i in range(len(maxima)):
        max_rev[maxima[i]] = max_xs [i] 
    maxima.sort(reverse = True)
    if len(maxima) < n:
        raise BaseException ("Non sono stati trovati abbastanza massimi")
    max_sorted = [maxima[k] for k in range(n)]
    max_x_sorted = [max_rev [t] for t in max_sorted]
    return (max_sorted , max_x_sorted)

