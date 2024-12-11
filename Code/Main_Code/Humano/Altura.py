import random 
from Form import Zigoto_Altura_Mae, Zigoto_Altura_Pai
# Atribuição de valores binários
Altura = {
    
    "1,70 m": 8,  # Dominante
    "1,60 m": 4,   # Dominante
    "1,90 m": 2,     # Recessivo
    "1,40 m": 1       # Recessivo
    
}

# Zigotos dos pais (pode ser alterado conforme necessário)
Zigoto_Altura_Mae
Zigoto_Altura_Pai
# Fim

# Função para gerar o zigoto do filho
def Zigoto_filho_Altura_depump(Zigoto_Altura_Mae, Zigoto_Altura_Pai):
    Gene_Mae_Altura = random.choice(Zigoto_Altura_Mae)
    Gene_Pai_Altura = random.choice(Zigoto_Altura_Pai)
    Zigoto_Filho_Altura = [Gene_Mae_Altura, Gene_Pai_Altura]
    return Zigoto_Filho_Altura
# Fim

# Função para determinar a cor dos Alturas com base na soma binária
def determinar_Altura(Zigoto_Filho_Altura):
    Gene1_Altura, Gene2_Altura = Zigoto_Filho_Altura
# Fim
    
    if Gene1_Altura == Gene2_Altura:  # Ambos os genes são iguais (homozigoto)
        return random.choice([get_color_by_gene(Gene1_Altura), get_color_by_gene(Gene2_Altura)])
    else:
        # Um é dominante e o outro é recessivo ou heterozigoto
        if (Gene1_Altura >= 4 and Gene2_Altura >= 4):  # Ambos os genes são dominantes
            return random.choice([get_color_by_gene(Gene1_Altura), get_color_by_gene(Gene2_Altura)])
        elif (Gene1_Altura >= 4 or Gene2_Altura >= 4):  # Um dos genes é dominante
            return get_color_by_gene(max(Gene1_Altura, Gene2_Altura))
        else:  # Ambos os genes são recessivos
            return random.choice([get_color_by_gene(Gene1_Altura), get_color_by_gene(Gene2_Altura)])
        # Fim

def get_color_by_gene(gene):
    for color, value in Altura.items():
        if value == gene:
            return color
    return None

# Dicionário para armazenar a contagem dos resultados
contagem_resultados_Altura = {Cor_Altura: 0 for Cor_Altura in Altura.keys()}
# Fim

