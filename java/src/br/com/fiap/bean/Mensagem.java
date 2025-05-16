package br.com.fiap.bean;

public class Mensagem {
    private String conteudo;
    private String tipo;

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

    public String toString() {
        return "[" + tipo.toUpperCase() + "] " + conteudo;
    }
}

