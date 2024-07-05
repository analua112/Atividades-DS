class Conta:
    # Método construtor
    def __init__(self, numero, senha, titular, saldo, limite):
        # ATRIBUTOS DA CLASSE CONTA
        self.__numero = numero
        self.__senha = senha
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    # Métodos gerais
    def sacar(self, valor):
        self.__saldo = self.__saldo - valor
        print("Saque efetuado! Saldo atual: ", self.__saldo)
    
    def depositar(self, valor):
        self.__saldo = self.__saldo + valor
        print("Depósito efetuado! Saldo atual: ", self.__saldo)

    def extrato(self):
        print("Saldo atual: ", self.__saldo)

    #limite
    def limiteGet(self):
        return self.__limite

    def limiteSet(self, valor):
        self.__limite = valor

    #saldo
    def saldoGet(self):
        return self.__saldo

    def saldoSet(self, valor):
        self.__saldo = valor

    #numero
    def numeroGet(self):
        return self.__numero

    def numeroSet(self, valor):
        self.numero = valor
   
    #numero
    def senhaGet(self):
        return self.__senha

    def senhaSet(self, valor):
        self.senha = valor
   
    #titular
    def titularGet(self):
        return self.__titular

    def titularSet(self, valor):
        self.__titular = valor
# FAZER OS GETS E SETS DE TODOS OS ATRIBUTOS DE SUA CLASSE!
