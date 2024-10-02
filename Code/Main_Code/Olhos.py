import random 
from Form import Zigoto_Olho_Mae, Zigoto_Olho_Pai
# Atribuição de valores binários
Olhos = {
    
    "Castanho": 8,  # Dominante
    "Amarelo": 4,   # Dominante
    "Verde": 2,     # Recessivo
    "Azul": 1       # Recessivo
    
}

# Zigotos dos pais (pode ser alterado conforme necessário)
Zigoto_Olho_Mae
Zigoto_Olho_Pai
# Fim

# Função para gerar o zigoto do filho
def Zigoto_filho_Olhos_depump(Zigoto_Olho_Mae, Zigoto_Olho_Pai):
    Gene_Mae_Olhos = random.choice(Zigoto_Olho_Mae)
    Gene_Pai_Olhos = random.choice(Zigoto_Olho_Pai)
    Zigoto_Filho_Olhos = [Gene_Mae_Olhos, Gene_Pai_Olhos]
    return Zigoto_Filho_Olhos
# Fim

# Função para determinar a cor dos olhos com base na soma binária
def determinar_olhos(Zigoto_Filho_Olhos):
    Gene1_Olhos, Gene2_Olhos = Zigoto_Filho_Olhos
# Fim
    
    if Gene1_Olhos == Gene2_Olhos:  # Ambos os genes são iguais (homozigoto)
        return random.choice([get_color_by_gene(Gene1_Olhos), get_color_by_gene(Gene2_Olhos)])
    else:
        # Um é dominante e o outro é recessivo ou heterozigoto
        if (Gene1_Olhos >= 4 and Gene2_Olhos >= 4):  # Ambos os genes são dominantes
            return random.choice([get_color_by_gene(Gene1_Olhos), get_color_by_gene(Gene2_Olhos)])
        elif (Gene1_Olhos >= 4 or Gene2_Olhos >= 4):  # Um dos genes é dominante
            return get_color_by_gene(max(Gene1_Olhos, Gene2_Olhos))
        else:  # Ambos os genes são recessivos
            return random.choice([get_color_by_gene(Gene1_Olhos), get_color_by_gene(Gene2_Olhos)])
        # Fim

def get_color_by_gene(gene):
    for color, value in Olhos.items():
        if value == gene:
            return color
    return None

# Dicionário para armazenar a contagem dos resultados
contagem_resultados_Olhos = {Cor_Olhos: 0 for Cor_Olhos in Olhos.keys()}
# Fim

