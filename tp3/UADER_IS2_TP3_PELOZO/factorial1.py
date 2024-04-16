class FactorialCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def factorial(self, n):
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)
        
if __name__ == "__main__":
    calculator = FactorialCalculator()
    num = int(input("Ingrese un número entero para calcular su factorial: "))
    print("El factorial de", num, "es:", calculator.factorial(num))
