def menor_nome(nomes):
    
    menor = nomes[0].strip()
    
    for i in range(len(nomes)):
        x = nomes[i].strip()
        if len(x) < len(menor):
            menor = x
    
    return menor.capitalize()

