class Veiculo:
    def _init_(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def calcular_imposto(self):
        return self.preco * 0.10


class Carro(Veiculo):
    def _init_(self, modelo, ano, preco, marca):
        super()._init_(modelo, ano, preco)
        self.marca = marca

    def desconto(self):
        return self.preco * 0.05


class Moto(Veiculo):
    def _init_(self, modelo, ano, preco, cilindrada):
        super()._init_(modelo, ano, preco)
        self.cilindrada = cilindrada

    def calcular_imposto(self):
        return self.preco * 0.05


# Criando objetos
carro1 = Carro("Civic", 2023, 80000.0, "Honda")
moto1 = Moto("Yamaha MT-07", 2022, 35000.0, 700)

# Exibindo resultados
print("=== CARRO ===")
print("Modelo:", carro1.modelo)
print("Marca:", carro1.marca)
print("Imposto:", carro1.calcular_imposto())
print("Desconto:", carro1.desconto())

print("\n=== MOTO ===")
print("Modelo:", moto1.modelo)
print("Cilindrada:", moto1.cilindrada)
print("Imposto:", moto1.calcular_imposto())