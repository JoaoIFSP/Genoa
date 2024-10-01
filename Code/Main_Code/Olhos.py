import random

X = 0
Y = 0

Dominante_Numb = 2
Recessivo_Numb = 1

Olhos_castanhos = Dominante_Numb
Olhos_amarelos = Dominante_Numb
Olhos_verdes = Recessivo_Numb
Olhos_azuis = Recessivo_Numb

Zigoto_Olho_Mae = [Olhos_castanhos, Olhos_azuis]
Zigoto_Olho_Pai = [Olhos_amarelos, Olhos_verdes]

# Fórmula de geração do zigoto do filho (Olhos)
def Zigoto_filho_Olhos_depump(Zigoto_Olho_Mae, Zigoto_Olho_Pai):
    # Escolhe o gene da mãe (Olhos)
    Gene_Mae_Olhos = random.choice(Zigoto_Olho_Mae)
    # Escolhe o gene do pai (Olhos)
    Gene_Pai_Olhos = random.choice(Zigoto_Olho_Pai)
    # Zigoto do filho (Olhos)
    Zigoto_Filho_Olhos = [Gene_Mae_Olhos, Gene_Pai_Olhos]
    return Zigoto_Filho_Olhos

def Numb_to_String (Zigoto_Filho_Olhos):
    Zigoto_Filho_Olhos_Mae_String = "Gene da mãe está errado"
    if Zigoto_Filho_Olhos[0] == Olhos_castanhos:
        Zigoto_Filho_Olhos_Mae_String = "Olhos castanhos"
    elif Zigoto_Filho_Olhos[0] == Olhos_amarelos:
        Zigoto_Filho_Olhos_Mae_String = "Olhos amarelos"
    elif Zigoto_Filho_Olhos[0] == Olhos_azuis:
        Zigoto_Filho_Olhos_Mae_String = "Olhos azuis"
    elif Zigoto_Filho_Olhos[0] == Olhos_verdes:
        Zigoto_Filho_Olhos_Mae_String = "Olhos azuis"
    
    Zigoto_Filho_Olhos_Pai_String = "Gene da mãe está errado"

    if Zigoto_Filho_Olhos[1] == Olhos_castanhos:
        Zigoto_Filho_Olhos_Pai_String = "Olhos castanhos"
    elif Zigoto_Filho_Olhos[1] == Olhos_amarelos:
        Zigoto_Filho_Olhos_Pai_String = "Olhos amarelos"
    elif Zigoto_Filho_Olhos[1] == Olhos_azuis:
        Zigoto_Filho_Olhos_Pai_String = "Olhos azuis"
    elif Zigoto_Filho_Olhos[1] == Olhos_verdes:
        Zigoto_Filho_Olhos_Pai_String = "Olhos azuis"
        
    Zigoto_Filho_Olhos_String = [Zigoto_Filho_Olhos_Mae_String, Zigoto_Filho_Olhos_Pai_String]
    return Zigoto_Filho_Olhos_String
    
    # eu to com muito sono então vou dormir, voce basicamente fez o mesmo
    # Code do zigoto, só que um tanto diferente, ta precisando imprimir se o olho do mano é
    # tipo a b c d tlg
      

def verificar_zigotagem(Zigoto_Filho_Olhos, Zigoto_Filho_Olhos_String):
    if Zigoto_Filho_Olhos[0] + Zigoto_Filho_Olhos[1] == 2:
        Caracteristica_Olho = random.choice(Zigoto_Filho_Olhos_String)
        return f"Característica do olho: {Caracteristica_Olho}"
    elif Zigoto_Filho_Olhos[0] + Zigoto_Filho_Olhos[1] == 3:
        Zigoto_define = "Heterozigoto"
        return Zigoto_define
    elif Zigoto_Filho_Olhos[0] + Zigoto_Filho_Olhos[1] == 4:
        Caracteristica_Olho = random.choice(Zigoto_Filho_Olhos_String)
        return f"Característica do olho: {Caracteristica_Olho}"
    else:
        Zigoto_define = "Valor inválido"
        return Zigoto_define

# Loop para gerar 100 zigotos
for _ in range(100):
    # Gera o zigoto do filho (Olhos)
    Zigoto_Filho_Olhos = Zigoto_filho_Olhos_depump(Zigoto_Olho_Mae, Zigoto_Olho_Pai)

    # Verifica e define o tipo de zigoto
    definin_Eye = verificar_zigotagem(Zigoto_Filho_Olhos)

    # Imprime o resultado
    print(definin_Eye)
