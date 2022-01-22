

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('Construindo o objeto...')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print(f'O saldo do titular {self.__titular} é de {self.__saldo}')