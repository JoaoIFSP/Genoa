import random

Numero_Teste = 0

AA = 0
Aa_aA = 0
aa = 0
    
Dominante_String = "A"
Recessivo_String = "a"

Dominante_Numb = 2
Recessivo_Numb = 1

Zigoto_Mae_String = [Dominante_String, Recessivo_String]
Zigoto_Pai_String = [Dominante_String, Recessivo_String]

# Fórmula de geração do zigoto do filho (String)
def Zigoto_filho_String_depump(Zigoto_Mae_String, Zigoto_Pai_String):
    # Escolhe o gene da mãe (String)
    Gene_Mae_String = random.choice(Zigoto_Mae_String)
    # Fim
    
    # Escolhe o gene do pai (String)
    Gene_Pai_String = random.choice(Zigoto_Pai_String)
    # Fim
    
    # Imprime o zigoto do filho (String)
    Zigoto_Filho_String = [Gene_Mae_String, Gene_Pai_String]
    # Fim
    
    # Essa merda é muito confusa, mas ta funcionando
    # Cata o resultado da function
    return Zigoto_Filho_String
    # Fim
    
# Fim

# Função para converter os genes do filho em números
def Zigoto_filho_Numb_depump(Zigoto_Filho_String):
    # Convertendo o gene da mãe para número
    Gene_Mae_Numb = 2 if Zigoto_Filho_String[0] == "A" else 1
    # Fim
    
    # Convertendo o gene do pai para número
    Gene_Pai_Numb = 2 if Zigoto_Filho_String[1] == "A" else 1
    # Fim 
    
    # Soma dos números dos genes do pai e da mãe
    Zigoto_Filho_Numb = Gene_Mae_Numb + Gene_Pai_Numb
    # Fim
    
    # Valor da function
    return Zigoto_Filho_Numb
    # Fim
    
# Fim

def verificar_zigoto(Zigoto_Filho_Numb):
    if Zigoto_Filho_Numb[0] == Zigoto_Filho_Numb[1]:
        return "Homozigoto"
    else:
        return "Heterozigoto"
    

# Função para contar as combinações de zigotos (AA, Aa/aA, aa)
def contagem(AA, Aa_aA, aa, Zigoto_Filho):
    if Zigoto_Filho[0] == "A" and Zigoto_Filho[1] == "A":
        AA += 1
    elif (Zigoto_Filho[0] == "A" and Zigoto_Filho[1] == "a") or (Zigoto_Filho[0] == "a" and Zigoto_Filho[1] == "A"):
        Aa_aA += 1
    elif Zigoto_Filho[0] == "a" and Zigoto_Filho[1] == "a":
        aa += 1
    return AA, Aa_aA, aa
# Fim
