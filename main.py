lista = [
    ["almendras", 100, 22],
    ["manzana", 100, 59],
    ["mate", 1000, 28],
    ["yerba", 1500, 57],
    ["arroz", 900, 24],
    ["termos", 15000, 55],
    ["bombillas", 3000, 20],
    ["facturas", 700, 50]
]

from funciones import * #importamos todo

bandera = True

while bandera:
    if menu() == 1:
        lista = cargar_inventario()
    elif menu() == 2:
        buscar_producto(lista)
    elif menu() == 3:
        ordenar_inventario(lista)
    elif menu() == 4:
        valor = input("¿cual desea saber?\n¿el mas caro, o el mas barato?\n")
        if valor == "caro":
            mostrar_producto_mas_caro(lista)
        else:
            mostrar_producto_mas_barato(lista)
    elif menu() == 5:
        mostrar_producto_mayor_a_15000(lista)
    elif menu() == 6:
        bandera = False
        print("saliendo del programa...")