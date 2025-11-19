items = []
n = 0


pila = []          
inicio = 0
fin = 0
i = 0
j = 0
separador = 0         
fase = ""


def init(vals):
    global items, n, pila, fase
    items = list(vals)
    n = len(items)

    pila = [(0, n - 1)]
    fase = ""


def step():
    global pila, inicio, fin, i, j, separador, fase, items

    #tomar un nuevo segmento
    if fase == "":
        if not pila:
            return {"done": True}

        inicio, fin = pila.pop()

        #segmento de un solo elemento
        if inicio >= fin:
            return {"a": inicio, "b": fin, "swap": False, "done": False}

        # Elegimos separador (último elemento del segmento)
        separador = items[fin]
        i = inicio - 1
        j = inicio
        fase = "particionar"

        return {"a": j, "b": fin, "swap": False, "done": False}

    #fase particion

    if fase == "particionar":
        #cuando j llega al separador se hace swap final
        if j == fin:
            i += 1

            hacer_swap = (items[i] != items[fin])
            if hacer_swap:
                items[i], items[fin] = items[fin], items[i]

            indice_separador = i

            #subsegmentos izquierdo y derecho
            izquierda = (inicio, indice_separador - 1)
            derecha = (indice_separador + 1, fin)

            if izquierda[0] < izquierda[1]:
                pila.append(izquierda)
            if derecha[0] < derecha[1]:
                pila.append(derecha)

            fase = ""
            return {"a": i, "b": fin, "swap": hacer_swap, "done": False}

        #comparar con el separador
        if items[j] < separador:
            i += 1

            hacer_swap = (items[i] != items[j])
            if hacer_swap:
                items[i], items[j] = items[j], items[i]

            viejo_j = j
            j += 1
            return {"a": i, "b": viejo_j, "swap": hacer_swap, "done": False}

        #solo se avanza no se intercambia
        viejo_j = j
        j += 1
        return {"a": viejo_j, "b": fin, "swap": False, "done": False}
