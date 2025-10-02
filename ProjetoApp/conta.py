class Conta:
    def __init__(self, titular, numero, saldo):
        self.numero = 0
        self.saldo = 0
        self.titular = titular
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print("Saldo não pode ser negativo")
        else:
            self._saldo = saldo
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")
    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")
    def extrato(self):
        print(f"{self.titular}, saldo atual: R$ {self.saldo:.2f}")

    """
    def get_saldo(self):
        return self._saldo
    def set_saldo(self, saldo):
        if (saldo < 0):
            print("Saldo não pode ser negativo")
        else:
            self._saldo = saldo
    """