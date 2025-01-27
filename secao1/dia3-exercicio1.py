"""
    Exercícios Práticos com Situações do Dia a Dia
    
    1. Calculando o Troco
    Você foi a uma padaria e comprou alguns itens:
    ● Pão: R$3.50
    ● Leite: R$4.20
    ● Café: R$2.80
    Você pagou com uma nota de R$20. Calcule quanto de troco você deve receber.
"""

# Preços dos itens
pao = 3.50;
leite = 4.20;
cafe = 2.80;

# Total da compra
total_compra = pao + leite + cafe;

# Pagamento
pagamento = 20.00;

# Calculando o troco
troco = pagamento - (total_compra);

print("Total da compra: " , total_compra);
print("Troco: " , troco);

"""
    2. Verificando Aprovação em um Exame
    Para ser aprovado em um exame, um estudante precisa ter uma nota média maior ou igual
    a 7.0 e uma frequência maior ou igual a 75%.
    Dados:
    ● Nota média: 8.5
    ● Frequência: 80%

    Verifique se o estudante foi aprovado.
    """
    
# Dados do estudante
nota_media = 8.5;
frequencia = 80;

# Verificando se o estudante foi aprovado
aprovado = (nota_media >= 7.0) and (frequencia >= 75);
print("Estudante aprovado? " , aprovado);