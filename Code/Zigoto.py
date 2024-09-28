import random
import Olhos


Numero_Teste = 0

# Classe Gene para representar 'A' (2) e 'a' (1)
class Gene:
    def __init__(self, letra, valor):
        self.letra = letra  # 'A' ou 'a'
        self.valor = valor  # 2 para dominante, 1 para recessivo

    def __str__(self):
        return self.letra

    # Comparação com base no valor numérico
    def __eq__(self, outro):
        return self.valor == (outro.valor if isinstance(outro, Gene) else outro)

# Criando genes dominante e recessivo
Dominante = Gene('A', 2)
Recessivo = Gene('a', 1)

# Contagem para ver densidade de zigotos
Quantidade_AA = 0
Quantidade_Aa_ou_aA = 0
Quantidade_aa = 0

# Trincheira de genes
Zigoto_Mae = [Dominante, Recessivo]
Zigoto_Pai = [Dominante, Recessivo]

# Repetição de código
for cnt in range(1, 101):
    Numero_Teste += 1
    # Parâmetro do envio do gene da mãe ao filho
    Gene_Mae = random.choice(Zigoto_Mae)
    
    # Parâmetro do envio do gene do pai ao filho
    Gene_Pai = random.choice(Zigoto_Pai)
    
    # Zigoto do filho
    Zigoto_Filho = [Gene_Mae, Gene_Pai]
    
    # Apenas para o print demonstrativo  
    if Zigoto_Filho[0] == Dominante and Zigoto_Filho[1] == Dominante:
        Quantidade_AA += 1
        
    elif (Zigoto_Filho[0] == Dominante and Zigoto_Filho[1] == Recessivo) or (Zigoto_Filho[0] == Recessivo and Zigoto_Filho[1] == Dominante):
        Quantidade_Aa_ou_aA += 1
        
    elif Zigoto_Filho[0] == Recessivo and Zigoto_Filho[1] == Recessivo:
        Quantidade_aa += 1
        
    # Soma os valores do primeiro gene com o segundo para saber se é
    # Homozigoto ou Heterozigoto
    Valor_Zigoto_Filho = Zigoto_Filho[0].valor + Zigoto_Filho[1].valor
    
    print(f"Filho número: {Numero_Teste}")
    print("\n")
        
    # Exibe os genes do filho
    print(f"Zigoto do Filho: {Zigoto_Filho[0]}{Zigoto_Filho[1]}")
    
    # Como o valor do gene recessivo é 1
    # E o valor do gene dominante é 2
    # Todo número inteiro duas vezes é par, e oque está entre eles é o 3
    # Então se os valors divergirem, os genes divergem, logo Heterozigotos
    
    if Valor_Zigoto_Filho == 3:
        Hetero_Zigoto = 1
    else:
        Hetero_Zigoto = 0
        
    print(f"Valor do Zigoto: {Valor_Zigoto_Filho}")
    
    # Compara se é Heterozigoto ou Homozigoto
    
    if Hetero_Zigoto == 0:
        print("Homozigoto")
    elif Hetero_Zigoto == 1:
        print("Heterozigoto")
        
    
    
    
    print("\n")
    print("\n")
    
# Resultados finais
print(f"Quantidade AA: {Quantidade_AA}")
print(f"Quantidade Aa ou aA: {Quantidade_Aa_ou_aA}")
print(f"Quantidade aa: {Quantidade_aa}")
