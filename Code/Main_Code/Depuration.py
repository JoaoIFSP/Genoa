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
    
    print("\n")

# (Pele)

    print("                [Pele]")   
    # Geração do zigoto do filho   
    Zigoto_Filho = Zigoto_filho_String_depump(Zigoto_Mae_String, Zigoto_Pai_String)
    print(f"          Zigoto:         {Zigoto_Filho[0]}{Zigoto_Filho[1]}")
    
    # Converte os genes em números e soma
    Zigoto_Filho_Valor = Zigoto_filho_Numb_depump(Zigoto_Filho)
    print(f"          Soma dos genes: {Zigoto_Filho_Valor}")
    
    # Verificação de homozigoto ou heterozigoto
    tipo_zigoto = verificar_zigoto(Zigoto_Filho)
    print(f"          {tipo_zigoto}.")

    AA, Aa_aA, aa = contagem(AA, Aa_aA, aa, Zigoto_Filho)

    # Contagem de Hetero/Homo zigotos
    if tipo_zigoto == "Homozigoto": 
        Homozigoto += 1
    if tipo_zigoto == "Heterozigoto":
        Heterozigoto += 1
    # Fim
# Fim

    print("\n")


# (Olhos)
    print("               [Olhos]")
    
    # Geração do zigoto do filho 
    Zigoto_Filho = Zigoto_filho_String_depump(Zigoto_Mae_String, Zigoto_Pai_String)
    print(f"          Zigoto:         {Zigoto_Filho[0]}{Zigoto_Filho[1]}")
    # Fim
    
    # Converte os genes em números e soma
    Zigoto_Filho_Valor = Zigoto_filho_Numb_depump(Zigoto_Filho)
    print(f"          Soma dos genes: {Zigoto_Filho_Valor}")
    # Fim
    
    # Verificação de homozigoto ou heterozigoto
    tipo_zigoto = verificar_zigoto(Zigoto_Filho)
    print(f"          {tipo_zigoto}.")
    # Fim
    
    AA, Aa_aA, aa = contagem(AA, Aa_aA, aa, Zigoto_Filho)
    
    # Contagem de Hetero/Homo zigotos
    if tipo_zigoto == "Homozigoto": 
        Homozigoto += 1
    if tipo_zigoto == "Heterozigoto":
        Heterozigoto += 1
    # Fim
    
# Fim

    print("\n")
# (Nariz)

    print("               [Nariz]")   
    
    # Geração do zigoto do filho
    Zigoto_Filho = Zigoto_filho_String_depump(Zigoto_Mae_String, Zigoto_Pai_String)
    print(f"          Zigoto:         {Zigoto_Filho[0]}{Zigoto_Filho[1]}")
    
    # Converte os genes em números e soma
    Zigoto_Filho_Valor = Zigoto_filho_Numb_depump(Zigoto_Filho)
    print(f"          Soma dos genes: {Zigoto_Filho_Valor}")
    
    # Verificação de homozigoto ou heterozigoto
    tipo_zigoto = verificar_zigoto(Zigoto_Filho)
    print(f"          {tipo_zigoto}.")
    
    AA, Aa_aA, aa = contagem(AA, Aa_aA, aa, Zigoto_Filho)
    
    # Contagem de Hetero/Homo zigotos
    if tipo_zigoto == "Homozigoto": 
        Homozigoto += 1
    if tipo_zigoto == "Heterozigoto":
        Heterozigoto += 1
    # Fim
# Fim    

    print("\n")
# (Altura)

    print("              [Altura]")   
    
    # Geração do zigoto do filho
    Zigoto_Filho = Zigoto_filho_String_depump(Zigoto_Mae_String, Zigoto_Pai_String)
    print(f"          Zigoto:         {Zigoto_Filho[0]}{Zigoto_Filho[1]}")
    
    # Converte os genes em números e soma
    Zigoto_Filho_Valor = Zigoto_filho_Numb_depump(Zigoto_Filho)
    print(f"          Soma dos genes: {Zigoto_Filho_Valor}")
    
    # Verificação de homozigoto ou heterozigoto
    tipo_zigoto = verificar_zigoto(Zigoto_Filho)
    print(f"          {tipo_zigoto}.")
    
    AA, Aa_aA, aa = contagem(AA, Aa_aA, aa, Zigoto_Filho)    
    
    # Contagem de Hetero/Homo zigotos
    if tipo_zigoto == "Homozigoto": 
        Homozigoto += 1
    if tipo_zigoto == "Heterozigoto":
        Heterozigoto += 1
    # Fim
# Fim

    print("\n")

    
# (Tipo de cabelo)

    print("           [Tipo de cabelo]")
    # Geração do zigoto do filho
    Zigoto_Filho = Zigoto_filho_String_depump(Zigoto_Mae_String, Zigoto_Pai_String)
    print(f"          Zigoto:         {Zigoto_Filho[0]}{Zigoto_Filho[1]}")
    
    # Converte os genes em números e soma
    Zigoto_Filho_Valor = Zigoto_filho_Numb_depump(Zigoto_Filho)
    print(f"          Soma dos genes: {Zigoto_Filho_Valor}")
    
    # Verificação de homozigoto ou heterozigoto
    tipo_zigoto = verificar_zigoto(Zigoto_Filho)
    print(f"          {tipo_zigoto}.")
    
    AA, Aa_aA, aa = contagem(AA, Aa_aA, aa, Zigoto_Filho)    
    
    # Contagem de Hetero/Homo zigotos
    if tipo_zigoto == "Homozigoto": 
        Homozigoto += 1
    if tipo_zigoto == "Heterozigoto":
        Heterozigoto += 1
    # Fim
# Fim

    print("\n")

# (Cor de cabelo) 

    print("           [Cor do cabelo]")  
    # Geração do zigoto do filho
    Zigoto_Filho = Zigoto_filho_String_depump(Zigoto_Mae_String, Zigoto_Pai_String)
    print(f"          Zigoto:         {Zigoto_Filho[0]}{Zigoto_Filho[1]}")
    
    # Converte os genes em números e soma
    Zigoto_Filho_Valor = Zigoto_filho_Numb_depump(Zigoto_Filho)
    print(f"          Soma dos genes: {Zigoto_Filho_Valor}")
    
    # Verificação de homozigoto ou heterozigoto
    tipo_zigoto = verificar_zigoto(Zigoto_Filho)
    print(f"          {tipo_zigoto}.")

    AA, Aa_aA, aa = contagem(AA, Aa_aA, aa, Zigoto_Filho)
    
    # Contagem de Hetero/Homo zigotos
    if tipo_zigoto == "Homozigoto": 
        Homozigoto += 1
    if tipo_zigoto == "Heterozigoto":
        Heterozigoto += 1
    # Fim
# Fim

    print("\n")

    print("[Fim do DNA do filho]")
    
    print("\n")
    
    # Contagem de combinações de zigotos

    
# Exibe os resultados finais
print(f"AA: {AA}")
print(f"Aa ou aA: {Aa_aA}")
print(f"aa: {aa}")
print(f"{Homozigoto} Homozigotos")
print(f"{Heterozigoto} Heterozigotos")
print("\n")



# até agora 20 horas
