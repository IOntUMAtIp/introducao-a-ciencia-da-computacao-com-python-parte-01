def maiusculas(frase):
    maiusculas = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
    letras = ""
    for i in frase:
        for x in maiusculas:
            if i == x:
                letras += i
    return letras
