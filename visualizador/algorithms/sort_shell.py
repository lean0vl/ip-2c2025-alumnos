# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0

salto = 0
indice = 0
indice_interno = 0
guardado = None
fase = "nuevo_salto"
conteo_swaps = 0


def init(vals):
    global items, n, salto, indice, indice_interno, guardado, fase, conteo_swaps
    items = list(vals)
    n = len(items)

    salto = n // 2
    indice = salto
    indice_interno = 0
    guardado = None
    fase = "nuevo_salto"
    conteo_swaps = 0  


def step():
    global items, n, salto, indice, indice_interno, guardado, fase, conteo_swaps

    if fase == "fin":
        return {"done": True, "swaps": conteo_swaps}

    # fase: nuevo_salto
    if fase == "nuevo_salto":
        if salto == 0:
            fase = "fin"
            return {"done": True, "swaps": conteo_swaps}
        indice = salto
        fase = "nuevo_indice"
        return {"a": indice, "b": indice - salto, "swap": False, "done": False}

    # fase: nuevo_indice
    if fase == "nuevo_indice":
        if indice >= n:
            salto //= 2
            fase = "nuevo_salto"
            return {"a": 0, "b": 0, "swap": False, "done": False}
        guardado = items[indice]
        indice_interno = indice
        fase = "bucle_interno"
        return {"a": indice_interno, "b": indice_interno - salto, "swap": False, "done": False}

    # fase: bucle_interno
    if fase == "bucle_interno":
        if indice_interno >= salto and items[indice_interno - salto] > guardado:
            items[indice_interno] = items[indice_interno - salto]
            a = indice_interno
            b = indice_interno - salto
            indice_interno -= salto
            conteo_swaps += 1 
            return {"a": a, "b": b, "swap": True, "done": False}

        items[indice_interno] = guardado
        indice += 1
        fase = "nuevo_indice"
        return {"a": indice_interno, "b": indice_interno, "swap": False, "done": False}

    return {"done": True, "swaps": conteo_swaps}
