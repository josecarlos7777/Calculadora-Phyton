num1 = float(input('digite o primeiro numero que deseja calcular '))
operação = input('digite a operação ')
num2 = float(input('digite o segundo numero que deseja calcular '))
if operação == '+':
  print(f'resultado é: {num1} + {num2} = {num1 + num2}')
elif operação == '-':
  print(f'resultado é: {num1} - {num2} = {num1 - num2}')
elif operação == '*':
  print(f'resultado é: {num1} * {num2} = {num1 * num2}')
elif operação == '%':
  print(f'resultado é: {num1} % {num2} = {num1 % num2}')
else:
  print('operação invalida')
