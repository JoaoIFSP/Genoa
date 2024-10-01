import random

# Atribuição de valores binários
Olhos = {
    "Castanho": 8,  # Dominante
    "Amarelo": 4,   # Dominante
    "Verde": 2,     # Recessivo
    "Azul": 1       # Recessivo
}

# Zigotos dos pais (pode ser alterado conforme necessário)
Zigoto_Olho_Mae = [Olhos["Amarelo"], Olhos["Verde"]]  # Exemplo: mãe com olhos castanhos e azuis
Zigoto_Olho_Pai = [Olhos["Castanho"], Olhos[ "Amarelo"]]   # Exemplo: pai com olhos amarelos e verdes
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
    gene1, gene2 = Zigoto_Filho_Olhos
# Fim
    
    if gene1 == gene2:  # Ambos os genes são iguais (homozigoto)
        return random.choice([get_color_by_gene(gene1), get_color_by_gene(gene2)])
    else:
        # Um é dominante e o outro é recessivo ou heterozigoto
        if (gene1 >= 4 and gene2 >= 4):  # Ambos os genes são dominantes
            return random.choice([get_color_by_gene(gene1), get_color_by_gene(gene2)])
        elif (gene1 >= 4 or gene2 >= 4):  # Um dos genes é dominante
            return get_color_by_gene(max(gene1, gene2))
        else:  # Ambos os genes são recessivos
            return random.choice([get_color_by_gene(gene1), get_color_by_gene(gene2)])
        # Fim

def get_color_by_gene(gene):
    for color, value in Olhos.items():
        if value == gene:
            return color
    return None

# Dicionário para armazenar a contagem dos resultados
contagem_resultados = {cor: 0 for cor in Olhos.keys()}
# Fim

# Gera 100 resultados
def gerar_resultados(num_geracoes=10000):
    for i in range(num_geracoes):
        Zigoto_filho_Olhos_dep = Zigoto_filho_Olhos_depump(Zigoto_Olho_Mae, Zigoto_Olho_Pai)
        resultado_final = determinar_olhos(Zigoto_filho_Olhos_dep)

        print(f"Zigoto {i + 1}: {Zigoto_filho_Olhos_dep} -> Resultado: {resultado_final}")
        
        # Atualiza a contagem para o resultado
        if resultado_final in contagem_resultados:
            contagem_resultados[resultado_final] += 1
        # Fim
# Fim

# Executa a geração de resultados
gerar_resultados()
# Fim

# Exibe o total de cada resultado ao final
print("\nContagem dos resultados após 10000 iterações:")
for resultado, contagem in contagem_resultados.items():
    print(f"{resultado}: {contagem}")
# Fim