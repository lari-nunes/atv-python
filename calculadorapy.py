def somaNumerosPares(inicio, fim):
    i = inicio 
    soma = 0
    while (i <= fim):
        if(i % 2 == 0):
            soma += i
            i += 1
            return soma

inicio = 1
fim = 10
resultado = somaNumerosPares(inicio, fim)
print("A soma dos números pares de {inicio} a {fim} é resultado")