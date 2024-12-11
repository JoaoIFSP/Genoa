import random 
from Form import Zigoto_Nariz_Mae, Zigoto_Nariz_Pai
# Atribuição de valores binários
Nariz = {
    
    "Largo": 8,  # Dominante
    "Fino": 4,   # Dominante
    "Redondo": 2,     # Recessivo
    "Adunco": 1       # Recessivo
    
}

# Zigotos dos pais (pode ser alterado conforme necessário)
Zigoto_Nariz_Mae
Zigoto_Nariz_Pai
# Fim

# Função para gerar o zigoto do filho
def Zigoto_filho_Nariz_depump(Zigoto_Nariz_Mae, Zigoto_Nariz_Pai):
    Gene_Mae_Nariz = random.choice(Zigoto_Nariz_Mae)
    Gene_Pai_Nariz = random.choice(Zigoto_Nariz_Pai)
    Zigoto_Filho_Nariz = [Gene_Mae_Nariz, Gene_Pai_Nariz]
    return Zigoto_Filho_Nariz
# Fim

# Função para determinar a cor dos Narizs com base na soma binária
def determinar_Nariz(Zigoto_Filho_Nariz):
    Gene1_Nariz, Gene2_Nariz = Zigoto_Filho_Nariz
# Fim
    
    if Gene1_Nariz == Gene2_Nariz:  # Ambos os genes são iguais (homozigoto)
        return random.choice([get_color_by_gene(Gene1_Nariz), get_color_by_gene(Gene2_Nariz)])
    else:
        # Um é dominante e o outro é recessivo ou heterozigoto
        if (Gene1_Nariz >= 4 and Gene2_Nariz >= 4):  # Ambos os genes são dominantes
            return random.choice([get_color_by_gene(Gene1_Nariz), get_color_by_gene(Gene2_Nariz)])
        elif (Gene1_Nariz >= 4 or Gene2_Nariz >= 4):  # Um dos genes é dominante
            return get_color_by_gene(max(Gene1_Nariz, Gene2_Nariz))
        else:  # Ambos os genes são recessivos
            return random.choice([get_color_by_gene(Gene1_Nariz), get_color_by_gene(Gene2_Nariz)])
        # Fim

def get_color_by_gene(gene):
    for color, value in Nariz.items():
        if value == gene:
            return color
    return None

# Dicionário para armazenar a contagem dos resultados
contagem_resultados_Nariz = {Cor_Nariz: 0 for Cor_Nariz in Nariz.keys()}
# Fim

