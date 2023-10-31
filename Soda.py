class Soda:
    marca = ""  # 0 Coca, 1 pepsi, 2 boing, 3 jarritos
    nombre = "" #*
    cantidad = 0  # int *
    precio = 0
    descuento = 0
    tamaño = 0  # 0 250ml, 1 500ml, 2 1L. 3 2.5L, 4 3L
    envase = 0  # 0 botellaplastico, 1 lata, 2 botellavidrio, 3 tetrapack
    idsoda = 0

    def abastecer(self, cantidadNueva):
        self.cantidad += cantidadNueva

    def precioTotal(self):
        self.precio *= self.descuento

    def venta(self, ventaproductos):
        return self.cantidad - ventaproductos

    def setMarca(self, nuevaMarca):
        self.marca = nuevaMarca

    def getMarca(self):
        return self.marca

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    def getNombre(self):
        return self.nombre

    def setCantidad(self, nuevaCantidad):
        self.cantidad = nuevaCantidad

    def getCantidad(self):
        return self.cantidad

    def setPrecio(self, nuevoprecio):
        self.precio = nuevoprecio

    def getPrecio(self):
        return self.precio

    def setEnvase(self, nuevoEnvase):
        self.envase = nuevoEnvase

    def getEnvase(self):
        return self.envase

    def setTamaño(self, nuevoTamaño):
        self.tamaño = nuevoTamaño

    def getTamaño(self):
        return self.tamaño

    def setDescuento(self, nuevoDescuento):
        self.descuento = nuevoDescuento

    def getDescuento(self):
        return self.descuento

    def setidSoda(self, nuevoIdSoda):
        self.idsoda = nuevoIdSoda

    def getidSoda(self):
        return self.idsoda

    def __init__(self, idSoda, marca, nombre, cantidad, precio, envase, tamaño, descuento):
        self.idsoda = idSoda
        self.marca = marca
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.envase = envase
        self.tamaño = tamaño
        self.descuento = descuento

    # def __del__(self):
    #   print("Se ha eliminado la instancia de la clase")

