print('Hello, world!')
class Cliente:
    def __init__(self, n, i, t):
        """Criando a classe Cliente, que abriga objetos.
        init é o método construtor, que estabelecer os valores obrigatórios para construção de um novo objeto.
        self é uma referência ao próprio objeto, para especificar atributos."""
        self.nome = n
        self.idade = i
        self.telefone = t
        """Todo objeto possuí um ID que o define"""