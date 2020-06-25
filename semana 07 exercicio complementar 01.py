def maior_elemento(lista):
	maior = 0
	for i in range(len(lista)):
		if lista[i] >= lista[i - 1]:
			maior = lista[i]
	return maior
