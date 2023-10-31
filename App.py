from Soda import Soda

capital = 0

salir = False
listaProductos = []
def menu():
    global salir
    while not salir:
        print(f"""
        ....Bienvenido al Menu de Soda.....
        .....¿Qué acción deseas hacer?.....
        1. Agregar producto
        2. Editar producto
        3. Vender producto
        4. Abastecer
        5. Mostrar Inventario
        6. Mostrar Balance
        7. Salir
    """)
        opcmenu = int(input("Ingresa una opción: "))
        match(opcmenu):
            case 1:
                agregarProducto()
            case 2:
                editarProducto()
            case 3:
                venderProducto()
            case 4:
                abastecer()
            case 5:
                mostrarInventario()
            case 6:
                mostrarBalance()
            case 7:
                salir = True
def agregarProducto():
    global capital
    print("Que producto desea agregar")
    nombre = input("Nombre: ")
    cantidad = int(input("Cuanta desea agregar: "))
    marca = int(input("0 -> Coca, 1 -> pepsi, 2 -> boing, 3 -> jarritos: "))
    precio = float(input("Precio: "))
    descuento = int(input("Descuento en % (ej: 10%): "))
    idSoda = len(listaProductos) + 1
    envase = int(input("0 botellaplastico, 1 lata, 2 botellavidrio, 3 tetrapack: "))
    tamaño = int(input("0  -> 250ml, 1 -> 500ml, 2 -> 1L, 3 -> 2.5L, 4 -> 3L:  "))

    descuento /= 100

    soda = Soda(idSoda, marca, nombre, cantidad, precio, envase, tamaño, descuento)
    listaProductos.append(soda)

    costo_compra = precio * cantidad
    capital -= costo_compra  # Restar el costo de compra al capital

    opcionAgrePro = input("Desea agregar otro producto (S/N): ")
    if opcionAgrePro == "S":
        agregarProducto()
    else:
        menu()


def getObtenerSodaID(id):
    for Soda in listaProductos:
        if Soda.getidSoda() == id:
            return Soda

def editarProducto():
    repetir = True
    while (repetir == True):
        mostrarInventario()
        id = int(input("Que ID desea editar? : "))
        Soda = getObtenerSodaID(id)
        if Soda != None:
            opceditarProducto = int(input("""Que desea editar del producto?: 
                                    1. Marca
                                    2. Nombre
                                    3. Cantidad
                                    4. Precio
                                    5. Envase
                                    6. Tamaño
                                    7. Descuento
                                    """))
            match(opceditarProducto):
                case 1:
                    marca = int(input("0 -> Coca, 1 -> pepsi, 2 -> boing, 3 -> jarritos: "))
                    Soda.setMarca(marca)
                case 2:
                    nombre = input("Nombre: ")
                    Soda.setNombre(nombre)
                case 3:
                    cantidad = int(input("Cuanta desea agregar: "))
                    Soda.setCantidad(cantidad)
                case 4:
                    precio = float(input("Precio: "))
                    Soda.setPrecio(precio)
                case 5:
                    envase = int(input("0 botellaplastico, 1 lata, 2 botellavidrio, 3 tetrapack: "))
                    Soda.setEnvase(envase)
                case 6:
                    tamaño = int(input("0  -> 250ml, 1 -> 500ml, 2 -> 1L, 3 -> 2.5L, 4 -> 3L:  "))
                    Soda.setTamaño(tamaño)
                case 7:
                    descuento = int(input("Descuento en % (ej: 10%): "))
                    Soda.setDescuento(descuento)
            opciondesEditPro = input("Desea agregar otro producto (S/N): ")
            if (opciondesEditPro == "S"):
                repetir = True
            else:
                menu()

def venderProducto():
    global capital
    repetir = True
    while repetir:
        mostrarInventario()
        id = int(input("Que ID desea vender? : "))
        Soda = getObtenerSodaID(id)
        if Soda is not None:
            productoventa = int(input("Cuanto producto desea vender? : "))
            productoactual = Soda.getCantidad()
            if productoventa > productoactual:
                print("No hay suficientes productos")
                venderProducto()
            else:
                Soda.setCantidad(productoactual - productoventa)
                ingresos_venta = Soda.getPrecio() * productoventa
                capital += ingresos_venta  # Sumar los ingresos de la venta al capital
                print("Venta exitosa :)")
            opciondesEditPro = input("Desea vender otro producto (S/N): ")
            if opciondesEditPro == "S":
                repetir = True
            else:
                menu()


def abastecer():
    repetir = True
    while (repetir == True):
        mostrarInventario()
        id = int(input("Que ID desea abastecer? : "))
        Soda = getObtenerSodaID(id)
        if Soda != None:
            productoabastecer = int(input("Cuanto producto desea abastecer? : "))
            productoactual = Soda.getCantidad()
            Soda.setCantidad(productoactual + productoabastecer)
            opciondesEditPro = input("Desea abastecer otro producto (S/N): ")
            if (opciondesEditPro == "S"):
                repetir = True
            else:
                menu()

def mostrarInventario():
    print("Este es el inventario")
    for Soda in listaProductos:
        print("|",f"""Id: {Soda.getidSoda()} | Marca: {Soda.getMarca()} | Nombre: {Soda.getNombre()} | Cantidad: {Soda.getCantidad()} | Precio: {Soda.getPrecio()} | Envase: {Soda.getEnvase()} | Tamaño: {Soda.getTamaño()} | Descuento: {Soda.getDescuento()}""","|")
        print("............................................................................................................................................................................................................................................................")

def llenarDatosPrueba():
    global listaProductos
    listaProductos.append(Soda(1,0,"coca cola",25,20,0,0,0))
    listaProductos.append(Soda(2,1,"Fuztea",20,0,2,30,1))
    listaProductos.append(Soda(3,2,"Pepsi",15,10,2,2,0))

def mostrarBalance():
    global capital
    print(f"Capital disponible: ${capital}")

llenarDatosPrueba()
menu()