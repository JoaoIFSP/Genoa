import random 
from Form import Zigoto_Tipo_Cabelo_Mae, Zigoto_Tipo_Cabelo_Pai
# Atribuição de valores binários
Tipo_Cabelo = {
    
    "Crespo": 8,  # Dominante
    "Liso": 4,   # Dominante
    "Cacheado": 2,     # Recessivo
    "Ondulado": 1       # Recessivo
    
}

# Zigotos dos pais (pode ser alterado conforme necessário)
Zigoto_Tipo_Cabelo_Mae
Zigoto_Tipo_Cabelo_Pai
# Fim

# Função para gerar o zigoto do filho
def Zigoto_filho_Tipo_Cabelo_depump(Zigoto_Tipo_Cabelo_Mae, Zigoto_Tipo_Cabelo_Pai):
    Gene_Mae_Tipo_Cabelo = random.choice(Zigoto_Tipo_Cabelo_Mae)
    Gene_Pai_Tipo_Cabelo = random.choice(Zigoto_Tipo_Cabelo_Pai)
    Zigoto_Filho_Tipo_Cabelo = [Gene_Mae_Tipo_Cabelo, Gene_Pai_Tipo_Cabelo]
    return Zigoto_Filho_Tipo_Cabelo
# Fim

# Função para determinar a cor dos Tipo_Cabelos com base na soma binária
def determinar_Tipo_Cabelo(Zigoto_Filho_Tipo_Cabelo):
    Gene1_Tipo_Cabelo, Gene2_Tipo_Cabelo = Zigoto_Filho_Tipo_Cabelo
# Fim
    
    if Gene1_Tipo_Cabelo == Gene2_Tipo_Cabelo:  # Ambos os genes são iguais (homozigoto)
        return random.choice([get_color_by_gene(Gene1_Tipo_Cabelo), get_color_by_gene(Gene2_Tipo_Cabelo)])
    else:
        # Um é dominante e o outro é recessivo ou heterozigoto
        if (Gene1_Tipo_Cabelo >= 4 and Gene2_Tipo_Cabelo >= 4):  # Ambos os genes são dominantes
            return random.choice([get_color_by_gene(Gene1_Tipo_Cabelo), get_color_by_gene(Gene2_Tipo_Cabelo)])
        elif (Gene1_Tipo_Cabelo >= 4 or Gene2_Tipo_Cabelo >= 4):  # Um dos genes é dominante
            return get_color_by_gene(max(Gene1_Tipo_Cabelo, Gene2_Tipo_Cabelo))
        else:  # Ambos os genes são recessivos
            return random.choice([get_color_by_gene(Gene1_Tipo_Cabelo), get_color_by_gene(Gene2_Tipo_Cabelo)])
        # Fim

def get_color_by_gene(gene):
    for color, value in Tipo_Cabelo.items():
        if value == gene:
            return color
    return None

# Dicionário para armazenar a contagem dos resultados
contagem_resultados_Tipo_Cabelo = {Cor_Tipo_Cabelo: 0 for Cor_Tipo_Cabelo in Tipo_Cabelo.keys()}
# Fim

