def soma_matrizes(matriz_um, matriz_dois):
    
    linhas_um = len(matriz_um)
    colunas_um = len(matriz_um[0])
    linhas_dois = len(matriz_dois)
    colunas_dois = len(matriz_dois[0])
    
    if (linhas_um == linhas_dois) and (colunas_um == colunas_dois):
        resultado = [[0] * colunas_um] * linhas_um
        print(resultado)
        for i in range(linhas_um):
            for j in range(colunas_um):
                resultado[i][j] = matriz_um[i][j] + matriz_dois[i][j]
        
        return resultado
    
    else:
        
        return False
