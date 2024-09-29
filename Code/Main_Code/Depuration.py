from Zigoto import Zigoto_filho_String_depump, Zigoto_filho_Numb_depump, contagem, verificar_zigoto
from Zigoto import Zigoto_Mae_String, Zigoto_Pai_String, AA, Aa_aA, aa

Filho_Numero = 0
Homozigoto = 0
Heterozigoto = 0

for i in range(100):  # Alterar para gerar mais filhos, se necessário
    Filho_Numero += 1
    if Filho_Numero < 10:
        print(f"Filho Número: 00{Filho_Numero}")
    elif Filho_Numero < 100:
        print(f"Filho Número: 0{Filho_Numero}")
    else:
        print(f"Filho Número: {Filho_Numero}")
        
    # Geração do zigoto do filho
    Zigoto_Filho = Zigoto_filho_String_depump(Zigoto_Mae_String, Zigoto_Pai_String)
    print(f"Zigoto do filho: ({Zigoto_Filho[0]}{Zigoto_Filho[1]})")
    
    # Converte os genes em números e soma
    Zigoto_Filho_Valor = Zigoto_filho_Numb_depump(Zigoto_Filho)
    print(f"Resultado da soma dos genes: {Zigoto_Filho_Valor}")
    
    # Verificação de homozigoto ou heterozigoto
    tipo_zigoto = verificar_zigoto(Zigoto_Filho)
    print(f"Tipo de Zigoto: {tipo_zigoto}")
    
    if tipo_zigoto == "Homozigoto": 
        Homozigoto += 1
    if tipo_zigoto == "Heterozigoto":
        Heterozigoto += 1
    
    
    
    print("\n")
    
    # Contagem de combinações de zigotos
    AA, Aa_aA, aa = contagem(AA, Aa_aA, aa, Zigoto_Filho)
    
# Exibe os resultados finais
print(f"AA: {AA}")
print(f"Aa ou aA: {Aa_aA}")
print(f"aa: {aa}")
print(f"{Homozigoto} Homozigotos")
print(f"{Heterozigoto} Heterozigotos")
print("\n")