"""
    3. Oferta Especial
    Uma loja oferece um desconto se o cliente comprar mais de 10 itens ou se o valor total da
    compra for superior a R$100.
    Dados:
    ● Quantidade de itens: 8
    ● Valor total: R$120


    Verifique se o cliente tem direito ao desconto.

"""

# Dados da compra
quanridade_itens = 8;
valor_total = 120.00;

# Verificar se o cliente tem direito ao desconto
tem_desconto = (quanridade_itens > 10) or (valor_total > 100.00);

print("Tem desconto: " , tem_desconto);


"""
    4. Sistema de Acesso
    Para acessar uma área restrita, o usuário deve inserir a senha correta e não pode estar
    bloqueado.
    Dados:
    ● Senha inserida: "abcd1234"
    ● Senha correta: "abcd1234" 
    ● Usuário bloqueado: False

    Verifique se o acesso deve ser concedido.
"""
# Dados do usuário
senha_inserida = "abcd1234";
senha_correta = "abcd1234";
usuario_bloqueado = False;

# Verificar se o acesso deve ser concedido
acesso_concedido = (senha_inserida == senha_correta) and not usuario_bloqueado;

print("Acesso concedido: " , acesso_concedido);

"""
    5. Divisão de Tarefas
    Três amigos vão dividir igualmente uma conta de R$150. Verifique quanto cada um deve
    pagar e se a divisão é exata (sem centavos restantes).
"""
# Valor total da conta
valor_total = 150.00;

# Quantidade de amigos
quantidade_amigos = 3;

# Calcular quanto cada amigo deve pagar
valor_por_amigo = valor_total / quantidade_amigos;

# Verificar se a divisão é exata
divisao_exata = (valor_total % quantidade_amigos) == 0;

print("Cada um deve pagar por pessoa: " , valor_por_amigo);
print("A divisão exata é: " , divisao_exata);

