class Factura:
    def __init__(self, importe, condicion_impositiva):
        self.importe = importe
        self.condicion_impositiva = condicion_impositiva

    def calcular_total(self):
        if self.condicion_impositiva == "1":
            total = self.importe * 1.21  
        elif self.condicion_impositiva == "2":
            total = self.importe
        elif self.condicion_impositiva == "3":
            total = self.importe * 1.00  
        else:
            raise ValueError("Opción de IVA no válida.")

        return total

    def generar_factura(self):
        total = self.calcular_total()
        print(f"Factura\nImporte: ${self.importe}\nCondición impositiva: {self.condicion_impositiva}\nTotal: ${total}")


# Ejemplo de uso
if __name__ == "__main__":
    importe = float(input("Ingrese el importe de la factura: "))
    print("Elija el tipo de IVA:")
    print("1. IVA Responsable (21%)")
    print("2. IVA No Inscripto")
    print("3. IVA Exento")

    opcion_iva = input("Ingrese el número correspondiente al tipo de IVA deseado (1/2/3): ")

    if opcion_iva not in {"1", "2", "3"}:
        print("Opción de IVA no válida.")
    else:
        factura = Factura(importe, opcion_iva)
        factura.generar_factura()
