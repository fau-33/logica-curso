# Desafios Extras

# 1. Aprovando Empréstimo Bancário
# Crie um programa para uma instituição bancária que analisa o pedido de empréstimo.
# ● O cliente deve informar o valor do empréstimo, a renda mensal e o número de
# parcelas.
# ● O empréstimo será aprovado se o valor da parcela não exceder 30% da renda
# mensal.

# valor_emprestimo = float(input("Digite o valor do empréstimo: R$ "));
# renda_mensal = float(input("Digite a renda mensal: R$ "));
# numero_parcelas = int(input("Digite o número de parcelas: "));

valor_parcela = valor_emprestimo / numero_parcelas;
limite_parcela = renda_mensal * 0.3;

if valor_parcela <= renda_mensal * limite_parcela:
  print("Empréstimo aprovado.");
  print(f"Valor da parcela: R${valor_parcela:.2f}")
else:
  print("Empréstimo negado.")

# 2. Jogo Pedra, Papel ou Tesoura
# Crie um programa que simula o jogo "Pedra, Papel ou Tesoura" entre o usuário e o
# computador

import random

opcoes = ["pedra", "papel", "tesoura"];
opcao_jogador = input("Escolha uma opção: ").lower();
opcao_computador = random.choice(opcoes);

if opcao_jogador == opcao_computador:
  print("Empate.");
elif opcao_jogador == "pedra":
  if opcao_computador == "papel":
    print("Computador ganhou.");
  else:
    print("Jogador ganhou.");
elif opcao_jogador == "papel":
  if opcao_computador == "tesoura":
    print("Computador ganhou.");
  else:
    print("Jogador ganhou.");
elif opcao_jogador == "tesoura":
  if opcao_computador == "pedra":
    print("Computador ganhou.");
  else:
    print("Jogador ganhou.");

# 3. Calculadora de Tarifas de Táxi
# Uma empresa de táxi cobra uma tarifa básica de R$4.00, mais R$0.25 por quilômetro
# rodado. Crie um programa que calcula o valor total da corrida com base na distância
# percorrida.

distancia_percorrida = float(input("Digite a distância percorrida: "));
tarifa_basica = 4.00;
tarifa_quilometro = 0.25;

tarifa_total = tarifa_basica + (distancia_percorrida * tarifa_quilometro);
print(f"Tarifa total: R${tarifa_total:.2f}")




  



