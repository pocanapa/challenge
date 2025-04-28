package br.com.fiap.main;

import br.com.fiap.bean.ArCondicionado;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArCondicionado ac1 = new ArCondicionado();
        Scanner scan;
        int escolha;
        try {
            scan = new Scanner(System.in);
            System.out.println("Escolha um modo e defina a temperatura");
            ac1.setModo(scan.next());
            ac1.setTemperatura(scan.nextInt());

            System.out.println("Faça uma escolha: \n(1) Mudar de modo\n(2) Aumentar temperatura\n(3) Diminuir temperatura");
            escolha = scan.nextInt();

            if (escolha == 1){
                System.out.println("Digite o novo modo");
                ac1.setModo(scan.next());
            } else if (escolha == 2) {
                System.out.println("Aumentando temperatura...");
            } else {
                System.out.println("Diminuindo temperatura...");
                ac1.diminuirTemperatura();
            }
            System.out.printf("Modo atual: %s\nTemperatura atual: %dC", ac1.getModo(), ac1.getTemperatura());

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }
}
