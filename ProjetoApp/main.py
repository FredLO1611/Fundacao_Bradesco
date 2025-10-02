class Main:
    pass
from cliente import Cliente
c1 = Cliente('Gab', 17, '+55 (11) 94606-0129')
print(c1._nome,'de idade', c1._idade, 'possui o telefone', c1._telefone)
from conta import Conta
conta=Conta(c1.get_nome(), c1.get_telefone(), 0)
conta.depositar(100)
conta.sacar(50)
conta.extrato()