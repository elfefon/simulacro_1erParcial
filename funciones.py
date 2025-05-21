#funciones a usar aca:

def append_manual(lista=list, elemento=str):
    """
    Agrega un elemento a la lista y la retorna
    """
    return lista + [elemento]

def comprobacion_input (mensaje=str):
    """
    En esta funcion ingresamos un texto, el cual luego lo ponemos en un variable, y verificamos que sea un numero, sino es asi le pedimos al usuario que vuelva a hacer el input.
    """

    #inicializamos bandera para ingresar al while
    bandera = True

    while bandera:

        entrada = input(mensaje) 

        if entrada.isdigit(): #comprobamos que haya un numero en el input
            return int(entrada) #cambiamos el tipo de la variable            
        else:
            print("ingrese lo pedido")

#funciones a exportar:

def menu():

    opciones = 0  # inicializamos opciones

    while opciones != 6: #no importa como entramos debido a que se va a romper el while pór el return
        print("\n--- Menú de Opciones --- \n1. Cargar producto/s \n2. Buscar producto. \n3. Ordenar inventario.\n4. Mostrar producto más caro y más barato \n5. Mostrar productos con precio mayor a 15000 \n6. Salir")

        opcion_input = input("\nIngrese una opción: ")

        if opcion_input.isdigit():  # validamos que sea numero
            opciones = int(opcion_input)
            if 1 <= opciones <= 6:
                return opciones  # retornamos la opcion elegida como int
            else:
                print("Por favor ingrese un número entre 1 y 6.")
        else:
            print("Entrada inválida. Ingrese un número.")

def cargar_inventario():
    
    cant_productos_input = comprobacion_input("Ingrese la cantidad de productos que quiere ingresar(en numero): ")

    lista = [] #inicializamos lista    

    #cargamos los datos que quiere ingresar:
    for i in range(cant_productos_input):

        producto = input ("ingresa el producto: ")
        precio = comprobacion_input("ingrese el precio: ")
        cantidad = comprobacion_input(f"ingrese la cantidad de {producto} (en formato de numero):")

        lista = append_manual(lista, producto)
        lista = append_manual (lista, precio)
        lista = append_manual (lista, cantidad)

    return lista

def buscar_producto(lista=list): #tenemos que ingresar una lista si o si
    """
    ingresamos una lista, y luego le pedimos al usuario que ingrese lo que quiere buscar dentro del inventario (que el mismo ingreso o el predeterminado) y se lo imprimimos con su stock y precio. 
    Caso contrario de que no se encuentre retorna un str
    """
    producto = input("ingrese el producto que quiere buscar: ")

    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i][j] == producto:
                return (lista[i])
    else:
        return ("elemento no encontrado")

def ordenar_inventario(lista=list):
    """
    es un ordenamiento burbuja, comparamos precio del indice 0 por el que sigue, y si es mayor cambian sus lugares, y asi consecutivamente hasta que encuentre un indice con precio mayor. Y luego sigue con el suigiente indice y hace lo mismo.
    """
    longitud = len(lista) #ya obtenemos el valor de lista 

    for i in range(longitud - 1):
        
        for j in range(longitud - 1 -i):

            if lista[j][1] > lista [j + 1][1]:

                #logica de cambio de lugar de inidices:

                aux = lista[j]
                lista [j]= lista[j + 1]
                lista [j + 1] = aux
    
    return lista #retornamos la lista ordenada

def mostrar_producto_mas_caro(lista=list):
    """
    ingresamos una lista, y comparamos su precio indice con "maximo", y si su valor es mayor se guarda en la misma, y asi precio por precio de cada indice de la matriz, hasta conseguir el mas caro.
    """
    logitud = len(lista)
    maximo = ["", float("-inf"), 0]   #inicializamos la lista
    #inicializamos 'float("-inf")' para no poner un valor exorbitante, y ademas por si todos los valores llegaran a ser negativos seguiria funcionando el codigo
    for i in range(1, logitud):
        if lista[i][1] > maximo[1]:
            maximo = lista [i]
    return maximo
lista = [
    ["almendras", 100, 22],
    ["manzana", 100, 59],
    ["mate", 1000, 28],
    ["yerba", 1500, 57],
    ["arroz", 9000, 24],
    ["termos", 17000, 55],
    ["bombillas", 3000, 20],
    ["facturas", 700, 50]
]
def mostrar_producto_mas_barato(lista=list):
    """
    ingresamos una lista, y comparamos su precio indice con "minimo", y si su valor es menor se guarda en la misma, y asi precio por precio de cada indice de la matriz, hasta conseguir el mas barato.
    """
    logitud = len(lista)
    minimo = ["", float("inf"), 0]  #inicializamos la lista
    #inicializamos 'float("inf")' inicializamos asi para no poner un valor exorbitante

    for i in range(1, logitud):

        if lista[i][1] < minimo[1]:
            minimo = lista [i]
    return minimo

def mostrar_producto_mayor_a_15000(lista):
    """
    ingresamos una lista, y comparamos su precio indice con "15000", y se van guardando en una lista aquellos productos que cumplan con la condicion.
    """
    logitud = len(lista)
    lista_maximos = []
    maximo = ["",15000, 0]   #inicializamos la lista
    #inicializamos '15000' para que entre solo aquellos de mayor a ese precio
    for i in range(1, logitud):
        
        if lista[i][1] > maximo[1]:

            lista_maximos = append_manual(lista_maximos, lista[i]) 

    return lista_maximos
