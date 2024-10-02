from Olhos import Zigoto_filho_Olhos_depump, determinar_olhos, Zigoto_Olho_Mae, Zigoto_Olho_Pai, contagem_resultados_Olhos
from Cabelo import Zigoto_filho_Cabelo_depump, determinar_Cabelo, Zigoto_Cabelo_Mae, Zigoto_Cabelo_Pai, contagem_resultados_Cabelo
from Pele import Zigoto_filho_Pele_depump, determinar_Pele, Zigoto_Pele_Mae, Zigoto_Pele_Pai, contagem_resultados_Pele
from Tipo_Cabelo import Zigoto_filho_Tipo_Cabelo_depump, determinar_Tipo_Cabelo, Zigoto_Tipo_Cabelo_Mae, Zigoto_Tipo_Cabelo_Pai, contagem_resultados_Tipo_Cabelo
from Nariz import Zigoto_filho_Nariz_depump, determinar_Nariz, Zigoto_Nariz_Mae, Zigoto_Nariz_Pai, contagem_resultados_Nariz
from Altura import Zigoto_filho_Altura_depump, determinar_Altura, Zigoto_Altura_Mae, Zigoto_Altura_Pai, contagem_resultados_Altura



def gerar_resultados(num_geracoes=1000):
    for i in range(num_geracoes):
        
        print(f"Filho número {i + 1}")

        print("\n")
        
        # Geração do parâmetro dos Olhos            
        Zigoto_filho_Olhos_dep = Zigoto_filho_Olhos_depump(Zigoto_Olho_Mae, Zigoto_Olho_Pai)
        resultado_final_Olhos = determinar_olhos(Zigoto_filho_Olhos_dep)

        # Atualiza a contagem para o resultado
        if resultado_final_Olhos in contagem_resultados_Olhos:
            contagem_resultados_Olhos[resultado_final_Olhos] += 1
        # Fim
        # Fim

        # Geração do parâmetro dos cabelos                
        Zigoto_filho_Cabelo_dep = Zigoto_filho_Cabelo_depump(Zigoto_Cabelo_Mae, Zigoto_Cabelo_Pai)
        resultado_final_Cabelo = determinar_Cabelo(Zigoto_filho_Cabelo_dep)
        
        # Atualiza a contagem para o resultado
        if resultado_final_Cabelo in contagem_resultados_Cabelo:
            contagem_resultados_Cabelo[resultado_final_Cabelo] += 1        
        # Fim
        # Fim
                
        # Geração do parâmetro da Pele            
        Zigoto_filho_Pele_dep = Zigoto_filho_Pele_depump(Zigoto_Pele_Mae, Zigoto_Pele_Pai)
        resultado_final_Pele = determinar_Pele(Zigoto_filho_Pele_dep)
        # Atualiza a contagem para o resultado
        if resultado_final_Pele in contagem_resultados_Pele:
            contagem_resultados_Pele[resultado_final_Pele] += 1    
        # Fim  
        # Fim    
  
        
        # Geração do parâmetro da Tipo de cabelo                
        Zigoto_filho_Tipo_Cabelo_dep = Zigoto_filho_Tipo_Cabelo_depump(Zigoto_Tipo_Cabelo_Mae, Zigoto_Tipo_Cabelo_Pai)
        resultado_final_Tipo_Cabelo = determinar_Tipo_Cabelo(Zigoto_filho_Tipo_Cabelo_dep)

        # Atualiza a contagem para o resultado
        if resultado_final_Tipo_Cabelo in contagem_resultados_Tipo_Cabelo:
            contagem_resultados_Tipo_Cabelo[resultado_final_Tipo_Cabelo] += 1    
        # Fim            
        # Fim
        
        # Geração do parâmetro de Nariz   
        Zigoto_filho_Nariz_dep = Zigoto_filho_Nariz_depump(Zigoto_Nariz_Mae, Zigoto_Nariz_Pai)
        resultado_final_Nariz = determinar_Nariz(Zigoto_filho_Nariz_dep)

        # Atualiza a contagem para o resultado
        if resultado_final_Nariz in contagem_resultados_Nariz:
            contagem_resultados_Nariz[resultado_final_Nariz] += 1    
        # Fim            
        # Fim
            
        # Geração do parâmetro de Altura         
        Zigoto_filho_Altura_dep = Zigoto_filho_Altura_depump(Zigoto_Altura_Mae, Zigoto_Altura_Pai)
        resultado_final_Altura = determinar_Altura(Zigoto_filho_Altura_dep)
         
        # Atualiza a contagem para o resultado
        if resultado_final_Altura in contagem_resultados_Altura:
            contagem_resultados_Altura[resultado_final_Altura] += 1                
        # Fim       
        # Fim      
        
         
        print(f"Zigoto Ocular: {Zigoto_filho_Olhos_dep}")
        print(f"Zigoto Capilar: {Zigoto_filho_Cabelo_dep}")
        print(f"Zigoto de Tipagem Capilar: {Zigoto_filho_Tipo_Cabelo_dep}")
        print(f"Zigoto Dermal: {Zigoto_filho_Pele_dep}")
        print(f"Zigoto Nasal: {Zigoto_filho_Nariz_dep}")
        print(f"Zigoto da Estatura: {Zigoto_filho_Altura_dep}")

        print("\n")

        print(f"(Olho: {resultado_final_Olhos})")
        print(f"(Cabelo: {resultado_final_Cabelo})")
        print(f"(Tipo de Cabelo: {resultado_final_Tipo_Cabelo})")
        print(f"(Pele: {resultado_final_Pele})")
        print(f"(Nariz: {resultado_final_Nariz})")
        print(f"(Altura: {resultado_final_Altura})")

        print("\n")
        
        print(f"[Fim do Filho {i + 1}]")
        
        print("\n")
       
# Fim

# Executa a geração de resultados
gerar_resultados()
# Fim

# Impressão dos resultados gerais dos olhos
print("\n(Olhos) Contagem dos resultados após iterações:")
for resultado_Olhos, contagem_Olhos in contagem_resultados_Olhos.items():
    print(f"{resultado_Olhos}: {contagem_Olhos}")
# Fim
    
# Impressão dos resultados gerais do Cabelo    
print("\n(Cabelo) Contagem dos resultados após iterações:")
for resultado_Cabelo, contagem_Cabelo in contagem_resultados_Cabelo.items():
    print(f"{resultado_Cabelo}: {contagem_Cabelo}")
# Fim
    
    
# Impressão dos resultados gerais da Pele    
print("\n(Pele) Contagem dos resultados após iterações:")
for resultado_Pele, contagem_Pele in contagem_resultados_Pele.items():
    print(f"{resultado_Pele}: {contagem_Pele}")
# Fim
    
# Impressão dos resultados gerais da Tipo Cabelo    
print("\n(Tipo Cabelo) Contagem dos resultados após iterações:")
for resultado_Tipo_Cabelo, contagem_Tipo_Cabelo in contagem_resultados_Tipo_Cabelo.items():
    print(f"{resultado_Tipo_Cabelo}: {contagem_Tipo_Cabelo}")
# Fim
    
# Impressão dos resultados gerais de Nariz  
print("\n(Nariz) Contagem dos resultados após iterações:")
for resultado_Nariz, contagem_Nariz in contagem_resultados_Nariz.items():
    print(f"{resultado_Nariz}: {contagem_Nariz}")
# Fim
    
# Impressão dos resultados gerais de Altura  
print("\n(Altura) Contagem dos resultados após iterações:")
for resultado_Altura, contagem_Altura in contagem_resultados_Altura.items():
    print(f"{resultado_Altura}: {contagem_Altura}")
# Fim