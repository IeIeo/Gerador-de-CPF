import random

#for _ in range(100):  #para gerar 100 cpf's

nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0,9))
 
contador_regressivo_1 = 10 
resultado_1 = 0

for numero in nove_digitos:
    resultado_1 += int(numero) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = resultado_1 *10 % 11

digito_1 = digito_1 if digito_1 <= 9 else 0
#print(digito_1)


nove_primeiros_2 = nove_digitos + str(digito_1)
contador_regressivo_2 = 11
resultado_2 = 0

for nuemero_2 in nove_primeiros_2:
    resultado_2 += int(nuemero_2) * contador_regressivo_2
    contador_regressivo_2 -=1

digito_2 = resultado_2 * 10 % 11

digito_2 = digito_2 if digito_2 <=9 else 0


novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'


print(novo_cpf)


