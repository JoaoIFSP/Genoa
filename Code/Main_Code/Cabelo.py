import random 
from Form import Zigoto_Cabelo_Mae, Zigoto_Cabelo_Pai
# Atribuição de valores binários
Cabelo = {
    
    "Moreno": 8,  # Dominante
    "Preto": 4,   # Dominante
    "Loiro": 2,     # Recessivo
    "Ruivo": 1       # Recessivo
    
}

# Zigotos dos pais (pode ser alterado conforme necessário)
Zigoto_Cabelo_Mae
Zigoto_Cabelo_Pai
# Fim

# Função para gerar o zigoto do filho
def Zigoto_filho_Cabelo_depump(Zigoto_Cabelo_Mae, Zigoto_Cabelo_Pai):
    Gene_Mae_Cabelo = random.choice(Zigoto_Cabelo_Mae)
    Gene_Pai_Cabelo = random.choice(Zigoto_Cabelo_Pai)
    Zigoto_Filho_Cabelo = [Gene_Mae_Cabelo, Gene_Pai_Cabelo]
    return Zigoto_Filho_Cabelo
# Fim

# Função para determinar a cor dos Cabelos com base na soma binária
def determinar_Cabelo(Zigoto_Filho_Cabelo):
    Gene1_Cabelo, Gene2_Cabelo = Zigoto_Filho_Cabelo
# Fim
    
    if Gene1_Cabelo == Gene2_Cabelo:  # Ambos os genes são iguais (homozigoto)
        return random.choice([get_color_by_gene(Gene1_Cabelo), get_color_by_gene(Gene2_Cabelo)])
    else:
        # Um é dominante e o outro é recessivo ou heterozigoto
        if (Gene1_Cabelo >= 4 and Gene2_Cabelo >= 4):  # Ambos os genes são dominantes
            return random.choice([get_color_by_gene(Gene1_Cabelo), get_color_by_gene(Gene2_Cabelo)])
        elif (Gene1_Cabelo >= 4 or Gene2_Cabelo >= 4):  # Um dos genes é dominante
            return get_color_by_gene(max(Gene1_Cabelo, Gene2_Cabelo))
        else:  # Ambos os genes são recessivos
            return random.choice([get_color_by_gene(Gene1_Cabelo), get_color_by_gene(Gene2_Cabelo)])
        # Fim

def get_color_by_gene(gene):
    for color, value in Cabelo.items():
        if value == gene:
            return color
    return None

# Dicionário para armazenar a contagem dos resultados
contagem_resultados_Cabelo = {Cor_Cabelo: 0 for Cor_Cabelo in Cabelo.keys()}
# Fim

