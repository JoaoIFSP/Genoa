import random

cnt = 1

# Demonstrativo de dominante ou recessivo
Dominante = 'A'
Recessivo = 'a'

# Contagem para ver densidade de zigotos
Quantidade_AA = 0
Quantidade_Aa_ou_aA = 0
Quantidade_aa = 0

# Trincheira de genes
Zigoto_Mae = [Dominante, Recessivo]
Zigoto_Pai = [Dominante, Recessivo]

# Repetição de código
while cnt <= 100:
    
    # Parâmetro do envio do gene da mãe ao filho
    Gene_Mae = random.randint(1, 2)
    if Gene_Mae == 1:
       Gene_Mae = Zigoto_Mae [0]
    else:
       Gene_Mae = Zigoto_Mae [1]

    
    # Parâmetro do envio do gene do pai ao filho
    Gene_Pai = random.randint(1, 2)
    if Gene_Pai == 1:
        Gene_Pai = Zigoto_Pai [0]
    else:
        Gene_Pai = Zigoto_Pai [1]
        
    # Zigoto do filho
    Gene_Filho = [Gene_Mae , Gene_Pai]
    
    # Apenas para o print demonstrativo  
    if Gene_Filho [0] == 'A' and Gene_Filho [1] == 'A':
        Quantidade_AA = Quantidade_AA + 1
        
    if Gene_Filho [0] == 'A' and Gene_Filho [1] == 'a' or Gene_Filho [0] == 'a' and Gene_Filho [1] == 'A':
        Quantidade_Aa_ou_aA = Quantidade_Aa_ou_aA + 1
        
    if Gene_Filho [0] == 'a' and Gene_Filho [1] == 'a':
        Quantidade_aa = Quantidade_aa + 1
        
    print(f"Gene do Filho: {Gene_Filho [0]}{Gene_Filho [1]}")
    
    
    
    cnt = cnt + 1

print(f"Quantidade AA:{Quantidade_AA}")
print(f"Quantidade Aa ou aA:{Quantidade_Aa_ou_aA}")
print(f"Quantidade aa:{Quantidade_aa}")






     






 