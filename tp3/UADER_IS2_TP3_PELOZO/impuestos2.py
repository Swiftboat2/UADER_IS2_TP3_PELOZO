class ImpuestosCalculator:
    _instance = None
    IVA = 0.21
    IIBB = 0.05
    MUNICIPAL = 0.012

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def calcular_impuestos(self, base_imponible):
        iva = base_imponible * self.IVA
        iibb = base_imponible * self.IIBB
        municipal = base_imponible * self.MUNICIPAL
        total_impuestos = iva + iibb + municipal
        return total_impuestos

if __name__ == "__main__":
    calculator = ImpuestosCalculator()
    base_imponible = float(input("Ingrese el valor de la base imponible: "))
    impuestos_totales = calculator.calcular_impuestos(base_imponible)
    print("El total de impuestos a pagar es:", impuestos_totales)
