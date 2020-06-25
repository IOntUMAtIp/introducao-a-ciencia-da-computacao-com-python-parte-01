def primeiro_lex(lista):
    ordem = lista[0]
    primeira_letra = ord(str(lista[0])[0])
    for i in lista:
        frase = str(i)
        letra = frase[0]
        primeiro = ord(frase[0])
        if primeiro < primeira_letra:
            primeira_letra = primeiro
            ordem = i
    return ordem
