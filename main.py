number = int(input('Quantos números quer passar? '))

soma_positiva = 0
soma_negativa = 0
count = 0

while count < number:
    n = int(input('Número: '))
    if n >= 0:
        soma_positiva += n
    else:
        soma_negativa += n
    count += 1

print(f'A soma dos números positivos é {soma_positiva}')
print(f'A soma dos números negativos é {soma_negativa}')
