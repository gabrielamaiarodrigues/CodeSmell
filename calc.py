class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            return "Divisão por zero não é definida"
        else:
            return a / b

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_idade(self):
        return self.idade

class Loja:
    def __init__(self, nome):
        self.nome = nome

    def vender_item(self, item, preco):
        print(f"Vendido {item} por R$ {preco}")

def main():
    calc = Calculadora()
    resultado = calc.soma(5, 7)
    print("Resultado:", resultado)

    pessoa = Pessoa("Alice", 30)
    pessoa.set_nome("Bob")
    print("Nome da pessoa:", pessoa.nome)
    print("Idade da pessoa:", pessoa.get_idade())

    loja = Loja("Minha Loja")
    loja.vender_item("Camiseta", 50)

if __name__ == "__main__":
    main()
