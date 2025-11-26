# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"
swaps = 0

def init(vals):
    global items, n, i, j, min_idx, fase, swaps
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"
    swaps = 0

def step():
    global items, n, i, j, min_idx, fase, swaps

    if i >= n-1:
        print("Selection Sort – swaps totales:", swaps)
        return {"done": True}

    if fase == "buscar":
        if j < n:
            j_actual = j
            if items[j] < items[min_idx]:
                min_idx = j

            j += 1

            return {"a": min_idx, "b": j_actual, "swap": False, "done": False}

        fase = "swap"

    if fase == "swap":
        a = i
        b = min_idx

        swapped = False
        if min_idx != i:
            items[a], items[b] = items[b], items[a]
            swapped = True
            swaps += 1

        i += 1
        if i < n:
            j = i + 1
            min_idx = i
            fase = "buscar"

        return {"a": a, "b": b, "swap": swapped, "done": False}
