"""
    Operadores de Comparação
"""

x = 10;
y = 5;

print(x > y);
print(x < y);
print(x >= y);
print(x <= y);
print(x == y);
print(x != y);

"""
    Exemplos Práticos
"""
idade = 20;
possui_carteira = True;

# Verificar se pode alugar um carro
pode_alugar = (idade >= 18) and possui_carteira;
print("Pode alugar: " , pode_alugar);

# Verificar se tem direito a meia-entrada
estudante = False;
idoso = idade >= 60;
meia_entrada = estudante or idoso;
print("Tem direito a meia-entrada: " , meia_entrada);

# Inverter uma condição
chovendo = False;
nao_chovendo = not chovendo;
print("Esta choavendo: " , chovendo);
print("Nao esta choavendo: " , nao_chovendo);

# Revisão
# nota > 7 and frequecia > 80%
nota = 8;
frequencia = 60;
passa_de_ano = (nota >= 7) or (frequencia >= 80);
print("Passa de ano: " , passa_de_ano);

# Senhas iguais
# criar registro de usuários
senha = "teste123";
confirmacao_senha = "teste1234";

aviso_senha_errada = senha != confirmacao_senha;
print("Senhas diferentes: " , aviso_senha_errada);

# Mesa de bar
# conta deu 123.85
# quanto cada pessoa deve pagar? 3 pessoas
conta = 123.85;
quantidade_pessoas = 3;
valor_por_pessoa = conta / quantidade_pessoas;
print("Valor por pessoa: " , valor_por_pessoa);
