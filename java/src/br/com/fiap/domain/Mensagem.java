package br.com.fiap.domain;

public class Mensagem {
    private String conteudo;
    private String tipo; // ex: lembrete, instrução, agradecimento

    public Mensagem(String conteudo, String tipo) {
        this.conteudo = conteudo;
        this.tipo = tipo;
    }

    public String getConteudo() {
        return conteudo;
    }

    public String getTipo() {
        return tipo;
    }

    @Override
    public String toString() {
        return "[" + tipo.toUpperCase() + "] " + conteudo;
    }
}
