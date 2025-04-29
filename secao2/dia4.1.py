# Exercícios Práticos

# 1. Verificando Se um Número é Positivo, Negativo ou Zero
# Crie um programa que solicita um número ao usuário e verifica se ele é positivo, negativo
# ou zero.

numero = float(input("Digite um número: "));

if numero > 0:
  print("O número digitado é positivo.");
elif numero < 0:
  print("O número digitado é negativo.");
else:
  print("O número digitado é zero.");

# 2. Calculadora Simples
# Crie um programa que pede ao usuário dois números e uma operação (+, -, *, /) e realiza
# o cálculo correspondente.

# numero1 = float(input("Digite o primeiro número: "));
# numero2 = float(input("Digite o segundo número: "));
# operacao = input("Digite a operação (+, -, *, /): ");

if operacao == "+":
  resultado = numero1 + numero2;
elif operacao == "-":
  resultado = numero1 - numero2;
elif operacao == "*":
  resultado = numero1 * numero2;
elif operacao == "/":
  resultado = numero1 / numero2;
else:
  print("Operação inválida.");

print("Resultado: " , resultado);


# 3. Classificação de Idade
# Crie um programa que classifica a idade de uma pessoa em:
# ● Criança: 0 a 12 anos
# ● Adolescente: 13 a 17 anos
# ● Adulto: 18 a 59 anos
# ● Idoso: 60 anos ou mais

idade = int(input("Digite sua idade: "));

if idade <= 12:
  print("Criança");
elif idade >= 13 and idade <= 17:
  print("Adolescente");
elif idade >= 18 and idade <= 59:
  print("Adulto");
else:
  print("Idoso");

# 4. Verificando Ano Bissexto
# Crie um programa que verifica se um ano é bissexto.
# ● Um ano é bissexto se for divisível por 4.
# ● Mas não é bissexto se for divisível por 100, exceto se for divisível por 400.

ano = int(input("Digite um ano: "));

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
  print("Ano bissexto");
else:
  print("Ano não bissexto");

# 5. Simulador de Caixa Eletrônico
# Crie um programa que simula um caixa eletrônico. O usuário deve informar o valor do saque
# (apenas valores inteiros) e o programa deve informar quantas cédulas de cada valor serão
# fornecidas.
# ● Considere cédulas de R$100, R$50, R$20, R$10, R$5 e R$2.

valor_saque = int(input("Digite o valor do saque: R$ "));

cedulas_100 = int(valor_saque / 100);
valor_saque = valor_saque % 100;

cedulas_50 = int(valor_saque / 50);
valor_saque = valor_saque % 50;

cedulas_20 = int(valor_saque / 20);
valor_saque = valor_saque % 20;

cedulas_10 = int(valor_saque / 10);
valor_saque = valor_saque % 10;

cedulas_5 = int(valor_saque / 5);
valor_saque = valor_saque % 5;

cedulas_2 = int(valor_saque / 2);
valor_saque = valor_saque % 2;

print("Cédulas de R$100: " , cedulas_100);
print("Cédulas de R$50: " , cedulas_50);
print("Cédulas de R$20: " , cedulas_20);
print("Cédulas de R$10: " , cedulas_10);
print("Cédulas de R$5: " , cedulas_5);
print("Cédulas de R$2: " , cedulas_2);

