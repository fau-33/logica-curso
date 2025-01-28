"""
    Desafios Extras
    
    1. Classificação Etária
    Crie um programa que verifica se uma pessoa pode assistir a um filme classificado como
    "maiores de 16 anos".
    Dados:
    ● Idade da pessoa: Pergunte ao usuário

"""

# Solicitar idade
idade = int(input("Digite sua idade: "));

# Verificar se pode assistir filme
pode_assistir = idade >= 16;

print("Pode assistir: " , pode_assistir)

"""
    2. Calculadora de IMC
    O Índice de Massa Corporal (IMC) é calculado dividindo o peso (em kg) pela altura (em
    metros) elevada ao quadrado.
    Crie um programa que calcula o IMC e verifica se a pessoa está dentro do peso ideal (IMC
    entre 18.5 e 24.9).
"""

# Solicitar peso e altura
peso = float(input("Digite seu peso: "));
altura = float(input("Digite sua altura: "));

# Calcular IMC
imc = peso / (altura**2);

# Verificar peso ideal
peso_ideal = (18.5 >= imc) and (imc <= 24.9);

print("Seu IMC é: " , imc);
print("Voce esta no peso ideal: " , peso_ideal)

"""
    3. Par ou Ímpar
    Crie um programa que solicita um número inteiro ao usuário e verifica se ele é par ou ímpar.
"""

# Solicitar número
numero = int(input("Digite um número: "));

# Verificar paridade
par = numero % 2 == 0;

print("O número digitado é par: " , par);