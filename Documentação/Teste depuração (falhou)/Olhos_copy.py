import Zigoto_copy
import random

class Gene_Olho:
    def __init__(self, letra, valor):
        self.letra = letra  # String
        self.valor = valor  # 2 para dominante, 1 para recessivo

    def __str__(self):
        return self.letra

    # Comparação com base no valor numérico
    def __eq__(self, outro):
        return self.valor == (outro.valor if isinstance(outro, Gene_Olho) else outro)

# Criando genes dominante e recessivo
Olhos_castanhos = Gene_Olho('Olhos castanhos', Zigoto_copy.Dominante.valor) # Um gene simplesmente dominante
Olhos_amarelos = Gene_Olho('Olhos castanhos', Zigoto_copy.Dominante.valor) # Um gene dominante, porém depende da mesclagem de melanina (Intermediária)
Olhos_verdes = Gene_Olho('Olhos verdes', Zigoto_copy.Recessivo.valor) # Ele é recessivo, e é isso
Olhos_azuis = Gene_Olho('Olhos azuis', Zigoto_copy.Recessivo.valor) # Ele é recessivo, e é isso

Zigoto_Olho_Mae = [Olhos_castanhos, Olhos_azuis]
Zigoto_Olho_Pai = [Olhos_azuis, Olhos_azuis]

Gene_Olho_Mae = random.choice(Zigoto_Olho_Mae)
Gene_Olho_Pai = random.choice(Zigoto_Olho_Pai)

Zigoto_Olho_Filho = [Gene_Olho_Mae, Gene_Olho_Pai]

if Gene_Olho_Mae.valor + Gene_Olho_Pai.valor == 3:
    Zigoto_Olho_Filho = Olhos_castanhos
else:
    Zigoto_Olho_Filho = Olhos_azuis

print(f"{Zigoto_Olho_Filho}")