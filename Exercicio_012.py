bordas = '\033[037m-=-\033[m' * 12
print(bordas)
print('{:^35}'.format('CALCULANDO DESCONTOS'))
print(bordas)
print()

pp = ''

while type(pp) != float:
    try:
        pp = float(input('Digite o preço do produto? R$'))
    except:
        print('Por favor digite um preço válido!')

desconto = ''

while type(desconto) != float:
    try:
        desconto = float(input('Digite a porcentagem de desconto: '))
    except:
        print('Por favor digite um desconto válido!')

print(f'Com a promoção de {desconto}% de desconto o desconto será de R${pp/desconto:.2f}'
      f' e o produto que antes custava R${pp:.2f} vai passar a custar R${pp-pp*(desconto/100):.2f}.')
