package application;

import java.util.Scanner;

public class CPF {
    public static void main(String[] args) {


        // ENTRADA DE DADOS
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite seu CPF: ");
        String CPF = teclado.nextLine();

        //VERIFICAÇÃO PRIMARIA DO CPF
        if(CPF.length() != 11 || CPF.equals("11111111111") || CPF.equals("22222222222") || CPF.equals("33333333333") || CPF.equals("44444444444") || CPF.equals("55555555555") || CPF.equals("66666666666") || CPF.equals("77777777777")  || CPF.equals("88888888888" ) || CPF.equals("99999999999") || CPF.equals("00000000000")){
            System.out.println("\u001b[31mCPF Invalido!!!\u001b[m");
        } else {

            // CALCULO 1° DIGITO VERIFICADOR DO CPF
            int soma = 0;
            for (int x = 0; x < 9; ++x) {
                char s = CPF.charAt(x);
                int v = Character.getNumericValue(s);
                soma = soma + (v * (10 - x));
            }
            int dig1 = 11 - (soma % 11);
            if (dig1 >= 10) {
                dig1 = 0;
            }

            // CALCULO 2° DIGITO VERIFICADOR DO CPF
            soma = 0;
            for (int x = 0; x < 10; ++x) {
                char s = CPF.charAt(x);
                int v = Character.getNumericValue(s);
                soma = soma + (v * (11 - x));
            }
            int dig2 = 11 - (soma % 11);
            if (dig2 >= 10) {
                dig2 = 0;
            }

            //SCRIPT VERIFICADOR DO CPF
            int v1 = Character.getNumericValue(CPF.charAt(9));
            int v2 = Character.getNumericValue(CPF.charAt(10));
            if (dig1 == v1 && dig2 == v2) {
                System.out.println("\u001b[32mCPF Valido!!!\u001b[m");
            } else {
                System.out.println("\u001b[31mCPF Invalido!!!\u001b[m");
            }
        }
    }
}
