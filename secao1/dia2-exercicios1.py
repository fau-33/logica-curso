"""
Variáveis declaradas:
- nome: seu nome.
- idade: sua idade.
- altura: sua altura.
- estudante: se você é estudante ou não (True/False).
"""

nome = "Flávio";
idade = 42;
altura = 1.70;
estudante = True;

print("Nome: " , nome);
print("Idade: " , idade);
print("Altura: " , altura);
print("Estudante: " , estudante);

# 3. Operações Simples
# Calcule o ano de nascimento com base na idade (considerando que o ano atual é 2023).

ano_nascimento = 2023 - idade;
print("Ano de nascimento: " , ano_nascimento);

maior_de_idade = idade >= 18;
print("Maior de idade: " , maior_de_idade);

# 4. Manipulação de Strings
# Crie uma variável frase que contenha a mensagem: "Olá, meu nome é [seu nome] e eu
# tenho [sua idade] anos."

frase = "Olá, meu nome é " + nome + " e eu tenho " + str(idade) + " anos.";
print(frase);

# 5. Calculadora Simples
# Peça ao usuário para inserir dois números e armazene-os em variáveis.
# Calcule a soma, subtração, multiplicação e divisão desses números.
# Exiba os resultados.

numero1 = float(input("Digite o primeiro número: "));
numero2 = float(input("Digite o segundo número: "));

soma = numero1 + numero2;
subtracao = numero1 - numero2;
multiplicacao = numero1 * numero2;
divisao = numero1 / numero2;

print("Soma: " , soma);
print("Subtração: " , subtracao);
print("Multiplicação: " , multiplicacao);
print("Divisão: " , divisao);