import random

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
    
    
    # Como o valor do gene recessivo é 1
    # E o valor do gene dominante é 2
    # Todo número inteiro duas vezes é par, e oque está entre eles é o 3
    # Então se os valors divergirem, os genes divergem, logo Heterozigotos
    
    if Valor_Zigoto_Filho == 3:
        Hetero_Zigoto = 1
    else:
        Hetero_Zigoto = 0
        
def Numero_do_filho (Numero_Teste):
    Numero_Teste += 1
    return Numero_Teste

def Parametro_Dominante_Recessivo (Zigoto_Filho, Zigoto_Mae):
    
    Zigoto_Mae = [Dominante, Recessivo]
    Zigoto_Pai = [Dominante, Recessivo]
    
    Gene_Mae = random.choice(Zigoto_Mae)
    Gene_Pai = random.choice(Zigoto_Pai)
    
    Zigoto_Filho = [Gene_Mae, Gene_Pai]
    return Zigoto_Filho

def Valor_do_Zigoto_Filho (Valor_Zigoto_Filho):
    Zigoto_Filho = [Gene_Mae, Gene_Pai]
    Valor_Zigoto_Filho = Zigoto_Filho[0].valor + Zigoto_Filho[1].valor
    return Valor_Zigoto_Filho

def Heterozigoto_ou_Homozigto (Hetero_Zigoto):
    Valor_Zigoto_Filho = Zigoto_Filho[0].valor + Zigoto_Filho[1].valor
    if Valor_Zigoto_Filho == 3:
        Hetero_Zigoto = 1
    else:
        Hetero_Zigoto = 0
    return Hetero_Zigoto

def Densidade_de_Zigotos (Quantidade_AA, Quantidade_Aa_ou_aA, Quantidade_aa):
    if Zigoto_Filho[0] == Dominante and Zigoto_Filho[1] == Dominante:
        Quantidade_AA += 1
        
    elif (Zigoto_Filho[0] == Dominante and Zigoto_Filho[1] == Recessivo) or (Zigoto_Filho[0] == Recessivo and Zigoto_Filho[1] == Dominante):
        Quantidade_Aa_ou_aA += 1
        
    elif Zigoto_Filho[0] == Recessivo and Zigoto_Filho[1] == Recessivo:
        Quantidade_aa += 1
        
    return Quantidade_AA, Quantidade_Aa_ou_aA, Quantidade_aa
        