class cuentabancaria:
    def __init__(self, saldo):
        self.saldo = saldo
    def deposito(self, sumar):
        self.sumar = sumar
        self.saldo += self.sumar
    def ver_sal(self):
        return f"El saldo de la cuenta bancaria es de: {self.saldo}"
    def retir(self, restar):
        self.restar = restar
        self.saldo -= self.restar

cuenta = cuentabancaria(1000)
cuenta.deposito(500)
cuenta.retir(300)
print(cuenta.ver_sal())