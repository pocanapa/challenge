package br.com.fiap.domain;

public class Cuidador {
    private String nome;
    private String telefone;

    public Cuidador(String nome, String telefone) {
        this.nome = nome;
        this.telefone = telefone;
    }

    public String getNome() {
        return nome;
    }

    public String getTelefone() {
        return telefone;
    }

    public void receberNotificacao(String mensagem) {
        System.out.println("Notificação enviada ao cuidador " + nome + ": " + mensagem);
    }
}
