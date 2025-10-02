print('Hello, world!')
class Cliente:
    def __init__(self, n, i, t):
        """Criando a classe Cliente, que abriga objetos.
        init é o método construtor, que estabelecer os valores obrigatórios para construção de um novo objeto.
        self é uma referência ao próprio objeto, para especificar atributos."""
        """_ significa que o atributo é privado"""
        self._nome = n
        self._idade = i
        self._telefone = t
        """Todo objeto possuí um ID que o define"""
    def get_nome(self):
        return self._nome
    def set_nome(self, nome):
        self._nome = nome
    def get_telefone(self):
        return self._telefone