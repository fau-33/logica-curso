# Variáveis

idade = 20;
nome = "Flávio";
altura = 1.70;

# Tipos de dados
# int, float, string, boolean

cidade = "Belo Horizonte";

esta_logado = True;

print(nome);

nome = 10;

print(nome);

# Verifica o tipo de dado
print(type(nome)); # str -> string
print(type(altura)); # float -> ponto flutuante 
print(type(esta_logado));# bool -> boolean
print(type(cidade));# str -> string

# Operadores aritméticos
numero1 = 10;
numero2 = 20.50;

print(numero1 + numero2);
print(numero1 - numero2);
print(numero1 * numero2);
print(numero1 / numero2);
print(numero1 % numero2);

# Concatenar strings
nome = "Carlos";
frase = "Olá " + nome +" Tudo bem?";
print(frase);

# Comparações
maior = 15 > 10;
print(maior);

menor = 5 < 2;
menor2 = 15 < 5;
print(menor);
print(menor2);

igual = 10 == 10;
diferente = 10 != 20;
print(igual);
print(diferente);

print("Flávio" == "flávio");
print("Flávio" == "Flávio");