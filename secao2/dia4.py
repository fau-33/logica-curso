# Dia 4: Estruturas Condicionais
# Declarações if, elif e else

# 1. Declaração if e else

idade = 16;

if idade >= 18:
    print("Maior de idade");
else:
    print("Menor de idade");

# 2. Declaração elif
nota = 85;

if nota >= 90:
    print("Sua nota é A.");
elif nota >= 80:
    print("Sua nota é B.");
elif nota >= 70:
    print("Sua nota é C.");
else:
    print("Você precisa melhorar.");

# Exemplos com Analogias do Mundo Real
# 1. Decidindo o Que Vestir
# Situação: Você olha pela janela para ver o clima e decide o que vestir.

clima = "ensolarado";

if clima == "ensolarado":
    print("Vista uma camiseta e shorts.");
elif clima == "nublado":
    print("Leve uma jaqueta leve.");
elif clima == "chuvoso":
    print("Não esqueça o guarda-chuva.");
else:
    print("Verifique a previsão do tempo.");

# 2.Semáforo
# Situação: Ao dirigir, você reage de acordo com a cor do semáforo.

semaforo = "vermelho";

if semaforo == "verde":
    print("Siga em frente.");
elif semaforo == "amarelo":
    print("Prepare-se para parar.");
elif semaforo == "vermelho":
    print("Pare o veículo.");
else:
    print("Sinal desconhecido, proceda com cautela.");

# 3. Calculando Descontos em Compras
# Situação: Uma loja oferece descontos com base no valor da compra.
# Se o valor for maior ou igual a R$1000, o desconto é de 10%.
# Se for entre R$500 e R$999, o desconto é de 5%.
# Caso contrário, não há desconto.

valor_compra = 1000;

if valor_compra >= 1000:
    desconto = valor_compra * 0.10;
    print("Você recebeu um desconto de 10%. Valor do desconto: R$ " , desconto);
elif valor_compra >= 500:
    desconto = valor_compra * 0.05;
    print(" você recebeu um desconto de 5%. Valor do desconto: R$ " , desconto);
else:
    desconto = 0;
    print("Não há desconto disponível.");

total_compra = valor_compra - desconto;
print("Valor total da compra: R$ " , total_compra);
    