# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0
swaps = 0

def init(vals):
    global items, n, i, j, swaps
    items = list(vals)
    n = len(items)
    i = 0
    j = 0
    swaps = 0

def step():
    global items, n, i, j, swaps # TODO:
    
    if i>=n-1: #si el algoritmo terminó
        print("Bubble Sort – swaps totales:", swaps)
        return {"done": True}#devuelve que ya no hay mas pasos
    
    a=j
    b=j+1# 1) Elegir índices a y b a comparar en este micro-paso (según tu Bubble).
    swap=False
    if items[a]>items[b]:
        items[a],items[b]=items[b],items[a]
        swap=True # 2) Si corresponde, hacer el intercambio real en items[a], items[b] y marcar swap=True.
        swaps += 1
    
    # 3) Avanzar punteros (preparar el próximo paso).
    if j+1<n-i-1: #si todavia quedan comparaciones
        j+=1  
    else:  
        j=0     #reinicia j y avanza i
        i+=1
    return {"a": a, "b": b, "swap": swap, "done": False}
    # 4) Devolver {"a": a, "b": b, "swap": swap, "done": False}.
    #
    # Cuando no queden pasos, devolvé {"done": True}.
