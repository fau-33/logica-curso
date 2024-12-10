package secao2;

public class Variavel {

    public static void main(String[] args) {
        // 1 - O que são variáveis?
        // tipo -> nome -> atribuir um valor
        String nome = "Joaquim";

        // nome = "Joaquim";
        System.out.println(nome);

        // Atribuição de uma variável para outra
        String teste = "Teste";
        String outra = teste;
        System.out.println(outra);

        long numeroGrande = 1_000_000_000L;
        System.out.println(numeroGrande);

        // 3 - Comentários

    /*
     * Comentários de linha 1
     * Comentários de linha 2
     * Comentários de linha 3
     */

    /**
      * função para somar dois números
      *param n1
      *param n2
      *return somar os dois numeros
     */

      // 4 - Strings

    String firstName = "Flávio";
    String lastName = "Silva";
    String fullName = firstName + " " + lastName;

    System.out.println(fullName);




    }
}