Olhos = {
    
    "Castanho": 8,  # Dominante
    "Preto": 4,   # Dominante
    "Verde": 2,     # Recessivo
    "Azul": 1       # Recessivo
    
}

Cabelo = {
    
    "Moreno": 8,  # Dominante
    "Preto": 4,   # Dominante
    "Loiro": 2,   # Recessivo
    "Ruivo": 1    # Recessivo
    
}

# Zigoto do cabelo do papai e da mamãe
Pele = {
    
    "Negro": 8,    # Dominante
    "Branco": 4,    # Dominante
    "Amarelo": 2,  # Recessivo
    "Pardo": 1    # Recessivo
    
}
# Zigoto do Tipo de cabelo do papai e da mamãe

Tipo_Cabelo = {
    
    "Cacheado": 8,    # Dominante
    "Liso": 4,    # Dominante
    "Grosso": 2,  # Recessivo
    "Fino": 1    # Recessivo
    
}
# Zigoto do Tipo de cabelo do papai e da mamãe
Nariz = {
    
    "Largo": 8,    # Dominante
    "Fino": 4,    # Dominante
    "Redondo": 2,  # Recessivo
    "Reto": 1    # Recessivo
    
}
# Zigoto do Tipo de cabelo do papai e da mamãe
Altura = {
    
    "1,70 m": 8,    # Dominante
    "1,60 m": 4,    # Dominante
    "1,90 m": 2,  # Recessivo
    "1,50 m": 1    # Recessivo
    
}

# Olhos
Zigoto_Olho_Mae = [Olhos["Castanho"], Olhos["Azul"]] # Opções:
Zigoto_Olho_Pai = [Olhos["Preto"], Olhos["Verde"]] # Castanho(A) / Amarelo(A) / Azul(a) / Verde(a)

# Fim

# Cabelo
Zigoto_Cabelo_Mae = [Cabelo["Moreno"], Cabelo["Loiro"]] # Opções:
Zigoto_Cabelo_Pai = [Cabelo["Preto"], Cabelo["Ruivo"]]  # Moreno(A) / Preto(A) / Loiro(a) / Ruivo(a)
# Fim

# Tipo de cabelo
Zigoto_Tipo_Cabelo_Mae = [Tipo_Cabelo["Cacheado"], Tipo_Cabelo["Grosso"]] # Opções:
Zigoto_Tipo_Cabelo_Pai = [Tipo_Cabelo["Liso"], Tipo_Cabelo["Fino"]]       # Cacheado(A) / Liso(A) / Grosso(a) / Fino(a)
# Fim

# Pele
Zigoto_Pele_Mae = [Pele["Negro"], Pele["Amarelo"]] # Opções:
Zigoto_Pele_Pai = [Pele["Branco"], Pele["Pardo"]]  # Negro(A) / Branco(A) / Amarelo(a) / Pardo(a)
# Fim

# Nariz
Zigoto_Nariz_Mae = [Nariz["Largo"], Nariz["Redondo"]] # Opções:
Zigoto_Nariz_Pai = [Nariz["Fino"], Nariz["Reto"]]     # Largo(A) / Fino(A) / Redondo(a) / Reto(a)
# Fim

# Altura
Zigoto_Altura_Mae = [Altura["1,70 m"], Altura["1,50 m"]] # Opções:
Zigoto_Altura_Pai = [Altura["1,60 m"], Altura["1,90 m"]] # 1,70 m (A) / 1,60 m (A) / 1,50 m(a) / 1,90 m(a)
# Fim


# Enlouqueci.