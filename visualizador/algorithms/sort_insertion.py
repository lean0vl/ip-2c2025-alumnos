# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0	     # Cantidad de elementos que tendrá la lista y que serán ordenados
i = 0      # índice del elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)
swaps = 0

def init(vals): 
    global items, n, i, j, swaps
    items = list(vals)
    n = len(items)
    i = 1      # insertion sort empieza en el segundo elemento
    j = None
    swaps = 0

def step():
    global items, n, i, j, swaps

    #Todo
    # - Si i >= n: devolver {"done": True}.
    if i >= n:
        print("Insertion Sort – swaps totales:", swaps)
        return {"a": None, "b": None, "swap": False, "done": True}

    # - Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap.
    if j is None:
        j = i
        if j > 0:
            return {"a": j-1, "b": j, "swap": False, "done": False}
        else:
            return {"a": 0, "b": 0, "swap": False, "done": False}

    # - Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True.
    if j > 0 and items[j-1] > items[j]:
        items[j-1], items[j] = items[j], items[j-1]
        swaps += 1
        j -= 1
        return {"a": j, "b": j+1, "swap": True, "done": False}

    # - Si ya no hay que desplazar: avanzar i y setear j=None.
    i += 1
    j = None
    return {"a": None, "b": None, "swap": False, "done": False}
