class CalculadoraDescuento:
    def calcularPorcentaje(self, precioYDescuento):
        precio = precioYDescuento[0]
        descuento = precioYDescuento[1]
        resultado = precio - (precio * 1/descuento)
        return resultado
    
    def aplicarDescuentofijo(self, precio):
        descuentoFijo = 20
        resultado = precio - 20
        return resultado