def conta_letras(frase, contar = "vogais"):
    vogais = "aeiou"    vogais_maiusculas = vogais.upper()
    consoantes = "bcdfghjklmnpqrstvyxz"
    consoantes_maiusculas = consoantes.upper()
    cont = 0
    if contar == "vogais":
        for i in frase:
            if i in vogais or i in vogais_maiusculas:
                cont += 1
    else:
        for i in frase:
            if i in consoantes or i in consoantes_maiusculas:
                cont += 1
    return cont
