# Ejercicio 12.1: Definir el tipo de datos CUENTA

class Cuenta:
    def __init__(self, cliente, saldo):
        """
        Inicializa una cuenta de depósito con el nombre del cliente y el saldo.

        Args:
        - cliente (str): Nombre del cliente.
        - saldo (float): Saldo inicial de la cuenta.
        """
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, cantidad):
        """
        Deposita una cantidad en la cuenta.

        Args:
        - cantidad (float): Cantidad a depositar.
        """
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se depositaron {cantidad} en la cuenta de {self.cliente}. Nuevo saldo: {self.saldo}.")
        else:
            print("Error: La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        """
        Retira una cantidad de la cuenta si hay suficiente saldo.

        Args:
        - cantidad (float): Cantidad a retirar.
        """
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                print(f"Se retiraron {cantidad} de la cuenta de {self.cliente}. Nuevo saldo: {self.saldo}.")
            else:
                print("Error: Saldo insuficiente para realizar la retirada.")
        else:
            print("Error: La cantidad a retirar debe ser mayor que cero.")

# Ejemplo de uso
cuenta_cliente1 = Cuenta("Juan", 1000)
cuenta_cliente1.depositar(500)
cuenta_cliente1.retirar(200)

print("----------------------------------------------------------------")


# Ejercicio 12.3: Definir las operaciones aplicables permitiendo descubiertos limitados y temporales

class CuentaConDescubierto(Cuenta):
    def __init__(self, cliente, saldo, descubierto_maximo):
        """
        Inicializa una cuenta de depósito con la opción de descubierto.

        Args:
        - cliente (str): Nombre del cliente.
        - saldo (float): Saldo inicial de la cuenta.
        - descubierto_maximo (float): Límite máximo del descubierto permitido.
        """
        super().__init__(cliente, saldo)
        self.descubierto_maximo = descubierto_maximo

    def retirar(self, cantidad):
        """
        Retira una cantidad de la cuenta permitiendo descubierto limitado y temporal.

        Args:
        - cantidad (float): Cantidad a retirar.
        """
        if cantidad > 0:
            if self.saldo + self.descubierto_maximo >= cantidad:
                self.saldo -= cantidad
                print(f"Se retiraron {cantidad} de la cuenta de {self.cliente}. Nuevo saldo: {self.saldo}.")
            else:
                print("Error: Saldo insuficiente para realizar la retirada.")
        else:
            print("Error: La cantidad a retirar debe ser mayor que cero.")

# Ejemplo de uso
cuenta_cliente2 = CuentaConDescubierto("María", 2000, 500)
cuenta_cliente2.retirar(2500)
