#Style
limpa = '\033[m'
bold = '\033[1m'
sub = '\033[4m'
red = '\033[31m'
green = '\033[32m'

casa = float(input('Qual o valor da casa? {}R${}'.format(bold, limpa)))
salario = float(input('Quanto você ganha? {}R${}'.format(bold, limpa)))
tempo = int(input('Em quantos meses você pretende pagar? '))
ano = tempo / 12

print('-'*50)

calculo1 = (salario * 30 / 100)
print('Você só pode comprometer {}30%{} do seu salário, que da {}R${}{}'.format(sub, limpa, bold, calculo1, limpa))
calculo2 = (casa / tempo)
print('A casa por esse preço, pagando por esse {} meses, você terá que pagar {}R${:.2f}{} por mês.'.format(tempo, bold, calculo2, limpa))

print('-'*50)

if calculo2 < calculo1:
    print('{}Tudo bem, você comprará sua casa, pagando {}R${:.2f}{} por mês durante {}{:.0f} anos{}.{}'.format(green, bold, calculo2, limpa, sub, ano, limpa, limpa))
else:
    print('{}Infelizmente o valor mínimo da prestação ultrapassa o seu limite máximo, tente parcelar por mais meses ou arrumar mais dinheiro!{}'.format(red, limpa))