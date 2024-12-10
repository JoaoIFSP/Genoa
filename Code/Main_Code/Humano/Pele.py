import random 
from Form import Zigoto_Pele_Mae, Zigoto_Pele_Pai
# Atribuição de valores binários
Pele = {
    
    "Negro": 8,  # Dominante
    "Branco": 4,   # Dominante
    "Amarelo": 2,     # Recessivo
    "Pardo": 1       # Recessivo
    
}

# Zigotos dos pais (pode ser alterado conforme necessário)
Zigoto_Pele_Mae
Zigoto_Pele_Pai
# Fim

# Função para gerar o zigoto do filho
def Zigoto_filho_Pele_depump(Zigoto_Pele_Mae, Zigoto_Pele_Pai):
    Gene_Mae_Pele = random.choice(Zigoto_Pele_Mae)
    Gene_Pai_Pele = random.choice(Zigoto_Pele_Pai)
    Zigoto_Filho_Pele = [Gene_Mae_Pele, Gene_Pai_Pele]
    return Zigoto_Filho_Pele
# Fim

# Função para determinar a cor dos Peles com base na soma binária
def determinar_Pele(Zigoto_Filho_Pele):
    Gene1_Pele, Gene2_Pele = Zigoto_Filho_Pele
# Fim
    
    if Gene1_Pele == Gene2_Pele:  # Ambos os genes são iguais (homozigoto)
        return random.choice([get_color_by_gene(Gene1_Pele), get_color_by_gene(Gene2_Pele)])
    else:
        # Um é dominante e o outro é recessivo ou heterozigoto
        if (Gene1_Pele >= 4 and Gene2_Pele >= 4):  # Ambos os genes são dominantes
            return random.choice([get_color_by_gene(Gene1_Pele), get_color_by_gene(Gene2_Pele)])
        elif (Gene1_Pele >= 4 or Gene2_Pele >= 4):  # Um dos genes é dominante
            return get_color_by_gene(max(Gene1_Pele, Gene2_Pele))
        else:  # Ambos os genes são recessivos
            return random.choice([get_color_by_gene(Gene1_Pele), get_color_by_gene(Gene2_Pele)])
        # Fim

def get_color_by_gene(gene):
    for color, value in Pele.items():
        if value == gene:
            return color
    return None

# Dicionário para armazenar a contagem dos resultados
contagem_resultados_Pele = {Cor_Pele: 0 for Cor_Pele in Pele.keys()}
# Fim

