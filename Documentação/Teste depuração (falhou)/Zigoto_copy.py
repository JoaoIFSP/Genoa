import random



class Gene:
    def __init__(self, letra, valor):
        self.letra = letra
        self.valor = valor

# Função para executar a simulação
def simular_zigotos(num_simulacoes):
    resultados = []
    Zigoto_Mae = [Gene('A', 2), Gene('a', 1)]  # Exemplo de genes da mãe
    Zigoto_Pai = [Gene('A', 2), Gene('a', 1)]  # Exemplo de genes do pai
    

    for _ in range(num_simulacoes):
        
        # Parâmetro do envio do gene da mãe ao filho
        Gene_Mae = random.choice(Zigoto_Mae)

        # Parâmetro do envio do gene do pai ao filho
        Gene_Pai = random.choice(Zigoto_Pai)

        # Zigoto do filho
        Zigoto_Filho = [Gene_Mae, Gene_Pai]
        


        # Soma os valores para saber se é Homozigoto ou Heterozigoto
        Valor_Zigoto_Filho = Zigoto_Filho[0].valor + Zigoto_Filho[1].valor

        # Determinando se é Heterozigoto ou Homozigoto
        Hetero_Zigoto = 1 if Valor_Zigoto_Filho == 3 else 0
        

        # Armazenando o resultado
        resultados.append((Zigoto_Filho, Valor_Zigoto_Filho, Hetero_Zigoto))

    return resultados  # Retornando a lista de resultados

