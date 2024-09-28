import Zigoto_copy
# Número de simulações que você deseja realizar
num_simulacoes = 100

# Executando a simulação e capturando os resultados
resultados = Zigoto_copy.simular_zigotos(num_simulacoes)

# Exibindo os resultados
for i, (Zigoto_Filho, Valor_Zigoto_Filho, Hetero_Zigoto) in enumerate(resultados):
    print(f"Filho número: {i + 1}")
    print(f"Zigoto do Filho: {Zigoto_Filho[0].letra}{Zigoto_Filho[1].letra}")
    print(f"Valor do Zigoto: {Valor_Zigoto_Filho}")
    print("Heterozigoto" if Hetero_Zigoto else "Homozigoto")
    print("\n")
    
